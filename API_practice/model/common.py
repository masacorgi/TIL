# model/common.py : DynamoDB 데이터 모델 클래스 중 가장 부모클래스 BaseModel 정의

from datetime import datetime, timezone
from pynamodb.attributes import (AttributeContainer, DiscriminatorAttribute,
                                 ListAttribute, NumberAttribute,
                                 UnicodeAttribute, UnicodeSetAttribute,
                                 UTCDateTimeAttribute)
from pynamodb.indexes import Index
from pynamodb.models import MetaModel, Model


def get_current_time_utc():
    return datetime.now(timezone.utc)


# 다른 모델의 부모 베이스모델 클래스
class BaseModel(Model):
    class Meta:
        region = "ap-northeast-2"
        table_name = "study-application"
    
    # index
    pk = UnicodeAttribute(hash_key=True, attr_name="PK") # 해시키
    sk = UnicodeAttribute(range_key=True, attr_name="SK") # 정렬키
    data = UnicodeAttribute(null=True, attr_name="data")
    entity = DiscriminatorAttribute(attr_name="entity")
    created_at = UTCDateTimeAttribute(
        default=get_current_time_utc, attr_name="createdAt")
    #생성시간 저장
    
    #스태틱메소드(상속관계없이 모두 사용가능)
    @staticmethod
    def to_dict(attr): # 해당 어트리뷰트를 딕셔너리형으로 변환
        if attr is None or isinstance(attr, Index): #인덱스형이거나 없을경우 none 반환
            return None
        elif isinstance(attr, AttributeContainer):
            return {key: BaseModel.to_dict(val) for key, val in attr.attribute_values.items() if key != "entity"}
        elif isinstance(attr, ListAttribute) or isinstance(attr, list):
            return [BaseModel.to_dict(val) for val in attr]
        elif isinstance(attr, MetaModel):
            return None
        else:
            return attr