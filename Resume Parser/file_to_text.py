# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:43:46 2018
@author: prasasaw

input: single file input
output: text string

TODOs:
filepath =[]
Employee = []

"""
import os
import re
import docx
from docx import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
import func

def text_converter(filename):

    """dir =  r"C:\Resume Miner1"
    files = glob.glob(os.path.join(dir,"*"))  
    
    for filename in files:"""

    fileext = os.path.splitext(filename)[1]
    OneText = ''
    
    regexdoc = re.compile('.*doc.*')
    regexpdf = re.compile('.*pdf.*')
    
    matchdoc = regexdoc.search(fileext)
    matchpdf = regexpdf.search(fileext)
    
    if matchdoc:    
        doc = Document(filename)
       
        parent_elm = doc.element.body
        for child in parent_elm.iterchildren():
            if isinstance(child, CT_P):
                para = Paragraph(child, doc)
                OneText = OneText + para.text + '\n'
            
            elif isinstance(child, CT_Tbl):
                tab = Table(child, doc)
                rowText = ''
                for row in tab.rows:
                    rowCell = ''
                    for cell in row.cells:
                        rowCell = rowCell.rstrip()
                        rowCell = rowCell + cell.text + ':' 
                    rowText = rowText + rowCell + '\n'
                
                OneText = OneText + rowText  + '\n'
    
    if matchpdf:
        OneText = func.extract_text_from_pdf(filename)  
    
    return(OneText)
    
  