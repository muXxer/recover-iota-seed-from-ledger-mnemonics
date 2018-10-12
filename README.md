# recover-iota-seed-from-ledger-mnemonics
Recover an IOTA seed from the ledger Nano S with your recovery phrase

## WARNING
Never give your seed or your recovery phrase to anyone! They will steal all your cryptocurrency token / money!
We will never ask you for this information!

## Step by step guide
### 1. Install requirements

You can either install the requirements on your own or use the following scripts, if you are on Ubuntu:
```sh
./install_virt_env.sh
./activate_virt_env.sh
```

#### Manual installation

1. [Create virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) (recommended, but not required)
2. `pip install -r requirements.txt`

### 2. Run the python script
Run the python script and enter your recovery phrase and passphrase in the command line.

```sh
python mnemonics_to_iota_seed.py
```

If you use the Romeo wallet, you can use the following script to enter your account and page index.
```sh
python mnemonics_to_iota_seed_romeo_wallet.py
```
