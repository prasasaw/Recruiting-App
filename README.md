# Recruiting App

process_resumes.py
------------------------
1) This is the script that is to be invoked to parse the set of resumes, once the resumes are uploaded to a specific folder

2) Edit the below script by replacing the path of the resume files
dir =  r"C:\Resume Miner"

3) ldamodel.pickle will be stored as a python object which will be later used in search_resumes.py script


search_resumes.py
-------------------------
1) this is the script that will search for the resumes

2) Below query variable has been hardcoded here. Later it should be captured as user input
query  = "profile with SAP experience"


func.py
---------
1) stores all function definations


