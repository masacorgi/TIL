# about EC2


## 콘솔 로그인

루트사용자 이메일로 로그인 -> 이메일, 패스워드 활용

## putty ssh 연결하기(윈도우)
1. pem 파일 puttyzen에서 ppk파일로 변환
2. putty에서 ppk파일, ip로 접속(첫 시도시 저장)

## aws 콘솔로 연결하기
1. SSH 사용 연결
2. AWS System Manager(SSM) 사용 연결

    ec2에 SSM 에이전트가 설치되어 있어야 함

3. AWS Management Console로 연결

    브라우저로 연결할수 있음

## 파일 전송하기
1. FTP, SFTP
2. AWS CLI

## 탄력적 ip 고정 ?
https://velog.io/@kwontae1313/EC2-%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4-IP%EC%A3%BC%EC%86%8C-%EA%B3%A0%EC%A0%95



## github action 수정

### 소스코드 .github/workflows/yaml 비활성화 ?

### Dockerfile, yml ?

## Docker

1. 설치되어 있는지 확인(버전 확인)

    docker --veresion

2. 도커 설치 정보 확인

    docker info

3. 실행중인 도커 컨테이너 확인

    docker ps

4. 도커 서비스 상태 확인

    sudo service docker status

5. 도커 서비스 실행여부 확인

    sudo systemctl status docker

도커가 설치되어 있지 않다면 다음과 명령어로 ec2에 도커 설치

    (Amazon Linux 2 인스턴스 기준)
    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo service docker start
    sudo usermod -a -G docker ec2-user  # 현재 사용자를 도커 그룹에 추가 (재로그인 필요)


