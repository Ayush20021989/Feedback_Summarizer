#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing libraries 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

# Input text - to summarize 
text = """I recently had the pleasure of trying out the new Velvet Dreams eyeshadow palette from Luxe Cosmetics, and I must say, I'm thoroughly impressed. From the moment I opened the sleek packaging, I could tell that this palette was something special. The range of colors is absolutely stunning, with a perfect mix of mattes and shimmers that allows for endless creativity in makeup looks. The formula itself is incredibly smooth and blendable, making application a breeze even for someone like me who is not a makeup pro. What really sets this palette apart, though, is the pigmentation. The colors are so rich and intense that you only need a small amount to achieve a bold and vibrant look. And the staying power? Let me tell you, I wore these shadows for a full day without any fading or creasing. Overall, I can't recommend the Velvet Dreams palette enough. Whether you're a makeup enthusiast or just someone looking to add a pop of color to your everyday routine, this palette is a must-have. Trust me, you won't be disappointed!"""

# Tokenizing the text 
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 

# Creating a frequency table to keep the 
# score of each word 

freqTable = dict() 
for word in words: 
	word = word.lower() 
	if word in stopWords: 
		continue
	if word in freqTable: 
		freqTable[word] += 1
	else: 
		freqTable[word] = 1

# Creating a dictionary to keep the score 
# of each sentence 
sentences = sent_tokenize(text) 
sentenceValue = dict() 

for sentence in sentences: 
	for word, freq in freqTable.items(): 
		if word in sentence.lower(): 
			if sentence in sentenceValue: 
				sentenceValue[sentence] += freq 
			else: 
				sentenceValue[sentence] = freq 



sumValues = 0
for sentence in sentenceValue: 
	sumValues += sentenceValue[sentence] 

# Average value of a sentence from the original text 

average = int(sumValues / len(sentenceValue)) 

# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
		summary += " " + sentence 
print(summary) 


# In[ ]:




