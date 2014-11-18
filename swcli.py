import sqlite3
import os

ver = 0.1
dbname = os.getenv("HOME")+'/Documents/spiceworks_prod - Copy.db'
con = sqlite3.connect(dbname)
cur = con.cursor()
cur.execute("SELECT * FROM tickets WHERE id = '5'")
data = cur.fetchall()
#print(data)

# Command prompt
def getCommand():
    command = input("?>")
    if command == "q":
        quit()
    if command == "t":
        showTicket()
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
def showTicket():
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
