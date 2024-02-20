# model/event.py : DynamoDB 데이터 모델, event 클래스. common.py의 BaseData 클래스 상속

import uuid # Universially Unique Identifier 고유값 부여 모듈
from model.common import BaseModel, get_current_time_utc
#from model.index import DataPKIndex, DataSKIndex, InvertedIndex
#from model.mission import MissionMap
#from model.reward import RewardMap
from pynamodb.attributes import (ListAttribute, MapAttribute, NumberAttribute,
                                 UnicodeAttribute, UTCDateTimeAttribute)


def create_pk():
    return str(f'EVENT#{uuid.uuid4()}')
# 'USER#' 접두사 + UUID 로 고유한 파티션키 생성

def create_sk():
    return str("METADATA")
# 정렬키값 생성

class Event(BaseModel, discriminator="event"): # event 데이터모델 정의 클래스
    pk = UnicodeAttribute(hash_key=True, attr_name="PK",
                          default_for_new=create_pk) 
    # pk , 없을시 클래스함수로 생성
    sk = UnicodeAttribute(range_key=True, attr_name="SK",
                          default_for_new=create_sk) 
    # sk , 없을시 클래스함수로 생성
    created_at = UTCDateTimeAttribute(
        default=get_current_time_utc, attr_name="createdAt") 
    #생성시간
    data = UnicodeAttribute(null=True, attr_name="data")
    #이벤트데이터
    title = UnicodeAttribute(null=True, attr_name="title") 
    #이벤트제목
    description = UnicodeAttribute(null=True, attr_name="description") 
    #설명
    image_url = UnicodeAttribute(null=True, attr_name="imageUrl") 
    #이미지 url
    started_at = UTCDateTimeAttribute(null=True, attr_name="startedAt") 
    #이벤트시작시각
    ended_at = UTCDateTimeAttribute(null=True, attr_name="endedAt") 
    #이벤트종료시각
    is_active = UnicodeAttribute(null=True, attr_name="isActive") 
    #활성화상태
    #rewards = ListAttribute(null=True, of=RewardMap, attr_name="rewards") 
    #리워드(리스트)
    #missions = ListAttribute(null=True, of=MissionMap, attr_name="missions") 
    #미션(리스트)
    share_link = UnicodeAttribute(null=True, attr_name="shareLink") 
    #공유링크
    total_entry_point = NumberAttribute(null=True, attr_name="totalEntryPoint") #총부여점수
    total_participant_num = NumberAttribute(
        null=True, attr_name="totalParticipantNum")
    #총참여자수
    event_id = UnicodeAttribute(null=True, attr_name="eventId") 
    #이벤트아이디
    user_id = UnicodeAttribute(null=True, attr_name="userId") 
    #이벤트생성자 아이디
    service_agreement = UnicodeAttribute(
        null=True, attr_name="serviceAgreement")
    #서비스동의상태