'''
Author:Jacob Thomas
Date:19/12/2024
'''
words="apple","banana","apple","orange","banana","apple"
s=str.split(',')
word_count={}

for word in words:
    word_count[word]=word_count.get(word,0)+1

print(word_count)