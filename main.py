#!/usr/bin/env/python3
# -*- coding: utf-8 -*-


import os
import sys
import traceback
from app.main_app import AutoWithdraw
from loguru import logger
from PySide6.QtWidgets import QApplication, QMessageBox


current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, 'logs')


def log_uncaught_exceptions(ex_cls, ex, tb) -> None:
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    QMessageBox.critical(None, 'Error', text)


def main():
    # try:
    sys.excepthook = log_uncaught_exceptions
    app = QApplication(sys.argv)
    window = AutoWithdraw()
    window.show()
    sys.exit(app.exec())
    # except Exception as error:
    #     logger.error(error)
    #     sys.excepthook = log_uncaught_exceptions


if __name__ == '__main__':
    main()