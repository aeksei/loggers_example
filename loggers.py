import json
import logging
import logging.handlers
import logging.config


CONSOLE_FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
FILE_FORMATTER = logging.Formatter("%(asctime)s — %(name)-12s — %(levelname)-8s — %(message)s")
LOG_FILENAME = 'file_rotating_logging.log'
LOGGING_CONFIG_FILE = 'logging.json'
LOGGER_NAME = 'console_and_file_logger'


def get_console_and_file_logger(logger_level='DEBUG', console_level='DEBUG', file_level="ERROR"):
    # Создаем логгер
    cf_logger = logging.getLogger(LOGGER_NAME)
    cf_logger.setLevel(logger_level)

    # Создаем обработчик, отправляющий сообщения в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(CONSOLE_FORMATTER)

    # Создаем обработчик, отправляющий сообщения в файл
    file_rotating_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
                                                                 maxBytes=100 * 1024,
                                                                 backupCount=5)
    file_rotating_handler.setLevel(file_level)
    file_rotating_handler.setFormatter(FILE_FORMATTER)

    # Добавляем обработчики логгеру
    cf_logger.addHandler(console_handler)
    cf_logger.addHandler(file_rotating_handler)

    return cf_logger


def get_logger_from_config(logger_name):
    with open(LOGGING_CONFIG_FILE, "r") as f:
        logging.config.dictConfig(json.load(f))
    return logging.getLogger(logger_name)


if __name__ == "__main__":
    cf_logger = get_console_and_file_logger()

    while True:
        cf_logger.debug("Всё идет по плану")
        cf_logger.warning("Что-то не так(((")
        cf_logger.critical("Всё совсем печально")
