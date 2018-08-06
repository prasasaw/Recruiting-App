# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:01:19 2018

@author: prasasaw
"""
import resume_parser
import file_to_text
import section
import glob
import os

dir =  r"C:\Resume Miner1"
files = glob.glob(os.path.join(dir,"*"))  
    
for filename in files:

    resumetext = file_to_text.text_converter(filename)
    sectiontext = section.sectionize(resumetext)
    output = resume_parser.parse_resume(sectiontext, filename)

