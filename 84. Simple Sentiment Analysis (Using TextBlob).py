from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

def main():
    text = input("Enter text for sentiment analysis: ")
    sentiment = analyze_sentiment(text)
    print("Sentiment:", sentiment)

if __name__ == "__main__":
    main()
