#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

from loguru import logger
from asyncio import gather
from app.models.account import Client


async def _prepare_account(wallet_data: str):
    try:
        address, private, to_address = wallet_data.split(':')
        address = int(address, 16)
        client = Client(address=address, private_key=int(private, 16), to_address=int(to_address, 16))
        await client.test_ui_interface()

    except Exception as exc:
        logger.critical(f"Unexpected error: {wallet_data} | {exc}. Work is ended! ")


async def prepare_accounts(ACCOUNTS_LIST):
    logger.info(f"Загрузил {len(ACCOUNTS_LIST)}")
    for account in enumerate(ACCOUNTS_LIST):
        task = _prepare_account(wallet_data=str(account))
    return


async def start(ACCOUNTS_LIST):
    await gather(*[_prepare_account(wallet_data=account) for account in ACCOUNTS_LIST])
    logger.info('Закончил работу')