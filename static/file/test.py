import itchat
import logging

def foo():    
    logging.debug("A log message")
    itchat.auto_login(picDir="wxpy/qr.png")

if __name__=="__main__":
    foo()
