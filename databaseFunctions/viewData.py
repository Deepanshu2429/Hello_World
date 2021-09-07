import sqlite3
from basicFunctions.LessLinkOpeningsPsychologist import findTop4PsychologistwithLessLinkOpenings


#view data from calendly links table
def viewCalendlyLinks():

    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    con.execute("SELECT * FROM calendlyLinks")
    data=con.fetchall()

    return data


def isPsyHavingSessionOn(psy,date):
    #connecting with database -- these lines shouldn't edited
   connection = sqlite3.connect('quality.db')
   con = connection.cursor()   

   con.execute("""SELECT * FROM scheduledSessions where psychologist =(?)and  date =(?)""",(str(psy),str(date)))
   data=con.fetchone()
   
   connection.close() 

   if data==None:
     return False
   else:
      return True    
  
    



def LinkOpenedinLast24Hrs(psy):  
   #connecting with database -- these lines shouldn't edited
   connection = sqlite3.connect('quality.db')
   con = connection.cursor()       

   query= """SELECT linkOpenedSinceLastSync,LinkOpenedinLas24Hrs FROM linkAccessed where name='""" + str(psy) +"'"
   con.execute(query)
   data=con.fetchone()
   
   connection.close()  

   return int(data[0])+int(data[1]) 




def getCalendlyInfo(psychologists,date)  :

     #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    psyWithNoOfTimesLinkAccess=dict()

    for psy in psychologists:
         if isPsyHavingSessionOn(psy,date)==False : #returning true or false based on if the psycholofist is having session on given day or not.. will be checking from ScheduledSession Table
             psyWithNoOfTimesLinkAccess[psy]=LinkOpenedinLast24Hrs(psy)


    psychologists=findTop4PsychologistwithLessLinkOpenings(psyWithNoOfTimesLinkAccess) # will return list of psychologist name    

    strOfPsychologist=str(psychologists)
    query="""SELECT * FROM calendlyLinks  where name in(""" + str(strOfPsychologist[1:-1]) +""")"""
    con.execute(query)
    data=con.fetchall()

    connection.close()
       
    return data


def updateLinkAccessed(name,val):

    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()   


    con.execute("Update linkAccessed set LinkOpenedinLas24Hrs ='" + str(val) +"' and linkOpenedSinceLastSync='0'  where name='" + str(name) +"'")


    connection.commit()
    connection.close()

    return




def detailsFromLinkAccessed():
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()   


    con.execute("SELECT * FROM linkAccessed")
    data=con.fetchall()

    for val in data:

        if val[1]==0:
            continue
        else: 
            total=int(val[1]) + int(val[2])
            updateLinkAccessed(val[0],total)
            # update both fields


    connection.close()        
    return        




def readCadLinksAndKeys(psycho):

    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()   

    strOfPsychologist=str(psycho)

    con.execute("SELECT * FROM calendlyLinks where Name in(?)""",str(strOfPsychologist[1:-1]))
    data=con.fetchall()

    connection.close() 
    return data


def checkingWaitingListprority(email):

    #connecting with database -- these lines shouldn't edited
   connection = sqlite3.connect('quality.db')
   con = connection.cursor()   

   con.execute("""SELECT * FROM waitingListprority where email ='""" + str(email) +"'")
   data=con.fetchall()

   connection.close() 

   if data==None:
     return False
   else:
      return data   




def checkingWaitingList(email):
   
   #connecting with database -- these lines shouldn't edited
   connection = sqlite3.connect('quality.db')
   con = connection.cursor() 


   con.execute("""SELECT * FROM waitinglist where email ='""" + str(email) +"'")
   data=con.fetchone()
   
   connection.close() 

   if data==None:
     return False
   else:
      return data  


def checkingScheduledSessions(email):
   #connecting with database -- these lines shouldn't edited
   connection = sqlite3.connect('quality.db')
   con = connection.cursor()   

   con.execute("""SELECT * FROM scheduledSessions where email ='"""+ str(email) +"'" )
   data=con.fetchone()
   
   connection.close() 

   if data==None:
     return False
   else:
      return True         


def deletingFromWaitinglist(email):

    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor() 
    con.execute("""DELETE FROM GF2 WHERE email=?""", (email,))

    connection.close() 

    return 



def deletingFromWaitinglistpriority(email):
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor() 

    con.execute("""DELETE FROM GF2 WHERE email=?""", (email,))

    connection.close() 

    return           


def isavailable(email,contact):

    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor() 


    con.execute("""SELECT * FROM clientDetails where email = (?) and contactNumber =(?)""",(str(email),str(contact)))
    data=con.fetchone()

    connection.close() 

    if data==None:
            return False
    else:
            return data    


def getURlForPsychologist(name):
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()   


    con.execute("SELECT calendlyLink FROM calendlyLinks where Name = '""" + str(name) + "'")
    data=con.fetchone()

    connection.close() 
    return data
   


def incrementLinkOpen(name):

   #connecting with database -- these lines shouldn't edited
   connection = sqlite3.connect('quality.db')
   con = connection.cursor()       

   query= """SELECT linkOpenedSinceLastSync FROM linkAccessed where name='""" + str(name) +"'"
   con.execute(query)
   data=con.fetchone()[0]
   
   data=int(data) +1

   con.execute("Update linkAccessed set linkOpenedSinceLastSync ='" + str(data) +"' where name='" + str(name) +"'")


   connection.commit()
   connection.close()
    
   return


def listOfScheduledSesions():
 #connecting with database -- these lines shouldn't edited
   connection = sqlite3.connect('quality.db')
   con = connection.cursor()   

   con.execute("""SELECT * FROM scheduledSessions""")
   data=con.fetchall()
   
   connection.close() 
 
   return data


def listOfClients():
   #connecting with database -- these lines shouldn't edited
   connection = sqlite3.connect('quality.db')
   con = connection.cursor()   

   con.execute("""SELECT * FROM clientDetails""")
   data=con.fetchall()
   
   connection.close() 
 
   return data

def getThePsychologistName(mailId):
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()   


    con.execute("SELECT Name FROM calendlyLinks where email = '""" + str(mailId) + "'")
    data=con.fetchone()

    connection.close() 
    return data



def getClientDetails(mailId):
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()   


    con.execute("SELECT Name,contactNumber FROM createClientDetails where email = '""" + str(mailId) + "'")
    data=con.fetchone()

    connection.close() 
    return data    


def getPsychologistConatct(Name):  
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()   


    con.execute("SELECT Name FROM contact where Name = '""" + str(Name) + "'")
    data=con.fetchone()

    connection.close() 
    return data
  



