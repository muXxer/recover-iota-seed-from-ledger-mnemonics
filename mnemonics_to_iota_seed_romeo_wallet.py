# -*- coding: utf-8 -*-
import xxhash
from six.moves import input
from mnemonics_to_iota_seed import MnemonicsToIotaSeed, InputRecoveryWords, InputPassphrase

#===============================================================================
def InputRomeoAccount():
    print("\nPlease enter your Romeo account now (number ranging from 0 to 999999999, or an arbitrary text):")

    try:
        romeo_account = input("   Romeo account: ")
        try:
            account = int(romeo_account)
        except:
            # Account is not an integer, hash the text with xxhash
            x = xxhash.xxh32(seed=0xABCD)
            x.update(romeo_account.upper().lstrip().rstrip())
            account = x.intdigest()
        
        if account >= 1000000000:           # from 0 to 999999999
            account_str = str(account)
            account = int(account_str[0:9])
        return account       
    except KeyboardInterrupt:
        return None

#===============================================================================
def InputRomeoPageIndex():
    print("\nPlease enter your Romeo page index now (it starts with index 1):")

    try:
        romeo_page = input("   Romeo page index: ")
        page_index = int(romeo_page) - 1
        if page_index < 0:
            raise Exception("Invalid page index!")
        return page_index
    except KeyboardInterrupt:
        return None

#===============================================================================
def RecoverRomeoSeed():
    print("\nWelcome to IOTA Ledger Nano seed recovery for Romeo wallet!")
    
    recovery_words = InputRecoveryWords()
    if recovery_words == None:
        return
    
    passphrase = InputPassphrase()
    if passphrase == None:
        return
    
    account    = InputRomeoAccount()
    if account == None:
        return
    

    page_index = InputRomeoPageIndex()
    if page_index == None:
        return
    
    print("\nRomeo account Nr: %d" % (account))
    print("Romeo page index: %d" % (page_index))
    MnemonicsToIotaSeed(recovery_words, passphrase, bip44_account=account, bip44_page_index=page_index)

#===============================================================================
if __name__ == '__main__':
    RecoverRomeoSeed()
