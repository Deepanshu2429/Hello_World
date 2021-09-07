
import sqlite3

def resetLinkedAccess():
    #connecting with database -- these lines shouldn't be edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()   


    con.execute("""update linkAccessed 
    set linkopenedinlas24hrs = '0', linkOpenedSinceLastSync='0'""")


    connection.commit()
    connection.close()

    return
