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
import basicFunctions.sessionSyncro as sync
import sqlite3

app = Flask(__name__) #create a flask object

@app.route('/')
def hello_words():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug= False ) #debug enabled is creating warning and error

