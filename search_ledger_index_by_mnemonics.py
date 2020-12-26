
# -*- coding: utf-8 -*-
from six.moves import input
from mnemonics_utils import MnemonicsToIotaSeed, InputRecoveryWords, InputPassphrase
from iota import Iota
from iota.crypto.addresses import AddressGenerator

api = Iota('https://nodes.iota.org:443')

#===============================================================================
def InputLedgerStartIndex():
    print("\nPlease enter ledger start index (Trinity default 0):")

    try:
        return input("   Ledger start index: ")
    except KeyboardInterrupt:
        return None

#===============================================================================
def InputLedgerEndIndex():
    print("\nPlease enter ledger end index (Trinity default 0):")

    try:
        return input("   Ledger end index: ")
    except KeyboardInterrupt:
        return None

#===============================================================================
def InputLedgerStartPage():
    print("\nPlease enter ledger start page (Trinity default 0):")

    try:
        return input("   Ledger start page: ")
    except KeyboardInterrupt:
        return None

#===============================================================================
def InputLedgerEndPage():
    print("\nPlease enter ledger end page (Trinity default 0):")

    try:
        return input("   Ledger end page: ")
    except KeyboardInterrupt:
        return None

#===============================================================================
def InputAddressAmount():
    print("\nPlease enter the amount of addresses to generate:")

    try:
        return input("   Address amount: ")
    except KeyboardInterrupt:
        return None

#===============================================================================
def SearchLedgerIndex(recovery_words, passphrase, ledger_start_index, ledger_end_index, ledger_start_page, ledger_end_page, address_amount):

    print("\nChecking ledger indexes for funds:")

    for ledger_index in range(ledger_start_index, ledger_end_index+1):
        for ledger_page in range(ledger_start_page, ledger_end_page+1):
            print("   Ledger Index: %d, Ledger Page: %d" % (ledger_index, ledger_page))

            iota_seed = MnemonicsToIotaSeed(recovery_words, passphrase, bip44_account=ledger_index, bip44_page_index=ledger_page)

            generator = AddressGenerator(iota_seed)
            addresses = generator.get_addresses(start=0, count=address_amount, step=1)
            result    = api.get_balances(addresses=addresses)

            found = False
            for address_index, balance in enumerate(result['balances']):
                if balance == 0:
                    continue

                found = True
                print("\n      Found balance %di (seed: %s, ledger index: %d, ledger page: %d, address index: %d" % (balance, iota_seed, ledger_index, ledger_page, address_index))
                print("\n      Your Address: %s" % (addresses[address_index]))
                print("\n                    https://thetangle.org/address/%s" % (addresses[address_index]))

            if not found:
                print("      no funds found!")

#===============================================================================
def RecoverSeedAndIndex():
    print("\nWelcome to IOTA Ledger Nano seed and index recovery!")

    recovery_words = InputRecoveryWords()
    if recovery_words == None:
        return

    passphrase = InputPassphrase()
    if passphrase == None:
        return

    ledger_start_index = InputLedgerStartIndex()
    if ledger_start_index == None:
        return
    ledger_start_index = int(ledger_start_index)

    ledger_end_index = InputLedgerEndIndex()
    if ledger_end_index == None:
        return
    ledger_end_index = int(ledger_end_index)

    if ledger_start_index > ledger_end_index:
        raise Exception("Ledger start index can't be bigger than the end index.")

    ledger_start_page = InputLedgerStartPage()
    if ledger_start_page == None:
        return
    ledger_start_page = int(ledger_start_page)

    ledger_end_page = InputLedgerEndPage()
    if ledger_end_page == None:
        return
    ledger_end_page = int(ledger_end_page)

    if ledger_start_page > ledger_end_page:
        raise Exception("Ledger start page can't be bigger than the end page.")

    address_amount = InputAddressAmount()
    if address_amount == None:
        return
    address_amount = int(address_amount)

    if address_amount < 1:
        raise Exception("Address amount can't be smaller than 1.")

    SearchLedgerIndex(recovery_words, passphrase, ledger_start_index, ledger_end_index, ledger_start_page, ledger_end_page, address_amount)

#===============================================================================
if __name__ == '__main__':
    RecoverSeedAndIndex()
