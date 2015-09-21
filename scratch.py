# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:32:58 2015

@author: Binoy
"""

import dataset
import re
def create():
    # connecting to a SQLite database
    db = dataset.connect('sqlite:///mydatabase.db')
    
    # get a reference to the table 'user'
    table = db['user']
    
    # Insert a new record.
    table.insert(dict(name='John Doe', age=46, country='China'))
    
    # dataset will create "missing" columns any time you insert a dict with an unknown key
    table.insert(dict(name='Jane Doe', age=37, country='France', gender='female'))

def read():
    # connecting to a SQLite database
    db = dataset.connect('sqlite:///mydatabase.db')
    users = db['user'].all()
    for user in users:
       print(user['country'])

def retest():
    txt = """'DO', 'BE' and 'HAVE' are the English auxiliary verbs used in a {Negative} structure, a {Question} or either Tense.

1/ 'DO', 'DON'T', 'DOES' and 'DOESN'T is used for questions and negatives in the {Present Simple} {Tense}, and 'DID' and 'DIDN'T' are used in the {Past Simple} {Tense}.

2/ 'BE' is used with the {Present Participle} in {Continuous Verbs}.

3/ 'HAVE' is used with the {Past Participle} to form the {Perfect} {Aspect}.  


See also {Causative Verb}; {Copula Verb}; {Ditransitive Verb}; {Dynamic Verb}; {Finite Verb}; 
{Inchoative Verb}; {Intransitive Verb}; {Irregular Verb}; {Modal Verb}; {Non-finite Verb}; {Phrasal Verb}; 
{Regular Verb}; {Stative Verb}; {Transitive Verb}; {Verb Group}; {Verb Phrase}; {Present Simple};"""
    patt = re.compile("\{.*?\}")
    match = patt.findall(txt, re.MULTILINE)
    if match:
        for i in match:
            print i,"->",i[1:-1]
        
        
retest()

    