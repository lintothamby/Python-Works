'''
Created on Jan 23, 2017

@author: lthamby
'''
stringReverse=input ("Enter the string for reverse: ")
'print (stringReverse[::-1])'
def reverse(stringReverse):
    r_text = ''
    index = len(stringReverse) - 1

    while index >= 0:
        r_text += stringReverse[index] #string can be concatenated
        index -= 1

    return r_text

stoer = reverse (stringReverse)
print (stoer)