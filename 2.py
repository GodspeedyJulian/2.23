FileHandle = open("BookInfo.txt","r")
line=FileHandle.readline()

a=0
File=open("BookInfo_new.txt","w")

while len(line)>0:
    a+=1
    for i in range (len(line)):
        if line[i]==",":
            Author=line[:i]
            BookTitle=line[i+1:-1]
            for n in range (len(Author)):
                if Author[n]==" ":
                    BookNumber=ord(Author[n+1])
                   
            if a<10:
                File.write("#0" + str(a)+" book author:"+ Author + "  book title: " + BookTitle +", number of copies: " + str(BookNumber)+"\n")
            else:
                File.write("#" + str(a)+"book author: "+ Author + "  book title: '" + BookTitle+", number of copies: " + str(BookNumber) + "\n")
    
    line=FileHandle.readline()
File.close()
FileHandle.close()

            
        
