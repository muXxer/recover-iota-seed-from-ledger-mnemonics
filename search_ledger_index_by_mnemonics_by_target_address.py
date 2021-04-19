
# -*- coding: utf-8 -*-
from six.moves import input
from mnemonics_utils import *
from iota.crypto.addresses import AddressGenerator, Address

#===============================================================================
def SearchLedgerIndexByTargetAddress(recovery_words, passphrase, ledger_start_index, ledger_end_index, ledger_start_page, ledger_end_page, address_amount, target_address):

    print("\nChecking ledger indexes for funds:")

    for ledger_index in range(ledger_start_index, ledger_end_index+1):
        for ledger_page in range(ledger_start_page, ledger_end_page+1):
            print("   Ledger Index: %d, Ledger Page: %d" % (ledger_index, ledger_page))

            iota_seed = MnemonicsToIotaSeed(recovery_words, passphrase, bip44_account=ledger_index, bip44_page_index=ledger_page)

            generator = AddressGenerator(iota_seed)
            addresses = generator.get_addresses(start=0, count=address_amount, step=1)

            # search given target address
            for address_index, address in enumerate(addresses):
                if target_address != address:
                    continue

                print("\n      Found address (seed: %s, ledger index: %d, ledger page: %d, address index: %d" % (iota_seed, ledger_index, ledger_page, address_index))
                print("\n      Your Address: %s" % (addresses[address_index]))
                print("\n                    https://explorer.iota.org/mainnet/address/%s" % (addresses[address_index][:81]))
                return

            print("      no funds found!")

#===============================================================================
def RecoverSeedAndIndex():
    print("\nWelcome to IOTA Ledger Nano seed and index recovery!")

    target_address_str = InputTargetAddress()
    if target_address_str == None:
        return

    if len(target_address_str) != 90:
        raise Exception("Please enter a valid target address with checksum. (90 chars)")

    target_address = Address(target_address_str.upper())
    if not target_address.is_checksum_valid():
        raise Exception("Wrong checksum. Please try again.")

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

    SearchLedgerIndexByTargetAddress(recovery_words, passphrase, ledger_start_index, ledger_end_index, ledger_start_page, ledger_end_page, address_amount, target_address)

#===============================================================================
if __name__ == '__main__':
    RecoverSeedAndIndex()
