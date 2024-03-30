import sys
import bleScannerV2
import funcBAddr
import runStats

if __name__ == "__main__":

    print("Welcome to our BLE Scanner")
    
    promptInput="0"

    while promptInput!="4":

        print("Please begin by choosing a mode (the numeric value) from those listed below:")
        print("1. Basic BLE Scan\n2. Scan for BLE devices and get metrics \n3. Get Metrics - assumes a BLE Scan has already been done \n4. Exit Program\n")


        #Take input
        print("Your choice: ")
        promptInput=str(input())

        if(promptInput=="1"):
            print("You've chosen option 1")

            #Doesn't generate a return... Generates a file
            initBLEScan=bleScannerV2.main()
            
        elif(promptInput=="2"):
            print("You've chosen option 2")

            #Doesn't generate a return... Generates a file
            initBLEScan=bleScannerV2.main()

            #Generates a return of all unique BAddr addresses
            unique_addresses=funcBAddr.getUniqueBAddrs()

            print("\nHere's a list of unique Bluetooth addresses found from the BLE scan\n")
            for addr in unique_addresses:
                print(addr)

            print("Which address do you wish to gather metrics for? Please enter the full address and device ( e.g., 00:04:4B:F9:01:DB :: NVIDIA SHIELD Remote )\n")

            opt1=""

            while(opt1 not in unique_addresses):
                opt1=str(input())

            opt1=opt1[0:17]

            print("Generating and retrieving entries for ", opt1)
            print("For more info on {} refer to ../filteredBAddr.txt".format(opt1))
            reorganizedEntries=funcBAddr.reorgByBAddr(opt1)

            avgSize=runStats.getAvgSizePacket()
            print("Average packet size in bytes: ", avgSize)

            avgTime=runStats.getAvgTimeBetweenPackets()
            print("Average time between packets in seconds: ", avgTime)

            print("\n")

        elif(promptInput=="3"):
            print("You've chosen option 3")

            #Generates a return of all unique BAddr addresses
            unique_addresses=funcBAddr.getUniqueBAddrs()

            print("\nHere's a list of unique Bluetooth addresses found from the BLE scan\n")
            for addr in unique_addresses:
                print(addr)

            print("Which address do you wish to gather metrics for? Please enter the full address and device ( e.g., 00:04:4B:F9:01:DB :: NVIDIA SHIELD Remote )\n")

            opt1=""

            while(opt1 not in unique_addresses):
                opt1=str(input())

            opt1=opt1[0:17]

            print("Generating and retrieving entries for ", opt1)
            print("For more info on {} refer to ../filteredBAddr.txt".format(opt1))
            reorganizedEntries=funcBAddr.reorgByBAddr(opt1)

            avgSize=runStats.getAvgSizePacket()
            print("Average packet size in bytes: ", avgSize)

            avgTime=runStats.getAvgTimeBetweenPackets()
            print("Average time between packets in seconds: ", avgTime)

            print("\n")

    print("Goodbye")
    exit