import logging
from os import path

# 로그 레벨 순서 : debug < info < warning < error < critical
# level : 지정한 레벨 이상의 로그만 뜸
# 로그 뭐 쓸지 세팅 format = 로그 뜬 시간, 로그 레벨, 메세지
# logging.basicConfig(level=logging.WARNING, format="%(asctime)s [%(levelname)s] %(message)s")

# logging.debug("debug")
# logging.info("자동화 준비")
# logging.warning("이 스크립트는 코드 몽키가 짜서 문제가 있을 수 있습니다.")
# logging.error("error!! error!! error!!")
# logging.critical("치명타 터짐 ㅅㄱ")

logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 스트림 (터미널)
steramHandler = logging.StreamHandler()
steramHandler.setFormatter(logFormatter)
logger.addHandler(steramHandler)

# 로그 파일
from datetime import datetime
filename = datetime.now().strftime("Desktop/File/logfile_%Y%m%d%H%M%S.log") # logfile_date날짜
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logging.debug("log를 남기는 테스트 진행")
logging.info("자동화 준비")
logging.warning("이 스크립트는 코드 몽키가 짜서 문제가 있을 수 있습니다.")
logging.error("error!! error!! error!!")
logging.critical("치명타 터짐 ㅅㄱ")
