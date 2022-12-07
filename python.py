
#myfile=open("file1.txt","r")
#data1=myfile.read()
#myfile.close()
#print(data1)
#username=input("enter username: ")
#myfile2=open("file1.txt","w")
#myfile2.write(username)
#myfile.close()





#myfile3=open("file1.txt","r")
#for  i in myfile3:
#    print(i[::-1],end="")
#myfile = open('file1.txt', 'r+')
#myfile.write('''Hello
#How are you!!
#Good Morning''')

#myfile.close()
#new = open('file1.txt', 'r')
#data1 = new.readlines()
#res = 0
#for line in data1:
#    res += 1
#print("no of lines: ", res)
#replicate = open('newfile.txt', 'w+')
#for line in data1:
#    replicate.write(line)
#replicate.close()



#fin=open("file.txt","r+")
#charCount=wordCount=linecount=0
#for line in fin:
#    linecount+=1
#    wordCount+=len(line,split())
#    charCount+=len(line,split())
#    charCount+=len(line)
#print("line count=",linecount)
#print("line count=",wordCount)
#print("line count=",charCount)



#fr1=open("file1.txt","r")
#fr2=open("file3.txt","w")
#for line in fr1:
#    fr2=write()




#try:
#    a=int(input("enter a: "))
#    b=int(input("enter b: "))
#    c=a+b
#    d=a/b
#    print("all operations are successful",c,d)
#except ZeroDivisionError:
#    print("a no can't be divided by zero")
#except ArithmeticError:
#    print("an ArithmeticError error occured ")



try:
    a={1:"a",2:"b",3:"c"}
    print(a[4])
except LookupError:
    print("Index out of bound occur")
else:
    print("succecc")