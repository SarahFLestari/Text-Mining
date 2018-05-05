import os 
from xml.dom import minidom
import xlsxwriter


location = os.getcwd() 
counter = 0 
trainfiles = [] 
otherfiles = [] 
fLabel = 'TrainingLabel.txt'  # Nama label

print(location)
workbook = xlsxwriter.Workbook('datatrain.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A',20)

for file in os.listdir(location):
    try:
        if file.endswith(".xml"):
            #print "txt file found:\t", file
            trainfiles.append(str(file))
            counter = counter+1
        else:
            otherfiles.append(file)
            counter = counter+1
    except Exception as e:
        raise e
        print ("No files found here!")


label = []
with open(fLabel) as f:
    lines = f.readlines()
    y = [(line.split()[1]) for line in lines]

# memasukkan data kedalam array

for i in range(len(y)):
    label.append(y[i])
prin(label)
   
count = 0

trainfiles.sort()
for i in trainfiles:
	print(i)
for xmlfile in trainfiles:
	xmldoc = minidom.parse(xmlfile)
	p = xmldoc.getElementsByTagName("p")[1]
	par = xmldoc.getElementsByTagName("p")	
	paragraph = " "
	h = xmldoc.getElementsByTagName("headline")
	headl = xmldoc.getElementsByTagName("h")
	headln = " "
	for i in range(0,len(headl)):
		h = xmldoc.getElementsByTagName("h")[i]
		headln += h.childNodes[0].data
		worksheet.write(count+1,0,headln)

	for i in range(0,len(par)):
		p = xmldoc.getElementsByTagName("p")[i]
		paragraph += p.childNodes[0].data
		worksheet.write(count+1,1,paragraph)
		#print(p.childNodes[0].data)
	#print("Isi tag : ",p.childNodes[0].data)

	count +=1
	

print ("Total files found:\t", counter)

workbook.close()
