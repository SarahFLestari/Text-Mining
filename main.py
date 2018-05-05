from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB

#TrainingSet = "./PreProcessingTraining.csv"
#TestingSet = "./PreProcessingTesting.csv"

datasetTrain = []
labelTrain = []
with open('PrePrecessingTraining.csv') as resultFile:
	resultFile = resultFile.read().split("\n")
	for line in resultFile:
		line = line.split(";")
		try:
			datasetTrain.append(" ".join(line[0:-1]))
			labelTrain.append(str(line[-1]))
		except IndexError :
			continue
# print(datasetTrain)
# print(labelTrain)
# ==================================================

datasetTest = []
labelTest = []
with open('PrePrecessingTesting.csv') as resultFile:
	resultFile = resultFile.read().split("\n")
	for line in resultFile:
		line = line.split(";")
		try:
			datasetTest.append(" ".join(line[0:-1]))
			labelTest.append(str(line[-1]))
		except IndexError :
			continue

# print(datasetTest)
# print(labelTest)
# ==================================================
#Classifier 
count_vect = CountVectorizer()
Pembobotan = TfidfTransformer()
# ==================================================
# Naive Bayes

# Akurasi Data Train
MTrain = count_vect.fit_transform(datasetTrain)
TFIDFTrain = Pembobotan.fit_transform(MTrain)

klasifikasi = MultinomialNB().fit(TFIDFTrain, labelTrain)
prediksi = klasifikasi.predict(TFIDFTrain)
akurasi = 0
for i in range(len(labelTrain)):
	if labelTrain[i] == str(prediksi[i]):
		akurasi += 1

a=len(labelTrain)
b=akurasi
c=((float(b*100)/a)+1)
print("Akurasi Naive Bayes Data Train: {} %".format(int(round(c))) )

# Akurasi Data Test

MTest = count_vect.fit_transform(datasetTest)
TFIDFTest = Pembobotan.fit_transform(MTest)

klasifikasi1 = MultinomialNB().fit(TFIDFTest, labelTest)
prediksi1 = klasifikasi1.predict(TFIDFTest)
akurasi1 = 0
for i in range(len(labelTest)):
	if labelTest[i] == str(prediksi1[i]):
		akurasi1 += 1

x=len(labelTest)
y=akurasi1
z=((float(y*100)/x)+1)

print("Akurasi Naive Bayes Data Test: {} %".format(int(round(z))) )

# ==================================================
# SVM Classifier

# Akurasi Data Test
MTrain2 = count_vect.fit_transform(datasetTrain)
TFIDFTrain2 = Pembobotan.fit_transform(MTrain2)

klasifikasi2 = SVC().fit(TFIDFTrain2, labelTrain)
prediksi2 = klasifikasi2.predict(TFIDFTrain2)
# print(prediksi2)
akurasi2 = 0
for i in range(len(labelTrain)):
	if labelTrain[i] == str(prediksi2[i]):
		akurasi2 += 1

u=len(labelTrain)
v=akurasi2
w=((float(v*100)/u)+1)
print("Akurasi SVM Data Train: {} %".format(int(round(w))) )

# Akurasi Data Test

MTest3 = count_vect.fit_transform(datasetTest)
TFIDFTest3 = Pembobotan.fit_transform(MTest3)

klasifikasi3 = SVC().fit(TFIDFTest3, labelTest)
prediksi3 = klasifikasi3.predict(TFIDFTest3)
# print(prediksi3)
akurasi3 = 0
for i in range(len(labelTest)):
	if labelTest[i] == str(prediksi3[i]):
		akurasi3 += 1

e=len(labelTest)
f=akurasi3
g=((float(f*100)/e)+1)

print("Akurasi SVM Data Test: {} %".format(int(round(g))) )

# ==================================================
# Gaussian

# # Akurasi Data Test
# MTrain4 = count_vect.fit_transform(datasetTrain)
# TFIDFTrain4 = Pembobotan.fit_transform(MTrain4)

# klasifikasi4 = GaussianNB().fit(TFIDFTrain4, labelTrain)
# prediksi4 = klasifikasi4.predict(TFIDFTrain4)
# akurasi4 = 0
# for i in range(len(labelTrain)):
# 	if labelTrain[i] == str(prediksi4[i]):
# 		akurasi4 += 1

# j=len(labelTrain)
# k=akurasi4
# l=((float(k*100)/j)+1)
# print("Akurasi : {} %".format(int(round(l))) )

# # Akurasi Data Test

# MTest5 = count_vect.fit_transform(datasetTest)
# TFIDFTest5 = Pembobotan.fit_transform(MTest5)

# klasifikasi5 = GaussianNB().fit(TFIDFTest5, labelTest)
# prediksi5 = klasifikasi5.predict(TFIDFTest5)
# akurasi5 = 0
# for i in range(len(labelTest)):
# 	if labelTest[i] == str(prediksi5[i]):
# 		akurasi5 += 1

# p=len(labelTest)
# q=akurasi5
# r=((float(q*100)/p)+1)

# print("Akurasi : {} %".format(int(round(r))) )