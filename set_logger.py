from logging import DEBUG, INFO, FileHandler, Formatter, StreamHandler, getLogger
from logging.handlers import QueueHandler, QueueListener
from queue import Queue


def set_async_logger(
    console_log_level=INFO, file_log_level=DEBUG, log_file_path=None
) -> QueueListener:
    """
    设置异步日志器

    Args:
        console_log_level: 控制台日志级别
        file_log_level: 文件日志级别
        log_file_path: 日志文件路径

    Returns:
        QueueListener: 日志队列监听器

    Warning:
        1: 全局仅调用一次
        2: 返回 QueueListener 对象，需要在程序退出之前调用 stop() 停止
        3: 可使用 try...finally 结构，在 finally 中调用 stop() 停止
    """

    root_logger = getLogger()
    root_logger.setLevel(file_log_level)
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handlers = []

    console_handler = StreamHandler()
    console_handler.setLevel(console_log_level)
    console_handler.setFormatter(formatter)
    handlers.append(console_handler)

    if log_file_path:
        file_handler = FileHandler(log_file_path, encoding='utf-8')
        file_handler.setLevel(file_log_level)
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)

    log_queue = Queue(-1)
    queue_handler = QueueHandler(log_queue)
    root_logger.addHandler(queue_handler)

    listener = QueueListener(log_queue, *handlers, respect_handler_level=True)
    listener.start()
    return listener
