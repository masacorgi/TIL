from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from uuid import uuid4
import boto3

app = FastAPI()

# DynamoDB 클라이언트 생성
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table_name = "study-application"
table = dynamodb.Table(table_name)

# TODO : crud, models, routers 폴더 하위로 코드 분리 필요
####################### USER ###########################
class User(BaseModel):
    '''HTTP요청의 body에서 데이터를 수신하거나 응답할때 pydantic이 자동으로
    데이터 유효성 검사를 수행하고, ORM모드를 통해 DB와 연동할 때 필요한 변환을 수행한다.'''
    
    # 필수 필드
    email: EmailStr
    name: str
    phone: str

    class Config:
        orm_mode = True
        # pydantic이 ORM(객체관계매핑)모드로 작동하게 설정
        # 모델을 DB에서 가져올때 필요한 변환을 수행하는데 사용
        
        # sqlarchemy 
        '''
        ORM : 관계형 데이터베이스 엔티티를 쿼리를 안쓰고 코드로 접근하는 방식
        
        '''
        
        

# POST user method
def create_user(request_data: User):
    email = request_data.email
    name = request_data.name
    phone = request_data.phone
    
    if not name or not email or not phone:
        raise HTTPException(status_code=400, detail="Name, Email, and Phone are required")

    user_id = str(uuid4()) # 유일한 ID 생성
    pk = f"USER#{user_id}" # 앞에 USER# 부착

    user_data = {
        'email': email,
        'name': name,
        'phone': phone,
        'is_active': 'Y',
        'data': email,
        'PK': pk,
        'SK': 'METADATA',
        'user_id': user_id
    }
    print(user_data)  # 로그 출력

    table.put_item(Item=user_data)

    # FastAPI에서는 JSON으로 데이터를 반환하는 것이 일반적이다.
    #return JSONResponse(content=jsonable_encoder(user.dict()), status_code=201)
    return user_data


# Post user : url - 메소드 라우팅
@app.post("/api/user")
async def create_user_endpoint(request_data: User = Depends(create_user)):
    return request_data
  
# GET user (by user id)
@app.get("/api/user/{user_id}")
async def get_user_by_id(user_id:str):
    data = table.get_item( Key={ 'PK':'USER#'+user_id ,'SK':"METADATA" } )
    user = data.get('Item')
    return user

# PUT user (by user id)
@app.put("/api/user/{user_id}")
async def update_user_by_id(user_id:str, request_data:User, table=Depends(lambda:table)):
    '''
    request_data:User <- body에서 받아온 데이터를 User모델을 사용해서 데이터 형식,유효성 검사
    table=Depends(lambda:table) <- 의존성 주입(Dependency Injection)
    함수나 클래스에 필요한 객체를 주입하는 매커니즘으로, 코드의 모듈성,재사용성을 높일수있다.
    lambda는 간단한 익명 함수를 생성한다.
    lambda는 테이블을 생성하는 함수를 나타낸다.
    
    update_user_by_id 함수가 실행될때마다 해당 함수에 필요한 table 객체를 생성하는데 사용된다.
    
    의존성 주입을 사용하면 함수 내에서 직접 객체를 생성하는 대신 필요한 객체를 외부에서 주입받아 사용할 수 있다.
    코드의 유연성을 향상시키고 객체를 주입하는 방식을 변경하거나 테스트의 용이성이 높아지는 이점을 누릴 수 있다.
    
    '''
    
    # DB에서 user_id로 사용자 데이터 조회,저장
    db_response = table.get_item(Key={'PK':f"USER#{user_id}",'SK':'METADATA'})
    existing_user_data = db_response.get('Item')
    
    # 없을시 404에러 반환
    if not existing_user_data:
        raise HTTPException(status_code=404, detail=f"cannot find ID: USER#{user_id}")
    
    # request body 데이터로 업데이트
    existing_user_data.update({
        'email' : request_data.email,
        'name' : request_data.name,
        'phone' : request_data.phone,
        'data' : request_data.email,
    })
    
    # DB save
    table.put_item(Item=existing_user_data)
    
    return existing_user_data

# DELETE user (by user id) 
@app.delete("/api/user/{user_id}")
async def delete_user_by_id(user_id:str):
    # DB에서 삭제
    db_response = table.delete_item(
        Key={'PK':f"USER#{user_id}", 'SK':'METADATA'},
        ReturnValues='ALL_OLD' # 삭제된 항목의 이전 값(삭제 전 데이터) 반환
    )
    
    deleted_user_data = db_response.get('Attributes')
    
    if not deleted_user_data:
        raise HTTPException(status_code=404, detail=f"cannot find ID: USER#{user_id}")
    
    return deleted_user_data


## PK, SK를 이용한 DynamoDB 항목 조회기능
@app.get("/get_item/{pk}/{sk}")
async def get_item(pk: str, sk: str):
    try:
        # DynamoDB 테이블에서 아이템 조회
        response = table.get_item(
            Key={
                'PK': pk,
                'SK': sk
            }
        )
        item = response.get('Item')
        if item:
            return item
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# FastAPI 엔드포인트 정의
@app.get("/")
async def read_root():
    return {"Hello": "World"}