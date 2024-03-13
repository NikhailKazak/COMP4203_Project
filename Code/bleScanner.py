import asyncio
import bleak
import datetime

async def scan_and_record():
    while True:
        try:
            #Scans for BLE devices
            devices = await bleak.discover()
            
            #Timestamp of current scan
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            #Dumps scanned BLE packet info to txt file
            with open("./bleScannerOutput.txt", "a") as file:
                for device in devices:

                    #CLI output
                    cliOutput = f"Timestamp: {timestamp}, Packet Type: BLE, Sending Address: {device.address}, Name: {device.name}\n"
                    for key, value in device.metadata.items():
                        cliOutput += f"{key}: {value}\n"
                    
                    #Writes the CLI output to a .txt file
                    file.write(cliOutput + "\n")
                    
                    #Also prints it to console
                    print(cliOutput.strip())
                    
            #Waits 5 seconds before scanning
            await asyncio.sleep(5)
            
        except(KeyboardInterrupt):
            #Press Ctrl+C to terminate program
            break

if __name__ == "__main__":
    print("Scanning for Bluetooth LE devices...")
    
    #Run the the scanner
    asyncio.run(scan_and_record())
