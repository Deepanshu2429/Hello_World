from flask import Flask, render_template,request,redirect, url_for
import yaml
import  initalGreetings.readingGf1 as ig1
import  initalGreetings.readingGF2 as ig2
import schedulingAlgo.basicFunctions as basFun
import databaseFunctions.insertData as inst
import databaseFunctions.createAllTables as crt
import databaseFunctions.viewData as vwdt
import databaseFunctions.deleteData as dlt
#everything is working above
import basicFunctions.resetLinkAccess as rst
import basicFunctions.sessionSyncro as sync
import sqlite3

app = Flask(__name__) #create a flask object

@app.route('/')
def home():
    #ig1.readingGF1()
    #ig2.readingGF2()
    #sync.syncro()
    return "execution completed"

@app.route('/reset')
def reset():
    rst.resetLinkedAccess()
    return "completed"



@app.route('/template')
def scheduling():
    return render_template("bookAppointment.html")


@app.route('/processing',methods=["POST"])
def processing():

  #fetching the values filled by user  
  date=request.values.get('date')
  freeTimeFrom=request.values.get('freeTimeFrom')
  freeTimeTo=request.values.get('freeTimeTo')
  
  #print(date,freeTimeFrom,freeTimeTo)

  #getting day for the corresponding date
  day=basFun.dayOfWeek(date)

  #getting free slots of psychologist on that day  
  psychologistFreeSlots=basFun.gettingPsychologistFreeSlotsOnDay(day)

  #checking the availabaity of psychologist at time asked by user  
  psychologists=basFun.psychologistFreeAtRequiredTime(psychologistFreeSlots,freeTimeFrom,freeTimeTo)

  #checking calednly urls and names of psychologist of with least openings of URL in last 24 hours  
  gettingLinksOfCadely= vwdt.getCalendlyInfo(psychologists,date)  

  return render_template('cadleyIntegration.html',desc=gettingLinksOfCadely)


@app.route('/psychologist/<keys>/<name>')
def gettingUrls(keys,name):
    vwdt.incrementLinkOpen(name)
    url=vwdt.getURlForPsychologist(name)[0]   
    return redirect(url)     




@app.route('/admin')
def admin():
    return render_template("admin/adminauth.html")


@app.route('/verifyAdmin',methods=["POST"])
def verifyAdmin():  
    #reading password value
    password=request.values.get('password')

    if password=='Amadeus': 
        #password is correct
        return render_template("admin/adminLib.html")
    else:
        #password is wrong    
        return "kripya bahar jae"



#will create all tables
@app.route('/crtTables')
def crtTables():

    crt.createAllTables()
    return "done"


    

@app.route('/addingCaledlydetails')
def addingCaledlydetails():
    return render_template("admin/CalendlyLinkAddition.html")

@app.route('/addingCalendlyUrlInfo',methods=["POST"])
def addingCalendlyUrlInfo():
    name=request.values.get('name')
    email=request.values.get('email')
    contact=request.values.get('contact')
    url=request.values.get('url')
    imageName=request.values.get('imageName')
    Description=request.values.get('Description')
    Type=request.values.get('Type')

    inst.insertIntoCalendlyLinks(name,email,contact,url,imageName,Description,Type)
    inst.insertIntoLinkAccessed(name,0,0)
    return "Done"


@app.route('/delCadlink')
def defCadlink():
    return render_template("admin/delCadLink.html")


@app.route('/delCadLinkValue')
def delCadLinkValue():
    name=request.values.get('name')
    dlt.delCadVal(name)
    return "done"


@app.route('/scldSessions')
def scldSessions():
    data=vwdt.listOfScheduledSesions()
    return render_template('admin/listOfsessions.html',data=data)


@app.route('/cltList')
def clinetlist():
    data=vwdt.listOfClients()
    return render_template('admin/listOfClients.html',data=data)

@app.route('/viewCaledlydetails')
def viewCaledlydetails():

    data=vwdt.viewCalendlyLinks()
    print(data)
    return render_template("admin/CalendlyLinkview.html",data=data)



@app.route('/sessioncompletd/<mailid>')
def sessioncompletdBypsycho(mailid):   
    inst.sessionCompleted(mailid)
    return
   









if __name__ == '__main__':
    app.run(debug= False ) #debug enabled is creating warning and error

