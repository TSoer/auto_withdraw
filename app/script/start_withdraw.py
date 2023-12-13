#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

from loguru import logger
from asyncio import gather
from app.models.account import Client


async def _prepare_account(index, wallet_data: str):
    try:
        address, private, to_address = wallet_data.split(':')
        address = int(address, 16)
        client = Client(address=address, private_key=int(private, 16), to_address=int(to_address, 16))
        await client.test_ui_interface()

    except Exception as exc:
        logger.critical(f"Unexpected error: {wallet_data} | {exc}. Work is ended! ")


async def prepare_accounts(ACCOUNTS_LIST):
    all_tasks = []
    logger.info(f"Загрузил {len(ACCOUNTS_LIST)}")
    for index, account in enumerate(ACCOUNTS_LIST):
        task = _prepare_account(wallet_data=account, index=index + 1,)
        all_tasks.append(task)
    return all_tasks


async def start(ACCOUNTS_LIST):
    await gather(*prepare_accounts(ACCOUNTS_LIST))
    logger.info('Закончил работу')