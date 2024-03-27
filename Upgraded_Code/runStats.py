import re
from datetime import datetime

def getAvgSizePacket():
    totalSize = 0
    count = 0

    with open("filteredBAddr.txt", "r") as file:
        for line in file:
            if "Adv. Packet size:" in line:
                size = int(re.search(r"Adv\. Packet size: (\d+)", line).group(1))
                totalSize += size
                count += 1

    avgSize = totalSize / count if count else 0
    
    return avgSize

def getAvgTimeBetweenPackets():
    timestamps = []
    with open("filteredBAddr.txt", "r") as file:
        for line in file:
            match = re.search(r"Timestamp: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
            if match:
                timestamp = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
                timestamps.append(timestamp)

    timeDif = [
        (t2 - t1).total_seconds() for t1, t2 in zip(timestamps, timestamps[1:])
    ]
    avgTime = sum(timeDif) / len(timeDif) if timeDif else 0

    return avgTime

if __name__ == "__main__":
    getAvgSizePacket()