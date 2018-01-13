import pandas as pd
import re

ap = pd.read_csv('ap.csv')
bbc = pd.read_csv('bbc.csv')
nash_scene = pd.read_csv('nash_scene.csv')
nc5 = pd.read_csv('nc5.csv')
econ = pd.read_csv('the_economist.csv')
time = pd.read_csv('time.csv')


# function to extract just tweet text from csv file
# returns a dataframe with one column containing the text
def extract_text(filename):
    data = pd.read_csv(filename)
    data['text'] = data['text'].str[2:]
    newdata = pd.DataFrame()
    newdata['tweet'] = data['text']
    return newdata


# "cleans" text of the tweet (to some extent)
def clean_text(dataframe):
    # remove RT
    dataframe['tweet'] = dataframe['tweet'].str.replace('RT', '')
    # remove links
    no_url_list = []
    for row in dataframe['tweet']:
        row = row.split('https')[0]
        row = row.split('http')[0]
        row = row.lstrip(' ')
        no_url_list.append(row)
    # remove unicode-escape utf-8 encoded stuff, and convert what can be
    no_escape = []
    for item in no_url_list:
        new = bytes(item, 'utf-8').decode('unicode-escape').encode('latin-1').decode('utf8')
        no_escape.append(new)
    ampersand = []
    no_amp = []
    for i in no_escape:
        if '&amp' in i:
            n = i.replace('&amp;', '&')
            ampersand.append(n)
        else:
            no_amp.append(i)
    ampersand.extend(no_amp)
    cleandf = pd.DataFrame()
    cleandf['tweet'] = ampersand
    return cleandf


# exports a dataframe with one column containing the text
# of a user's tweets to a csv
def export_tweet(dataframe, name):
    dataframe.to_csv('/Users/powermac/PycharmProjects/news_thesis/' + name + '.csv', index=False)

a = clean_text(ap)
b = clean_text(bbc)
n = clean_text(nash_scene)
nc = clean_text(nc5)
e = clean_text(econ)
t = clean_text(time)

export_tweet(t, 'time_clean')



