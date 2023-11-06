깃 사용법
=======================================================================
목차
1. GitHub
2. Add
3. Commit
4. Branch
5. Push
6. Pull Request (PR)
7. Pull
   
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


7.Pull
-----------------------------------------------------------------------
