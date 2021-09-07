import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import yaml



def dayOfWeek(date):

    #we are recieving date om ormat of 2021-08-22
    #so splitting into list
    dateList=date.split("-")

    week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    week_num=datetime.date(int(dateList[0]),int(dateList[1]),int(dateList[2])).weekday()
    return week_days[week_num]


def psychologistFreeAtRequiredTime(psychologistFreeSlots,freeTimeFrom,freeTimeTo):
    
    psychologistName=list()
    for psychologist in psychologistFreeSlots:
        avalaibleTime=psychologistFreeSlots[psychologist]

        fromTimePsycho= avalaibleTime.split("-")[0]
        toTimePsycho= avalaibleTime.split("-")[1]

        if fromTimePsycho >=freeTimeFrom and  fromTimePsycho<=freeTimeTo:
            psychologistName.append(psychologist)
        elif toTimePsycho >=freeTimeFrom and  toTimePsycho<=freeTimeTo:
            psychologistName.append(psychologist)
        elif  fromTimePsycho<= freeTimeFrom and toTimePsycho <= freeTimeTo:
            psychologistName.append(psychologist)
        else:
            continue

    return psychologistName          


def gettingPsychologistFreeSlotsOnDay(day):

    with open("configuration.yml", "r") as ymlfile:
        cfgMain = yaml.load(ymlfile)  

    #mainsheet name
    TimeSheet=cfgMain["timingSheet"] 

    #reading spreadsheet
    scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds =ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
    client = gspread.authorize(creds)
        
    #reading data from Timings 1
    spreadsheetData = client.open(str(TimeSheet)).worksheet("Timings2")
    spData = spreadsheetData.get_all_values()
    spheadings= spData[0]
    spRemainingData=spData[1:]
    
    indx=spheadings.index(day)
    
    restultSheet=dict()
    
    for i in spRemainingData:
        
        if i[indx]=='NA' or i[indx]=='':
            continue
        
        restultSheet[i[0]]=i[indx]
    

    return restultSheet     
    
    