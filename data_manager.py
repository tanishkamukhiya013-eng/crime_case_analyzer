import csv

FILE = "cases.csv"

def save_cases(cases):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(cases)

def load_cases():
    try:
        with open(FILE, "r") as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        return []