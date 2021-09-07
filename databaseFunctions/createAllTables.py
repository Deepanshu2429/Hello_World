import yaml
import pandas as pd
import hashlib 
import sqlite3
import datetime


# createGf1 
def createGf1(con):

        con.execute("""CREATE TABLE
        GF1 (
        Name text ,
        WhatsappNumber text,
        email text,
        country text,
        othermedium text,
        issuse text,
        Referral text
        )""")


        return



# createGf1 
def createGf2(con):

        con.execute("""CREATE TABLE
        GF2 (
        Name text ,
        WhatsappNumber text,
        email text,
        issuse text
        )""")


        return


# create table for calendly links and authentication  key
def calendlyLinks(con):

        con.execute("""CREATE TABLE
        calendlyLinks (
        Name text ,
        email text,
        contact text,
        calendlyLink text ,
        imageName text,
        Description text,
        Type text 
        )""")


        return



def createClientDetails(con):

            con.execute("""CREATE TABLE
            clientDetails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,    
            Name text ,
            email text,
            contactNumber text,
            country text,
            psychologist text DEFAULT "NA"
            )""")

            return





#waitingList
def waitinglist(con):

        con.execute("""CREATE TABLE
        waitingList(
        id text,
        email text,
        problemStatement text,
        preferableTimings text)""")

        return



# waitingListPrority
def waitingListPrority (con):

        con.execute("""CREATE TABLE
        waitingListPrority (
        id text,
        email text,
        psychologist text,
        paidOrNot text )""")

        return


 #scheduledSessions       
def scheduledSessions(con):

        con.execute("""CREATE TABLE
        scheduledSessions (
        id text,
        email text,
        problemStatement text,
        psychologist text,
        date text,
        time text,
        paidOrNot text )""")

        return


 #linkAccessed       
def linkAccessed(con):

        con.execute("""CREATE TABLE
        linkAccessed(
        name text,
        linkOpenedSinceLastSync text,
        LinkOpenedinLas24Hrs text)""" )  

        return  



def completedsession(con):
            con.execute("""CREATE TABLE
            completedsession (
            client_id text,    
            paid text,
            email text,
            date text,
            time text,
            status text,
            psychologist text
            )""")

            return




#feedBackForm
def createAllTables():

    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    createGf1(con)
    createGf2(con)
    calendlyLinks(con)
    createClientDetails(con)
    waitingListPrority(con)
    waitinglist(con)
    linkAccessed(con)
    scheduledSessions(con)
    completedsession(con)


    
    connection.commit()
    connection.close()

    return
    













    


 


 



