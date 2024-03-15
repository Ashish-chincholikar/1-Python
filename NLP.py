# -*- coding: utf-8 -*-
"""
Created on Tue May 16 08:08:57 2023

@author: 91721
"""

#python for NLP (Natural language processing) in machine learning

#tokenization
txt = 'Welcome to the new year 2023'
x = txt.split()
print(x)

#remove special characters 
import re# function to remove special characters
def remove_special_characters(text):
    #define patter to keep
    pat = r'[^a-zA-Z0-9.,!?/:;\"\'\s]'
    return re.sub(pat , "" , text)

#call function
remove_special_characters("007 Not sure@ about this #match today! , **what is&&& your option?")

#remove numbers
import re# function to remove special characters
def remove_numbers(text):
    #define patter to keep
    pat = r'[^a-zA-Z.,!?/:;\"\'\s]'
    return re.sub(pat , "" , text)

""""007 Not sure@ about this #match today! , **what is&&& your option?" """
#call function
remove_numbers("007 Not sure@ about this #match today! , **what is&&& your option?")

import re
txt = 'Welcome: to the, new year; 2023!'
x = re.split(r'(?:,|;|\s)\s*', txt)
print(x)    

#removing punctuation is easy and can be done by using string.punctuation

import string
def remove_punctuation(text):
    text = "".join([c for c in text if c not in string.punctuation])
    return text 

remove_punctuation("Article: @first sentence of some, {important} arcticle")
#================================slot-2================================
#stemming 
#stemming is the process of reducing inflected/derived words
#to their stem word. base or root form 
#these mainly rely on chopping off 's' 'es' 'ing' , 'ly' etc from
#the end of the words and sometimes the conversation is not desirable.
#but nonthless ,  stemming helps us in standard 
import nltk # function for stemming
def get_stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text = ' '.join([stemmer.stem(word)for word in text.split()])
    return text

print(get_stem("we are eating and swimming ; we have running and sleeping"))

#lemmatization
#it is the advanced form of stemming , it does conversion proerty with the 
#help of vocubualary

line = 'asdf fjdk afed, fjek,asdf, foo'
re.split(r'(?:,|;|\s)\s*' , line)

#matching text at the start or at end of the string
filename = 'spam.txt'
filename.endswith('.txt')

area_name = '6th lane west Andheri'
area_name.endswith('west Andheri')

#-------------------------------------------------------------------
#startswith() method and endswith() method are provided by nltk
choices = ('http:' , "ftp:")
url = 'http://www.python.org'
url.startswith(choices)

#--------------------------------------------------------------------
#slicing a string
#string_name[start : end :step]
S = "ABCDEFGHI"
print(S[2:7]) #CDEFG
#note the item at the index 7 i.e 'H' is not included
#slicing with negative values
print(S[-7:-2:]) #CDEFG

#slicing with postive and negative indexing
S = "ABCDEFGHI"
print(S[2:-5]) #CD

#specifing the step-value for slicing
print(S[2:7:2]) #CEG

#negative slice value
print(S[6:1:-2]) #GEC

#slice at the beginning and end
print(S[:6]) #beg--->ABCDEF
print(S[6:]) #end-->GHI

#reverse a string
S = "ABCDEFGHI"
print(S[::-1])

#similar operations can be done with slicing
filename = 'spam.txt'
filename[-4 : ] =='.txt'

#------------------------------------------------------------------------
url = 'https://www.python.org'
url[:6] == 'https:' 
url[:7] == 'https:' 
url[:4] == 'ftps'
#or

url[:6] =='https:'

# -*- coding: utf-8 -*-
"""
Created on Wed May 17 08:19:22 2023

@author: 91721
"""

from fnmatch import fnmatch , fnmatchcase
names = ['Dat1.csv' , 'Dat2.csv' , 'conig.ini' , 'foo.py']
[name for name in names if fnmatch(name , 'Dat*.csv')]
#['Dat1.csv', 'Dat2.csv']
#------------------------------------------------------
from fnmatch import fnmatch ,fnmatchcase
names  = ["Anderi East" , "parel East" , "Dadar west"]
[name for name in names if fnmatch(name , '*East')]
#------------------------------------------------------
from fnmatch import fnmatch , fnmatchcase
address = [
    '5412 N clark ST',
    '1060 W ADDISION ST',
    '1039 W ABC AVE',
    '5018 N clark ST',
    '4000 N brodaway',
    ]
#[name for name in address if fnmatch(name , '* ST')]
[addr for addr in address if fnmatch(addr , '* ST')]
#-------------------------------------------------------
text = 'yeah , but no ,but yeah , but no , but yeah'
text == 'yeah'

text.startswith('yeah')
text.endswith('no')

#to find the first occurance of any word in the sting
#searches for the location of first occurance
text.find('no')

#---------------------------------------------------------------
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
#simple matching: 
if re.match(r'\d+/\d+/\d+' , text1):
    print("yes")
else:
    print("no")

#####################
if re.match(r'\d+/\d+/\d+' , text2):
    print("yes")
else:
    print("no")
        

if re.match(r'\d{2}-\d{2}-\d{4}' , text1):
    print("yes")
else:
    print("no")
    
#===================================Slot-2==============================
txt = "this is Artificial Intelligence era"
x = txt.split()
print(x)

import re
txt1 = "India: has Great history: in 2023 India is leading to it's glorious future!"
pat = r'[.,!?/:;\"\s]'
re.sub(pat , " " , txt1)

x = re.split(r'[.,!?/:;\"]' , txt1)
print(x)


txt1 = "India, has Great history, in 2023 India is leading to it's glorious future!"
y = re.split(r'[.,?/:;\"]' , txt1)
print(y)

#----------------------------------------------------------------------
#matching text in starting or end
txt2 = "rama went to haridwar to bring gangajal"
txt2.endswith("gangajal")

#if you need to check for multiple choices simply provide values in a
#tuple to check for start or end
#here choices must be in tuple not in list
choices = ("jal" , "bring" , "to")
txt2.endswith(choices)
txt2.startswith(choices)


txt3 = "I like Mango"
txt3[7:] == "Mango" #True
txt3[-5::] == "Mango" #True
txt3[7:] == "Mango" #True

txt4 = "I had been visited pune on 11/5/23"
x = txt4[-7::]
x
if(re.match(r'\d+/\d+/\d+' , txt4)):
    print("date is extracted")
else:
    print("no")    

if(re.match(r'\d+/\d+/\d+' , x)):
    print("date is extracted")
else:
    print("no")
    
#searching and replacing text
text = 'yeah , but no ,but yeah , but no , but yeah'
print(text.replace("yeah" , "yep"))
print(text)

import re
text5 = "today is 17/5/23 and our exam will start from 3/6/23"
re.sub(r'(\d+)/(\d+)/(\d+)' , r'\3-\2-\1' , text5)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2' , text5)

newtext , n = datepat.subn(r'\3-\1-\2' , text5)
newtext 
n

#searching and replacing case sensitive text
#their are scenirios where you need to search particular text and 
#replace them irrespective of case sensitivity

text = "UPPER PYTHON , lower python , Mixed Python"
re.findall("python" , text , flags = re.IGNORECASE)
re.sub('python' , 'snake' , text , flags=re.IGNORECASE)


# -*- coding: utf-8 -*-
"""
Created on Tue May 23 09:04:52 2023

@author: 91721
"""

import re
import nltk 
import string

def matchcase(word):
    def replace(m):
        text = m.group()
        #print(text)
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace  

text = "UPPER PYTHON , lower python , Mixed Python"
re.sub('python' , matchcase('snake') , text , flags = re.IGNORECASE)


#extracting the text that is inside the "" of a string
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1)
#['no.']

text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2)
#['no." Phone says "yes.']
#this is undesired output

str_pat = re.compile(r'\"(.*?)\"')
text1 = 'Computer says "no." Phone says "yes"'
str_pat.findall(text2)
#['no.', 'yes.']

#extracting the data/code written in comments

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/*this is a comment */'
comment.findall(text1)

#extracting multiline comment
text2 = '''/* this is a 
            multiline comment */
'''
comment.findall(text2)
#the same pattern is not applied here

#to fix this problem , you can add support for newline.
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)
#[' this is a \n            multiline comment ']

#===========================slot2======================================
#removing numbers from text
import re

def remove_numbers(text):
    result = re.sub(r'\d+', '' , text)
    return result

input_str = "There are 3 balls in this bag and 12 in the other."
remove_numbers(input_str)

#converting numbers to words
import inflect
p = inflect.engine()

#convert numbers into words
def convert_number(text):
    #split sting into list of words
    temp_str = text.split()
    #initialise empty list
    new_string = []
    for word in temp_str:
        #if word is a digit , convert the digit to numbers
        #and append into the newstring lis
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)
        else:
            #append the word as it is
            new_string.append(word) 
            
        #join the words of new_string to form a string
        temp_str  = ' '.join(new_string)
    return temp_str

input_str = "there are 3 balls int this bag and 12 in the other"
convert_number(input_str)       

#======================================================================
#1) reverse each word of a string 
def reverseWordSentence(Str1):

	words = Str1.split(" ")
	
	newWords = [word[::-1] for word in words]
	newSentence = " ".join(newWords)

	return newSentence

Str1 = 'My Name is jessa'
print(reverseWordSentence(Str1))

#2)assume you have a file(sample.txt) in following way
#line1
#line2
#line3

#expected output: 
#line1 line2 line3

obj = open("sample.txt")
content = obj.read()
content.replace('\n' , " ")

#OR
#obj.read().replace('\n' , " ")




# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:56:07 2023

@author: 91721
"""
#link and videos

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1 == s2


#normalization
import unicodedata
t1 = unicodedata.normalize('NFC' , s1)
t2 = unicodedata.normalize('NFC' , s2)
t1 == t2
print(ascii(t1))
#normalization using NFD
t3 = unicodedata.normalize('NFD' , s1)
t4 = unicodedata.normalize('NFD' , s2)
t3 == t4
print(ascii(t3))

#unicodedata.combining() method 
#.join()method

t1 = unicodedata.normalize('NFD'  , s1)
"".join(c for c in t1 if not unicodedata.combining(c))

#working with unicode characters in regular expressions
import re
num = re.compile('\d+')
#Ascii digits
num.match('123')
#<re.Match object; span=(0, 3), match='123'>

pat = re.compile('stra\u00dfe' , re.IGNORECASE)
s = 'straße'
pat.match(s) #matches
#<re.Match object; span=(0, 6), match='straße'>

pat.match(s.upper())

#stripping unwanted characters from strings
#no need to specify the parameters while deleting the white spaces
s = '  hello world  \n'
s.strip()
#all the whitespaces are deleted form both sides
#'hello world'

s.lstrip()
#whitespace are removed from left side
#'hello world \n'

s.rstrip()
#whitespace are removed from right side
#'  hello world'

# -*- coding: utf-8 -*-
"""
Created on Thu May 25 08:21:46 2023

@author: 91721
"""


#character stripping
#explicitly specifying the symbols to be removed from the left or the right side
t = "---hello=="

t.lstrip("-")
#'hello=='

t = "---hello=="
t.rstrip("=")
#'---hello'

t = "---hello=="
t.strip("-=")

s = 'hello world    \n'
s = s.strip()
s
#'hello world'
s.replace(' ' , '')
# now we replace the white space with empty string
#'helloworld'

import re 
re.sub('\s+' , ' ', s)
#we seperate it back with whitespace

s = 'pýtĥöñ\fis\tawesome\r\n'
#the first step is to clean up the whitespaces . to do this,
#make a small translation table and use translate():
remap = {
            ord('\t') : ' ',
            ord('\f') : ' ',
            ord('\r') : None #deleted
    }

a = s.translate(remap)
a
a.replace("\n" , "")

#cleaning of text 
import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD' , a)
#'pýtĥöñ is awesome\n'
b
b.translate(cmb_chrs)
#'python is awesome\n'

#yet another techinque for cleaning up the text involves I/O decoding functions
# and 
#encoding , the idea here is to first do some preliminary cleanup of the
#text  , and then run it
#through a combination of encode() or decode() opertaions to strip or alter it

a = 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD' , a)
b.encode('ascii' , 'ignore').decode('ascii')
#'python is awesome\n'

#aligining the text string
text = "Hello world"
text.ljust(20)
#'Hello world         '
text.rjust(20)
#'         Hello world'
text.center(20)
#'    Hello world     '

#All these mehtods accept an optional characters & fill character as well
text.rjust(20 , "=")

text.center(20 , "*")

#aligning the text using the format method
format(text , ">20")
#here the direction of the arrow show to which direction the text is
#going to shift
#
format(text , "<20")
#
format(text , "^20")

#filling the whitespaces using the format() method

format(text , "*^20")

#these format codes can also be used in the format() method when formatting
#values , for ex:
'{:>10s} {:>10s}'.format('Hello' , 'World')
#'     Hello      World'
#=========================slot2====================================

x = 1.2345
format(x , '>10')

format(x , '^10.2f')

parts = ["Is" , "chicago" , "Not" , "Chicago?"]
" ".join(parts)
#'Is chicago Not Chicago?'

",".join(parts)
#'Is,chicago,Not,Chicago?'

"".join(parts)
#'IschicagoNotChicago?'

#if you join very few strings then you can use + operator
a = "Is Chicago"
b = "Not Chicago?"
a + ' ' + b
#'Is Chicago Not Chicago?'
print('{} {}'.format(a , b))
print(a + ' ' + b)

#----------------------------

a = 'hello'  'world'
a
#'helloworld'
#if we wish to add some characters between the sting b then 
#we must explicity add it in the single quotes ' ' between the string
# to be inserted
b = 'hello' ' ' 'world'
b
#'hello world'

#interpolating variables in strings
#you want to create a string in which embedded variable names are
#substitued 
#string representation of variable's value;
s = '{name} has {n} messages'
s.format(name = 'Guido' , n=40)

#all the previous values get mapped with the format_map() function 
s = '{name} has {n} messages'
name = "Gudio"
n = 30
s.format_map(vars())


# to apply justification of the text -->specified explicitly
s = 'look into my eyes , look into my eyes , the eyes , the eyes ,\
    the eyes , not around the eyes , dont look around the eyes , \
        look into my eyes , your under'
        
import textwrap 
print(textwrap.fill(s , 40))
        
import textwrap
print(textwrap.fill(s , 70))

#initial indent
print(textwrap.fill(s, 40, initial_indent=' '))

#subsuquent indentation
print(textwrap.fill(s , 40 , subsequent_indent = ' '))

# -*- coding: utf-8 -*-
"""
Created on Fri May 26 08:14:53 2023

@author: 91721
"""

#tokenization
#sentence tokenization
import nltk
nltk.download('punkt')
sentence_data = "the first sentence is about python. todays topic text processing in nlp . python for datascience is very intresting"
nltk_tokens = nltk.sent_tokenize(sentence_data)
print(nltk_tokens)

#non english tokenization
import nltk
german_tokenizer  = nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens = german_tokenizer.tokenize('Wie geht es Thnen? Gut , danke.')
print(german_tokens)

#word tokenization
word_data = "the first sentence is about python. todays topic text processing in nlp . python for datascience is very intresting"
nltk_tokens = nltk.word_tokenize(word_data)
print(nltk_tokens)

#========================================================================
import nltk
nltk.download('stopwords')
#it will download a file english stopwords.
#verifying the stiopwords

from nltk.corpus import stopwords
stopwords.words('english')
#the variou languages other than english which has these stopwords are as the

from nltk.corpus import stopwords
print(stopwords.fileids())

#=====================================================================
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))

all_words = ['There' , 'is' , 'a' , 'tree' , 'near' , 'the' , 'river']
for word in all_words:
    if word not in en_stops:
        print(word)
        
#=====================================================================
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.corpus import wordnet        

synonyms = []
for syn in wordnet.synsets('Soil'):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))

synonyms = []
for syn in wordnet.synsets('brave'):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))
#====================================================================
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.corpus import wordnet        

antonyms = []
for syn in wordnet.synsets('ahead'):
    for lm in syn.lemmas():
        if lm.antonyms():    
            antonyms.append(lm.antonyms()[0].name())

print(set(antonyms))
