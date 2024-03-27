import asyncio
from bleak import BleakScanner
import datetime
import sys

async def scan_and_record():
    counter = 0

    while counter<10:    

        #Scans for BLE devices
        devices = await BleakScanner.discover()

        #Timestamp of current scan
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Dumps scanned BLE packet info to txt file
        with open("./bleScannerOutput2.txt", "a") as file:
            for device in devices:

                #Size of adv. data in bytes
                sumVal = 0
                md = device.metadata["manufacturer_data"]
                su = device.metadata["uuids"]
                dn = device.name
                sumVal += (sum(len(bytes(value)) for value in md.values())) + (sum(16 for x in su)) 
                try:
                    sumVal += len(dn)
                except(TypeError):
                    pass

                #CLI 
                #For Manufacturer Data, the keys are assigned Company Identifiers (by Bluetooth SIG) and the values are bytes
                cliOutput = f"Timestamp: {timestamp} \n Device Name: {device.name}\n Device Address: {device.address}\n Manufacturer data {device.metadata["manufacturer_data"]}\n Service UUIDs {device.metadata["uuids"]}\n RSSI {device.rssi}\n Adv. Packet size: {sumVal} bytes\n"
                
                #Writes the CLI output to a .txt file
                file.write(cliOutput + "~~~\n")
                
                #Also prints it to console
                print(cliOutput.strip())
                
        #Increase counter
        counter+=1
            
def main():
    print("Scanning for Bluetooth LE devices...")
    
    #Run the the scanner
    asyncio.run(scan_and_record())

if __name__ == "__main__":
   main()