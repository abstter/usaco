'''
ID: Abhiram Avasarala
LANG: PYTHON3
TASK: gift1
'''
def process_gifts(NP, names, gift_data):
    accounts = {name: 0 for name in names}

    for giver, amount, num_recipients, recipients in gift_data:
        if num_recipients > 0:
            gift_amount = amount // num_recipients
            remainder = amount % num_recipients
            accounts[giver] -= amount - remainder

            for recipient in recipients:
                accounts[recipient] += gift_amount

    return accounts

def read_input(filename="gift1.in"):
    with open(filename, "r") as file:
        NP = int(file.readline().strip())
        names = [file.readline().strip() for _ in range(NP)]
        gift_data = []

        for _ in range(NP):
            giver = file.readline().strip()
            amount, num_recipients = map(int, file.readline().split())
            recipients = [file.readline().strip() for _ in range(num_recipients)]
            gift_data.append((giver, amount, num_recipients, recipients))

    return NP, names, gift_data

def write_output(accounts, filename="gift1.out"):
    with open(filename, "w") as file:
        for name, balance in accounts.items():
            file.write(f"{name} {balance}\n")

if __name__ == "__main__":
    NP, names, gift_data = read_input()
    accounts = process_gifts(NP, names, gift_data)
    write_output(accounts)

