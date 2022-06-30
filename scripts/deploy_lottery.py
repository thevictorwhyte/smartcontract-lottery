from itertools import accumulate
from helpful_scripts import get_account, get_contract
from brownie import Lottery

def deploy_lottery():
    account = get_account()
    Lottery.deploy(get_contract("eth_usd_price_feed").address, {"from": account})


def main():
    deploy_lottery()