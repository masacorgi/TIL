from flask import Flask, request, jsonify
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, DiscriminatorAttribute, UTCDateTimeAttribute, ListAttribute, NumberAttribute
from pynamodb.connection.base import Connection

from model.user import User

app = Flask(__name__)
app.config['ALLOWED_METHODS'] = ['GET','POST','DELETE','PUT']

# PynamoDB 모델 정의
class BaseModel(Model):
    class Meta: #Meta 클래스 내에서 모델의 설정을 지정
        table_name = "study-application"  # 테이블 이름 설정
        region = 'ap-northeast-2'  # 원하는 AWS 지역으로 설정

    # 테이블의 속성 정의
    pk = UnicodeAttribute(hash_key=True,attr_name="PK") #PK 해시키
    sk = UnicodeAttribute(range_key=True, attr_name="SK") #SK 정렬키
    data = UnicodeAttribute(null=True, attr_name="data")
    entity = DiscriminatorAttribute(attr_name="entity")

# DynamoDB 테이블 생성
if not BaseModel.exists(): #해당 테이블이 없을 경우
    BaseModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
# wait=True : 테이블 생성이 완료될 때까지 대기


# TODO : Blueprint를 이용해서 curd/user.py 모듈에 옮기기
######################## USER ########################
# GET user by user_id
@app.route("/api/user/user_id/<user_id>",methods=["GET"])
def get_user_by_id(user_id):

    #try:
        user = User.get(hash_key=f"USER#{user_id}", range_key='METADATA')
        # pynamodb Model-BaseModel-User 클래스, hash_key:PK, range_key:SK 사용 검색
        return user.to_dict(user)
        # static method(to_dict)사용, 딕셔너리형으로 리턴

    #except Exception as e:
    #    return jsonify({"message":"Item does not exists"})
    

'''
def get_users(page_number: int = 1, page_size: int = 100):  # admin
    if page_number < 1:
        raise ValueError("page_number must be greater than or equal to 1")
    if page_size < 1:
        raise ValueError("page_size must be greater than or equal to 1")

    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    users = list(User.inverted_index.query(
        hash_key="METADATA",
        range_key_condition=User.pk.startswith('USER#'),
        limit=end_index
    ))

    ret = [User.to_dict(user) for user in users[start_index:end_index]]

    return {
        "page_number": page_number,
        "page_size": page_size,
        "total_items": len(users),
        "items": ret
    }
'''

''' POST JSON 복붙용 데이터
{
    "email" : "test@test.com",
    "name" : "tester",
    "phone" : "1234"
}
'''
# POST user : 새 사용자 생성
@app.route("/api/user",methods=["POST"])
def create_user():
    request_data = request.get_json() #request body데이터 저장
    email = request_data["email"]
    name = request_data['name']
    phone = request_data['phone']
    
    if not name:
        raise ValueError('Name is required')
    if not email:
        raise ValueError('Email is required')
    if not phone:
        raise ValueError('Phone is required')
    
    user = User( #객체에 저장
        email=email,
        name=name,
        phone=phone,
        is_active="Y",
        data=email
    )
    print(user) #로그 출력

    user.user_id = user.pk.split('#')[1] # pk는 'USER#*****'라 id를 편하게 쓰려면 파싱필요
    user.save() # save to dynamoDB
    return user.to_dict(user) #save data returning
    
    
# PUT user : user update
@app.route("/api/user/<user_id>",methods=["PUT"])
def update_user(user_id):
    user = User.get(hash_key=f"USER#{user_id}", range_key='METADATA')# db 데이터 추출
    user.email = request.json.get("email")
    user.name = request.json.get("name") # request json데이터로 변경
    user.phone = request.json.get("phone")
    
    user.save() # DB update
    return user.to_dict(user) # 업데이트된 데이터 리턴

# DELETE user
@app.route("/api/user/<user_id>",methods=["DELETE"])
def delete_user(user_id):
    try:
        user = User.get(hash_key=f"USER#{user_id}", range_key='METADATA')
        user.delete()
        return user.to_dict(user)
    except Exception as e:
        return jsonify({"message":"user not found"})
######################## USER ########################

######################## EVENT ########################
'''
class Event(BaseModel, discriminator="event"):
    pk = UnicodeAttribute(hash_key=True,attr_name="PK")
    sk = UnicodeAttribute(range_key=True,attr_name="SK")
    data = UnicodeAttribute(null=True, attr_name="data")
    title = UnicodeAttribute(null=True, attr_name="title")
    event_id = UnicodeAttribute(null=True, attr_name="eventId")
    user_id = UnicodeAttribute(null=True, attr_name="userId")
    description = UnicodeAttribute(null=True, attr_name="description")
    started_at = UTCDateTimeAttribute(null=True, attr_name="startedAt")
    ended_at = UTCDateTimeAttribute(null=True, attr_name="endedAt")
    is_active = UnicodeAttribute(null=True, attr_name="isActive")
    rewards = ListAttribute(null=True, attr_name="rewards")
    # TODO: We need to specifiy this field
    missions = ListAttribute(null=True, attr_name="missions")
    share_link = UnicodeAttribute(null=True, attr_name="shareLink")
    total_participant_num = NumberAttribute(null=True, attr_name="totalParticipantNum")
'''

######################## EVENT ########################

    
# run
if __name__ == "__main__":
    app.run(host="localhost",port=8080,debug=False)
