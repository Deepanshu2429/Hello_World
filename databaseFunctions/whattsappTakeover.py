import requests
import time
import json
import yaml



def whattsappTakeover():



    #configurations need to read from configurations.yaml file
    with open("configuration.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)

    #reading instance id   
    instanceid=cfg["instanceName"]

    url = "https://api.chat-api.com/"+ str(instanceid)+ "/takeover?token=bfllgpii7xqb42zq"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if str(json.loads(response.text)['result'])=='Takeover request sent to WhatsApp':
        print("Instance takingover taking place , will take around 4-5 seconds")
        time.sleep(5)
    
    print("Whattsapp instance is activated")

    return 



    