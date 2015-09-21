# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:13:42 2015

@author: Binoy
"""

import re
import dataset

def createDB():
    _file = open("Glossary.swd", 'r')
    
    db = dataset.connect('sqlite:///glossary.db')
    table = db['glossary']
    
    count = 1
    FLG_SECTION = 0 
    line = _file.next()
    curKey = ""
    curdic = None
    patt = re.compile("\{.*?\}")
    
    while line:
        

            
        if line[0] != ">":
            
            curdic['description'] += line 
        else:
            if curdic:
                match = patt.findall(curdic['description'] , re.MULTILINE)
                if match:
                    
                    for i in range(len(match)):
                        match[i] = match[i][1:-1]
                        comstr = "[\{\}]"
                        curpatt = re.compile(comstr)
                        curdic['description'] = curpatt.sub("",\
                        curdic['description'] )
                    curdic['keywords'] = ",".join(match)
                table.insert(curdic)
            line = line[1:]
            count  += 1
            curKey = line
            curdic = {}
            curdic['term'] = curKey.strip()
            curdic['description'] =""
            
        
            
        
        
        
        
        try:
            line = _file.next()
        except:
            break
    
            
#        if count > 100:

def readdbsingle():
    db = dataset.connect('sqlite:///glossary.db')
    table = db['glossary']
    
    
    
    for i in table['term']:
        print table.find_one(term = i['term'])['description']
            
            
if __name__ == '__main__':
    readdbsingle()