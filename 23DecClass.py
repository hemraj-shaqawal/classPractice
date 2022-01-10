from genericpath import exists
import os,shutil
import platform
from datetime import date,datetime
from PIL import Image
import cv2
import smtplib
from email.mime.text import MIMEText
#import ssl
import socket
hasattr(socket, "ssl")


def str_len(s):
    """ input will be string and it will give you length of string."""
    if type(s) == str:
        count = 0
        for item in s:
            count = count  + 1;

        return count;
    else:
        return "input type is not string."


def getIndexOfPremitiveEle(param):
    """input will be primitive type of collection data and it will return a index of it's element."""
    if type(param) != str and type(param) != int:
        i = []
        for item in range((len(param))) :
            i.append(item)
        return i
    else:
        return "Please enter premitive type of data"


def getDictValueAsList(param):
    """input type is Dictionary and it will give you list of it's item with 2 level down."""
    if type(param) == dict:
        itemList = []
        for index,value in enumerate(param.values()):
            if type(value) == dict:
                for index1,val in enumerate(value.values()):
                    itemList.append(val)
            else:
                itemList.append(value)
        return itemList
    else:
        "Input type is wrong, Please provide dict."

def call2():
    print("function 2 is invoked")

def call1():

    """Nested function invocation"""

    print("function 1 is invoked")
    call2()

def cancadinationOfListStrItem(lst):
    """Concadination of all string type item with in list"""
    if type(lst) ==  list:
        s = ""
        for item in lst:
            if type(item) == str:
                s = s+item

        if s == "":
            return "No string item found in list"

        return s
    else:
        return "input will be list type, try again!"

def indexOfList(param):
    """get index of list items"""
    if type(param) == list:
        i = []
        for item in range((len(param))) :
            i.append(item)
        return i
    else:
        return "Please enter list type of data"


def getListOfFilenameFromDirc(path):
    """get all file name form directory"""
    if os.path.exists(path):
        return os.listdir(path)
        
    else:
        return "invalid path"


def getSystemConfig():
    """Get System configuration details"""
    system_prop = platform.uname()
    print("System Name: ", system_prop.system)
    print("Processor: ", system_prop.processor)
    print("Machine: ", system_prop.machine)

def showCurrDateTime():
    today = datetime.now()
    return today.strftime("%d/%m/%Y %H:%M:%S")

#10
def showImage(path):
    """show image as per provided Path"""
    if os.path.isfile(path):
        img = Image.open(path)
        img.show()

#11
def play_videoFile(filePath):
    """input of video file path, it Play video for you"""

    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(filePath)
    
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video  file")
    
    # Read until video is completed
    while(cap.isOpened()):
        
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
        
            # Display the resulting frame
            cv2.imshow('myFrame', frame)
        
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        # Break the loop
        else: 
            break
    
    # When everything done, release 
    # the video capture object
    cap.release()
    
    # Closes all the frames
    cv2.destroyAllWindows()

#12
def moveFile(sourcePath, DestinationPath):
    """input will be source directory and distination directory, it will move file form source to destination.."""
    allFileList = getListOfFilenameFromDirc(sourcePath)
    for item in allFileList:
        item = f"\{item}"
        src = sourcePath+item
        desc = DestinationPath+item
        #shutil.move(src,desc)
        os.rename(src,desc)

#13


#14

#15
def sendMyEmail(host,password,receiver,msg):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(host,password)
    server.sendmail(host, receiver, msg)
    server.quit()


#
def appendAllFileTxtinSingle():
    listFileCon = []
    for i in [item for item in os.listdir() if ".txt" in item]:
        filePath = os.getcwd()+"/"+i
        f = open(filePath,"r+")
        listFileCon.append(f.read())
        f.close()
    f1 = open("newFile.txt","r+")
    f1.writelines(listFileCon)
    f1.read()
    f1.close()

"""
print(str_len("hemraj shaqawal"))
print(getIndexOfPremitiveEle([2,3,4,2,5,5]))
print(getIndexOfPremitiveEle({"wef":2,"4":3,"#":3}))
print(getDictValueAsList({"wef":2,"4":3,"#":23456,"demo":{"a":1,"B":[1,2,2,3,3],"c":"hemraj"}})) 
print(cancadinationOfListStrItem(["hemu","shaky"]))
print(indexOfList([2,2,2,2,2]))
print(getListOfFilenameFromDirc("D:\Python_Project\Class Practice"))
getSystemConfig()
print(showCurrDateTime()) 
showImage("E:\Architechture Diagram\image_2021_11_16T06_09_21_479Z.png")
play_videoFile("D:\Python_Project\Class Practice\sample-mp4-file-small.mp4")
moveFile("D:\Python_Project\Class Practice\src","D:\Python_Project\Class Practice\des")
sendMyEmail("test@gmail.com","password","test123@gmail.com","Hii")
"""

