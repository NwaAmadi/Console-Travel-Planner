#Credits: chibuisiukegbu@gmail.com

from Functions import *
import string
from datetime import date, datetime
import random
import os

#Generating Airline Deperture Date
AirlineDepartureDate = ''
Tdate = CurrentTime()
jet = getJet()
#print(type(Tdate))
print('\n\tWELCOME TO OUR CONSOLE TRAVEL PLANNER\n')
#Taking User Details
CustomerName = str(input('Enter your name: '))
CustomerSex = str(input('Enter your sex: '))
CustomerAge = str(input('Enter your Age: '))
while(True):  
  print('\nWe offer:')
  print('[1] Flights')
  print('[2] Hotels')
  print('[3] Itinerary')
  print('[4] Exit\n')
  
  UserChoice = int(input('Enter an Option: '))
  if (UserChoice == 1):
      print('[1] Book Flight')
      print('[2] Check Flight deperture date')
      print('[3] Cancel Flight')
      UserChoice = int(input('\nEnter an Option: '))
      if (UserChoice == 1):
          AirlineDepartureDate = generateDate("2023-01-01", "2023-12-31")
          #Tp = take off point
          #Dest = Destination
          global Airline 
          Airline = str(input('\nEnter Airline: '))
          TP = str(input('Enter your Takeoff point: '))
          Dest = str(input('Enter your Destination: '))
          DepartureDate = input('Enter your departure date in (YYYY-MM-DD): ')
          #The Final documents will be written to outfile.txt in the same directory
          #writing into the file
          outfile = open("outfile.txt", "w")
          outfile.write("        FLIGHT DETAILS\n")
          outfile.write("========================================")
          outfile.write("\nAirline: " + Airline + " Airways.\n")
          print("Jet: " + jet + ".\n")
          outfile.write("Customer Name: " + CustomerName + ".\n")
          outfile.write("Customer Age: " + CustomerAge + ".\n")
          outfile.write("Sex: " + CustomerSex + ".\n")
          outfile.write("Take off point: " + TP + ".\n")
          outfile.write("Departure Date: " + DepartureDate + ".\n")
          outfile.write("Airline Departure Date: " + AirlineDepartureDate + ".\n")
          outfile.write("Destination: " + Dest + ".\n")
          outfile.write("This record was generated on " + Tdate + " by " + CustomerName + " .\n")
          outfile.write("Enjoy your Flight!\n")
          outfile.write("Courtesy of " + Airline + " Airways.")
          outfile.write("\n")
          outfile.close()
          print("\nYour Flight Summary\n")
          print("========================================")
          print("\nAirline: " + Airline + "Airways.\n")
          print("Jet: " + jet + ".\n")
          print("Customer Name: " + CustomerName + ".\n")
          print("Customer Age: " + CustomerAge + ".")
          print("Sex: " + CustomerSex + ".\n")
          print("\nTake off point: " + TP + ".\n")
          print("Departure Date: " + DepartureDate + ".\n")
          print("Airline Departure Date: " + AirlineDepartureDate + ".\n")
          print("Destination: " + Dest + ".\n")
          print("This record was generated on " + Tdate + " by " + CustomerName + ".\n")
          print("Enjoy your Flight!")
          
      elif (UserChoice == 2):
          if(bool(AirlineDepartureDate) == False):
            print("\nDear" + CustomerName + ", you have not made any airline reservations")
          else:
            print("Flight Deperture Date: " + AirlineDepartureDate + ".")
      elif (UserChoice == 3):
          CF = ""
          CF = str(input("Are you sure you want to cancel your flight? Y/N: "))
          CF = CF.lower()
          if (CF == "y"):
              os.remove("outfile.txt")
              print("Your booking records have been deleted successfully")
          else:
              print("Error, Try again later")
              print("Exiting.......\n")
              
  elif (UserChoice == 2):
      print("List of Available hotels :\n")
      print("[1] Freehand Los Angeles [$69,426]\n")
      print("[2] Beverly Hill Hotel [$1,567,000]\n")
      print("[3] Post Ranch inn [$859,426]\n")
      print("[4] FUTO Guest House [₦100,000]\n")
      UserChoice = int(input("Enter an option: "))
      if (UserChoice == 1):
          print("\n\tHOTEL BOOKING DETAILS\n")
          print("Freehand Hotels and Suites, Los Angeles")
          print("Name: " + CustomerName + ".")
          print("Bill: $69,426.00")
          print("Discount: $10.00")
          print("Total: $68,731.00")
          
          booking = open("BookingDetails.txt", "w")
          booking.write("        BOOKING DETAILS\n")
          booking.write("===================================\n")
          booking.write("Freehand Hotels and Suites, Los Angeles\n")
          booking.write("Name: " + CustomerName + "\n")
          booking.write("Games: $500\n")
          booking.write("Meals: $800\n")
          booking.write("Bill: $70,726.00\n")
          booking.write("Discount: $10.00\n")
          booking.write("Total: $63,653.40\n")
          booking.close()
          
      elif (UserChoice == 2):
          print("\tHOTEL BOOKING DETAILS PER NIGHT\n")
          print("Beverly Hills Hotel")
          print("Name: " + CustomerName + "\n")
          print("Date of booking: " + Tdate + ".\n")
          print("Games: $100\n")
          print("Meals: $300\n")
          print("Bill: $1,567,400.00\n")
          print("Discount: $100.00\n")
          print("Total: $1,551,726.00\n")
          print("Have a blissful day\n")
          
          #Writing to the file BookingDetails .txt 
          booking = open("BookingDetails.txt", "w")
          booking.write("\tBOOKING DETAILS\n")
          booking.write("===================================\n")
          booking.write("Beverly Hills hotel\n")
          booking.write("Name: " + CustomerName + ".\n")
          booking.write("Date of booking: " + Tdate + ".\n")
          booking.write("Games: $100.00\n")
          booking.write("Meals: $300.00\n")
          booking.write("Bill: $1,567,400.00\n")
          booking.write("Discount: $100.00\n")
          booking.write("Total: $1,551,726.00\n")
          booking.write("Have a blissful day\n")
          booking.close()
          
      elif (UserChoice == 3):
          print("\tHOTEL BOOKING DETAILS\n")
          print("Post Ranch inn, CA, USA")
          print("Name: " + CustomerName + "\n")
          print("Date of booking: " + Tdate + ".\n")
          print("Bill: $859,426\n")
          print("Discount: $50.00\n")
          print("Total: $842,237.48\n")
          print("Have a blissful day\n")
          
          #writing to text file
          booking = open("BookingDetails.txt", "w")
          booking.write("\tHOTEL BOOKING DETAILS\n")
          booking.write("Post Ranch inn, CA, USA\n")
          booking.write("Name: " + CustomerName + "\n")
          booking.write("Date of booking: " + Tdate + ".\n")
          booking.write("Bill: $859,426\n")
          booking.write("Discount: $50.00\n")
          booking.write("Total: $842,237.48\n")
          booking.write("Have a blissful day\n")
          booking.close()
          
      elif (UserChoice == 4):
          print("\twelcome To FUTO Guest House\n")
          print("Location: Imo State, Owerri")
          print("Name: " + CustomerName + ".")
          print("Date of booking: " + Tdate + ".")
          print("Bill: $1000.00 per night")
          print("Total = $1000.00")
          
          booking = open("BookingDetails.txt", "w")
          booking.write("\tWelcome To FUTO Guest House\n")
          booking.write("===================================\n")
          booking.write("Name: " + CustomerName + "\n")
          booking.write("Date of booking: " + Tdate + ".\n")
          booking.write("Bill: ₦100,000.00 per night\n")
          booking.write("Total: ₦100,000.00\n")
          booking.close()
          
      else:
          print("Invalid input!\n")
          print("Check your Input and try again")
          print("Exiting.......\n")
          
  elif (UserChoice == 4):
      print("Exiting.......\n")
      break
  elif (UserChoice == 3):
      print('\tITINERARY PLANNER\n')
      print('[1] Show Itinerary')
      UserChoice = int(input("Enter an option: "))
      if (UserChoice == 1):
        fileName1 = "outfile.txt"
        fileName2 = "BookingDetails.txt"
        file = writefile(fileName1, fileName2)
        with open("Itinerary.txt", "r") as infile:
          ItData = infile.read()
        print(ItData)
        infile.close()
