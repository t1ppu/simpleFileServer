import os
import os
import xmlrpc.client
# import traceback
# import logging

path= "C:/Users/kolli/OneDrive/Desktop/Part-1/client/"      #path of client folder  
    
rpccall= xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True)

x= int(input("Select your operation-\n1. Upload file to the server\n2. Download file from the server\n3. Rename file in the server\n4. Delete file from the server\n"))

while True:
    if x==1:
        fname= input("Please enter filename to upload: ")
        try:
            with open(path+"uploads/"+fname,'rb') as handle:
                buffer = xmlrpc.client.Binary(handle.read())
                rpccall.upload(fname, buffer)
                print("File uploaded successfully!")
                handle.close()
                break
        except FileNotFoundError:
            print("Couldn't locate file. Try again!")      

    elif x==2:
        fname= input("Please enter filename to download: ")
        try:
            with open(path+"downloads/"+fname,'wb') as handle:
                buffer= rpccall.download(fname)
                handle.write(buffer.data)
                handle.close()
                print("File downloaded successfully!")
                break
        except Exception as e:
            os.remove(path+"downloads/"+fname)
            print("Couldn't locate file. Try again!")

    elif x==3:
        while True:
            fname= input("Please enter the current name of the file: ")
            nname= input("Please enter the new name of the file: ")
            if fname != nname:
                break
            else:
                print("Please enter a new name for the file!")

        try:
            err=rpccall.rename(fname,nname)
            if type(err)== int:
                raise err
            print("File renamed successfully!")
            break
        except:
            print("Couldn't locate file. Try again!")

    elif x==4:
        fname= input("Please enter filename to delete from the server: ")
        try:
            err=rpccall.delete(fname)
            #print(err)
            if type(err)== int:
                raise err
            print("File deleted successfully!")
            break
        except:
            print("Couldn't locate file. Try again!")

    else:
        print("Please enter the operation correctly!")
    
