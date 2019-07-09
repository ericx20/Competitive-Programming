import sys

def formatted(address):
    plusIndex = address.find('+')
    atIndex = address.find('@')
    if plusIndex == -1:
        return address[0:atIndex].replace('.', '') + address[atIndex:]
    else:
        return address[0:plusIndex].replace('.', '') + address[atIndex:]

for i in range(10):
    numAddresses = int(sys.stdin.readline())
    addressList = ['']*numAddresses
    for j in range(numAddresses):
        newAddress = formatted(sys.stdin.readline().lower())
        addressList[j] = newAddress
    print(len(set(addressList)))
