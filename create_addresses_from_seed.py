# -*- coding: utf-8 -*-
from six.moves import input
from iota.crypto.addresses import AddressGenerator

#===============================================================================
def InputSeed():
    print("\nPlease enter your seed:")
    
    try:
        return input("   IOTA Seed: ")
    except KeyboardInterrupt:
        return None

#===============================================================================
def InputIndex():
    print("\nPlease enter address start index:")
    
    try:
        return input("   Address start index: ")
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
def CreateAddress():
    print("\nWelcome to IOTA addresses generator!")
    
    seed = InputSeed()
    if seed == None:
        return
    
    index = InputIndex()
    if index == None:
        return
    index = int(index)

    amount = InputAddressAmount()
    if amount == None:
        return
    amount = int(amount)

    generator = AddressGenerator(seed)
    addresses = generator.get_addresses(start=index, count=amount, step=1)

    offset = 0
    for address in addresses:
        print("\nYour Address #%d: %s" % (index+offset, address))
        print("\n                  https://thetangle.org/address/%s" % (address))
        offset += 1
    
    print()

#===============================================================================
if __name__ == '__main__':
    CreateAddress()
