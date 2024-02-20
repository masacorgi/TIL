# model/user.py : DynamoDB 데이터 모델, user 클래스. common.py의 BaseData 클래스 상속

import uuid # Universially Unique Identifier 고유값 부여 모듈
from common import BaseModel, get_current_time_utc # model/common.py
from pynamodb.attributes import (UnicodeAttribute,UTCDateTimeAttribute)


def create_pk(): 
    return str(f'USER#{uuid.uuid4()}')
# 'USER#' 접두사 + UUID 로 고유한 파티션키 생성

def create_sk():
    return str("METADATA")
# 정렬키값 생성

class User(BaseModel, discriminator="user"): # user 데이터모델 정의 클래스
    pk = UnicodeAttribute(hash_key=True, attr_name="PK",
                          default_for_new=create_pk) 
    # pk , 없을시 클래스함수로 생성
    sk = UnicodeAttribute(range_key=True, attr_name="SK",
                          default_for_new=create_sk) 
    # sk , 없을 시 클래스함수로 생성
    created_at = UTCDateTimeAttribute(
        default=get_current_time_utc, attr_name="createdAt") 
    #생성시각 common.py 시간획득함수 사용
    email = UnicodeAttribute(null=True, attr_name="email") 
    #유저이메일
    data = UnicodeAttribute(null=True, attr_name="data") 
    #유저데이터
    name = UnicodeAttribute(null=True, attr_name="name") 
    #닉네임
    phone = UnicodeAttribute(null=True, attr_name="phone") 
    #유저전화번호
    is_active = UnicodeAttribute(null=True, attr_name="isActive") 
    #활성화상태
    user_id = UnicodeAttribute(null=True, attr_name="userId") 
    #유저아이디
    
    