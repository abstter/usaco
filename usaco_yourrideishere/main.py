'''
DATE: 8/21/23 4:30p.m
ID: Abhiram Avasarala
LANG: PYTHON3
TASK: ride
'''

def checksum1(name):
    checksum = 1
    for char in name:
        checksum *= ord(char) - ord('A') + 1
    return checksum % 47

def main():
    with open('ride.in', 'r') as fin:
        lines = fin.readlines()

    arr_str = []
    for line in lines:
        arr_str.append(line.strip())

    comet_checksum = checksum1(arr_str[0])
    group_checksum = checksum1(arr_str[1])

    with open('ride.out', 'w') as fout:
        if comet_checksum == group_checksum:
            fout.write("GO\n")
        else:
            fout.write("STAY\n")

    exit()


if __name__ == "__main__":
    main()







