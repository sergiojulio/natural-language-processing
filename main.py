from textblob import TextBlob

text = '''
I'm just lying in a bar with my drip feed on
Talking to my girlfriend waiting for something to happen
And I wish it was the sixties
I wish I could be happy
I wish, I wish
I wish that something would happen'''

blob = TextBlob(text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
# 0.060
# -0.341
