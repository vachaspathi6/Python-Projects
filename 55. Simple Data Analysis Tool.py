## To run this code, you must have csv file.
## You can get a demo csv file from here - https://sample-videos.com/csv/Sample-Spreadsheet-100-rows.csv

import pandas as pd

def analyze_data(csv_file):
    df = pd.read_csv(csv_file)
    print("Summary Statistics:")
    print(df.describe())
    print("\nHead of DataFrame:")
    print(df.head())

def main():
    csv_file = input("Enter CSV file path: ")
    analyze_data(csv_file)

if __name__ == "__main__":
    main()
