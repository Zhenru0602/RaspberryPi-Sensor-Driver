import time
import socket
import json
import bluetooth as bt

#
# This program is a bluetooth sender to send the data
#

PORT = 3
BUF_SZ = 1024

def display_devs(nb_devs):
    for n, name in enumerate(nb_devs):
        print("%d: %s" % (n+1, name))

def search_devs():
    # scan for bt devices
    nearby_devices = bt.discover_devices(lookup_names = True)
    display_devs(nearby_devices)
    i = int(input("select device with index (0 to exit):\n"))
    if i <= 0: exit(0)
    return nearby_devices[i-1]


def run_bt(bd_address="unknown"):
    try:
        #device select if no arg passed to run_bt
        if bd_address == "unknown":
            bd_address = search_devs()

        #socket setup
        s = bt.BluetoothSocket(bt.RFCOMM)
        s.connect((bd_address, PORT))

        while True:
            #receive data from server
            raw_data = s.recv(BUF_SZ)
            if not raw_data: raise ConnectionError
            data = json.loads(raw_data.decode()) # a dictionary
            print(data)

    except ConnectionError:
        print("Connection Failed")

    except KeyboardInterrupt:
        print("Program stopped by user")

    except bt.btcommon.BluetoothError:
        print("Connection closed by host")

    finally:
        s.close()

if __name__ == "__main__":
    # currently hardcoded this MAC ad to illustrate
    # pass empty argument to run_bt to allow bt scanning
    run_bt("B8:27:EB:F9:F6:38")


