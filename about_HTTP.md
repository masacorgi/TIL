HTTP란 무엇인가?
====================================================================
### 목차
1. [HTTP란?](#1.HTTP란?)
2. [HTTP의 동작](#2.HTTP의-동작)
3. [HTTP Status Code](#3.HTTP-Status-Code)
   
   3.1 Status Code?
   
   3.2 Status Code의 종류
   
   3.3 백엔드가 잘 알아야 하는 이유
4. [HTTP method](#4.HTTP-method)

    4.1 HTTP 메소드란

    4.2 HTTP 메소드의 종류별 의미와 기능
5. [HTTP 메시지 예시](#5.HTTP-메시지-예시)


1.HTTP란?
---------------------------------------------------------------------
#### HTTP란 무엇인가?
HTTP는 Hyper Text Transfer Protocol의 줄임말로, 인터넷 데이터 통신규약이다.

인터넷 상에서 주고받는 데이터의 형식을 규칙으로 정함으로써 서로 다른 사람과 조직이 만든 프로그램이 인터넷을 통해 데이터를 주고 받을 수 있다.

컴퓨터는 네트워킹에서 TCP/IP 프로토콜을 이용한다.<br>
이것을 기반으로 동작하는 응용 프로토콜에는 다음과 같은 프로토콜이 있다. 

* FTP(파일전송) 

* SMTP,POP3,IMAP(이메일, 웹메일)

* HTTP(인터넷데이터통신)

HTTP는 이중 가장 널리 이용되며, 웹 브라우징 및 웹 애플리케이션과 관련된 데이터(HTML과 다양한 멀티미디어 자원)을 송수신 하는데 사용된다. 
<br><br>


2.HTTP의 동작
---------------------------------------------------------------------
#### HTTP는 어떻게 동작하는가?

HTTP는 기본적으로 Client(이용자)가 Server(제공자)에게 데이터를 요청하고 응답받는 방식이다.

#### Client -> Server
클라이언트는 서버에게 응답받고 싶은 자원에 대한 HTTP요청을 전송한다.<br>
요청은 다음과 같은 요소를 포함하여 전송한다.<br>
* 요청 방식(GET,POST,PUT,DELETE,PATCH)
* 요청 URI : 자원의 경로
* HTTP Header : 요청의 메타데이터(전반적 정보)
* 요청 본문(필요시에만) : 요청방식중 POST와 같이 데이터를 서버로 전송할 시

#### Server Processing
요청을 받은 서버는 해당 요청에 대해 처리(processing)한다.<br>
서버는 요청에 대해 자원을 찾아내거나, 동적으로 생성하여 응답을 준비한다.<br>
이 때 서버는 DB나 다른 서비스를 이용해 데이터를 검색하거나 가공한다.

#### Server -> Client
웹 서버는 클라이언트에게 준비된 자원을 HTTP메시지로 응답한다.<br>
응답(Response)는 다음과 같은 요소를 포함한다.
* HTTP Status Code(상태코드) : 요청의 성공 또는 실패 등 처리 결과에 대한 상태
* HTTP Header : 응답의 메타데이터(전반적 정보)
* 응답 본문 : 요청된 자원

HTML 페이지만이 HTTP 통신으로 얻을 수 있는 유일한 자원이 아니다.<br>
Plain text 데이터로부터 JSON 형식 데이터나 XML과 같은 형식의 데이터 또한 주고받을 수 있다.

클라이언트는 서버로부터 받은 응답을 이용하여 웹 페이지를 랜더링하거나(브라우저의 경우), 다시 데이터를 가공하여 이용할 수 있다.


3.HTTP Status Code
---------------------------------------------------------------------
#### 3.1 Status Code?
HTTP Status Code(상태코드)는 세자리 숫자로 이루어져 있다.<br>
서버의 Request에 대한 처리결과(성공 또는 실패)를 나타내어 Response에 담겨 제공된다.<br>
요청 처리에 실패했을 경우 실패의 원인을 알려준다.<br>

클라이언트와 서버는 Status Code를 보고 주로 실패 원인을 파악하는데 이용한다.

#### 3.2 Status Code의 종류
세자리 숫자로 이루어진 HTTP Code는 첫번째 숫자로 대략적인 큰 의미를 제공한다.
* 1XX : 조건부 응답. 요청을 받았으며 작업을 계속한다.
* 2XX : 성공. request를 수신, 이해했으며 처리를 완료했다.
* 3XX : 클라이언트는 요청을 마치기 위해 추가 동작을 취해야 할것.
* 4XX : 요청오류. 클라이언트의 요청에 오류가 있어 처리에 실패했다.
* 5XX : 서버오류. 서버의 처리에 오류가 있어 처리에 실패했다.

<br>
다음은 자주 나타나는 HTTP Code에 대한 예시이다.

    100 Continue : 임시적인 응답. 지금까지의 상태가 괜찮고 클라이언트가 계속해서 응답을 해도 된다. 이미 요청이 완료된 경우 무시해도 된다.
    103 Early Hints : Link 헤더와 함께 사용된다. 서버가 응답을 준비하는동안 client가 사전로딩을 할 수 있도록 하는 응답코드
    
    200 OK : 요청이 성공적으로 처리되었다. 
    201 Created : 요청이 성공적으로 처리되어서 리소스가 생성되었음
    204 No Content : 요청이 성공적으로 처리되었지만 컨텐츠를 제공하지 않는다.(API요청에서 주로 사용)

    400 Bad Request : 요청 자체가 잘못되었다. 요청메소드나 헤더, 본문이 잘못되었다.
    403 Forbidden : 요청을 거부한다. client가 권한이 없거나, 특정 ip 범위를 서버가 차단한 경우
    404 Not Found : 요청한 리소스가 없다.
    408 Request Timeout : 요청중 시간이 초과되었다.

    500 Internal Server Error : 서버에 오류가 발생해 처리하지 못했다.
    503 Service Temporarily Unavailable : 서비스를 일시적으로 사용할 수 없다.(주로 서버 과부화시)
    504 Gateway Timeout : 게이트웨이가 연결된 서버로부터 응답시간이 초과되었다.



#### 3.3 백엔드가 잘 알아야 하는 이유
HTTP 상태코드를 알맞게 사용하면 구체적으로 어떤 성공인지, 어떤 실패인지 확인할 수 있다.<br>
때문에 개발 시 잘 적용한다면 코드 리뷰는 물론 프런트엔드 개발자들이 API 호출 결과에 따른 예외처리를 구현하는데 훨씬 수월하게 할 수 있다.

이런 개발 시의 장점 외에도 권한 처리 관련 보안성 향상을 기대할 수 있고, 디버깅 및 모니터링을 쉽게 해주는 장점을 가진다.<br><br>

4.HTTP method
---------------------------------------------------------------------
#### 4.1 HTTP 메소드란?
HTTP Method 어떻게 쓰이고, 어떤 의미인지 (GET / POST / PUT / DELETE / PATCH )
HTTP 프로토콜은 request 시에 이미 정의되어 있는 HTTP 메소드 중 하나를 선택해서 주어진 리소스에 수행하길 원하는 행동을 나타낸다.

행동을 정의하는 HTTP 메소드를 통해 웹서비스와 RESTful API는 클라이언트와 서버간의 상호작용을 정의하고, 적절한 메소드를 통해 리소스를 요청/생성/업데이트/삭제(CRUD)할수 있도록 한다.


#### 4.2 HTTP 메소드의 종류별 의미와 기능
* GET : GET 메소드는 서버의 리소스를 가져올 때 사용한다. 서버는 GET으로 요청을 받을 시 응답으로 데이터를 반환한다. <br>GET메소드는 일반적으로 본문에 데이터를 포함하지 않으며, 브라우저의 uri를 통해 웹페이지를 요청할 때 사용한다.
  
* POST :  클라이언트에서 서버로 데이터를 제출하고 리소스를 생성할때 사용된다.<br>제출하는 데이터는 HTTP메시지 중 본문에 포함되어 전송된다.
  
* PUT : 서버의 리소스를 업데이트하거나 생성할때 사용한다. <br>HTTP메시지 본문에 업데이트할 데이터와 업데이트 대상 리소스의 URI를 포함한다. <br>기존 리소스를 교체하거나, 존재하지 않는 경우 새로 생성한다.
  
* DELETE : 서버의 리소스를 삭제할 때 사용한다.<br>본문에 데이터를 포함하지 않으며, 서버에 지정된 리소스를 삭제한다.

* PATCH : 서버 리소스의 부분만 업데이트할 때 사용한다. 전체 리소스를 교체하는 것이 아닌 부분만을 수정한다.
<br><br>

5.HTTP 메시지 예시
---------------------------------------------------------------
method GET 의 request 메시지 예시
    
    GET /example/page.html HTTP/1.1         //HTTP 메소드, 요청한 리소스의 uri, http버전
    Host: www.example.com                   //요청할 서버의 호스트명 or 도메인이름
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate, br
    Referer: https://www.google.com/
    Connection: keep-alive
    Cache-Control: max-age=0                //HTTP메시지 메타데이터


method POST 의 request 메시지 예시

    POST /submit-form HTTP/1.1              //HTTP 메소드,요청이보내질 리소스uri,http버전
    Host: www.example.com                   //요청할 서버의 호스트명 or 도메인이름
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 35      //본문 길이     //HTTP메시지 메타데이터

    username=johndoe&password=secretpass    //본문(데이터)

기본적인 response 메시지 예시
 
    HTTP/1.1 200 OK                         //http버전, status code
    Date: Thu, 01 Dec 2022 12:00:00 GMT     //response생성 날짜,시간
    Server: ExampleServer/1.0               //서버정보(버전)
    Content-Type: application/json          //본문의 미디어 형식
    Content-Length: 38                      //본문 길이

    {
        "status": "authorized"          //본문( html,xml,JSON 등 다양한 데이터 가능)
    }