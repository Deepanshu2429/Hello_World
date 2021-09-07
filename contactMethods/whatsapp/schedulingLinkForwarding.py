import requests
import os
import smtplib
import imghdr
import json
from email.message import EmailMessage
import yaml


#configurations to read main configurations
with open("configuration.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

#reading instance id   
instanceid=cfg["instanceName"]    


#ncomplete message needes to be completed
def schedulingLinkForwarding(name,number):


    url = "https://api.chat-api.com/"+ str(instanceid) +"/sendLink?token=bfllgpii7xqb42zq"

    payload="{\r\n  \"body\": \"Hi " + str(name.title()) + "\\nPlease you the below link to schedule your session \xF0\x9F\x98\x83 . \\n\\n  https://drivekraftheroku.herokuapp.com/template \",\r\n  \"phone\": \"" +str(number) + "\"\r\n}"
    headers = {
            'Content-Type': 'application/json'
            }

    response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.text)
    return





#schedulingLinkForwarding("dipesh","918284990439")