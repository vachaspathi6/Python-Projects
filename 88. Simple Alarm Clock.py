import time

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm! Wake up!")
            break
        time.sleep(1)

def main():
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
