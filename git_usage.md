깃 사용법
=======================================================================
목차
1. GitHub
2. Add
3. Commit
4. Branch
5. Push
6. Pull Request (PR)
7. Merge
8. gitignore
9. Pull
10. Clone
   
1.GitHub
-----------------------------------------------------------------------

    git status // 현상태 확인하기

### git의 여러 스테이지

Working Directory -> Staging Area -> Local Repository -> Remote Repository


    Working Directory 작업디렉토리
    
    Staging Area 스테이징 영역
    변경된 파일의 스냅샷을 저장. git add를 사용해서 작업디렉토리에서 옮김

    Local Repository 로컬저장소
    커밋된 버전의 스냅샷을 저장. git commit을 사용해서 스테이징에서 옮김

    Remote Repository 원격저장소
    협업자들 간 코드를 공유하고 저장하는 공간 제일중요!!!
    git push로 local -> remote
    git pull로 local <- remote


2.Add
-----------------------------------------------------------------------
다음 Commit(변경)을 저장할때까지 변경분을 모아놓는 작업

    git add filename.file
    git add .                   // 현위치 전체 파일 add
    git add *.txt               // 모든 .txt 파일 add
    git add project/app/*/      // 디렉토리 add
    git add --update            // 현재 git이 추적하고 있는 파일만 add

    add 취소하기
    git rm --cached filename.file



3.Commit
-----------------------------------------------------------------------
### 커밋이란
Add를 통해 staging area에 저장된 변경사항들을 로컬저장소에 저장하는 명령어
변경사항을 확정한다.

    git commit -m "???: commit message"

    커밋메시지 수정하기
    git commit --amend -m "수정된 메시지"

### 커밋메시지
프로젝트 변경사항을 쉽게 추적할 수 있게 접두어를 활용하자!

    Add: 새로운 기능, 파일, 모듈 또는 데이터를 추가한 경우 사용
    예시: Add: Implement user registration feature

    Fix: 버그 수정을 나타낼 때 사용
    예시: Fix:  Resolve issue with login form validation

    Update: 기존의 기능을 개선하거나 업데이트할 때 사용
    예시: Update: Update the styling of the homepage

    Remove: 코드 또는 파일을 제거하거나 사용하지 않는 요소를 삭제할 때 사용
    예시: Remove: Remove deprecated utility function

    Refactor: 코드를 개선하거나 재정리할 때 사용
    예시: Refactor: Extract a reusable utility function

    Docs: 문서 업데이트
    예시: Docs: Update README with installation instructions

    Test: 테스트 코드를 추가, 수정 또는 삭제할 때 사용
    예시: Test: Add unit tests for the user authentication module

    Chore: 빌드, 배포, 설정 또는 일반적인 유지 보수 작업을 나타낼 때 사용
    예시: Chore: Update dependencies in package.json

    Style: 코드 스타일 개선이나 변경할 때 사용
    예시: Style: Format code with consistent indentation

    Revert: 이전 커밋을 되돌리는 커밋
    예시: Revert: Revert the last commit to fix a critical bug


4.Branch
-----------------------------------------------------------------------

### 브랜치란?

브랜치는 프로젝트를 병렬적으로 개발하고 테스트할 수 있게 만드는 기능이다.
각 브랜치는 독립적으로 변경 내용을 저장하고 관리할 수 있다.

팀원 간 병렬적으로 관리되기 때문에 충돌이 나지 않게 꼼꼼히 살펴야한다.

브랜치 생성은 git branch, git checkout
변경 내용 병합은 git merge, git rebase 를 사용한다.

### 브랜치명 접두어
접두어를 활용하면 브랜치의 목적을 명확하게 식별가능, 코드관리 협업에 도움이 된다!

    feature/ 
    새로운 기능을 개발하는 브랜치
    feature/user-authentication 또는 feature/add-payment-gateway 와 같이 새로운 기능을 추가하는 작업에 사용가능

    bugfix/ 
    버그 수정 브랜치
    bugfix/issue-123 와 같이 특정 버그를 수정하는 작업에 사용가능

    hotfix/ 
    긴급한 버그 수정 브랜치
    일반적으로 프로덕션 환경에서 발생한 심각한 문제를 고치기 위한 브랜치에 사용된다.
    hotfix/security-issue 와 같이 긴급한 보안 문제를 해결하기 위한 작업에 사용

    release/ 
    프로덕션 릴리스를 준비하는 작업 브랜치
    release/1.0 와 같이 특정 버전의 릴리스를 준비하는 브랜치에 사용

    test/ 또는 experiment/
    새로운 아이디어나 실험적인 작업 브랜치
    주로 프로덕션 코드에 영향을 미치지 않는 실험 또는 테스트에 사용

    docs/ 
    문서 업데이트를 위한 브랜치
    프로젝트 문서를 개선하거나 업데이트할 때 유용합니다.

    chore/ 또는 refactor/
    코드 정리, 리팩터링 또는 일반적인 작업 브랜치
    주로 기능 개발이나 버그 수정과는 관련이 적은 작업에 사용

    release candidate (rc/)
    릴리스 후보 버전을 준비하기 위한 브랜치
    rc/2.0 와 같이 특정 릴리스 후보 버전을 준비하는 작업에 사용

### 브랜치를 만들고 푸시하기

1. 원격 브랜치 생성<br>
   git 홈페이지에서 생성가능, 아니면 스킵해도 됨 로컬에서 만들면 원격에서도 만들어진다.

2. git checkout -b 브랜치명<br>
   로컬에서 브랜치를 만들고 브랜치로 전환

3. git add 파일명
   
4. git commit -m "커밋메시지"
   
5. git push origin 브랜치명<br>
   이때 원격에 브랜치가 없다면 생성된다.

5.Push
-----------------------------------------------------------------------
로컬저장소에 commit된 파일들을 모두 원격저장소에 모두 업로드하는 명령어 
    
    git push "remote" "branch"          // 원격저장소, 저장할 브랜치
    예시: git push origin main  
    예시: git push origin feature/user-auth

포스푸시 추가
옵션설명 추가

6.Pull Request (PR)
-----------------------------------------------------------------------
Pull Request는 브랜치에서 일어난 코드 변경을 다른 브랜치로 병합하기 전에 리뷰 및 토론을 할 수 있는 협업 기능이다.

다음과 같은 순서로 이용 가능하다.

    1. 새 브랜치 생성
    2. 코드 변경, commit, 원격 브랜치로 push
    3. 깃허브에서 해당 브랜치 Pull Request 생성
        * 리뷰어 선택(유료버전 이용 시 다수 선택가능)
    4. 코드 리뷰 및 토론
        * 지속적인 커밋, 토론이 코드 병합 전까지 가능하다.
    5. 브랜치 병합(merge)
        * 코드 리뷰와 토론이 종료되면 PR을 원격저장소에 병합한다.
    6. 삭제(선택)
        * PR이 merge 된 후에 더이상 필요하지 않을 경우 해당 브랜치를 삭제하여 저장소 정리 가능



7.Merge
-----------------------------------------------------------------------
### merge 란?
  
merge는 두개의 다른 브랜치에서의 작업을 하나로 통합하는 데 사용된다.<br>
주로 다른 개발자들이나 다른 브랜치에서의 변경사항을 현재 브랜치에 병합할 때 활용된다.<br>
여러 옵션을 통해 다양한 병합 전략을 선택 가능하다.



    * git merge 다른브랜치명
        기본, 다른 브랜치에서 현재 브랜치로 병합
        병합이 자동완료 될 수 없는 충돌이 일어날 경우 사용자에게 알려줌.
        사용자는 수동으로 충돌을 해결한 후에
        git merge --continue 로 병합을 완료한다.

    주요 옵션
    * --no-ff      //No Fast-Forward
        항상 새로운 커밋을 생성해서 브랜치를 병합.
        Fast-Forward 병합을 방지하고 항상 명시적인 커밋을 만든다.
        예시) git merge --no-ff other/branch
    
    * --squash
        병합되는 모든 커밋을 하나의 커밋으로 압축한다.
        이후 새로운 커밋을 만들어서 병합된 브랜치에 적용
        예시) git merge --squash other/branch

    주요 병합 전략
    -s / -strategy 옵션을 사용해서 병합 전략을 선택할 수 있다.

    * recursive : 기본값. 기본적인 재귀적 병합전략이며 대부분의 상황에서 적합하다.
        예시) git merge -s recursive other/branch
    
    * resolve : 간단한 충돌 해결을 수행
        예시) git merge -s resolve other/branch

    * ours : 항상 현재 브랜치의 변경사항을 유지
        예시) git merge -s ours other/branch

    * octopus : 다중 부모를 가진 병합을 수행
        예시) git merge -s octopus other/branch1 other/branch2
  
<br>

### merge 와 rebase의 차이

merge는 두개의 다른 브랜치를 하나로 합치는 가장 기본적인 방법이다.
병합 커밋이 새로 생성되고, 각 브랜치의 변경내용이 합쳐진다.

간단하고 직관적이며, 이력이 선형적으로 유지된다.<br>
병합 커밋이 추가되기 때문에 이력이 복잡해질 수 있다.<br>
Fast-forward 병합을 피하려면 --no-ff 옵션을 사용해야 한다.<br>

rebase는 브랜치의 기록을 재작성해서 다른 브래치의 변경사항을 현재 브랜치에 적용하는 방법이다.
이전의 커밋들이 새로운 기반 위에 재배치되서 새로운 이력이 생성된다.

        git checkout feature/branch
        git rebase main

이력이 깔끔하게 유지되고 기본 브랜치의 이력이 선형적으로 나타난다.
Fast-forward 병합이 가능하다.
하지만 충돌이 발생할수 있고, 이를 해결해야 되는 상황이 발생할 수 있다.
<br><br><br>
merge는 공동 작업 중인 팀이나 개발자가 있을 경우, 이미 공개된 브랜치에 변경사항을 추가할 때 주로 사용한다.

rebase는 로컬에서 개인적인 작업을 하고있고, 기능을 완성한 뒤에 다른 브랜치로 합칠 때 사용한다.
팀에서 협업 중이지만 로컬에서만 브랜치를 유지하고 원격 저장소에 push하지 않을 때도 사용한다.





8.gitignore
-----------------------------------------------------------------------

.gitignore 파일은 Git 저장소에서 여러 이유로 추적되지 않아야 할 파일이나 디렉토리를 지정하는 데 사용된다.<br>
이 파일을 통해 Git은 변경 추적을 할 필요가 없는 파일을 확인하고 저장소에 저장하지 않는다.

주로 로컬 개발환경이나 빌드 도구에서 생성되는 파일, 디렉토리, 중간 결과물 또는 민감한 정보가 담긴 파일 등을 '.gitignore' 파일에 명시한다.

.gitignore 파일은 Git 저장소의 루트 디렉토리에 위치하며, 각 줄에는 무시할 파일 또는 디렉토리 패턴이나 규칙이 작성된다.<br>

### .gitignore 예시

```.gitginore

    # Compiled Python files
    __pycache__/

    # Byte-compiled / optimized / DLL files
    *.pyc
    *.pyo
    *.pyd

    # Virtual environment 파이썬 가상환경설정
    venv/

    # IDE files
    .idea/

    # macOS 맥 폴더 내부의 파일 및 폴더 배치, 설정
    .DS_Store

    # Environment variables 환경변수(비밀정보, 로컬설정 저장)
    .env
```

_ _pycache_ _, .pyc, .pyo, .pyd, venv/, .idea/, .DS_Store, .env와 같은 파일과 디렉토리를 Git에서 무시하도록 설정.

#으로 주석을 달고, 디렉토리는 경로로, 파일종류는 *.filetype 으로 간단히 명시할 수 있다.


++
파이썬 프로젝트에서 파이썬은 소스코드를 실행하기 전에 바이트코드를 생성해서 실행 속도를 향상시킨다.
*.pyc, *.pyo, *.pyd 파일은 컴파일된 파일들이다. *.pyc는 일반적인 컴파일된 파일, *.pyo는 최적화된 컴파일된 파일, *.pyd는 Python 확장 모듈 파일이다.

이러한 바이트코드들은 일반적으로 Git 원격저장소에 업로드하지 않는다.




9.Pull
-----------------------------------------------------------------------

pull은 원격 레포지토리에서 최신 변경사항을 가져와 현재 작업 중인 로컬 저장소를 업데이트 하는 기능이다.

일반적으로 다른 사람이나 다른 기기에서 작업한 내용을 가져오거나 원격 저장소의 최신 버전을 로컬로 업데이트 할 때 사용한다.

    git pull origin 브랜치명
<br>
git pull 명령어는 실제로 두가지 작업을 수행한다.

 1. git fetch : <br>
        원격저장소에서 최신내용을 가져와 로컬에 반영한다.
        실제 작업 디렉토리나 트리에는 아직 반영되지 않음

 2. git merge 또는 git rebase : <br>
        가져온 변경 내용을 현재 브랜치에 병합하거나 재배치
        이 단계에서 작업 디렉토리가 실제로 변경되어 최신 내용이 반영됨.


10.Clone
------------------------------------------------------------------------

git clone은 원격저장소에 있는 프로젝트의 복사본을 로컬 컴퓨터로 가져오는 과정을 의미한다.

    git clone 레포지토리URL
    ex) git clone https://github.com/사용자명/레포지토리.git

레포지토리 url은 깃허브 레포지토리에서 복사할 수 있다.

비공개 레포지토리를 클론하려면 사용자 인증이 필요하다.
다음과 같이 사용자명과 비밀번호/엑세스토큰을 입력해야 한다.

    비밀번호 사용 : 
    git clone https://사용자명:비밀번호@github.com/사용자명/레포지토리.git
    엑세스 토큰 사용 :
    git clone https://사용자명:토큰@github.com/사용자명/레포지토리.git

위와 같은 방법으로 클론을 수행하면 로컬 환경에 새로운 디렉토리가 생성되고, 해당 디렉토리 안에 원격저장소의 모든 파이로가 히스토리가 포함되며 그곳에서 작업을 수행할 수 있게 된다.