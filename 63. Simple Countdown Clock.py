import time

def countdown(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Countdown complete!")

def main():
    seconds = int(input("Enter number of seconds to countdown: "))
    countdown(seconds)

if __name__ == "__main__":
    main()
