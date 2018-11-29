import tweepy
from wordcloud import WordCloud
import matplotlib.pyplot as plt

consKey = "4TGPfg62pT76yWTnTE8INjJCL"
consSecret = "dkhHybaFTIAflvCVB5vFHQPu0eCHFQN1BIbpdx3hjt8q3aRqWy"
accessKey = "3061686882-PrrngsYGKlMV92KseseATs1Gjr5Yyucry61Lwl2"
accessSecret = "aLOiD62JKQg29mSoz6chfpLP7fbBpG4syMuaUvlAqe9J0"

auth = tweepy.OAuthHandler(consumer_key=consKey, consumer_secret=consSecret)

auth.set_access_token(accessKey, accessSecret)

api = tweepy.API(auth)
search_term = input("Enter the term to be searched")
number_of_tweets = int(input("Enter the number of tweets"))

tweets = tweepy.Cursor(api.search, q=search_term, lang="en").items(number_of_tweets)

cloud = ""
for each in tweets:
    cloud = cloud + each.text

cloud = WordCloud(background_color="white").generate(cloud)

plt.imshow(cloud)
plt.axis('off')
plt.show()
