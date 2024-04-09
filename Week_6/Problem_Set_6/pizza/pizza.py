import sys
import csv
import os
from tabulate import tabulate

def print_usage_and_exit():
    print("Usage: python pizza.py <csv_file>")
    sys.exit(1)

def read_csv_file(csv_file):
    if not os.path.exists(csv_file):
        print("File does not exist")
        sys.exit(1)

    if not csv_file.endswith('.csv'):
        print("Not a CSV file")
        sys.exit(1)

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    return header, data

def main():
    if len(sys.argv) != 2:
        print("Too few or too many command-line arguments")
        print_usage_and_exit()

    csv_file = sys.argv[1]

    header, data = read_csv_file(csv_file)

    print(tabulate(data, headers=header, tablefmt="grid"))

if __name__ == "__main__":
    main()
