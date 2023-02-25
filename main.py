from textblob import TextBlob

text = '''
Your last chance has arrived
Best, you've got to be the best
You've got to be the best
You've got to change the world
And use this chance to be heard
Your time is now (Your time is now)
'''

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
