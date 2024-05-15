import logging
from logging.handlers import TimedRotatingFileHandler



def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    '''Function to setup a logger; create if doesn't exist.'''
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=14)
    handler.suffix = '%Y-%m-%d'
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# アクセスロガーの設定
access_logger = setup_logger('access_logger', 'logs/access.log', logging.INFO)

# エラーロガーの設定
error_logger = setup_logger('error_logger', 'logs/error.log', logging.ERROR)

# アプリケーションロガーの設定
info_logger = setup_logger('info_logger', 'logs/info.log', logging.INFO)
