import re
from datetime import datetime

def getUniqueBAddrs():
    '''
    Searches through the BLE Scanner (V2) results
    for unique Bluetooth addresses. 

    Adds the unique addresses to a list.

    Returns the list.
    '''

    #List for unique addresses + device name
    addrDevs = []

    #Reads through the scanner output to get unique addrs
    with open("bleScannerOutput2.txt", "r") as file:
        curName = ""
        for line in file:
            if "Device Name:" in line:
                curName = line.strip().split(": ")[1]
            if "Device Address:" in line:
                address = line.strip().split(": ")[1]
                device_info = f"{address} :: {curName}"
                if device_info not in addrDevs:
                    addrDevs.append(device_info)

    #Returns the addresses
    return addrDevs

def reorgByBAddr(targetAddress):    
    '''
    Uses the user's input to search for the logs with the pertinent
    Bluetooth address.

    Retrieves these entries and sorts them by timestamp - in order of
    earliest time detected to most recent time detected.
    '''          

    #Reads the input file and splits the entries based on the delimiter "~~~"
    with open("bleScannerOutput2.txt", "r") as file:
        content = file.read()
    entries = content.strip().split("~~~")

    #Parses the entries and filters by Bluetooth address
    filteredEntries = []
    for entry in entries:
        if targetAddress in entry:
            filteredEntries.append(entry)

    #Uses REGEX to match the pattern and convert the timestamp string into a DateTime Object necessary for sorting
    def parse_timestamp(entry):
        match = re.search(r"Timestamp: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", entry)
        return datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S") if match else None

    #Sorts the entries
    sortedEntries = sorted(filteredEntries, key=parse_timestamp)

    #Writes the sorted entries a new file, overwriting any existing content
    with open("filteredBAddr.txt", "w") as file:
        file.write("~~~".join(sortedEntries))
