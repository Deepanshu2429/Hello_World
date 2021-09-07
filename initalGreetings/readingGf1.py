#usig google api 
from databaseFunctions.insertData import insertIntoGf1
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3
import pandas as pd 
import databaseFunctions.viewData as vwdt
import databaseFunctions.insertData as inst
import basicFunctions.contactCorrection as bfun
from contactMethods.whatsapp import greetingMessages as whts
from contactMethods.whatsapp import schedulingLinkForwarding as slf
import databaseFunctions.whattsappTakeover as wt
import yaml


def readingGF1():

    #configurations need to read from configurations.yaml file
    with open("configuration.yml", "r") as ymlfile:
        cfgMain = yaml.load(ymlfile)  


    #mainsheet name
    sheetName=cfgMain["mainSheetName"]      
    lastreadindex=cfgMain["gf1LastReadIndex"] 

    #file path
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json',scope)
    client = gspread.authorize(credentials)


    #reading data from Google form 1 
    gf1Spreadsheet = client.open(str(sheetName)).worksheet("GF1")
    gf1Data = gf1Spreadsheet.get_all_values()
    headings= gf1Data[0]
    gf1RemainingData=gf1Data[lastreadindex:]

    print("processing "+ str(len(gf1RemainingData)) + " enteries ")
    entryNumber=1

    for entry in gf1RemainingData:

        timeStamp=entry[0]
        name= entry[1]
        number= entry[2]
        email=entry[3]
        country=entry[4]
        otherPlatform=entry[5]
        issue=entry[6]
        referral=entry[7]

        insertIntoGf1(name,number,email,country,otherPlatform,issue,referral)
        val=vwdt.isavailable(email,number)


        if val==False:
            contactVerifierd=bfun.contactCorrection(number,country)
            inst.insertClientDetails(name,email,contactVerifierd,country)
            whts.send_Message(name,contactVerifierd)
            

        else:
            client_id,Name,email,contactnumber,country,Psychologist=val
            inst.insertIntoWaitingListPrority(client_id,email, Psychologist, "NO")
            slf.schedulingLinkForwarding(Name,contactnumber)


        print("Currently processing----------->" + str(entryNumber) + " out of "+ str(len(gf1RemainingData)))
        lastreadindex=lastreadindex+1


    cfgMain["gf1LastReadIndex"]= lastreadindex
    with open('configuration.yml', 'w') as fp:
        yaml.dump(cfgMain, fp)
    

    return

   
   