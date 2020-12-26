# -*- coding: utf-8 -*-
from mnemonics_utils import MnemonicsToIotaSeed, InputRecoveryWords, InputPassphrase

#===============================================================================
def RecoverSeed():
    print("\nWelcome to IOTA Ledger Nano seed recovery!")

    recovery_words = InputRecoveryWords()
    if recovery_words == None:
        return

    passphrase = InputPassphrase()
    if passphrase == None:
        return

    print("\nCalculating your IOTA seed...")
    iota_seed = MnemonicsToIotaSeed(recovery_words, passphrase)
    print("Seed: %s, Length: %d" % (iota_seed, len(iota_seed)))

#===============================================================================
if __name__ == '__main__':
    RecoverSeed()
