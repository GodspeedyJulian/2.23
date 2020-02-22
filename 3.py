def addNewBook():
    File=open("BookInfo.txt","a")
    while True:
        Author=input("input the author of a new book")
        Title=input("input the Title os a new book")
        if len(Author)!=0 and len(Title)!=0:
            break
    File.write("\n"+ Author + " , " + Title)
    File.close()
def SearchBookByAuthor():
    File=open("BookInfo.txt","r")
    while True:
        SearchName=input("input the author of the book: ")
        if len(SearchName)!=0:
            break
    found = Flase
    for line in File.readlines():
        BookAuthor=""
        BookName=""
        Get=False
        for i in line:
            if i ==",":
                Get=True
            if Get==Flase:
                BookAuthor+=i
            elif Get==True and i !=",":
                BookName+=i
        if BookAuthor ==NewName:
            found=True
            print(BookName)
    if found ==Flase:
        print("sorry, there is no book by this author.")
    File.close()
while True:
    a=input("input 1 if you want to add new book to the BookInfo.txt  ;"
            " input 2 if you want to Seach book by its author"
            " input 3 to exit the program")
    if a =="1":
        addNewBook()
    if a=="2":
        SearchBookByAuthor()
    if a=="3":
        break
    else:
        print("flase input")
