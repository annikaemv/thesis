import pandas as pd
import re

ap = pd.read_csv('ap.csv')
bbc = pd.read_csv('bbc.csv')


# function to extract just tweet text from csv file
# returns a dataframe with one column containing the text
def extract_text(filename):
    data = pd.read_csv(filename)
    data['text'] = data['text'].str[2:]
    newdata = pd.DataFrame()
    newdata['tweet'] = data['text']
    return newdata


# exports a dataframe with one column containing the text
# of a user's tweets to a csv
def export_tweet(dataframe, name):
    dataframe.to_csv('/Users/powermac/PycharmProjects/news_thesis/' + name + '.csv', index=False)


# "cleans" text of the tweet (to some extent)
def clean_text(dataframe):
    # remove RT
    dataframe['tweet'] = dataframe['tweet'].str.replace('RT', '')
    # remove links
    newdf = pd.DataFrame()
    newdf['tweet'] = ''
    no_url_list = []
    for row in dataframe['tweet']:
        row = row.split('https')[0]
        row = row.split('http')[0]
        no_url_list.append(row)
        print(row)
    newdf['tweet'] = no_url_list

clean_text(bbc)


