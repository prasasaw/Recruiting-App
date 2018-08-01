# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 18:41:34 2018
@author: prasasaw

TODO:
Name    
Universities : NNP parsing of school, college and universities
certification
Companies
Education
country
city

See code examples from Sci kit
http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.build_preprocessor

try spacy
"""

import func
import re

def parse_resume(resumetext):
      
        tokens = func.process_message(resumetext, stem = False) ## tokens, used to build dictionary later
        cleansed_text = str(tokens) 
        cleansed_text = re.sub('[^A-Za-z0-9]+', ' ', cleansed_text)
               
        # extract birth date
        dob = func.find_BirthDate(resumetext)
               
        # calculate age
        
        age = ''
        if dob != '':    
            age=func.calculate_age(dob)
          
        # extract email
        emailid = ''
        emailid = func.extract_email(resumetext)
               
        # extract phone
        phone = ''
        phone = func.extract_phone(resumetext)
        
        # extract experience
        experience = ''
        experience = func.find_experience(resumetext)
        
        # extract summary
        summary = ''
        summary = func.extract_summary(resumetext)
            
        # extract skills
        for categories, x in func.get_conf('Categories').items():
            
            if categories == 'programming':
                programming = func.extract_skills(resumetext,categories,x)
                 
            if categories == 'packages':
                packages = func.extract_skills(resumetext,categories,x)
               
            if categories == 'domain':
                domains = func.extract_skills(resumetext,categories,x)
                 
            if categories == 'roles':
                roles = func.extract_skills(resumetext,categories,x)
    
        return {'summary':summary,
                'dob':dob,
                'age':age,
                'experience':experience,
                'emailid':emailid,
                'phone':phone,
                'programming':programming,
                'packages':packages,
                'domains':domains,
                'roles':roles
               # 'resumetext':resumetext, 
               # 'tokens':tokens,
               # 'cleansed_text':cleansed_text,
                }    


