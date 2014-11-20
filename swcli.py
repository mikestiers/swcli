# add format option to displayTicket() for single, multiple, etc
# add curses support
# figure out a good way to assign all items in a query to their column name in the database
# check if command is numeric
# add command line switches
# is there a better way to construct command detection?  of course there is.
# figure out a way to login via web interface.  it does not use a detectible auth according to curl
# map out stored procedures for creating, closing, deleting, etc..
# add option to open ticket in web interface

import sqlite3
import os
import re

ver = 0.1
dbname = os.getenv("HOME")+'/Documents/spiceworks_prod - Copy.db'
con = sqlite3.connect(dbname)
cur = con.cursor()
ticketNo = int

# Main menu
def getCommand():
    command = input("?>")
    if command == "q":
        quit()
    if command == "t":
        ticketMenu()
    else:
        interHelp()

# Ticket menu
def ticketMenu():
    ticketCommand = input("ticket?>")
    if ticketCommand == "d":
        showDue()
    if ticketCommand == "o":
        showOpenTickets()
    if ticketCommand == "q":
        raise SystemExit
    showTicket(ticketCommand)

# Display interactive help menu
def interHelp():
    print("Spiceworks Command Line Interface v", ver)
    print("(t)icket menu")
    print("(q)uit")
    getCommand()
    return

# Display command line help    
def cliHelp():
    print("-i    interactive mode")
    return

# Display specific ticket information
def showTicket(ticketNo):
    cur.execute("SELECT id, assigned_to, created_by, priority, closed_at, status, summary FROM tickets WHERE id =(?)", (ticketNo,))
    data = cur.fetchone()
    # print(data)
    if data == None:
        ticketMenu()
    else:
        displayTicket(data)
        ticketMenu()
    return

# Display open tickets
def showOpenTickets():
    cur.execute("SELECT id, assigned_to, created_by, priority, closed_at, status, summary FROM tickets WHERE status ='open'")
    data = cur.fetchall()
    for x in data:
        displayTicket(data[0])
    return

# Print ticket information
def displayTicket(data):
    print("--------------")
    print("ID: ",data[0])
    print("Assigned to: ",data[1])
    print("Created by: ",data[2])
    print("Priority: ",data[3])
    print("Closed at: ",data[4])
    print("Status: ",data[5])
    print("Summary: ",data[6])
    return

# Display tickets due
def showDue():
    cur.execute("SELECT id, assigned_to, created_by, priority, closed_at, status, summary FROM tickets WHERE status ='open'")
    data = cur.fetchall()
    return

# Quit
def quit():
    cur.close()
    print("later")
    raise SystemExit # or sys.exit().  what is the difference?

interHelp()
getCommand()

