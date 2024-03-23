from pytube import YouTube

def download_video(url, resolution='720p'):
    yt = YouTube(url)
    stream = yt.streams.filter(res=resolution).first()
    stream.download()
    print("Video downloaded successfully!")

def main():
    url = input("Enter YouTube video URL: ")
    resolution = input("Enter video resolution (1080p, 720p, etc.): ")
    download_video(url, resolution)

if __name__ == "__main__":
    main()
