# 가상환경을 설정하고 실행하기

## 가상환경을 사용하는 이유

## 실행단계(윈도우환경)

1. 프로젝트 디렉토리로 이동
2. 가상환경 생성

    python -m venv venv

3. 가상환경 활성화

    venv\Scripts\activate

    명령 프롬프트 앞에 (venv)가 붙는다.

    ** PowerShell을 관리자 권한으로 열어야함(vscode 터미널의 경우 vscode를 관리자 권한으로 열면 됨)
    PowerShell은 기본적으로 스크립트 실행정책이 제한되어 있으므로
    스크립트 실행정책을 변경해야한다.
    
        Set-ExecutionPolicy RemoteSigned

    현재 사용자에 대해서만 변경하려면

        Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Restricted


    작업을 마치면 PowerShell 실행정책을 복원하는게 좋다.(보안)

        Set-ExecutionPolicy Restricted

4. 패키지 설치

    pip install -r requirements.txt

    (현재 가상환경에 설치된 패키지 확인)
    pip freeze

5. 가상환경 종료

    deactivate