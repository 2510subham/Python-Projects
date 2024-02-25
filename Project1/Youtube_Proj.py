import sqlite3
con = sqlite3.connect("tutorial.db")
cursor=con.cursor()
import json


cursor.execute('''
                Create table if not exists Movie(
                    id Integer PRIMARY KEY,
                    name Text not null,
                    time Text not null
                )
               ''')

def listAllVideos():
    # pass # here we are using pass keyword which means that we will come in future and write our functionallity ,it helps to not get error
    # ih=n these the data does n't contain the indexing so will use Enumerate 
    # print(videos)
    videos=load_data()
    print("*" *70)
    for video in videos:
        print(f"{video[0]} Name is=  {video[1]} and time is {video[2]}\n")
    print("*" *70)
    
    
    
def addVideos():
    vid=load_data()
    le=len(vid)+1
    name=input("enter a videos name ")
    time=input("enter a time ")
    try:
        cursor.execute("Insert into Movie values(?,?,?)",(le,name,time))
        con.commit()
    except Exception:
        print(Exception)
    
def updateVideos():
    listAllVideos()
    id=int(input("select id which you want to update  "))
    name=input("enter a Updated videos name ")
    time=input("enter a Updated time ")
    try:
        cursor.execute("Update Movie set name=?,time=? where id=?",(name,time,id))
        con.commit();
    except Exception:
        print(Exception)

def deleteVideos():
    listAllVideos()
    id=int(input("select id which you want to delete  "))
    try:
        cursor.execute("Delete from Movie where id=?",(id,))
        con.commit()
    except Exception:
        print(Exception)
    

def load_data():
    try:
       allMovie=cursor.execute("Select * from Movie")
       data=(allMovie.fetchall())
       print('data while fetching ',data)
       if data =='None':
           return []
       
       return data
    except FileNotFoundError:
        return []

# def saveDataHelper(videos):
#     # We will write the data in all functions that wahy we are creating  one function it will write our data 
#     with open('youtube.txt','w') as file:
#         #takes 2 argments the data which we want to update and the file path
#         json.dump(videos,file) 


def main():
    video=load_data()
    while True:
        print("\n Youtube Manager | Choose an Option ")
        print("1. List All Vidoes ")
        print("2. Add A New Videos ")
        print("3. Update videos details ")
        print("4. Delete the video ")
        print("5. Exit teh App ")
        
        choice=input("enter Ur Choice ")
        
        # here we can use If-else but we have switchcase (match in python) here we will use these for better readibility
        match choice:
            case '1': #here we are entering in quotes beacuse while taking input we are taking in string that's why
                listAllVideos()
                continue
            case '2':
                addVideos()
                continue
            case '3': 
                updateVideos()
                continue
            case '4':
                deleteVideos()
                continue
            case '5':
                break;
            case _: # work as default
                break
    con.close() # Closing the connection with sqlite
    

if __name__ =='__main__':
    main()

    