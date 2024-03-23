import calendar

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    print(calendar.month(year, month))

if __name__ == "__main__":
    main()
