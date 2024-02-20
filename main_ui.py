#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
import asyncio
import os
import sys
import traceback

from PySide6.QtAsyncio import QAsyncioEventLoopPolicy

from app.main_app import AutoWithdraw
from loguru import logger
from PySide6.QtWidgets import QApplication, QMessageBox


current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, 'logs')


def log_uncaught_exceptions(ex_cls, ex, tb) -> None:
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    QMessageBox.critical(None, 'Error', text)


if __name__ == '__main__':
    # sys.excepthook = log_uncaught_exceptions
    app = QApplication(sys.argv)
    window = AutoWithdraw()
    window.show()
    asyncio.set_event_loop_policy(QAsyncioEventLoopPolicy())
    asyncio.get_event_loop().run_forever()
