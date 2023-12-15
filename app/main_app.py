#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

import os
import sys
from loguru import logger
from PySide6 import QtWidgets
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QFileDialog, QDialog
from app.uix.ui_untitled import Ui_MainWindow
from app.logger import LoggerHandler, setup_logger
from app.worker import Worker


class AutoWithdraw(QtWidgets.QMainWindow, Ui_MainWindow):
    ACCOUNTS_LIST = []
    ACC_DIR = 'home'
    to_address = ''

    def __init__(self):
        super().__init__()
        self.worker_thread = None
        self.worker = None
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda *args, **kwargs: self.load_file())
        self.btnStart.clicked.connect(lambda *arge, **kwargs: self.start_work())
        logger.remove()
        logging_handler = LoggerHandler(self.txtBrowserLog)
        setup_logger(logging_handler)

    def start_work(self):
        self.worker = Worker(self.ACCOUNTS_LIST)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(lambda *args, **kwargs: self.worker.do_work())
        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.worker.error.connect(lambda er: sys.excepthook(type(er), er, er.__traceback__))
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.worker_thread.start()

    def open_file(self, directory='', fmt='txt'):
        path = ''
        dialog = QFileDialog()
        dialog.setOption(QFileDialog.HideNameFilterDetails, True)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.DontUseNativeDialog, False)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        if fmt != '':
            dialog.setDefaultSuffix(fmt)
            dialog.setNameFilters([f'{fmt} (*.{fmt})'])

        directory = str(directory) if directory != '' else os.path.abspath(os.curdir)
        dialog.setDirectory(directory)

        if dialog.exec_() == QDialog.Accepted:
            pathNew = dialog.selectedFiles()[0]  # returns a list
            if pathNew:
                path = pathNew
        if path:
            return path

    def load_file(self):
        with open(self.open_file(), 'r') as file:
            self.ACCOUNTS_LIST = [x.rstrip() for x in file.readlines()]

