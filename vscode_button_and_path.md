# 절대경로, 상대경로와 VSCode 실행 버튼
절대경로 / 상대경로가 뭔지 알아보고 파이썬에서 그거 어떻게 쓰는지 (os.path 모듈) + 윈도우/리눅스에서는 어떻게 쓰이는지 (그냥 개념정도만)<br>
이번 문제가 왜 생겼는지 정리해보기! (vscode 의 버튼이 무슨 역할을 했고, 왜 이런 문제가 발생했는지)<br>
참고 : glow-backend/v2/app 이런 우리 프로젝트 내부 v2/app 경로에서 python3 main.py 실행하도록 하는걸 가정하고 쭉 작업했었습니다.


## 절대경로와 상대경로
컴퓨터에서는 파일의 위치를 절대경로와 상대경로의 방법으로 표시한다.
트리 구조로, 가장 위의 폴더 root 를 기준으로 갈라져 내려가는 방식을 생각하면 쉽다.

* 절대경로
    
    절대경로는 컴퓨터의 root 부터 표시하고자 하는 파일의 위치를 모두 나타낸다.
    
        C:\Users\사용자명\Documents\folder1\file.txt
    
* 상대경로

    상대경로는 검색중인 현재 위치를 기준으로 대상 파일의 위치를 나타낸다.<br>
    '.'은 현재위치, '..'은 상위 폴더를 나타낸다.

    ex. 현재위치가 C:\Users\사용자명\Documents\folder1 일때 위 file.txt의 위치:
        
        .\file.txt

    ex.현재위치가 C:\Users\사용자명 일때 위 file.txt의 위치:
        
        .\Documents\file.txt
    
    ex.현재위치가 C:\Users\사용자명 일때

        ../parent_directory/file.txt 는 
        C:\Users\parent_directory\file.txt 와 같다.(절대경로)
<br>
<br>

    
## 파이썬에서의 경로설정 ( 모듈 os.path )
os.path 모듈, 윈도우/리눅스에서는 어떻게 쓰이나?

파이썬에서는 디렉토리 및 파일 조작, 프로세스 관리, 환경변수 엑세스 등 다양한 기능이 포함되어 있는 os 라이브러리를 통해 운영체제와 상호작용하는데 사용되는 여러 기능을 이용한다.

라이브러리 중 path 모듈은 파일 경로와 관련된 함수들을 포함하고 있어 경로 조작에 유용하다.

다음은 os 라이브러리를 통해 사용할 수 있는 다양한 기능의 예시이다.

* 디렉토리 및 파일 조작
    
        os.getcwd() : 현재 작업 디렉토리 반환
        os.chdir(path) : 현재 작업디렉토리를 'path'경로로 변경
        os.listdir(path='.') : 주어진 경로의 디렉토리 내용을 리스트로 반환

* 파일 및 디렉토리 생성, 제거

        os.mkdir(path) : 주어진 경로에 디렉토리 생성
        os.makedirs(path) : 중간단계 디렉토리를 모두 생성하면서 디렉토리 생성
        os.remove(path) : 파일 삭제
        os.rmdir(path) : 주어진 디렉토리를 삭제

* 파일 경로 조작:

        os.path.join(path1, path2, ...) : 경로의 각 구성요소를 결합하여 새 경로 생성
        os.path.abspath(path) : 상대경로->절대경로로 변환
        os.path.dirname(path) : 주어진 경로의 디렉토리 부분을 반환
        os.path.basenaem(path) : 주어진 경로의 기본 파일 이름을 반환

* 경로 검사 및 분리:

        os.path.exists(path): 주어진 경로가 존재하는지 여부 확인
        os.path.isfile(path): 주어진 경로가 파일인지 여부 확인
        os.path.isdir(path): 주어진 경로가 디렉토리인지 여부 확인
        os.path.split(path): 디렉토리와 파일 이름을 분리하여 튜플로 반환

* 경로 확장자 및 기타 정보:

        os.path.splitext(path): 파일 이름과 확장자를 분리하여 튜플로 반환
        os.path.getsize(path): 주어진 파일의 크기를 바이트 단위로 반환
        
        os.path.getctime(path),
        os.path.getmtime(path),
        os.path.getatime(path) : 파일의 생성 시간, 수정 시간, 최근 접근 시간을 반환
  
<br>
<br>

## 무슨 문제가 발생했는가?

fastAPI 웹 프로젝트 개발 중 main.py에서 로깅 기능을 구현하던 중
logconfig.yaml 파일을 파이썬이 찾지 못하는 현상이 일어났다.

```py
logger = get_logger(__name__)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5001,
        reload=True,
        log_config="log_config.yaml",
    )
```
log_config.yaml 파일은 main.py가 있는 프로젝트 디렉토리 v2/app 에 있었고, main이 실행되면 작업디렉토리가 그곳으로 설정될 것이라고 생각했기 때문에 위치를 위와같이 설정했다.

하지만 계속해서 파일을 찾지 못하는 오류가 지속됐고, 결국 os.path 모듈을 통해 해결할 수 있었다.


```py
logger = get_logger(__name__)

print("path: ",os.getcwd())
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5001,
        reload=True,
        log_config=f"{os.path.dirname(os.path.abspath(__file__))}" + "/log_config.yaml",
    )
```

print문에 os.getcwd()를 사용해 현재 디렉토리가 어딘지 출력해보면 다음과 같이 나온다.

    path:  C:\study\glow-backend\glow-backend

main.py의 위치가 아닌 프로젝트 최상단의 위치가 나온다.

그러므로 os.path.abspath(현재파일)을 통해 절대경로를 획득하고,<br>
해당 경로의 디렉토리명을 os.path.dirname()으로 획득한 후 <br>
log_config.yaml을 붙여 경로를 붙이니 해결되었다.




