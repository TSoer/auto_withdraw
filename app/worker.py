#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

import asyncio
from PySide6.QtCore import QObject, Signal
from app.script.start_withdraw import start


class Worker(QObject):
    finished = Signal()
    started = Signal()
    error = Signal()
    log_message = Signal(str)

    def __init__(self, ACCOUNTS_LIST, parent=None):
        super().__init__(parent)
        self.ACCOUNTS_LIST = ACCOUNTS_LIST

    def do_work(self):
        loop = asyncio.get_event_loop()

        try:
            self.started.emit()
            loop.create_task(start(self.ACCOUNTS_LIST))
            self.finished.emit()
        except Exception as e:
            self.error.emit()
        finally:
            loop.close()