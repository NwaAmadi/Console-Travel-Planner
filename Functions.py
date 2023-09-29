#Credits: chibuisiukegbu@gmail.com

import datetime
import random


def reminder():
    pass

def Flights(Airline, AirlineDepertureDate, CustomerName):
    pass

def ConvertDate():
    pass

#Takes two dates as parameters and returns their customized string format
def generateDate(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + datetime.timedelta(days = random_days)
    return random_date.strftime("%Y-%m-%d")

#This function returns the current time @ the time of call
def CurrentTime():
    now = datetime.datetime.now()
    return(now.strftime("%A, %B %d, %Y %I:%M:%S %p"))

def getJet():
    jetlist = ['Boeing 747','Boeing 777', 'Boeing 787 Dreamliner', 'Boeing 737-300ER', 'Airbus A380',
               'Airbus A300']
    randomJet = random.choice(jetlist)
    return(randomJet)
  
#This function takes data from two text files and writes them into a new file.
def writefile(outfile, BookingDetails):
  file1 = open(outfile, "r")
  file2 = open(BookingDetails, "r")
  output = open("Itinerary.txt", "w")
  for line1 in file1:
    # Write the line to the output file
    output.write(line1)
  for line2 in file2:
    # Write the line to the output file
    output.write(line2)
  # Closing the files
  file1.close()
  file2.close()
  output.close()
  return(output)
