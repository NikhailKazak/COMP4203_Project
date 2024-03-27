import bluetooth
import datetime

#Timestamp of current scan
def get_timestamp():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp

#Bluetooth Inquiry Scans
def bluetooth_classic_scanner():
    with open('bluetooth_data.txt', 'a') as file:
        file.write("Bluetooth Inquiry Scan Results\n")

    while True:
        try:
            #Does inquiry scans for Bluetooth classic
            devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
            for address, name in devices:
                timestamp = get_timestamp()

                #Print the timestamp, device name and address to CLI
                cliOutput = f"{timestamp} - Device name: {name}, Address: {address}\n"
                print(cliOutput)

                #Writes the CLI output to a .txt file 
                with open('bluetooth_data.txt', 'a') as file:
                    file.write(cliOutput)

        except KeyboardInterrupt:
            #Press Ctrl+C to terminate program
            break

#Callss the bluetooth_classic_scanner() function
bluetooth_classic_scanner()