# Reverse Proxy

목차

1. Reverse Proxy란 무엇인가?
2. Nginx


## 1. Reverse Proxy란 무엇인가?

Reverse Proxy는 클라이언트와 서버 간의 통신을 중계하는 서버이다.

클라이언트는 리버스 프록시를 통해 서버에 대한 요청을 보내며, 리버스 프록시는 이 요청을 받아서 백엔드 서버로 전달하고 응답을 클라이언트에게 반환한다.

이 과정에서 리버스 프록시는 클라이언트로부터 받은 요청을 수정하거나 필터링하여 백엔드 서버에 전달한다.

리버스 프록시는 여러 목적으로 사용되며, 주요 기능은 다음과 같다.

1. 로드 밸런싱 (Load Balancing)

    리버스 프록시는 클라이언트로부터 받은 요청을 여러 백엔드 서버로 분산시켜 부하를 균등하게 분배한다. 이를 통해 서버의 성능을 향상시키고 가용성을 높일 수 있다.

2. SSL 암호화 및 해독 (SSL Termination)

    클라이언트와의 통신에서 SSL 암호화를 해독하여 백엔드 서버와의 통신은 암호화되지 않은 상태로 처리한다.
    이를 통해 리버스 프록시가 SSL 인증서 관리를 담당하게 하므로 백엔드 서버에서 SSL 처리에 대한 부하를 줄일 수 있다.

3. 캐싱 (Caching)

    리버스 프록시는 이전에 처리한 요청의 응답을 캐시에 저장하여 동일한 요청이 들어올 경우 백엔드 서버에 요청을 전달하지 않고 직접 캐시된 응답을 반환한다.<br>
    이는 성능 향상과 트래픽 감소에 도움이 된다.

4. 보안 (Secruity)

    리버스 프록시는 웹 어플리케이션 방화벽을 통해 공격으로부터 보호하거나 IP주소 필터링, 접근 제어등의 기능을 제공해 보안을 강화할 수 있다.

5. 애플리케이션 캐시 및 압축 (Application-level Caching & Compression)

    리버스 프록시는 정적인 콘텐츠를 캐시하고 동적인 콘텐츠를 필요에 따라 동적으로 생성해서 응답의 속도를 향상시키고 대역폭을 절약한다.<br>
    또한 콘텐츠를 압축해서 효율적인 데이터 전송을 도모한다.

6. 로깅 및 모니터링 (Logging & Monitoring)

    클라이언트와 백엔드 서버간의 모든 트래픽을 기록하고 모니터링할 수 있기 때문에 시스템의 성능을 추적하고 문제가 발생할 시 문제 진단에 도움이 된다.

## 3. Nginx

Nginx는 오픈소스로 제공되는 웹 서버 및 리버스 프록시 서버로, 높은 성능과 안정성을 제공하는 소프트웨어이다. 가벼우면서도 동시 접속처리, 부하 분산, 캐싱, SSL/TLS 처리 등 다양한 기능을 지원하기 때문에 많은 웹 서버 및 애플리케이션에서 사용되고 있다.

Nginx는 비동기 이벤트 기반 아키텍처를 사용하기 때문에 많은 동시 접속을 효과적으로 처리할 수 있다. 또한 가벼운 용량으로 메모리 사용량을 적게 차지하기 때문에 적은 리소스로 높은 성능을 낼 수 있도록 도와준다.

또한 로드밸런싱, 리버스 프록시, SSL/TLS 처리, 가상 호스팅 등의 다양한 기능을 통해 애플리케이션의 효율적 활요에 도움을 줄 수 있다.

다만 Nginx는 주로 정적 파일 서빙에 특화되어 있어 동적 컨텐츠 처리에는 Apache등의 다른 웹서버보다 불리할 수 있으며 특히 Apache와 설정 파일이 다르고 구성이 다르기 때문에 처음 학습에 충분한 시간이 필요할 수 있다.


전반적으로 엔진엑스는 가벼우면서도 높은 성능을 제공하는 리버스 프록시로, 효율적인 어플리케이션 사용을 위해 다양한 환경에 적용 가능한 소프트웨어이다.