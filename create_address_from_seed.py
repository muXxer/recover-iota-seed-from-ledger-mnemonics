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
    print("\nPlease enter address index:")
    
    try:
        return input("   Address Index: ")
    except KeyboardInterrupt:
        return None

#===============================================================================
def CreateAddress():
    print("\nWelcome to IOTA address generator!")
    
    seed = InputSeed()
    if seed == None:
        return
    
    index = InputIndex()
    if index == None:
        return
    
    generator = AddressGenerator(seed)
    addresses = generator.get_addresses(start=int(index), step=1)

    print("\nYour Address: %s" % addresses[0])
    print("\nhttps://thetangle.org/address/%s\n" % (addresses[0]))

#===============================================================================
if __name__ == '__main__':
    CreateAddress()
