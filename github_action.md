# github Action, CI / CD

1. GitHub Actions 란?
2. Runner
3. MarketPlace Actions
4. Secrets
5. GitHub Actions 작업 단위
6. Django에서의 GitHub Actions 흐름
## GitHub Actions란?

github actions는 깃허브가 제공하는 CI(지속적 통합), CD(지속적 배포) 서비스이다.

* 개발 프로세스 자동화
* 소스코드 변경테스트/빌드/배포까지 자동으로 수행

## Runner
Workflow는 Github에서 호스팅하는 가상환경인 Runner에서 실행된다. 

Runner는 Workflow에서 정의된 작업을 수행하는 데 사용되는 가상머신 또는 컨테이너이다.<br>
가상환경에서 workflow가 실행되기 때문에 다양한 스크립트 명령어를 통해 환경을 제어할 수 있다.

## Marketplace Actions
GitHub Actions Marketplace에는 미리 만들어진 다양한 액션(Action)이 제공된다.

액션은 재사용 가능한 작업단위로서, 다른 프로젝트에서도 사용할 수 있다.

## Secrets
보안정보(API 토큰, 비밀 키)를 안전하게 저장하고 액세스하는 데 사용되는 보안 변수를 제공한다.

Secrets에 저장된 민감정보들은 야믈파일에서 ${{ secrets.민감정보명 }}으로 사용가능하다. 




## Github Actions 작업 단위

요약: GitHub 이벤트 발생 -> Workflow( job1-> job2(step1,step2..) -> job3 ..)
### 작업 기본단위 Workflow
github actions 작업 기본단위를 workflow라고 부른다.

workflow는 프로젝트의 .github/workflows 폴더에 yaml 파일로 작성하여 정의한다.

### Event
github actions는 깃허브에 작동하는 여러 이벤트(push,PR(pull_request),issues ..)에 반응하여 workflow를 실행한다.

특정 이벤트가 발생하면 해당 이벤트를 감지하고 설정된 워크플로우가 실행된다.

### Job
Workflow는 여러 단계로 구성되며, 각 단계는 하나이상의 "Job"으로 구성된다.

각 Job은 독립적으로 실행될 수 있으며, 하나의 워크플로우에 여러 Job을 정의할수도 있다.

### Step
Job은 여러 Step으로 나뉜다. 각 Step은 Workflow에서 수행해야하는 개별적인 작업을 나타낸다.

예를들어 코드 체크아웃, 의존성 설치, 빌드, 테스트 등의 작업이 각각의 스텝으로 정의될 수 있다.


## Django에서의 github actions 흐름

1. Push 등 GitHub 이벤트 발생
2. GitHub는 프로젝트 파일 중 .github/Workflows/야믈파일 에 정의된 job을 수행
3. job : 도커파일을 보고 도커 빌드/로그인/업로드 -> 서버에서 도커 pull



