from textblob import TextBlob
Name = input("\nName: ")
while True:
    Sentence = input("Sentence (Or 'Exit'): ")
    if Sentence.lower() == 'Exit':
        print("Bye!", Name)
        break
    Polarity = TextBlob(Sentence).sentiment.polarity
    if Polarity > 0:
        print("\U0001F642", Polarity)
    elif Polarity < 0:
        print("\U0001F641", Polarity)
    else:
        print("\U0001F610", Polarity)