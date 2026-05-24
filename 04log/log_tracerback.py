import logging
# 创建记录器
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
# 创建格式化器
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
# 创建FileHandler处理器，将日志消息输出到文件
file_handler = logging.FileHandler('traceback.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# 测试异常处理的函数
def func(num1, num2):
    try:
        x = num1 * num2
        y = num1 / num2
        return x, y
    except Exception:
        # 输出日志消息
        logger.error('出现异常！', exc_info=True)
        logger.info('已记录日志！')
if __name__ == '__main__':
    func(2,0)           # 除以0触发异常

