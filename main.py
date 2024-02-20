#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

# Created by TrueSoer at 20.02.2024

import asyncio
from app.script.start_withdraw import start
from app.logger import setup_logger


if __name__ == '__main__':
    setup_logger()
    with open('account.txt', 'r') as file:
        ACCOUNTS_LIST = [x.rstrip() for x in file.readlines()]
    asyncio.run(start(ACCOUNTS_LIST))