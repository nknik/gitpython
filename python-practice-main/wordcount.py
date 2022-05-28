# # Here are all the installs and imports you will need for your word cloud script and uploader widget

# !pip install wordcloud
# !pip install fileupload
# !pip install fileupload
# !pip install ipywidgets
# !jupyter nbextension install --py --user fileupload
# !jupyter nbextension enable --py fileupload

from sympy import re
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    non_punctuation_text=""
    for char in file_contents:
        if char not in punctuations:
            non_punctuation_text=non_punctuation_text+char
    words=non_punctuation_text.split()
    clean_words=[]
    frequencies={}
    for word in words:
        if word.isalpha():
            if word not in uninteresting_words:
                clean_words.append(word)
    for alpha_word in clean_words:
        if alpha_word not in frequencies:
            frequencies[alpha_word]=1
        else:
            frequencies[alpha_word]+=1
    #wordcloud
    def plan_change(nk):
        n={f"{x} {y}":y for x,y in nk.items()}
        return n 
    # freqq=plan_change(frequencies)
    freqq=frequencies
    freqq["NIKHIL CHALIKWAR"]=10
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freqq)
    # nk sayes if you want to remove count from word then coment above two lines VV
    # cloud = wordcloud.WordCloud()
    # cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


   
    # Display your wordcloud image
# def _cb(change):
# global file_contents
file_contents="Python DataStructure Algorithms Flutter HTML CSS JS NoSQL  Git GitHub Django Python Python C CPP JAVA ProblemSOLVING CRITICAL THINKING React Javacript Bootstrap MongoDB sql sql sql sql MySql  MachineLearning MachineLearning MachineLearning MachineLearning AI AI AI AI AI AI NodeJS Angular RPA ServiceNOW jeera AWS CLoud DATABASE "
# myimage = calculate_frequencies(file_contents)

# # print(plan_change(myimage))
# plt.imshow(myimage, interpolation = 'nearest')
# plt.axis('off')
# plt.show()
file_contents+="NIKHILCHALIKWAR "*10
wordcloud = wordcloud.WordCloud( max_font_size=50, max_words=100, background_color="white").generate(file_contents)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
