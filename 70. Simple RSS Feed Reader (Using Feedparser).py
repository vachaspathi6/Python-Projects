import feedparser

def read_feed(feed_url):
    feed = feedparser.parse(feed_url)
    print("Title:", feed.feed.title)
    print("Description:", feed.feed.description)
    print("Entries:")
    for entry in feed.entries:
        print("- Title:", entry.title)
        print("  Summary:", entry.summary)
        print("  Link:", entry.link)
        print()

def main():
    feed_url = input("Enter RSS feed URL: ")
    read_feed(feed_url)

if __name__ == "__main__":
    main()
