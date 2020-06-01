import logging
import os.path
import time


# 创建一个logger对象
logger = logging.getLogger()
logger.setLevel(logging.INFO)

rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

# 日志路径
log_path = os.path.dirname(os.getcwd())+ "\\logs\\"
# 日志文件名称
log_name = log_path +rq + ".log"
logfile = log_name

fh = logging.FileHandler(logfile,mode="w")
fh.setLevel(logging.DEBUG)

# 定义handler的输出格式
# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
# 第四步，将logger添加到handler里面
logger.addHandler(fh)
# 日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')



def logg():

    logging.basicConfig(level=logging.NOTSET)
    logging.debug("DEBUG")
    logging.info("INFO")
    logging.warning("WARNING")
    logging.error("ERROR")
    logging.critical("CRITICAL")

