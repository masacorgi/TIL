# Test Code

백엔드, 혹은 소프트웨어 개발시 테스트 코드가 무엇인지 조금 알아보기 테스트에는 unit test , end to end test 등의 여러가지 테스트 종류도 존재합니다.

우리 백엔드 테스트 코드는 unit test 기반으로 하게 될 것이구요.
파이썬에서의 테스트코드 프레임워크인 pytest에 대해서 조금 알아보시고! fastapi 에서의 테스트코드 짜는것도 한번 알아보시면 좋겠습니다.

앞으로 작성해야할 테스트코드는 크게 3가지 정도 있을 것 같아요.

* pynamodb 모델이 정상 동작하는지에 대한 테스트 코드
* FastAPI 테스트 클라이언트를 통해 실제로 우리 백엔드앱에 CRUD 요청을보내고, 우리가 원하는 동작을 하는지 테스트하기 위한 코드
* 그 외 비즈니스로직에 대한 코드

추가적으로 설명드리자면 이 테스트 코드를 돌릴때에는 아마존 DynamoDB를 쓰지 않고, 로컬버전 DynamoDB 를 도커로 띄워서 테스트하고 내리는 그런 코드를 사용해서 테스트 할 예정입니다. 
따라서 Docker로 DynamoDB 로컬 버전을 띄워보시고, 한번 로컬 DynamoDB 에 요청을 어떻게 보낼수 있는지. (boto3 , PynamoDB 등등) 테스트 해보시는 것도 좋을것 같아요.

--------------------------------------------------------------
<br>
<br>

목차

1. 테스트 코드란?
2. 테스트 코드의 종류
3. 단위테스트(Unit Test)
4. pytest
5. FastAPI 에서의 pytest

<br>
<br>
<br>


## 1. 테스트 코드란?

테스트 코드는 소프트웨어 품질을 향상시키기 위해 사용되는 코드이다.

개발자들은 주로 자신이 작성한 코드가 의도한 대로 동작하는지 확인하고,
코드 변경이나 개선 작업을 수행할 때
이전 기능들이 영향을 받지 않도록 보장하기 위해 테스트 코드를 작성한다.<br>
테스트 코드를 작성하면 코드의 안정성과 신뢰성을 높일 수 있고,
코드를 더 쉽게 유지보수하거나 확장할 수 있다.

### 테스트 코드의 장점

* 개발 과정 중 예상치 못한 문제를 미리 발견 가능
* 코드 변경 시 기존 기능에 영향을 미치는지 빠르게 확인 가능
* 코드 수정이나 리팩토링 시 안정성 유지
* 코드의 신뢰성 향상
* 개발 문서로서의 역할 가능
* 개발자 간 협업 및 코드 이해 용이성 증가
  
테스트 코드를 작성할 때는 코드의 경계조건, 예외상황, 정상동작 등 다양한 시나리오를 고려하여 테스트 케이스를 작성하는 것이 중요하다.


## 2. 테스트 코드의 종류

1. 단위 테스트 (Unit Test)
    
    개별 함수, 메소드 또는 모듈 단위의 독립적 기능 테스트.<br>
    언어별로 지원하는 테스트 프레임워크를 사용하여 테스트 케이스를 작성, 함수 또는 메소드가 기대한 대로 동작하는지 확인한다.

    "어떤 기능이 실행되면 어떤 결과가 나온다" 정도로 테스트 목적을 갖고 작성한다.

2. 통합 테스트 (Integration Test)

    여러 모듈 또는 컴포넌트들이 함께 제대로 동작하는지 확인한다.<br>
    시스템 부분들 간 상호작용을 테스트하여 전체적인 통합 상태를 확인한다.

    통합 테스트는 각 모듈에 대한 설정 또는 사전 조건이 필요한 경우가 많기 때문에 단위 테스트보다 테스트 코드 작성이 복잡하다.<br>
    하지만 단위 테스트보다 더 넓은 범위의 종속성까지 테스트하기 때문에 단위 테스트보다 더 유의미한 테스트가 되는 경우가 많다.

3. 시스템 테스트 (System Test)

    전체 시스템이 예상대로 동작하는지 확인하는 테스트.
    사용자의 관점에서 시스템의 기능을 테스트하며, 비즈니스 요구사항을 충족하는지 확인한다.
    UI 테스트, 성능 테스트, 안전성 테스트 등이 해당된다.

    이중 UI 테스트는 실제 클라이언트가 사용하는 화면에 대한 테스트를 진행하여 서비스의 기능이 정상적으로 작동하는지를 검증한다.

    실제 애플리케이션을 사용하는 사용자의 흐름에 대해 테스트함으로써 UI 변경사항으로 인해 발생할 수 있는 문제를 사전에 차단하여 앱의 신뢰도를 높일 수 있다.



## 3. 단위 테스트 (Unit Test)

일반적으로 개발시 테스트를 작성한다고 하면 단위 테스트를 의미한다.

통합 테스트는 실제 여러 모듈간의 상호작용을 테스트하기 때문에 모든 모듈들이 준비가 된 상태에서 테스트를 하게 된다.<br>
그렇기에 통합 테스트를 위해서는 캐시나 데이터베이스 등 다른 컴포넌트들과 실제 연결을 해야 하고, 시스템을 구성하는 컴포넌트들이 많아질 수록 테스트를 위한 비용과 시간이 상당히 많이 소요된다.

반면에 단위테스트는 해당 기능과 메소드만 독립적으로 테스트하기 때문에 어떤 코드를 리팩토링 하여도 빠르게 문제 여부를 확인할 수 있고 기능이 똑같이 동작하는지 확인할 수 있다.

다음은 Clean Code에서 정의한 좋은 단위테스트의 5가지 규칙, FIRST이다.

    1. Fast : 테스트는 빠르게 동작하여 자주 돌릴 수 있어야함
    2. Independent : 각각의 테스트는 독립적, 비의존적이어야 함
    3. Repeatable : 테스트는 어느 환경에서도 반복 가능해야 함
    4. Self-Validating : 테스트는 성공 or 실패의 결과를 bool 값으로 내어 자체적으로 검증되어야 함
    5. Timely : 테스트는 적시에 해야함(테스트 하려는 코드를 실제 구현하기 직전)

## 4. pytest

개발 시 테스트는 각 프로그램 언어마다 지원하는 테스트 프레임워크를 사용한다.

파이썬의 경우 unittest, pytest, nose 등의 테스트 프레임워크를 제공한다.<br>
간단히 unittest 는 파이썬 표준 라이브러리에 포함된 모듈로, 클래스를 만들고 테스트 메소드를 작성하는 방식으로 테스트를 구성한다.

pytest 는 unittest와 달리 추가적인 라이브러리나 클래스를 상속받지 않고도 간단한 문법으로 테스트를 작성할 수 있는 테스트 프레임워크이고, nose는 unittest와 pytest의 기능을 확장해서 테스트 디스커버리 및 실행, 테스트 결과보고서 등을 지원한다.

<br>
이 중 pytest는 unittest 모듈보다 더 간결하고 가독성이 뛰어나 많은 파이썬 개발자들이 이용하며, 다음은 pytest의 주요 특징이다.

* 간결하고 가독성 높은 문법
* 테스트 파일 자동탐지 및 실행 : 특별한 규칙 필요 없이 test_ 로 시작하는 파일/함수를 실행함
* assert문 사용 자동검증
* Fixture 지원
* 매개변수화 된 테스트 : 동일한 테스트를 여러번 실행하고 다른 매개변수를 사용하여 테스트 수행 가능
* 풍부한 플러그인 : 다양한 플러그인 제공으로 테스트 환경 확장, 맞춤화 가능
* 다양한 테스트 타입 지원 : 단위테스트, 함수테스트, 모듈테스트 ..
* 파이썬 코드와의 호환성 : 기존 unittest, doctest와의 호환성으로 기존 코드를 쉽게 통합할 수 있음

<br>
다음은 간단한 pytest 예시이다.

테스트할 파이썬 파일 (ex. calculator.py)
```py
def add(x,y):
    return x + y
```
테스트 파일 (ex. test_calculator.py)
```py
from calculator import add

def test_add():
    result = add(2, 3)
    assert result == 5
```
실행은 터미널에서 pytest라는 명령어 입력으로 간단히 수행할 수 있다.<br>
pytest 명령어가 입력되면 파이썬은 자동으로 test_ 로 시작되는 파일을 찾아 테스트를 수행하고 결과를 반환한다.
<br>
<br>

## 5. Fast API 에서의 테스트코드

다음은 Fast API에서 pytest를 사용하는 간단한 예시이다.

테스트할 main.py : <br>
root(), read_item(), create_item() 세가지 API 함수가 정의되어 있다.

```py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The   bartenders"},
}

class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

@app.get("/")
async def root():
    return {"msg": "Hello World"}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return fake_db.get(item_id, None)


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already   exists")

    fake_db[item.id] = item
    return item
```
<br>


Fast API는 자체적으로 테스트 유틸리티 또한 제공한다.<br>
아래와 같이 FastAPI 에서 제공하는 TestClient 객체를 사용하면 <br>
위에서 작성한 API 코드를 client 변수를 통해 요청하고
응답코드 및 json 결과값을 테스트 할 수 있다.

```py
from fastapi.testclient import TestClient
from src.api.main import app # 테스트 대상 임포트

client = TestClient(app)


# test_root() : root() API 함수에 대해 GET 방식으로 요청하여 테스트하는 테스트함수
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

# test_read_item(): read_item() API 함수에 대해 item_id가 1인 item을 params 값에 추가하여 GET 방식으로 요청하여 테스트하는 함수
def test_read_item():
    response = client.get("/items/foo", params={"item_id": "1"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }

# test_create_item(): create_item() API 함수에 대해 생성할 item을 json 값에 추가하여 POST 방식으로 요청하여 테스트하는 함수
def test_create_item():
    response = client.post(
        "/items/",
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }
```
