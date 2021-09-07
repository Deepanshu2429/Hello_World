import requests
import os
import smtplib
import imghdr
import json
from email.message import EmailMessage
import yaml
import time


#configurations to read main configurations
with open("configuration.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

#reading instance id   
instanceid=cfg["instanceName"]    


def firstMsg(name,number):


    url = "https://api.chat-api.com/"+ str(instanceid) +"/sendMessage?token=bfllgpii7xqb42zq"

    payload="{\r\n  \"body\": \"Hi " + str(name.title()) + "\\nYou registered for the interactive session with Drivekraft and here we are as promised \xF0\x9F\x98\x83 . \\n\\nIt's great that you are ready to talk and remember it's never too late.\",\r\n  \"phone\": \"" +str(number) + "\"\r\n}"
    headers = {
            'Content-Type': 'application/json'
            }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return
    

def sendLink(name,number):
    
    url = "https://api.chat-api.com/"+ str(instanceid) +"/sendLink?token=bfllgpii7xqb42zq"
    
    payload="{\r\n  \"body\": \"https://forms.gle/dFdsNJMErDgeauWy5\",\r\n  \"previewBase64\": \"nn\",\r\n  \"title\": \"Follow up form\",\r\n  \"phone\": \"" +str(number) + "\"\r\n}"
    headers = {
      'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    return


def SecondMsg(name,number):
    url = "https://api.chat-api.com/"+ str(instanceid) +"/sendMessage?token=bfllgpii7xqb42zq"
    
    payload="{\r\n  \"body\": \"Can you please fill this above form \xF0\x9F\x98\x83  \\n\\nThis will help to know more about you and assign you the best match of psychologist \xF0\x9F\x98\x87 \xF0\x9F\x98\x87  \\n\\nDo let me know once you filled the form , I will proceed with scheduling it..... \\n\\n In case the above link doesn't work reply back with *not working* link will be activated as it is Whatsapp security feature \\nlinks are not activated unless there is a conversation before... once you text back link will be activated\xF0\x9F\x98\x83 \xF0\x9F\x98\x83 \",\r\n  \"phone\": " +str(number) +"\r\n}"
    headers = {
      'Content-Type': 'application/json'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    
    return



def send_Message(name,number):

    if str(number[0])=='+':
        number = number[1:]
        
    if len(number)==10:
        number='91'+ str(number)

    firstMsg(name,number)
    time.sleep(1)
    sendLink(name,number) 
    time.sleep(1)
    SecondMsg(name,number)
     
    return




send_Message("dipesh","918284990439")