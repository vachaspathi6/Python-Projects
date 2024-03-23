import webbrowser

def play_video(video_url):
    webbrowser.open(video_url)

def main():
    video_url = input("Enter YouTube video URL: ")
    play_video(video_url)

if __name__ == "__main__":
    main()
