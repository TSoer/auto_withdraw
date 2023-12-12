#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

from loguru import logger
from typing import Union
from starknet_py.hash.address import compute_address
from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair
from app.config import *
from starknet_py.contract import Contract, PreparedFunctionCall


class Client:

    def __init__(self, address, private_key, to_address):
        self.full_node_client = FullNodeClient(node_url=RPC)
        self.address = address
        self.to_address = to_address
        self.private_key = private_key
        self.key_pair = KeyPair.from_private_key(private_key)

        # self.address_original = address
        # self.address = self._get_braavos_account()
        self.account = Account(client=self.full_node_client,
                               address=self.address,
                               key_pair=self.key_pair,
                               chain=StarknetChainId.MAINNET)
        self._last_prepared_tx = None

    def _get_braavos_account(self) -> int:
        selector = get_selector_from_name("initializer")
        calldata = [self.key_pair.public_key]
        address = compute_address(
            class_hash=BRAAVOS_PROXY_CLASS_HASH,
            constructor_calldata=[BRAAVOS_IMPLEMENTATION_CLASS_HASH, selector, len(calldata), *calldata],
            salt=self.key_pair.public_key,
        )
        return address

    async def do_withdraw(self):
        contract = self.get_contract()
        if self.address != self.to_address:
            tx_hash = await self.send_transaction(interacted_contract=contract,
                                                  function_name='transfer',
                                                  recipient=self.to_address,
                                                  amount=1000000000000000)
            if tx_hash:
                logger.info('nhfypfrwbz jnghfdktyf')
                return True
        else:
            logger.info("Адрес отправителя и получателя совпадаю")

    def get_contract(self, contract_address: int = None, abi: Union[dict, None] = None):
        if contract_address is None:
            contract_address = TOKENS.get('ETH')
        if abi is None:
            abi = ERC20_ABI
        contract = Contract(address=contract_address, abi=abi, provider=self.account)
        return contract

    async def estimate_fee(self, prepared_tx: PreparedFunctionCall = None):
        """Проверка цены на газ и оценка цены транзакции"""
        async def _response():
            nonlocal prepared_tx
            if not prepared_tx:
                prepared_tx = self._last_prepared_tx
            response = await prepared_tx.estimate_fee()
            overall_fee = response.overall_fee
            gas_price = response.gas_price / 10 ** 9
            self._last_prepared_tx = prepared_tx
            return {'gas_price': gas_price, 'overall_fee': overall_fee}

        response = await _response()
        # ЧТОБЫ ПОТОМ ВЫСТОВЛЯТЬ ЦЕНУ ЗА ГАЗ
        # gas_price = response.get('gas_price')
        # while gas_price >= Config.MAX_GWEI:
        #     logger.warning(f"Current gas price: {gas_price} GWEI. Waiting to dump...")
        #     try:
        #         response = await _response()
        #         gas_price = response.get('gas_price')
        #     except Exception as exc:
        #         logger.error(exc)
        #     await asyncio.sleep(randint(60, 120))
        overall_fee = response.get('overall_fee')
        return overall_fee

    async def send_transaction(self, interacted_contract, function_name='transfer', **kwargs) -> bool:
        try:
            logger.debug(f"[{hex(self.address)}] Sending tx...")

            prepared_tx = interacted_contract.functions[function_name].prepare(**kwargs)
            fee = await self.estimate_fee(prepared_tx)
            logger.info(f'Цена за транзакцию сейчас {fee} Wei')
            tx = await prepared_tx.invoke(
                                        max_fee=int(fee * 1.1),
                                        # auto_estimate=True
                                        )
            try:
                receipt = await self.account.client.wait_for_tx(tx.hash, retries=15)
                block = receipt.block_number
                print(block)

                if block:
                    return True
            except Exception as exc:
                logger.debug(f"Ошибка транзакции {exc}")

        except Exception as exc:
            logger.error(f"Couldn't send tx: {exc}")

    async def get_balance(self, token_address=TOKENS.get('ETH'), decimals=18):
        balance = await self.account.get_balance(token_address=token_address)
        return balance
