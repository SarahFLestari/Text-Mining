from bs4 import BeautifulSoup as bs
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.moses import MosesDetokenizer
from nltk.stem import WordNetLemmatizer
import os
import csv
import pprint
import numpy as np
import pandas as pnd

stop_words = set(stopwords.words('english'))
detokenizer = MosesDetokenizer()
lemmatizer = WordNetLemmatizer()
filelabelTest = "Label/TestingLabel.txt"
filelabelTrain = "Label/TrainingLabel.txt"
labelTest = pnd.read_csv(filelabelTest, delim_whitespace=True)
labelTrain = pnd.read_csv(filelabelTrain, delim_whitespace=True)
#Diubah ke matriks
labelTest = np.matrix(labelTest)
labelTrain = np.matrix(labelTrain)
# print(labelTrain)
# print(labelTest)
datasetTrain = []
label = []
output = []

for i in range(len(labelTrain)):
	soup = bs(open("Training/"+ str(labelTrain[i,0])+".xml",'r').read(),'html.parser')

	headline = soup.find("headline").get_text().replace('\n','')
	paragraph = soup.find("text").get_text().replace('\n','')
	label = int((labelTrain[i,1]) == "YES")
	datasetTrain.append([[str(headline)],[str(paragraph)],[label]])
# ==================================================
# Case Folding
tmp0 = []
tmp1 = []
for i in range(len(datasetTrain)):
	# print(datasetTrain[i][0][0])
	tmp0.append(datasetTrain[i][0])
	tmp1.append(datasetTrain[i][1])
# print(tmp0)
for i in range(len(tmp0)):
	valsLower = [item.lower() for item in tmp0[i]]
	tmp0[i] = valsLower
# print(tmp0)
for i in range(len(tmp1)):
	valsLower1 = [item.lower() for item in tmp1[i]]
	tmp1[i] = valsLower1
# print(tmp1)

# ==================================================
#Remove Punctuation
for p in list(punctuation):
	for i in range(len(tmp0)):
		valsPunc = [item.replace(p, '') for item in tmp0[i]]
		tmp0[i] = valsPunc
	for i in range(len(tmp1)):
		valsPunc1 = [item.replace(p, '') for item in tmp1[i]]
		tmp0[i] = valsPunc1
# print(tmp1)
# print(tmp0)
# ==================================================
# #Remove Stop Word
filteredSentences = []
filteredSentences = [w for w in tmp0 if not w in stop_words]
for w in tmp0:
	if not w in stop_words:
		filteredSentences.append(w)
print(filteredSentences)
# ==================================================
# Tokenize
for i in range(len(tmp0)):
	valsToken = [word_tokenize(item) for item in tmp0[i]]
	tmp0[i] = valsToken
# print(tmp0)
for i in range(len(tmp1)):
	valsToken1 = [word_tokenize(item) for item in tmp1[i]]
	tmp1[i] = valsToken1
# print("token",tmp1)
# print("token",tmp0)

# #stemmer
# stemSentences = []
# for i in filteredSentences:
# 	j = lemmatizer.lemmatize(i)
# 	stemSentences.append(j)

# PraprosesTrain = detokenizer.detokenize(stemSentences, return_str=True)
# datasetTrain = PraprosesTrain

# for i in range(len(labelTrain)):
# 	label = int((labelTrain[i,1]) == "YES")
# 	datasetTrain.append(" ".join(label))


