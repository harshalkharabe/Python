import pickle

a = "Python"
b = 2+3j
c = 3.5
d = [1,3,4,6,5,89,]
e = {1:10,2:20}

# convert any python data into binary format
b1 = pickle.dumps(a)
b2 = pickle.dumps(b)
b3 = pickle.dumps(c)
b4 = pickle.dumps(d)
b5 = pickle.dumps(e)

print(b1,b2,b3,b4,b5,sep='\n')

#convert binary data into specific python type

a1 = pickle.loads(b1)
a2 = pickle.loads(b2)
a3 = pickle.loads(b3)
a4 = pickle.loads(b4)
a5 = pickle.loads(b5)

print(a1,a2,a3,a4,a5,sep='\n')

# Write binary data into file
a=12
b="Harshal Kharabe"
c=[12,34,678,90]

fileobj = open("pickle_file.ser","wb")
pickle.dump(a,fileobj)
pickle.dump(b,fileobj)
pickle.dump(c,fileobj)
fileobj.close()

# read data from file

fileobj = open("pickle_file.ser","rb")
data1 = pickle.load(fileobj)
data2 = pickle.load(fileobj)
data3 = pickle.load(fileobj)

print(data1,data2,data3,sep='\n')


# copying photo in 1 file to another file

file1 = open("Harshal.jpg","rb")
file2 = open("copy.jpg","wb")

photo = file1.read(1024*130)
file2.write(photo)
file1.close()
file2.close()