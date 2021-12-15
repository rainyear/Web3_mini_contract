from brownie import accounts, SimpleStorage

def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    tx = simple_storage.store(100, {"from": account})

    tx.wait(1)
    print("favNum: ", simple_storage.retrieve())

def main():
    print("Deploy main func...")
    deploy_simple_storage()