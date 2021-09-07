# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 09:12:04 2021

@author: hp
"""


from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime,timedelta
import databaseFunctions.viewData as vwdt
import databaseFunctions.insertData as inst



def syncro():
    credentials = pickle.load(open("basicFunctions/token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)
    result = service.calendarList().list().execute()
    
    ids=result['items']
    now = datetime.now() - timedelta(days = 2)
    minDate=now.strftime('%Y-%m-%dT%H:%M:%S') + str("+05:30")
    
    for val in ids:
        eventlist=service.events().list(calendarId=val['id'],orderBy="updated",updatedMin=minDate).execute()
        
        allEvents=eventlist['items']
        
        for itm in allEvents:
            
                try:
                    desc=itm['description']
                
                
                    if desc.lower().find('drivekraft')>0:
                       
                        for atd in range(0,len(itm['attendees'])):
                    
                            
                            if itm['attendees'][atd]['email']==val['id']:
                                continue
    
                            avail=vwdt.checkingScheduledSessions(itm['attendees'][atd]['email'])
                            
                            if avail==False:
                                
                                Payment='No'
                                avail=vwdt.checkingWaitingListprority(itm['attendees'][atd]['email'])
                                
                                if avail==True:
                                    vwdt.deletingFromWaitinglistpriority(itm['attendees'][atd]['email'])
                                    Payment='Yes'
                                
                                else:
                                      avail=vwdt.checkingWaitingList(itm['attendees'][atd]['email'])
                                      vwdt.deletingFromWaitinglist(itm['attendees'][atd]['email'])
                                
                                ide,email, problemStatement = avail[0],avail[1],avail[2]
                                psychologist= vwdt.getThePsychologistName(val['id'])[0]
                                date, time=itm['start']['dateTime'].split('T')
                                paidOrNot=Payment
                                inst.insertIntoScheduledSessions(ide,email, problemStatement, psychologist, date, time, paidOrNot)
            
                                print(avail,"************************")
                                
                            else:
                               continue
        
                except:
                    continue
                        
         

#insertIntoWaitingList('23','drishi_be16@thapar.edu', problemStatement)
