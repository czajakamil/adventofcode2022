"""
1. The start of a packet is indicated by a sequence of four characters that are all different.
2. Find first letter after the start of the packet
3. Get the index of that letter
"""
def packet_finder(n: int, datastream: str) -> int:
    # find first letter after n different characters
    for i in range(n, len(datastream)-n):
        if len(set(datastream[i-n:i])) == n:
            return i
        


def main():
    with open("day6/data.txt", "r") as i:
        datastream = i.read()

    print(packet_finder(4, datastream))
    print(packet_finder(14, datastream))


if __name__ == "__main__":
    main()