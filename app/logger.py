import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Literal

from PySide6 import QtGui
from tqdm.asyncio import tqdm
from loguru import logger


LoggingLevel = Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
FILE_LOG_FORMAT = "<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <green>{message}</green>"
CONSOLE_LOG_FORMAT = "<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <green>{message}</green>"


class LoggerHandler:

    def __init__(self, parent=None):
        super().__init__()
        if parent:
            self.widget = parent

    def write(self, record, *args):
        if self.widget:
            self.widget.append(record.strip())
            self.widget.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)


def setup_logger(handler):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(current_dir, 'logs')
    logger.remove()
    log_filename = f"{datetime.now().strftime('%d-%m-%Y')}.log"
    log_filepath = Path(log_dir, log_filename)
    logger.add(handler, format=CONSOLE_LOG_FORMAT, level=logging.DEBUG)
    logger.add(log_filepath, format=FILE_LOG_FORMAT, level=logging.DEBUG, rotation='1 day')
    logger.add(lambda msg: tqdm.write(msg, end=''), colorize=True, format=CONSOLE_LOG_FORMAT, level=logging.DEBUG)  # ?
    logger.add(
        sink=sys.stdout,
        backtrace=True,
        diagnose=True,
        colorize=True,
        catch=True,
        format="<green>{time:HH:mm:ss}</green> | "
               "<level>{level: <8}</level> | "
               "<cyan>{name}</cyan>:"
               "<cyan>{function}</cyan>:"
               "<cyan>{line}</cyan> - "
               "<level>{message}</level>",
        level="ERROR",
    )

    # добавляем обработчик записи в файл
    # TODO после добавить excel
    logger.add(
        sink=log_filepath,
        colorize=True,
        rotation="100 MB",    # как часто ротировать лог-файл
        retention="7 days",   # как долго хранить логи
        compression="zip",    # как сжимать старые логи
        format="{time:YYYY-MM-DD HH:mm:ss} |"
               "{level: <8} | "
               "{name}:"
               "{function}:"
               "{line} - "
               "{message}",
        level="INFO",
    )


current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, 'logs')
# setup_logger()

