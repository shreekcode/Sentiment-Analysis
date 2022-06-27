# this program is for sentiment analysis of facebook data

import pandas as pd  # importing pandas lib
import nltk  # importing nltk lib
from nltk.sentiment.vader import SentimentIntensityAnalyzer  # importing analyser from nltk

nltk.downloader.download('vader_lexicon')
# instead of importing we are directly downloading the vader lexicon

# loading file
file='Facebook_data.xlsx'
# reading from excel file using pandas library
xl=pd.ExcelFile(file)

# parsing and coverting excel file to data frame
dfs=xl.parse(xl.sheet_names[0])
# deleting blank rows from data frame
dfs=list(dfs['Timeline'])  # removes blank rows from the data frame.

print(dfs)

# performing sentiment analysis on data frames

sid=SentimentIntensityAnalyzer()     # initiating sentiment intensity analyzer
str1="19:49 + UTC"

# this only anallyses the main post not the time i mentioned above.
# it skips the string(str1) i have written mentioning time

for data in dfs:
    a=data.find(str1)  # this comand finds str1 in data frames.
    if a==-1:  # this if will be executed when str1 is not found in a perticular line.
        ss=sid.polarity_scores(data)  # this analyses the main post part and performes sentiment analysis.
        print(data)
        for k in ss:
            print(k,ss[k])
