import pandas as pd
import os
from pdf2image import convert_from_path
import pyperclip as pc
from os import listdir
from os.path import isfile, join
import pytesseract
from PyPDF2 import PdfWriter, PdfReader
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from numpy import nan

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

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

html = urllib.request.urlopen('https://www.pwc.com/us/en/industries/financial-services/fintech/bitcoin-blockchain-cryptocurrency.html').read() #test article
article_str = text_from_html(html)