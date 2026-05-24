import logging
# 创建记录器，将其命名为Test
logger = logging.getLogger("Test")
# 默认日志级别为WARNING，这里改为DEBUG
logger.setLevel(logging.DEBUG)
# 创建FileHandler处理器，将日志消息输出到文件中，并设置特定的消息格式和日期格式
logfile = logging.FileHandler(filename='mylog.log',mode='w')
formatter1 = logging.Formatter(fmt='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')
logfile.setFormatter(formatter1)
# 创建StreamHandler处理器，将WARNING或更高级别的日志消息输出到控制台，设置特定消息格式
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter2)
# 将处理器添加到记录器
logger.addHandler(logfile)
logger.addHandler(console)
# 输出不同级别的日志消息
logger.debug('debug,调式信息')
logger.info('info,一般信息')
logger.warning('waring，警告信息')
logger.error('error，错误信息')
logger.critical('critical，致命的错误信息')
