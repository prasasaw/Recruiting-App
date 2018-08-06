# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:43:46 2018
@author: prasasaw

"""
import re

def sectionize(resumetext):

    all_lines=resumetext.splitlines()
    sectiontext = ""
        
    for x in all_lines:
        
        found = 'False'
        x=" ".join(x.split()) # removing whitespaces
        
        match = re.findall(r'.*objective.*|.*qualification.*|.*career.*|.*experience.*|.*prof.*summary.*|.*synopsis.*|.*skill.*|.*competenc.*|.*achievement.*|.*project.*detail.*|.*training.*|.*education.*|.*personal.*', x, flags=re.IGNORECASE)
        
        for i in match:
            found = 'True'
    
        if len(x) < 30 and found == 'True':
            sectiontext = sectiontext + '\n' + "##########NEWSECTION##########" + '\n'
        
        if x != "":
            sectiontext = sectiontext + x + '\n'   
            
    
    
    return(sectiontext)
    
  