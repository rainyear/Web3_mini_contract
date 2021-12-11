from solcx import compile_standard, install_solc

with open("SimpleStorage.sol", "r") as f:
    sol_file = f.read()
    print(sol_file)
