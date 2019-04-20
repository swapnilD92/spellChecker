# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 22:58:46 2019

@author: sd120
"""

from spellchecker import SpellChecker
from flask import Flask
import re
import wordninja
from collections import OrderedDict

app = Flask(__name__)

@app.route('/spellCorrect/<name>')
def hello_name(name):
    try:
        name = re.split('[^a-zA-Z]', name)
        spell = SpellChecker()
        misspelled = name
        op = OrderedDict()
        
        for word in misspelled:
            word = spell.correction(word)
            word_split = wordninja.split(word)
            for wrd in word_split:
                op[wrd] = spell.candidates(wrd)
        return str(op)
    
    except Exception as e:
        return str(e)
    
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050)


