# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:09:52 2018
@author: prasasaw
for all function definitions
"""
import yaml
import re
from nltk.tokenize import TreebankWordTokenizer
import datefinder
from datetime import date
from datetime import datetime
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import io
from io import StringIO
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

# Custom stop words list
stop = ["technical", "activities","client", "capgemini", "copyright", "understand", "right", "reserved", "project","name", "reference", "refer", "free", "start", "department", "development", "develop", "information", "need", "significant", "want", "lot", "transparent", "across", "include", "account", "leading", "market", "tools", "control", "organization", "base", "rights", "manage", "management", "possible", "close", "level","put",
        "confidential", "custom", "case", "solution", "date", "custom", "last", "report", "version", "status", "use", "management", "implementation", "implement", "confidential", "function", "global", "application", "custom", "etc", "functionality", "contract", "country", "technology", "service", "provider", "management", "detail", "business", "work", "system", "offer", "using", "experience"]

# Function for text preprocessing : lower casing > tokenize > gram > stopwords 
tokenizer = TreebankWordTokenizer()
def process_message(message, lower_case = True, stem = True, stop_words = True, gram = 1):
    if lower_case:
        message = message.lower()
        clean_text = re.sub('[^A-Za-z ]',' ',message)
    words = tokenizer.tokenize(clean_text)
    if gram > 1:
        w = []
        for i in range(len(words) - gram + 1):
            w += [' '.join(words[i:i + gram])]
        return w
    if stop_words:
        StopWords = list(set(stopwords.words('english')))
        custom_stop = StopWords + stop
       # sw = stopwords.words('english')
        words = [word for word in words if word not in custom_stop]
    if stem:
        stemmer = PorterStemmer()
        words = [stemmer.stem(word) for word in words]
    
    return words
   
def cleanse_name(name):
    name = re.sub('[^A-Za-z ]',' ',name)
    name = re.sub('Resume','', name, flags= re.IGNORECASE)
    name = name.strip()
    name = name.title()
    return name

def find_BirthDate(text):
    birthDate = ''
    items=re.findall(".*DOB.*|.*irth.*$",text,re.MULTILINE)   
    for x in items:
            matches = datefinder.find_dates(x)
            for match in matches:
                birthDate = match
    if birthDate != '':   
           birthDate = birthDate.date()
    return birthDate

def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))            
    return age

def find_experience(text):
    experience = ''
    items=re.findall(".*years.*",text,re.MULTILINE)   
    for x in items:
            for s in x.split():
                if s.isdigit():
                    experience = s
    return experience

def extract_email(text):
    emailid = ''
    match = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    for i in match:
        emailid = i
    return emailid   

def extract_phone(text):
    phone = ''
    match = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
    for i in match:
        phone = i
    return phone

def load_conf():
    conf = yaml.load(open('./conf/conf.yaml'))
    return  conf # returns a dict object. Items are accessible by dict['item_name']

def get_conf(conf_name):
    return load_conf()[conf_name]
    

def check_match(string_to_search, term):
  
    result = re.search(term, string_to_search, re.IGNORECASE)
    return result

def extract_skills(OneText,categories,x):
    
    matched_skills = []
    
    for a in x:
        found = False
        found = check_match(OneText, a.lower())
        if found:
            matched_skills.append(a.strip())
    
    #return (' '.join(matched_skills)) # not returning string but list instead
    return matched_skills
      #  if skill_matches > 0:
      #      matched_skills.append(a)
        

def get_LDA_vector(text, ldamodel, dictionary):
    
    # clean, stem and remove stopwords, punctuation
    text_clean = process_message(text)

    # transform text into the bag-of-words space
    bow_vector = dictionary.doc2bow(text_clean)
    
    # transform into LDA space
    lda_vector = ldamodel[bow_vector]
    
    return lda_vector

def extract_text_from_pdf(pdf_path): # works fairly well. Issue with DOB
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(pdf_path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text   

def extract_summary(resumetext):
    all_lines=resumetext.splitlines()
    filled_lines=[]
    
    for x in all_lines:
        x=" ".join(x.split()) # removing whitespaces
      #  f=re.search('[^A-Za-z ,]\1{3}', x)
        if len(x) > 50:
            filled_lines.append(x)
    
    summary=" ".join(filled_lines[1:2])
    return summary
