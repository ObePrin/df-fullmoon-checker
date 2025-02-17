#Index
#1 - Function Definitions
#2 - Variable Declarations
#3 - Main Code Block




#    1 - beginning of function definitions
# switches month from numeral form to proper spelling
def monthnumeraltostring(monthnumeral):
    match monthnumeral:
        case 1:
            return "Morning Star"
        case 2:
            return "Sun's Dawn"
        case 3:
            return "First Seed"
        case 4:
            return "Rain's Hand"
        case 5:
            return "Second Seed"
        case 6:
            return "Mid Year"
        case 7:
            return "Sun's Height"
        case 8:
            return "Last Seed"
        case 9:
            return "Hearthfire"
        case 10:
            return "Frostfall"
        case 11:
            return "Sun's Dusk"
        case 12:
            return "Evening Star"

# switches month input into numeral form for calculations
def monthstringtonumeral(monthstring):
    match monthstring:
        case "mst":
            return 1
        case "sda":
            return 2
        case "fse":
            return 3
        case "rha":
            return 4
        case "sse":
            return 5
        case "mye":
            return 6
        case "she":
            return 7
        case "lse":
            return 8
        case "hfi":
            return 9
        case "ffa":
            return 10
        case "sdu":
            return 11
        case "est":
            return 12
        case "help":
            helpmonth()
            return monthstringtonumeral(input("\nPlease check your current date and enter the month again"+"\n"+"or enter 'help' for a list of proper abbreviations used in the program : "))
        case _:
            return monthstringtonumeral(input("\nPlease check your current date and enter the month again"+"\n"+"or enter 'help' for a list of proper abbreviations used in the program : "))

# returns how many years have passed since first day
def daytoyear(daytotal):
    daytotal -= 1
    daytotal -= daytotal % 360
    return int(daytotal / 360)

# returns month the date is on
def daytomonth(daytotal):
    if daytotal > 360:
        daytotal %= 360
    daytotal -= 1
    daytotal -= daytotal % 30
    return int(daytotal / 30)

# returns which day of month the date is on
def daytoday(daytotal):
    daytotal -= 1
    #print(str(type(daytotal % 30)))
    return int(daytotal % 30)

# calculates Messer's last rise
def messerfullmoon(daytotal):
    messerdaytotal = 1 #initialization
    messerdayoriginal = 21
    messerdaytotal = daytotal - messerdayoriginal
    #print(str(type(messerdaytotal))+str(type(messerdayoriginal))+str(type(daytotal)))
    if messerdaytotal < 0:
        return -1
    elif messerdaytotal % 32 == 0:
        #print(str(type(10000 + (messerdaytotal / 32))))
        return 10000 + (messerdaytotal / 32)
    elif messerdaytotal % 32 != 0:
        messerdaytotal -= (messerdaytotal % 32)
        #print(str(type(messerdaytotal)))
        #print(str(type(messerdaytotal / 32)))
        return int(messerdaytotal / 32)

# calculates Secunda's last rise
def secundafullmoon(daytotal):
    secundadaytotal = 1 #initialization
    secundadayoriginal = 25
    secundadaytotal = daytotal - secundadayoriginal
    if secundadaytotal < 0:
        return -1
    elif secundadaytotal % 32 == 0:
        return 10000 + (secundadaytotal / 32)
    elif secundadaytotal % 32 != 0:
        secundadaytotal -= (secundadaytotal % 32)
        return int(secundadaytotal / 32)

# help with month abbreviations
def helpmonth():
    print("\nHere is a list of all months observed on Nirn and their proper abbreviations used in this program : ")
    print(" 1- Morning Star : mst")
    print(" 2- Sun's Dawn   : sda")
    print(" 3- First Seed   : fse")
    print(" 4- Rain's Hand  : rha")
    print(" 5- Second Seed  : sse")
    print(" 6- Mid Year     : mye")
    print(" 7- Sun's Height : she")
    print(" 8- Last Seed    : lse")
    print(" 9- Hearthfire   : hfi")
    print("10- Frostfall    : ffa")
    print("11- Sun's Dusk   : sdu")
    print("12- Evening Star : est")
#    end of function definitions




#    2 - beginning of variable declaration block
day = 1 #initialization
monthstring = "" #initialization
year = 1 #initialization
monthnumeral = 13 #initialization

originalday = 1
originalmonth = 1
originalyear = 405

daytotal = 0 #initialization
daytotalplaceholder = 1 #initialization

messerdaytotal = 1 #initialization
messerdaymultiplier = 1 #initialization
secundadaytotal = 1 #initialization
secundadaymultiplier = 1 #initialization

messeroriginalday = 21
secundaoriginalday = 25

dayplaceholder = 1 #initialization
#print(str(type(dayplaceholder)))
monthstringplaceholder = "" #initialization
yearplaceholder = 1 #initialization
monthnumeralplaceholder = 1 #initialization
# end of variable declaration block




#    3 - beginning of main function
# takes current day as input from user
day = int(input("Enter the current day : "))
while day < 1 or day > 30:
    day = int(input("\nPlease check your current date and enter the day again : "))
#monthstring = input("Enter the current month : ")
while monthnumeral < 1 or monthnumeral > 12:
    monthnumeral = monthstringtonumeral(input("Enter the current month : "))
year = int(input("Enter the current year : "))
while year < 405:
    year = int(input("\nPlease check your current date and enter the year again : "))
#monthnumeral = monthstringtonumeral(monthstring)

# current day test print
print("\nYou are on day "+str(day)+" of "+monthnumeraltostring(monthnumeral)+" of the year "+str(year)+", 4E.")

# turns date into a single numeral for easier calculation
if year > 405:
    daytotal += (year - originalyear) * 360
daytotal += (monthnumeral - originalmonth) * 30
daytotal += day

# calculates last full moons
messerdaymultiplier = messerfullmoon(daytotal)
if messerdaymultiplier > 10000:
    messerdaytotal = ((messerdaymultiplier - 10000) * 32) + 21
else:
    messerdaytotal = (messerdaymultiplier * 32) + 21
secundadaymultiplier = secundafullmoon(daytotal)
secundadaytotal = (secundadaymultiplier * 32) + 25
#print(str(type(dayplaceholder)))
# final printout - the actual use of this whole code
# exception for first ever full moon
if daytotal == 21:
    print("\nToday is a full moon!")
    print("Next full moon will be on 25 Morning Star 405, 4E.")
# before first ever full moon
elif messerdaymultiplier == -1 and secundadaymultiplier == -1:
    print("\nNext full moon will be on 21 Morning Star 405, 4E.")
# between first ever two full moons
elif secundadaymultiplier == -1:
    print("\nLast full moon was on 21 Morning Star 405, 4E.")
    print("Next full moon will be on 25 Morning Star 405, 4E.")
# Messer has risen
elif messerdaymultiplier > 10000:
    print("\nToday is a full moon!")
    dayplaceholder = daytoday(secundadaytotal) + originalday
    monthnumeralplaceholder = daytomonth(secundadaytotal) + originalmonth
    monthstringplaceholder = monthnumeraltostring(monthnumeralplaceholder)
    yearplaceholder = daytoyear(secundadaytotal) + originalyear
    print("Previous full moon was on "+str(dayplaceholder)+" "+monthstringplaceholder+" "+str(yearplaceholder)+", 4E.")
    secundadaytotal += 32
    dayplaceholder = daytoday(secundadaytotal) + originalday
    monthnumeralplaceholder = daytomonth(secundadaytotal) + originalmonth
    monthstringplaceholder = monthnumeraltostring(monthnumeralplaceholder)
    yearplaceholder = daytoyear(secundadaytotal) + originalyear
    print("Next full moon will be on "+str(dayplaceholder)+" "+monthstringplaceholder+" "+str(yearplaceholder)+", 4E.")
# Secunda has risen
elif secundadaymultiplier > 9999:
    #print(str(type(dayplaceholder)))
    print("\nToday is a full moon!")
    dayplaceholder = daytoday(messerdaytotal) + originalday
    monthnumeralplaceholder = daytomonth(messerdaytotal) + originalmonth
    monthstringplaceholder = monthnumeraltostring(monthnumeralplaceholder)
    yearplaceholder = daytoyear(messerdaytotal) + originalyear
    #print(str(type(dayplaceholder)))
    print("Previous full moon was on "+str(dayplaceholder)+" "+monthstringplaceholder+" "+str(yearplaceholder)+", 4E.")
    messerdaytotal += 32
    dayplaceholder = daytoday(messerdaytotal) + originalday
    monthnumeralplaceholder = daytomonth(messerdaytotal) + originalmonth
    monthstringplaceholder = monthnumeraltostring(monthnumeralplaceholder)
    yearplaceholder = daytoyear(messerdaytotal) + originalyear
    #print(str(type(dayplaceholder)))
    print("Next full moon will be on "+str(dayplaceholder)+" "+monthstringplaceholder+" "+str(yearplaceholder)+", 4E.")
# last Messer rose (no current full moon)
elif messerdaymultiplier > secundadaymultiplier:
    dayplaceholder = daytoday(secundadaytotal) + originalday
    monthnumeralplaceholder = daytomonth(secundadaytotal) + originalmonth
    monthstringplaceholder = monthnumeraltostring(monthnumeralplaceholder)
    yearplaceholder = daytoyear(secundadaytotal) + originalyear
    print("\nPrevious full moon was on "+str(dayplaceholder)+" "+monthstringplaceholder+" "+str(yearplaceholder)+", 4E.")
    secundadaytotal += 32
    dayplaceholder = daytoday(secundadaytotal) + originalday
    monthnumeralplaceholder = daytomonth(secundadaytotal) + originalmonth
    monthstringplaceholder = monthnumeraltostring(monthnumeralplaceholder)
    yearplaceholder = daytoyear(secundadaytotal) + originalyear
    print("Next full moon will be on "+str(dayplaceholder)+" "+monthstringplaceholder+" "+str(yearplaceholder)+", 4E.")
# last Secunda rose (no current full moon)
elif messerdaymultiplier == secundadaymultiplier:
    dayplaceholder = daytoday(messerdaytotal) + originalday
    monthnumeralplaceholder = daytomonth(messerdaytotal) + originalmonth
    monthstringplaceholder = monthnumeraltostring(monthnumeralplaceholder)
    yearplaceholder = daytoyear(messerdaytotal) + originalyear
    print("\nPrevious full moon was on "+str(dayplaceholder)+" "+monthstringplaceholder+" "+str(yearplaceholder)+", 4E.")
    messerdaytotal += 32
    dayplaceholder = daytoday(messerdaytotal) + originalday
    monthnumeralplaceholder = daytomonth(messerdaytotal) + originalmonth
    monthstringplaceholder = monthnumeraltostring(monthnumeralplaceholder)
    yearplaceholder = daytoyear(messerdaytotal) + originalyear
    print("Next full moon will be on "+str(dayplaceholder)+" "+monthstringplaceholder+" "+str(yearplaceholder)+", 4E.")
#    end of main function




# added to stop program from exiting to allow a last revision glance
input("Press ENTER to continue...")
