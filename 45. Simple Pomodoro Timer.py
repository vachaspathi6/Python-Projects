import time

def pomodoro_timer(work_minutes, break_minutes):
    print("Pomodoro Timer started!")
    while True:
        print("Work for {} minutes".format(work_minutes))
        time.sleep(work_minutes * 60)
        print("Take a break for {} minutes".format(break_minutes))
        time.sleep(break_minutes * 60)

def main():
    work_minutes = int(input("Enter work duration (in minutes): "))
    break_minutes = int(input("Enter break duration (in minutes): "))
    pomodoro_timer(work_minutes, break_minutes)

if __name__ == "__main__":
    main()
