from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.connection.base import Connection
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection

# PynamoDB 모델 정의
class MyModel(Model):
    class Meta: #Meta 클래스 내에서 모델의 설정을 지정
        table_name = 'Music_test'  # 테이블 이름 설정
        region = 'ap-northeast-2'  # 원하는 AWS 지역으로 설정

    # 테이블의 속성 정의
    hash_key = UnicodeAttribute(hash_key=True) #PK 파티션키 : Artist
    range_key = UnicodeAttribute(range_key=True) #SK 정렬키 : SongTitle
    #data = UnicodeAttribute()

# DynamoDB 테이블 생성
if not MyModel.exists(): #해당 테이블이 없을 경우
    MyModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
# wait=True : 테이블 생성이 완료될 때까지 대기

# 아이템 생성 및 저장
item = MyModel('artist_1', 'song_1')
item.save()

# 다른 아이템 추가
item2 = MyModel('artist_2', 'Another piece of data')
item2.save()

# 아이템 조회
item = MyModel.get('artist_1','song_1')
# 조회한 아이템 파싱,출력
print("Hash Key:",item.hash_key)
print("Range Key: ",item.range_key)