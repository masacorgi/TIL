# 인증, 인가에 대하여
* JWT 토큰 , 세션 같이 인증/인가와 관련된 부분 한번 살펴보기
* Authz / Authn 이라고 부르는게 둘이 무슨 차이인지
* FastAPI 에서 보통 인증/인가 코드 어떻게 구현하는지

목차

1. 인증과 인가(Authn, Authz)
2. JWT 토큰과 세션
3. FastAPI에서의 인증/인가 구현



## 인증과 인가 (Authn, Authz)
인증과 인가는 비슷하게 들릴 수도 있지만 IAM(Identity and Access Management) 환경에서는 명확히 구분되는 서로다른 보안 프로세스이다.

인증(Authn, Authentication)은 사용자의 '신원을 검증'하는 행위로서 보안 프로세스의 첫번째 단계이다.
주로 비밀번호, 일회용 핀, 인증 앱, 생체인식 등의 1개 이상의 인증요소를 성공적으로 확인해야만 인증 단계를 넘게 한다.

인가(Authz, Authorization)는 사용자에게 특정 리소스나 기능에 액세스 할 수 있는 '권한을 부여'하는 프로세스로, 액세스제어나 권한제어 등으로 불리기도 한다.<br>

대표적으로 서버의 특정파일 다운로드 권한, 특정부분 액세스 권한, 애플리케이션 관리자 권한 액세스 등등 다양하게 나누어 설계한 권한을 부여하는 과정이다.

간단히 예시를 들어 요약하면 다음과 같다.

1. 로그인(보안 프로세스)에서 
2. ID/비밀번호 사용, 자격증명 입증 -> 인증 Authn
3. 서버가 일반or관리자 권한 부여 -> 인가 Authz


## JWT 토큰과 세션

### JWT
JWT는 JSON Web Token으로, 웹에서 정보를 안전하게 전송하기 위한 토큰 기반의 표준으로, RFC 7519에 정의되어 있다.

JWT는 주로 사용자 인증에 활용되며, 서버로 전송된 JWT는 서버가 해당 토큰을 검증하여 클라이언트의 정체성을 확인하고, 클라이언트에게 안전하게 정보를 전달한다.

특히, JWT는 토큰 자체에 필요한 정보를 포함하고 있어서 서버 측에서 데이터베이스를 조회하지 않아도 클라이언트의 요청을 처리할 수 있다.

JWT는 다음 세가지 부분으로 이루어져 있다.

1. Header
    
    토큰의 유형과 알고리즘 등의 메타데이터 포함

2. Payload
   
   클레임(claim)이라 불리는 데이터 조각들을 포함
   클레임은 사용자 ID, 권한등 정보의 조각이다.

3. Signature
   
   Header와 Payload의 조합을 서명하여 토큰이 유효한지 검증

### Session
세션은 서버와 클라이언트 간의 상태를 유지하고, 클라이언트의 요청에 대한 상태를 기억하는 메커니즘이다.

세션은 다음과 같은 흐름으로 동작한다.
1. 사용자의 로그인 - 서버는 고유한 세션 ID를 생성하고 클라이언트에게 전송
2. 클라이언트는 해당 세션ID를 쿠키나 URL 매개변수 등을 통해 저장하고, 각 요청에서 서버로 세션ID를 제공해 세션 상태를 유지
3. 서버는 세션ID를 통해 클라이언트의 상태를 기억하고, 사용자를 인증하고 인가를 수행한다.

세션은 서버에 저장되어 클라이언트에게는 세션ID만 전달되므로 보안상 JWT보다 안전하다고 볼 수 있다.

그러나 서버에 상태를 저장해야 하므로 확장성 측면에서는 일부 제약이 있을 수 있다.

### 둘 중 선택해야 한다면

세션은 상태유지(Stateful) 특성이 있다.
서버가 상태를 저장하므로 클라이언트가 추가적인 관리를 할 필요가 없다. 서버에 상태를 저장하므로 확장성에 제약이 있을 수 있지만, 상태관리에 대한 부담을 덜 수 있다.

반대로 JWT는 무상태(Stateless)적이며, 서버가 토큰 자체에 정보를 저장하지 않으므로 확장성이 뛰어나다.
하지만 클라이언트에서 토큰을 저장하고 관리해야 하며, 이에 따라 토큰이 유출될 경우에는 보안상 문제가 발생할 수 있음을 유념해야 한다.
<br>
<br>

## FastAPI 에서의 인증/인가 구현

FastAPI에서는 fastapi.security 라이브러리와 OAuth2 라이브러리를 이용해 사용자 인증을 구현할 수 있다.

1. OAuth2 설정 및 모델 정의

    OAuth2를 위한 설정 및 모델 정의(클라이언트 ID, 클라이언트 시크릿, 허용된 범위)

   1. OAuth2 스키마 정의, 해당 스키마를 사용하여 클라이언트 정보 및 토큰 엔드포인트를 설정

```python
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

# OAuth2 스키마 정의
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl="token",  # 토큰을 받을 엔드포인트 설정
    scopes={"read": "Read access", "write": "Write access"}  # 허용된 범위 설정
)

```

   2. 사용자 모델 정의
```python
from pydantic import BaseModel

# 사용자 모델 정의
class User(BaseModel):
    username: str
    password: str

```

1. 인증 메커니즘 구현(Depends 사용)

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi_users import FastAPIUsers, models
from fastapi_users.db import TortoiseUserDatabase

# OAuth2 설정
oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="token")

# 사용자 모델 정의
class User(models.BaseUser):
    pass

# FastAPI-Users 라이브러리를 사용하여 사용자 데이터베이스 설정
user_db = TortoiseUserDatabase(UserDB, UserModel)
fastapi_users = FastAPIUsers(
    user_db,
    [oauth2_scheme],
    User,
    UserModel,
)

# 의존성을 사용한 인증 메커니즘
def get_current_user(current_user: User = Depends(fastapi_users.get_current_user)):
    return current_user

```
<br>
<br>

3. 인가 메커니즘 구현(데코레이터를 엔드포인트에 적용, 권한있는지 확인)


```python
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer

app = FastAPI()

# 데코레이터를 사용하여 인가 메커니즘 구현
def get_current_user(token: str = Depends(oauth2_scheme)):
    # 사용자 확인 로직
    # 예: 토큰 디코딩 및 사용자 반환
    pass

@app.get("/secure-endpoint")
def secure_endpoint(current_user: User = Depends(get_current_user)):
    # 사용자에게 허용된 동작 수행
    return {"message": "This is a secure endpoint"}

```


젤 중요한건 인증/인가가 어떻게 다른건지

방법은 세션, 쿠키, JWT 종류는 다양하다.

우리는 지금 코그니토를 쓰고있음 JWT방식
카카오나 구글 연동은 OIDC(Oauth2 비슷)

중요하게 생각해야될거는 가입할때 비밀번호치라고 하자나
그거를 평문으로 치라고 하는데 그걸 우리가 평문으로 알게되면 법적으로 문제가 생김
또 해킹 당하면 난리가 남

지금 작업할거는??

지금 질문답변하는 기능 구현하고 있는데 그거 분리작업하는게 좋을것 같긴한데 단순작업이라 고민,,

모델이라는 코드를 보면 다이나모에서 쓰는 코드랑 파이댄틱이랑 섞여있음
이거 분리하는거 노가다,,,ㅋㅋㅋㅋ 하기는 할거임

개선해야될 부분은 crud부분에 라우터코드에는 crud어떤 함수 호출할지만 연결해놓은 상태

CRUD 코드들 안에서 리펙터링 할만한 부분이 있는지
리팩터링 중점은 공통적으로 중복되는 코드가 있으면
그거를 함수로 만들어서 공통적으로 사용할 수 있게

그 외 뭔가 리펙터링할 부분이 있다면 (네이밍/가독성/중복제거)
