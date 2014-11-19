import sqlite3
import os
import re

ver = 0.1
dbname = os.getenv("HOME")+'/Documents/spiceworks_prod - Copy.db'
con = sqlite3.connect(dbname)
cur = con.cursor()
ticketNo = int

#cur.execute("SELECT * FROM tickets WHERE id = '5'")
#data = cur.fetchall()
#print(data)

# Command prompt
def getCommand():
    command = input("?>")
    if command == "q":
        quit()
    if command == "t":
        ticketMenu()
    if int(command) >= 0:
        showTicket(command)
    if command == "d":
        showDue()
    else:
        getCommand()

# Ticket menu
def ticketMenu():
    ticketNo = input("ticket?>")
    showTicket(ticketNo)

# Display interactive help menu
def interHelp():
    print("Spiceworks Command Line Interface v", ver)
    print("(t)icket menu")
    print("(q)uit")
    return

# Display command line help    
def cliHelp():
    print("-i    interactive mode")
    return

# Display specific ticket information
def showTicket(ticketNo):
    cur.execute("SELECT id, assigned_to, created_by, priority, closed_at, status, summary FROM tickets WHERE id =(?)", (ticketNo,))
    data = cur.fetchone()
    print("ID: ",data[0])
    print("Assigned to: ",data[1])
    print("Created by: ",data[2])
    print("Priority: ",data[3])
    print("Closed at: ",data[4])
    print("Status: ",data[5])
    print("Summary: ",data[6])
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
getCommand()

