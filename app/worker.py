#!/usr/bin/env/python3
# -*- coding: utf-8 -*-


from PySide6.QtCore import QObject, Signal
from app.script.start_withdraw import start
from asyncio import run


class Worker(QObject):
    finished = Signal()
    started = Signal()
    error = Signal()
    log_message = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def do_work(self, ACCOUNTS_LIST):
        run(start(ACCOUNTS_LIST))
        self.finished.emit()
