from brownie import Lottery, network, config
from scripts.helpful_scripts import get_account, get_contract

def deploy_lottery():
    account = get_account()
    Lottery.deploy(
        get_contract("eth_usd_price_feed").address, 
        get_contract("vrf_coordinator").address, 
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False)
    )
    print("Deployed Lottery!")

def start_lottery():
    account = get_account()
    lottery = Lottery[-1]
    starting_tx = lottery.startLottery({ "from": account})
    starting_tx.wait(1)
    print("The lottery is started!")

def enter_lottery():
    account = get_account()
    lottery = Lottery[-1]
    value = lottery.getEntranceFee() + 10000000
    tx = lottery.enter({"from": account, "value": value})
    tx.wait(1)
    print("You entered the lottery!")

def end_lottery():
    account = get_account()
    lottery = Lottery[-1]
    #TODO: Fund the contract with LINK which it needs to call request randomness
    # Then end the lottery
    tx = lottery.endLottery({"from": account})
    tx.wait()
    print("The lottery ended")

def main():
    deploy_lottery() 
    start_lottery()
    enter_lottery()