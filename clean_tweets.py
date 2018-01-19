import pandas as pd
import re

ap = pd.read_csv('ap_clean.csv')
bbc = pd.read_csv('bbc_clean.csv')
nash_scene = pd.read_csv('nash_scene_clean.csv')
nc5 = pd.read_csv('nc5_clean.csv')
econ = pd.read_csv('the_economist_clean.csv')
time = pd.read_csv('time_clean.csv')

anew_dataset = pd.read_csv('all.csv')


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


# Calculate valence, arousal, and dominance scores of each tweet
def calculate_anew(dataframe):
    anew_original = anew_dataset
    anew = pd.DataFrame()
    anew['Description'] = anew_original['Description']
    anew['Valence Mean'] = anew_original['Valence Mean']
    anew['Arousal Mean'] = anew_original['Arousal Mean']
    anew['Dominance Mean'] = anew_original['Dominance Mean']

    valence = []
    arousal = []
    dominance = []

    for row in dataframe['tweet']:
        vscore = 0
        ascore = 0
        dscore = 0
        for word, val, aro, dom in zip(anew['Description'], anew['Valence Mean'],
                                       anew['Arousal Mean'], anew['Dominance Mean']):
            if word in row:
                vscore += float(val)
                ascore += float(aro)
                dscore += float(dom)
        valence.append(vscore)
        arousal.append(ascore)
        dominance.append(dscore)
    dataframe['Valence'] = valence
    dataframe['Arousal'] = arousal
    dataframe['Dominance'] = dominance
    print(dataframe)






calculate_anew(ap)



