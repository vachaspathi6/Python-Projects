import time

def set_alarm(hour, minute):
    alarm_time = f"{hour:02}:{minute:02}"
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm! Wake up!")
            break
        time.sleep(60)  # Check every minute

def main():
    print("Alarm Clock")
    hour = int(input("Enter the hour (0-23): "))
    minute = int(input("Enter the minute (0-59): "))
    set_alarm(hour, minute)

if __name__ == "__main__":
    main()
