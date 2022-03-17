import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

FRSMS = pd.read_csv('FR_SMS_Data.csv')
FRSMSTXT = FRSMS['SMS_ANON'].squeeze()

def firstwordscrape(dataframe, list): 
  for index in range(len(dataframe)):
    try:
      tokens = nltk.word_tokenize(dataframe[index])
      list.append(tokens[0])
    except Exception:
      pass

First_Words = []
firstwordscrape(FRSMSTXT, First_Words)

FW_df = pd.DataFrame(First_Words, columns = ['First Words'])
print(FW_df['First Words'].value_counts()[:30])
FW_df.to_csv('First_Words.csv')

def jewordscrape(dataframe, list):
  for index in range(len(dataframe)):
    try:
      tokens = nltk.word_tokenize(dataframe[index])
      if tokens[0] == 'Je':
        elmnt = tokens[0] + " " + tokens[1]
        list.append(elmnt)
    except Exception:
      pass

Je_Words = []
jewordscrape(FRSMSTXT, Je_Words)

JW_df = pd.DataFrame(Je_Words, columns = ['Je + Word'])
print(JW_df['Je + Word'].value_counts()[:10])
JW_df.to_csv('Je+Words.csv')

def ouiwordscrape(dataframe, list):
  for index in range(len(dataframe)):
    try:
      tokens = nltk.word_tokenize(dataframe[index])
      if tokens[0] == 'Oui':
        elmnt = tokens[0] + " " + tokens[1]
        list.append(elmnt)
    except Exception:
      pass

Oui_Words = []
ouiwordscrape(FRSMSTXT, Oui_Words)

OW_df = pd.DataFrame(Oui_Words, columns = ['Oui + Word'])
print(OW_df['Oui + Word'].value_counts()[:10])
OW_df.to_csv('Oui+Words.csv')

def okwordscrape(dataframe, list):
  for index in range(len(dataframe)):
    try:
      tokens = nltk.word_tokenize(dataframe[index])
      if tokens[0] == 'Ok':
        elmnt = tokens[0] + " " + tokens[1]
        list.append(elmnt)
    except Exception:
      pass

OK_Words = []
okwordscrape(FRSMSTXT, OK_Words)

OKW_df = pd.DataFrame(OK_Words, columns = ['Ok + Word'])
print(OKW_df['Ok + Word'].value_counts()[:10])
OKW_df.to_csv('Ok+Words.csv')
