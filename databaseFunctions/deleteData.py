import sqlite3



def delCadVal(name):
    
    #connecting with database -- these lines shouldn't edited
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()

    con.execute("""Delete from  calendlyLinks where name='""" + str(name) +"'")
   
    connection.commit()
    connection.close()
    
    return