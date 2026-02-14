from logging import getLogger

from set_async_logger import set_async_logger

# 日志相关
log_file_path = 'logs/luo_li_backend.log'
log_listener = set_async_logger(log_file_path=log_file_path)
logger = getLogger(__name__)
logger.info(f'<main.py> 异步日志器已设置并启动，日志文件路径：{log_file_path}')
log_listener.stop()
