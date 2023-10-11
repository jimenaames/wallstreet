import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords = stopwords.words("english")

class Keyword:
    def __init__(self,text_col):
        self.text_col = text_col
    def keyword_list(self):
        keyword_list = replaceSpecial(self.text_col)
        self.keyword_list = CountFrequencyinWords(keyword_list)[0]
        self.keyword_list_short = self.keyword_list[0:7]
    def keyword_dict(self):
        keyword_dict = replaceSpecial(self.text_col)
        self.keyword_dict = CountFrequencyinWords(keyword_dict)[1]

def replaceSpecial(text_col):
    list = str([word for word in text_col if not word in stopwords])
    list = list.lower()
    list=list.replace(",","")
    list=list.replace("the","")
    list=list.replace("'","")
    list=list.replace(":","")
    list=list.replace("•","")
    list=list.replace("_","")
    list=list.replace("x000d","")
    list=list.replace(r"\n"," ")
    list=list.replace("§","")
    list = list.replace("●","")
    list=list.replace("mangroves","")
    list=list.replace("corals","")
    list=list.replace("reefs","")
    list=list.replace("and","")
    list=list.replace("of","")
    list = list.split()
    return list

def CountFrequencyinWords(my_list):
    desc_dict = []
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1.
    freq_sorted_keys = dict(sorted(freq.items(), key=lambda item: (item[1]), reverse = True,))
    for r in freq_sorted_keys:
        desc_dict.append(r)
    return desc_dict, freq_sorted_keys

