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
import os

def parse_resume(resumetext, filename, sections):
    
        employee = os.path.splitext(filename)[0]
        employee = os.path.split(employee)[1]
        # cleanse employee Name
        employee = func.cleanse_name(employee)
              
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
        
        # Not used. Extracts first 2-3 lines of resume
        summary = ''
        summary = func.extract_summary(resumetext)
        
        skills = sections['Skills'] + sections['Profsummary'] + sections['Trainings'] + sections['Qualification'] +  sections['Achievements']
        
        # extract skills
        for categories, x in func.get_conf('Categories').items():
            
            if categories == 'programming':
                programming = func.extract_skills(skills,categories,x)
                 
            if categories == 'packages':
                packages = func.extract_skills(skills,categories,x)
               
            if categories == 'domain':
                domains = func.extract_skills(skills,categories,x)
                 
            if categories == 'roles':
                roles = func.extract_skills(skills,categories,x)
        
   
        return {'employee':employee,
                #'summary':summary,
                'dob':dob,
                'age':age,
                'experience':experience,
                'emailid':emailid,
                'phone':phone,
                'programming':programming,
                'packages':packages,
                'domains':domains,
                'roles':roles,
                'sProfsummary':sections['Profsummary'],
                'sObjective':sections['Objective'],
                'sQualification':sections['Qualification'],
                'sSkills':sections['Skills'],
                'sProjects':sections['Projects'],
                'sAchievements':sections['Achievements'],
                'sTrainings':sections['Trainings'],
                'sEducation':sections['Education'],
                'sPersonalsummary':sections['Personalsummary'],
                'resumetext':resumetext
               # 'tokens':tokens,
               # 'cleansed_text':cleansed_text,
                }    


