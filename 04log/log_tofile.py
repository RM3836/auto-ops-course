import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='test_tofile.log',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s -  %(name)s - %(levelname)s - %(message)s - %(module)s - %(lineno)d')
logging.debug('此消息应记录到日志文件')
logging.info('同样记录到日志文件')
logging.warning('也应当记录到日志文件')
logging.error('这是模拟的错误消息')

