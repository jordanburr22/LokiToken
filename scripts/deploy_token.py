from brownie import LokiToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

def deploy_token():
    account = get_account()
    token = LokiToken.deploy(initial_supply, {"from": account})
    print(f'Deployed {token.name()} ({token.symbol()})')
    return token

def main():
    deploy_token()
