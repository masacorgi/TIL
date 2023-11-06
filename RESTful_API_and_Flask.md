RESTful API와 Flask
====================================================================
### 목차
1. RESTful API<br>
   1.1 RESTful API 란?<br>
   1.2 RESTful API의 설계<br>

2. Flask<br>
   2.1 Flask란?<br>
   2.2 Flask의 API 경로<br>
   2.3 Flask의 응답코드<br>
   2.4 Flask의 JSON 응답<br>

3. Swagger<br>
   3.1 Swagger란?<br>
   3.2 Swagger 문서란?<br>


1.RESTful API
--------------------------------------------------------------------
<br>

### 1.1 RESETful API 란?

대부분의 비즈니스 애플리케이션은 다양한 작업을 수행하기 위해 다른 내부 애플리케이션, 서드 파티 애플리케이션과 통신해야 한다.<br>
RESTful API는 두 컴퓨터 시스템이 인터넷을 통해 정보를 안전하게 교환하기 위해 사용하는 인터페이스이다.<br><br>

REST는 Roy Fielding이 정의한 네트워크 통신을 위한 소프트웨어 아키텍처이다.<br> 
처음에 인터넷과 같은 복잡한 네트워크에서 통신을 관리하기 위한 지침으로 만들어졌고, REST기반 아키텍처를 사용해서 대규모의 고성능 통신을 안정적으로 지원할 수 있게 되었다.<br>
다음은 REST 아키텍처의 주요 특징 및 원칙이다.

    자원(Resource) : 모든것을 자원으로 표현한다.

    표현(Representation) : 자원은 여러 표현(형식)으로 사용된다. 

    통일적 인터페이스(Uniform Interface) : 통일된 인터페이스를 사용해야 한다.

    상태없음(Statelessness) : 각 요청은 독립적이며 상태를 유지하지 않는다. 클라이언트가 모든 필요한 정보를 요청에 포함한다.

    계층화(Layered System) : REST 아키텍처는 다중 계층으로 구성된다. 클라이언트는 서버와 직접 통신하지 않고 중간 계층 (로드밸런서, 캐시서버)를 통해 통신할 수 있다.

<br><br>
API(Application Programming Interface)는 다른 소프트웨어 시스템과 통신하기 위해 따라야 하는 규칙이다. 개발자는 다른 앱이 프로그래밍 방식으로 앱과 통신할 수 있도록 API를 표시하거나 생성한다.<br>
API를 통해 특정 기능이나 데이터에 접근할 수 있게 표준화된 방법이 제공되면 다른 개발팀이 그 API를 사용해 데이터나 기능을 공유받을 수 있다.
<br>
<br>
<br>
RESTful API는 데이터 송수신에 최적화된 아키텍처인 REST를 도입하여 만든 API로, 다음과 같은 특징을 가진다.

    자원(Resource) : RESTful API는 자원을 제공하며, 이러한 자원은 고유한 식별자(URI)를 가지고 있다.

    표현(Representation) : RESTful API는 자원의 상태를 나타내는 표현을 제공한다. 일반적으로 JSON, XML, HTML과 같은 형식으로 데이터를 표현한다.

    통일적 인터페이스(Uniform Interface) : RESTful API는 통일된 인터페이스를 제공해서 일관된 규칙을 따르도록 한다. 이로써 Client - Server 간 통신이 단순하고 예측 가능해진다.

    상태없음(Statelessness) : RESTful API는 요청 간에 상태를 유지하지 않으며, 각 요청은 독립적이고 모든 필요한 정보를 포함해야 한다. 서버는 클라이언트의 상태를 저장하지 않는다.

    HTTP method : HTTP 프로토콜의 다양한 메서드 (GET,POST,PUT,DELETE)를 사용해서 자원을 조작한다.(CRUD 작업)
<br>
한마디로 RESTful API는 자원을 URI로 식별하고, HTTP 메소드를 사용해서 CRUD 작업을 할 수 있게 하는 설계이다.
<br><br><br>

### 1.2 RESTful API의 설계

RESTful API는 위에서 설명한 특징을 다음과 같은 설계를 통해 만족시켜야 한다.<br>

1.URI 설계 : <br>
* 자원을 URI로 나타낸다. 명확하고 직관적인 계층구조로 자원을 나타내야한다.<br>
* 복수형 '명사'를 사용하는 것이 일반적이다. 동사는 사용하지 않고, HTTP method를 통해 행위를 구분한다. <br>
* ex)____/getUser (x),   _____/users (o)
* 대문자를 사용하지 않는다.
* _(underbar) 대신 -(dash)를 사용한다.
* 마지막에 '/'를 포함하지 않는다.

2.HTTP 메소드 활용 :<br>
* HTTP 메소드를 사용해서 CRUD 작업을 수행한다.
* 메소드와 URI 경로(자원)을 조합해서 작업을 수행한다.

3.표현의 다양성 : 
* 다양한 형식의 표현을 지원한다. 주로 JSON 데이터를 반환

4.상태없음 : 
* API 요청 간에 상태정보를 공유하지 않는다. 모든 필요한 정보는 요청 자체에 포함시킨다.

5.보안 :
* 인증 및 권한 부여를 통해 API를 보호한다. HTTPS를 사용해 통신을 암호화하고 민감한 정보는 인증과 권한부여를 세세하게 조정한다.
* 비정상적인 방법(Dos, Brute-force attack)으로 API를 이용하려는 경우 429-Too Many Request 오류응답과 함께 일정 시간 뒤 요청할 것을 나타낸다.

6.명확한 문서화 :
* API의 목적, 자원, 엔드포인트(API경로), 매개변수, 응답 등을 자세히 문서화하여 사용자나 개발자에게 이해하기 쉽게 설명한다.
  

<br>

2.Flask
--------------------------------------------------------------------
### 3.1 Flask란?
Flask는 Python 웹 애플리케이션 및 RESTful API를 만들기 위한 경량 웹 프레임워크이다.<br><br>

### 3.2 Flask의 API 경로
Flask에서 API경로는 URL규칙을 사용해서 정의된다. API경로는 Flask 앱을 작성할 때<br>
@app.route() 의 데코레이터를 사용해서 정의된다.
```python

    app = Flask(__name__)

    @app.route('/test/resource', methods=['GET'])
    def get_resource():
        # API 경로 '/test/resource'에 해당하는 요청 처리 로직
        return 응답

    if __name__ == 'main': 
        app.run()
```
위와 같이 api 경로를 설정하고, methods 파라미터를 사용해서 HTTP method에 따른 방식을 분리하여 설정할 수 있다. (작성하지 않을 시 default는 GET이다.)
<br><br>

### 3.3 Flask의 응답코드
웹 어플리케이션에서 응답코드는 HTTP 요청에 대한 서버의 처리결과를 나타내주는 부분이다.<br>
응답코드(상태코드, Status Code)는 HTTP response에 담겨 제공되는데,<br>
Flask에서는 make_response() 함수를 이용하거나 리턴 시에 직접 반환값을 설정해서 제공할 수 있다.
```python
    app = Flask(__name__)

    @app.route('/test/resource', methods=['GET'])
    def get_resource():
        # API 경로 '/test/resource'에 해당하는 요청 처리 로직
        response = make_response(응답,200)  #응답결과와 상태코드 부착
        return response

    @app.route('/test/resource2', method=['GET'])
    def get_resource2():
        # API 경로 '/test/resource2'에 해당하는 요청 처리 로직
        return 응답, 200                    #리턴시에 바로 상태코드 첨부

    if __name__ == 'main': 
        app.run()
```
<br>

### 3.4 Flask의 JSON 응답
Flask는 Python 기반으로 동작하는 웹 앱 프레임워크이기 때문에, 파이썬의 문법을 사용한다. <br>
Python 에서는 딕셔너리 자료형이 있고 이것은 JSON의 형식과 매우 유사하기 때문에 상호 변환이 매우 간편하고 유용하다.<br>
flask 라이브러리의 jsonify를 import 하면 딕셔너리나 리스트의 데이터를 JSON형식으로 변환할 수 있다.
```python
    @app.route('/api/data', methods=['GET'])
    def get_data():
    data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    return jsonify(data)

```

jsonify를 사용하면 Flask가 JSON형식의 응답을 생성하며 필요한 HTTP헤더(Content-Type)또한 설정한다.<br>
파이썬 객체(딕셔너리, 리스트)를 JSON으로 직렬화할때 데이터를 보다 쉽게 다룰 수 있으며, 필요한 겨우 상태코드와 다른 헤더정보도 설정할 수 있다.


백엔드의 웹 API는 웹 프론트엔드나 모바일 앱처럼 HTML을 이용하여 페이지를 렌더링하는 것이 목적이 아니라 다른 애플리케이션(프론트엔드, 모바일 앱)이 데이터에 엑세스할 수 있도록 하는 것이기 때문에 HTML 템플릿 렌더링을 위한 코드나 리소스는 불필요하다.

JSON 응답은 이러한 백엔드 API의 목적에 이상적이며, 위에서 설명한 Flask의 jsonify를 이용하여 간단하게 반환할 수 있다.
<br>
<br>
<br>


4.Swagger
--------------------------------------------------------------------

### 4.1 Swagger란?
Swagger는 개발한 RESTful API를 편리하게 문서화하고 관리하거나 제3 사용자가 편리하게 api를 호출해보고 테스트할 수도 있는 작업도구(오픈소스 프레임워크)이다.<br>
API의 형식, 동작, 매개변수, 응답 등을 자동으로 문서화하고 시각화하는데 도움을 준다.
<br>

Swagger는 다음과 같은 요소로 구성되어있다.
    
    Swagger UI : 웹 기반 인터페이스로 직관적이다. API문서를 시각화하고 탐색할 수 있게 하며 API엔드포인트(자원경로)를 테스트하거나 호출해볼 수 있다.
    
    Swagger Specification(스펙) : API에 대한 자세한 설명과 메타데이터를 포함하는 문서.
    API의 엔드포인트, HTTP메소드, 매개변수, 응답을 정의한다.
    YAML 이나 JSON으로 작성함

    Swagger Editor : API 스펙을 작성하고 편집하는 온라인도구.


<br><br>

### 4.2 Swagger 문서란?
Swagger 문서는 Swagger 또는 OpenAPI Specification을 따라 작성된 API의 자세한 설명 및 문서화된 정보를 포함하는 문서이다.<br>
이 문서는 API를 설명하고 API엔드포인트, HTTP메소드, 매개변수, 응답 및 기타 메타데이터에 대한 정보를 제공한다.

++ Swagger는 초기 API 스펙 및 문서화 도구의 이름이고, OpenAPI는 이 스펙을 개선하고 표준화한 것으로 Swagger스펙에 따른 API 문서는 OpenAPI 스펙에 적용되며, 많은 개발자 및 조직이 OpenAPI 스펙을 이용하여 API문서를 관리하고 있다.

