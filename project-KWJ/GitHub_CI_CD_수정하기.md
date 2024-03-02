# GitHub CI / CD 수정하기

프로젝트 KingWangJJang 에서 서버를 기존 Synology 개인서버 -> AWS EC2로 이전하면서 GitHub Actions에서 관리하는 CI/CD를 수정해야하는 작업이 할당됐다.

EC2 인스턴스는 프리티어 계정으로 팀장님이 생성해두었다. 호스트 정보, 사용자 이름을 받아서 수정하면 된다.

#### 작업 요약
* .github/workflows/야믈파일 수정
* Dockerfile 수정


작업에 대한 내용을 먼저 파악해보자

1. CI/CD 개념 파악
2. GitHub Actions 사용법 파악
3. Yml 파일 수정
4. Dockerfile 수정


## 1. CI/CD 개념 파악

CI(Continuous Integration, 지속적 개발)는 개발자들이 작성한 코드를 지속적으로 통합하여 충돌 및 오류를 최소화하고 품질을 높이는 과정이다.
CD(Contiuous Deployment/Delivery, 지속적 배포)는 지속적으로 개발,테스트,배포해서 빠른 소프트웨어 전달과 안정적인 배포를 실현하는 과정이다.
Continous Deployment는 자동화된 테스트를 통과한 코드를 자동으로 프로덕션 환경에 배포,
Contiuous Delivery는 자동화된 테스트를 통과한 코드를 스테이징 환경으로 배포하고, 프로덕션 배포는 수동으로 결정하는 미묘한 용어적 차이가 있다.

## 2. GitHub Actions 파악

github actions는 깃허브가 제공하는 CI(지속적 통합), CD(지속적 배포) 서비스이다.

다음과 같은 기능을 제공한다.

* 개발 프로세스 자동화
* 소스코드 변경테스트/빌드/배포까지 자동으로 수행

GitHub actions 사용법은 다음 게시글에 정리해서 포스팅하겠다.


#### GitHub Actions 흐름

1. Push 등 GitHub 이벤트 발생
2. GitHub는 프로젝트 파일 중 .github/Workflows/야믈파일 에 정의된 job을 수행
3. job 1 : 
	step 1: 깃허브 가상환경 Runner에서 도커이미지 build
    step 2: 깃허브 가상환경 Runner에서 도커허브 로그인
    step 3: 깃허브 가상환경 Runner에서 도커허브에 push
    
4. job 2 :
	step 1: Secrets에 저장된 ssh key를 이용해 ec2 접속, 도커허브 pull
		job 2(run) 단계에서 접속할 인스턴스가 synology->ec2로 변경되었기 때문에 GitHub Secrets에 저장된 host, ssh key 등 접속정보를 변경해야 한다.

## 3. YML 파일 수정

GitHub가 주시하면서 언제, 어떻게 action을 할지 적어놓는 파일을 수정해야한다.
프로젝트의 /.github/workflows/ 에 위치하고 있다.
원하는 workflow마다 하나씩 생성하면 된다.

이 파일에서 서버 인스턴스에 접속해 도커허브 pull 하는 부분을 수정했다.

파일은 정리해서 다른 게시글로 포스팅하겠다.


## 4. Dockerfile 수정
도커파일은 수정할 부분이 없었다 .. ,, ... ,,


