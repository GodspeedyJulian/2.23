FileHandle = open("BookInfo.txt","r")
line=FileHandle.readline()
a=00
while len(line)>0:
    a+=1
    for i in range (len(line)):
        if line[i]==",":
            if a<10:
                print("#0" + str(a)+" book author:"+ str(line[:i]) + "  book title: " + line[i+1:])
            else:
                print("#" + str(a)+" book author: "+ str(line[:i]) + "  book title: " + line[i+1:])

    line=FileHandle.readline()
