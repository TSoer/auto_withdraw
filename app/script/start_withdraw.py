#!/usr/bin/env/python3
# -*- coding: utf-8 -*-


import asyncio
from app.config import *
from loguru import logger
from app.models.account import Client


async def _prepare_account(wallet_data: str):
    try:
        address, private, to_address = wallet_data.split(':')
        address = int(address, 16)
        client = Client(address=address, private_key=int(private, 16), to_address=int(to_address, 16))
        await client.do_withdraw(TOKENS.get('STRK'), abi=ERC20_ABI)

    except Exception as exc:
        logger.critical(f" ошибка {exc}. Work is ended! ")


# async def prepare_accounts(ACCOUNTS_LIST):
#     """ не пмню старая ли версия контракта"""
#     logger.info(f"Загрузил {len(ACCOUNTS_LIST)}")
#     for account in enumerate(ACCOUNTS_LIST):
#         task = _prepare_account(wallet_data=str(account))
#     return


async def start(ACCOUNTS_LIST):
    tasks = []
    for account in ACCOUNTS_LIST:
        tasks.append(asyncio.create_task(_prepare_account(wallet_data=account)))
    await asyncio.gather(*tasks)
    logger.info('Закончил работу')
