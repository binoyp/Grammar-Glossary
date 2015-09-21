# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:30:09 2015

@author: Binoy
"""
import dataset
from PyQt4 import QtGui
from PyQt4.QtCore import *
from ui_MainForm import Ui_MainWindow
import re, os

class GrammarGlossary(QtGui.QMainWindow, Ui_MainWindow):
    
    
    def __init__(self):
        super(GrammarGlossary, self).__init__()
        self.setupUi(self)
        
        path = 'sqlite:///'+os.path.join(os.getcwd(), 'glossary.db')
        print path
        self.db = dataset.connect(path)
        self.table = self.db['glossary']
        self.fillList()
#        self.filterList() 
        
        
        
    def fillList(self, lst = None):
        
        if not lst:
            lst = self.table['term']
        
            
            
        for i in lst:
            if i['term'] != "":
                self.wid_lstWords.addItem(i['term'])

        
    @pyqtSignature("QListWidgetItem*")
    def on_wid_lstWords_itemClicked(self):
        self.wid_pleDis.clear()
        curword = str(self.wid_lstWords.currentItem().text())
        self.displayData(curword)
        
    @pyqtSignature("QListWidgetItem*")
    def on_wid_lstWords_itemActivated(self):
        self.wid_pleDis.clear()
        curword = str(self.wid_lstWords.currentItem().text())
        self.displayData(curword)

    @pyqtSignature("QString")
    def on_wid_leInput_textChanged (self,*arg):
        word = str(arg[0])
        if word:
            lst = self.filterList(str(arg[0]))
            self.wid_lstWords.clear()
            
            self.wid_lstWords.addItems(lst)
        else:
            self.wid_lstWords.clear()
            self.fillList()
                
            
    @pyqtSignature("QListWidgetItem*")
    def on_wid_lstKeywords_itemClicked(self):
#        self.wid_pleDis.clear()
        curword = self.wid_lstKeywords.currentItem()
#        self.wid_lstWords.setSelection()
#        self.displayData(str(curword.text()))
        
        self.wid_leInput.setText(curword.text())
        
        self.wid_lstWords.setCurrentItem(curword)
        self.wid_lstWords.scrollToItem(curword)
        

    def displayData(self, word):
        desc =  self.table.find_one(term = word)['description']
        self.wid_pleDis.insertPlainText(desc)
        
        self.wid_lstKeywords.clear()
        for i in self.table.find_one(term = word)['keywords'].split(","):
            self.wid_lstKeywords.addItem(i)
            
    def filterList(self, word ="ver"):
        List = []
        patt = re.compile(word, re.IGNORECASE)
        for i in self.table['term']:
            if i['term'] != "":
                mo =patt.search(i['term'])
                if mo:
                    List.append(i['term'])
        return List
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = GrammarGlossary()
    window.show()
    app.exec_()