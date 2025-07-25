from textblob import TextBlob
Name = input("\nName: ")
Name = Name.capitalize()
while True:
    Sentence = input("Sentence (Or 'Exit'): ")
    if Sentence.lower() == 'Exit':
        print("Bye!", Name)
        break
    Polarity = TextBlob(Sentence).sentiment.polarity
    if Polarity > 0.8:
        print(f"😍 {Name} Your Sentiment Polarity Is {Polarity}")
    elif Polarity > 0.6:
        print(f"🥰 {Name} Your Sentiment Polarity Is {Polarity}")
    elif Polarity > 0.4:
        print(f"😘 {Name} Your Sentiment Polarity Is {Polarity}")
    elif Polarity > 0.2:
        print(f"😊 {Name} Your Sentiment Polarity Is {Polarity}")
    elif Polarity == 0:
        print(f"😐 {Name} Your Sentiment Polarity Is {Polarity}")
    elif Polarity < -0.2:
        print(f"😔 {Name} Your Sentiment Polarity Is {Polarity}")
    elif Polarity < -0.4:
        print (f"😟 {Name} Your Sentiment Polarity Is {Polarity}")
    elif Polarity < -0.6:
        print (f"😢 {Name} Your Sentiment Polarity Is {Polarity}")
    elif Polarity < -0.8:
        print (f"😭 {Name} Your Sentiment Polarity Is {Polarity}")
    else:
        print (f"\U0001F610")