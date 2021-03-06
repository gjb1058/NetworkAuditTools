import socket
import ipaddress
import sys

def createAddressList( aRange ): 
    addressList = list()
    if aRange.find('-') != -1:
        aRange = aRange.split('-')
        start = ipaddress.IPv4Address( aRange[0] )
        end = ipaddress.IPv4Address( aRange[1] )
        for i in range( int( start ), int( end ) + 1 ):
            addressList.append( str( ipaddress.IPv4Address( i ) ) )
    elif aRange.find('/') != -1:
        aRange = list( ipaddress.ip_network(aRange).hosts() )
        for i in aRange:
            addressList.append( str( i ) )
    else:
        addressList.append( aRange )
    return addressList


def createPortList( pRange ):
    portList = list()
    if pRange.find('-') != -1:
        pRange = pRange.split('-')
        start = pRange[0]
        end = pRange[1]
        for i in range( int( start ), int( end ) + 1 ):
            portList.append( i )
    elif pRange.find(',') != -1:
        portList = pRange.split(',')
    else:
        portList.append( pRange )
    return portList

def scanPort( address, port, sock ):
    try:
        sock.connect(( address, int(port)))
        print( address + ":" + str(port) + " is opened")
        sock.close()
    except socket.timeout:
        print( address + ":" + str(port) + " is filtered")
    except socket.error:
        print( address + ":" + str(port) + " is closed")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print( "Incorrect number of arguments")
        print( "Usage: portScan.py [IP Address Range] [Port Range]")
    addressRange = sys.argv[1]
    portRange = sys.argv[2]
    addressList = createAddressList( addressRange )
    portList = createPortList( portRange )
    for i in addressList:
        for j in portList:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            scanPort( i, j, s )
