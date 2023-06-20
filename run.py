"""
Developed by: Zachary Walsh

Steps to my process:
Step 1a: Ask for the directory of where the log files are located.
     1b) Optionally, you can hard set a path in the path variable at the top.
Step 2a: List all of the present log files, and ask which they wish to update log entries from.
     2b: After a file is selected, read the desired .log file.
Step 3: Ask user for an input of two dates in standard time, which we will convert to UNIX time.
Step 4: Output all entries that fall within the desired date range the user inputs.

1) ask_directory()
2) select_and_read()
3) date_or_whole()
3) daterange()
4) print_entirelog()**** Optional
"""
#THIS IS WRONG: https://www.python.org/dev/peps/pep-0008/#id19
#Imports should be seperate, according to PEP 8 rules.

import os, fnmatch

# This is your local path to where your log files are located. 
# Right click folder in File Explorer, and Copy address as text for easy replacement.

path = r"C:\Users\itzwa\Desktop\coding\Python\LogViewer\Logs"
global openThis
global file
global logTime

def ask_directory():        
    # Check if directory exists or not
    if os.path.exists(path):
        os.chdir(path)
        print(f'Directory is valid.\n')
    else:
        print(f'Directory is NOT valid.')
        
    select_and_read()

def select_and_read():   
    # Lists files in your directory that follow that pattern variable. (In our case .log extension)
    # Uses user's input (An integer) to determine what log file they want to open and read.
    fileList = os.listdir('.')    
    pattern = "*.log"
    counter = 0
    global numFile

    for entry in fileList:
        if fnmatch.fnmatch(entry, pattern):
            print(str(counter) + ': '+ entry)
        counter += 1

    while True:
        selected_file = input('Press the corresponding number to the log file you want:')
        
        if not selected_file.isnumeric():
            print("Please select a valid number.")

        elif int(selected_file) > int(counter):
            print("Please select a valid log file of 0 through", counter - 1)
        else:
            numFile = selected_file
            break

    date_or_whole()

def date_or_whole():

    while True:
            specific_or_whole = input("Do you wish to search for a specific date range (Press 1), or print entire log? (Press 2)")
            
            if not specific_or_whole.isnumeric():
                print("Please enter 1 or 2.")
            elif int(specific_or_whole) > 2:
                print("Please enter a value less than 2.")
            elif int(specific_or_whole) == 1:
                daterange()
                break
            elif int(specific_or_whole) == 2:
                print_entirelog()
                break

def daterange():
    # User inputs two different dates in UNIX time format, and it returns all entries that fall within that range.
    # Conditional's added so if the user enters an invalid date format, it will ask them to try again.

    while True:
        date1 = input('Enter first date:')

        if not date1.isnumeric():
            print("Please enter an integer in UNIX date form.")

        else:
            break
        
    while True:
        date2 = input('Enter second date:')

        if not date2.isnumeric():  
            print("Please enter an integer in UNIX date form.")
        else:
            break

    counter = 1
  
    openThis = os.listdir(path)[int(numFile)]
    file = open(openThis, "r")

    for line in file:
        fields = line.split(",")

        logTime = fields[1]

        if date1 <= logTime <= date2:
            print(str(counter) + ":\n", "UNIX Time: " + logTime)

            from datetime import datetime
            datetime = datetime.fromtimestamp(int(logTime))

            print("Date Time:", datetime, "\n")  
            
            counter+= 1    
        else:
            continue

    print(counter - 1, "entries within Date Range")


    search_again()

def print_entirelog():
    
    openThis = os.listdir(path)[int(numFile)]
    file = open(openThis, "r")
    counter = 1
    
    for line in file:
        fields = line.split(",")

        logType = fields[0]
        logTime = fields[1]
        logSeverity = fields[2]
        logMessage = fields[3]

        #THIS IS WRONG: https://www.python.org/dev/peps/pep-0008/#id16
        #Line break is improper, should break on the + signs for the print statement
        
        print('Log Type: ' + logType + '\n' + 'Log Time: ' + logTime + '\n' + 'Log Severity: ' + logSeverity + '\n' + 'Log Message: ' + logMessage + '\n')
        
        print("UNIX Time: " + logTime)
        from datetime import datetime
        convert = datetime.fromtimestamp(int(logTime))
        print("Date Time:", convert, "\n")

        counter+= 1

    print(counter - 1, "entries within Date Range")

    search_again()

def search_again():
    while True:
        rerun = input("Do you wish to perform another search?: (Y/N):")

        #THIS IS WRONG: https://www.python.org/dev/peps/pep-0008/#id24
        #Ideally, it's not the greatest to put your function you're calling on the same line as your IF statement.
        
        if rerun == "Y" or rerun == "y": ask_directory()
        
        elif rerun == "N" or rerun == "n":
            print("Ending LogViewer.")
            break
        else:
            print("Unknown response, ending LogViewer.")
            break

ask_directory()