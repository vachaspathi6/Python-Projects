import datetime

def set_reminder():
    reminder = input("Enter your reminder: ")
    time_delay = int(input("Enter time delay in minutes: "))
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=time_delay)
    print(f"Reminder set for {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}: {reminder}")

def main():
    set_reminder()

if __name__ == "__main__":
    main()
