import threading
import os
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import logging
import traceback


path= "C:/Users/kolli/OneDrive/Desktop/Part-1\server/"      #path of server directory
#list=[]

class uploadthread(threading.Thread):
    def __init__(self, fname, fdata):
        threading.Thread.__init__(self)
        self.fname= fname
        self.fdata= fdata
    def run(self):
        with open(path+self.fname,'wb') as handle:
            buffer=handle.write(self.fdata.data)    

class dloadthread(threading.Thread):
    def __init__(self, fname):
        threading.Thread.__init__(self)
        self.fname= fname
    def run(self):
        try:
            with open(path+self.fname,'rb') as handle:
                buffer=handle.read()
                return xmlrpc.client.Binary(buffer)
        except Exception as e:
            logging.error(traceback.format_exc())



class renamethread(threading.Thread):
    def __init__(self, fname, nname):
        threading.Thread.__init__(self)
        self.fname= fname
        self.nname= nname
    def run(self):
        try:
            os.rename(path+self.fname,path+self.nname)
        except Exception as e:
            logging.error(traceback.format_exc())

class deletethread(threading.Thread):
    def __init__(self, fname):
        threading.Thread.__init__(self)
        self.fname= fname
    def run(self):
        try:
            os.remove(path+self.fname)
        except Exception as e:
            logging.error(traceback.format_exc())



def download_op(fname):
    try:
        return dloadthread(fname).run()
    except Exception as e:
        logging.error(traceback.format_exc())

def upload_op(fname, fdata):
    try:
        uploadthread(fname,fdata).start()
    except Exception as e:
        logging.error(traceback.format_exc())

def rename_op(fname,nname):
    try:
        renamethread(fname, nname).start()
    except:
        return 1

def delete_op(fname):
    try:
        deletethread(fname).start()
    except:
        return 1


server = SimpleXMLRPCServer(("localhost", 8000), logRequests=True, allow_none=True)
server.register_function(upload_op,"upload")
server.register_function(download_op,"download")
server.register_function(rename_op,"rename")
server.register_function(delete_op,"delete")
print("Server starting!")
server.serve_forever()
