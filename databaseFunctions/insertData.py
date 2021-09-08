import sqlite3
from contactMethods.whatsapp import sessionScheduledConfirmation as ssc

def insertIntoGf1(name,WhatsappNumber ,email,country,othermedium,issuse,Referral):
    
   
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    con.execute("""Insert into GF1
    (Name,WhatsappNumber,email,country,othermedium,issuse,Referral) 
    values(?,?,?,?,?,?,?)""", (str(name),str(WhatsappNumber ),str(email),str(country),str(othermedium),str(issuse),str(Referral)))

    connection.commit()
    connection.close()

    return



def insertIntoGf2(name,WhatsappNumber ,email,issues):
    
   
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    con.execute("""Insert into GF2
    (Name,WhatsappNumber,email,issuse) 
    values(?,?,?,?)""", (str(name),str(WhatsappNumber ),str(email),str(issues)))

    connection.commit()
    connection.close()

    return



def insertIntoCalendlyLinks(name,email,contact,calendlyLink,imageName,Description,Type):

    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    con.execute("""Insert into calendlyLinks
    (Name,email,contact,calendlyLink,imageName,Description,Type)
    values(?,?,?,?,?,?,?)""", (str(name),str(email),str(contact),str(calendlyLink),str(imageName),str(Description),str(Type)))

    connection.commit()
    connection.close()

    return




def insertClientDetails(Name,email,contactnumber,country):

    
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    con.execute("""Insert into ClientDetails
    (Name,email,contactNumber,country) 
    values(?,?,?,?)""", (str(Name),str(email),str(contactnumber),str(country)))

    connection.commit()
    connection.close()

    return



def insertIntoWaitingList(ide,email, problemStatement):

    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    con.execute("""Insert into waitingList 
     (id,email, problemStatement) values(?,?,?)""",(str(ide), str(email),str(problemStatement)))

    connection.commit()
    connection.close()
    
    return


def insertIntoWaitingListPrority(id,email, psychologist, paidOrNot):
    
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    con.execute("""Insert into waitingListPrority
    (id,email, psychologist, paidOrNot) values(?,?,?,?)""",(str(id), str(email),str(psychologist),str(paidOrNot)))
   
    connection.commit()
    connection.close()
    
    return

def insertIntoScheduledSessions(ide,email, problemStatement, psychologist, date, time, paidOrNot):
    
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()
    
    con.execute("""Insert into scheduledSessions
    (id,email, problemStatement, psychologist, date, time, paidOrNot) values(?,?,?,?,?,?,?)""",(str(ide),str(email),str(problemStatement),str(psychologist),str(date),str(time),str(paidOrNot)))
    
    ssc.sendSessionConfirmationMSg(email, problemStatement, psychologist, date, time, paidOrNot)

    connection.commit()
    connection.close()
    
    return   

def insertIntoLinkAccessed(name,linkopenedSinceLastSync,LinkOpenedinLast24Hrs):

    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    con.execute("""Insert into linkAccessed 
    (name,linkOpenedSinceLastSync,LinkOpenedinLas24Hrs) values(?,?,?)""",(str(name),str(linkopenedSinceLastSync),str(LinkOpenedinLast24Hrs)) )
    
    connection.commit()
    connection.close()

    return



def insertIntoCompletedSession(client_id,paid,email,date,time,status,pyschologist):

    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    con.execute("""Insert into completedsession
    (client_id,paid,email,date,time,status,psychologist) 
    values(?,?,?,?,?,?)""", (int(client_id),str(paid),str(email),int(date),int(time),str(status),str(pyschologist)))

    connection.commit()
    connection.close()


    return

def sessionCompleted(email):
     #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()   

    con.execute("""SELECT * FROM scheduledSessions where email in(?)""",str(email))
    data=con.fetchall()
    
    if data==None:
        connection.close() 
        return

    else:
     con.execute("""DELETE FROM scheduledsession WHERE email=?""", (email,))
     for i in data:
      insertIntoCompletedSession(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
    
    connection.commit()
    connection.close() 
    return  


