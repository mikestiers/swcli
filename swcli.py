import sqlite3
import os
import re

ver = 0.1
dbname = os.getenv("HOME")+'/Documents/spiceworks_prod - Copy.db'
con = sqlite3.connect(dbname)
cur = con.cursor()
#cur.execute("SELECT * FROM tickets WHERE id = '5'")
#data = cur.fetchall()
#print(data)

# Command prompt
def getCommand():
    command = input("?>")
    if command == "q":
        quit()
    if int(command) >= 0:
        showTicket(command)
    if command == "d":
        showDue()
    else:
        getCommand()

# Display interactive help menu
def interHelp():
    print("Spiceworks Command Line Interface v", ver)
    print("(q) = quit")
    return

# Display command line help    
def cliHelp():
    print("-i    interactive mode")
    return

# Display specific ticket information
def showTicket(command):
    cur.execute("SELECT id, priority, closed_at FROM tickets WHERE id =?", command)
    data = cur.fetchone()
    print(data)
    getCommand()
    return

# Display tickets due
def showDue():
    return

# Quit
def quit():
    cur.close()
    print("later")
    raise SystemExit # or sys.exit().  what is the difference?
    
    
        
interHelp()
cliHelp()
getCommand()
