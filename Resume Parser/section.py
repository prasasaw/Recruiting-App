# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:43:46 2018
@author: prasasaw

"""
import re

def sectionize(resumetext):
    size = 30
    all_lines=resumetext.splitlines()
    objective = 'False'          
    profsummary = 'False'
    qualification = 'False'
    skills = 'False'
    projects = 'False'
    achievements = 'False'
    trainings = 'False'
    education = 'False'
    personal = 'False'
    
    objective_txt = ""
    profsummary_txt = ""
    qualification_txt = ""
    skills_txt = ""
    projects_txt = ""
    achievements_txt = ""
    trainings_txt = ""
    education_txt = ""
    personal_txt = ""

        
    for x in all_lines:
        
        x=" ".join(x.split()) # removing whitespaces
        if(re.match(r'.*objective.*|.*qualification.*|.*career.*|.*experience.*|.*prof.*summary.*|.*synopsis.*|.*skill.*|.*competenc.*|.*achievement.*|.*certification.*|.*project.*detail.*|.*training.*|.*education.*|.*personal.*|.*course.*', x, flags=re.IGNORECASE)) and len(x) < size:
            objective = 'False'          
            profsummary = 'False'
            qualification = 'False'
            skills = 'False'
            projects = 'False'
            achievements = 'False'
            trainings = 'False'
            education = 'False'
            personal = 'False'
            
        if (re.match(r'.*objective.*', x, flags=re.IGNORECASE) and len(x) < size) or objective == 'True':   
                objective = 'True'
                objective_txt = objective_txt + x + '\n'
        
        if (re.match(r'.*prof.*summary.*|.*synopsis.*', x, flags=re.IGNORECASE) and len(x) < size) or profsummary == 'True':   
                profsummary = 'True'
                profsummary_txt = profsummary_txt + x + '\n'
   
        if (re.match(r'.*qualification.*', x, flags=re.IGNORECASE) and len(x) < size) or qualification == 'True':   
                qualification = 'True'
                qualification_txt = qualification_txt + x + '\n'
                
        if (re.match(r'.*skill.*|.*competenc.*', x, flags=re.IGNORECASE) and len(x) < size) or skills == 'True':   
                skills = 'True'
                skills_txt = skills_txt + x + '\n'        
        
        if (re.match(r'.*career.*|.*project.*detail.*|.*experience.*', x, flags=re.IGNORECASE) and len(x) < size) or projects == 'True':   
                projects = 'True'
                projects_txt = projects_txt + x + '\n'
        
        if (re.match(r'.*achievement.*', x, flags=re.IGNORECASE) and len(x) < size) or achievements == 'True':   
                achievements = 'True'
                achievements_txt = achievements_txt + x + '\n'
                
        if (re.match(r'.*training.*|.*certification.*|.*course.*', x, flags=re.IGNORECASE) and len(x) < size) or trainings == 'True':   
                trainings = 'True'
                trainings_txt = trainings_txt + x + '\n'
        
        if (re.match(r'.*education.*', x, flags=re.IGNORECASE) and len(x) < size) or education == 'True':   
                education = 'True'
                education_txt = education_txt + x + '\n'
        
        if (re.match(r'.*personal.*', x, flags=re.IGNORECASE) and len(x) < size) or personal == 'True':   
                personal = 'True'
                personal_txt = personal_txt + x + '\n'
        
        
    return{'Objective':objective_txt,
           'Profsummary':profsummary_txt,
           'Qualification':qualification_txt,
           'Skills':skills_txt,
           'Projects':projects_txt,
           'Achievements':achievements_txt,
           'Trainings':trainings_txt,
           'Education':education_txt,
           'Personalsummary':personal_txt
           
           }
           
           
    
    
    
    
    
    
    
    
  