#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

import sys
import asyncio
from PySide6.QtCore import QObject, Signal
from loguru import logger

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
from app.script.start_withdraw import start


class Worker(QObject):
    finished = Signal()
    started = Signal()
    error = Signal()
    log_message = Signal(object)

    def __init__(self, ACCOUNTS_LIST, parent=None):
        super().__init__(parent)
        self.ACCOUNTS_LIST = ACCOUNTS_LIST

    def do_work(self):

        try:
            self.started.emit()
            logger.info("Начал работу")
            asyncio.ensure_future(start(self.ACCOUNTS_LIST))
            self.finished.emit()
        except Exception as ex:
            self.error.emit(ex)
