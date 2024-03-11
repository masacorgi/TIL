# 버전 컨트롤

Docker로 이미지를 만들고 배포하는 과정에서 이미지 태그를 통한 버전을 일관되게 관리할 수 있게 수정하는 작업이 할당됐다.

## 작업 요약

1. Git Actions Runner : Docker 이미지 생성
2. Git Actions Runner : DockerHub image PUSH
3. AWS EC2 : DockerHub image PULL
4. AWS EC2 : Docker image로 컨테이너 생성

위 과정에서 모두 동일한 버전을 사용해야 한다.

현재는 버전 정보가 모두 각 코드에 숫자로 하드코딩 되어있다.

버전을 올리거나 내릴때 각 부분을 모두 찾아 수정해야 한다.

변수를 활용해서 한번에 수정할 수 있게 변경하려고 함


## 작업

