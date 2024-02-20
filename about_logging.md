# logging
목차

1. logging 이란?
2. Python 에서의 로그
3. FastAPI 에서 logging 활용하기
## 1. logging 이란?

로깅은 현재 우리 프로그램이 어떤 상태를 가지고 있는지, 외부 출력을 하게 만들어서 프로그램의 동작을 이해하고, 문제 발생 시 진단과 해결에 도움을 얻기 위해 추가하는 기능이다. 

### 로깅을 사용하는 이유
* 디버깅 및 문제 해결
* 성능 모니터링 : 성능에 관한 정보를 제공, 성능 병목현상이나 최적화 필요 부분을 식별 가능
* 보안 : 보안 이벤트를 기록하여 시스템에 대한 불법적 접근, 공격 감지 가능
* 오디팅 : 특정 이벤트나 행동에 대한 기록을 제공하여 나중에 검토, 증명 가능

### 로깅의 레벨
로깅은 다양한 레벨이 있다.
* DEBUG : 디버깅 목적의 상세한 정보 기록
* INFO : 정보성 메시지 기록
* WARNING : 잠재적 문제를 나타내는 경고 기록
* ERROR : 심각한 문제 발생 기록 (프로그램 계속 실행 가능)
* CRITICAL : 심각한 문제 발생 (프로그램 중단)
  
## 2. Python 에서의 로그

로깅은 각 언어 및 프레임워크에서 다양한 방식으로 구현될 수 있다.

Python의 경우 내장 모듈인 logging을 사용해서 로깅을 구현할 수 있다.

```py
import logging

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)

# 로그 메시지 출력
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")

```

## 3. FastAPI 에서 logging 활용하기

유틸리티 관련 설정을 분리해놓았다면,
유틸리티 파일에 로거를 만들고
```py
import logging

def get_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)
    return logger
```

메인에서 프로그램이 시작할 때 로깅이 작동하게 설정을 추가한다.
```py
from util(유틸리티파일) import get_logger

logger = get_logger(__name__)

uvicorn.run(
    ...
    log_level = "info"
    # 출력/저장할 로그 레벨 설정 debug/info/warning/error/critical
    log_config = "log_config.yaml"
    ...
)
```

이후 로깅이 필요한 파일에서(주로 crud 파일) import 후 사용한다.

```py
from util import get_logger

logger = get_logger(__name__) # name은 현재 파일의 위치를 나타낸다

##로깅이 필요한 위치에서
logger.info('log message')
logger.error('error message')
```