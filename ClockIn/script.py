import time
import datetime
from datetime import date
import calendar
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(r"C:\Users\chromedriver.exe")
# driver.get("https://edyd.fa.us2.oraclecloud.com/hcmUI/faces/FndOverview?fnd=%3B%3B%3B%3Bfalse%3B256%3B%3B%3B&fndGlobalItemNodeId=HWM_HCMWFMWORKAREA_FUSE_WEBCLOCK&_afrLoop=8337365441095987&_afrWindowMode=0&_afrWindowId=l8us4u4y3&_adf.ctrl-state=b6f3fc3ox_105&_afrFS=16&_afrMT=screen&_afrMFW=1680&_afrMFH=561&_afrMFDW=1680&_afrMFDH=1050&_afrMFC=8&_afrMFCI=0&_afrMFM=0&_afrMFR=96&_afrMFG=0&_afrMFS=0&_afrMFO=0") #opens that time page
# time.sleep(5)
# driver.find_element_by_id("_FOpt1:_FOr1:0:_FOSrHWM_HCMWFMWORKAREA_FUSE_WEBCLOCK:0:_FOTsr1:1:wcUpl:UPsp1:wcRgn:0:cil21j_id_1").click()  #clock out
# time.sleep(2)
# driver.refresh() # Refreshes page don't know why I put this
# driver.find_element_by_id("_FOpt1:_FOr1:0:_FOSrHWM_HCMWFMWORKAREA_FUSE_WEBCLOCK:0:_FOTsr1:1:wcUpl:UPsp1:wcRgn:0:btn3Pgl").click() #clock in


my_date = date.today()
print(calendar.day_name[my_date.weekday()])
currentDT = datetime.datetime.now()
x = (currentDT.strftime("%I:%M:%S %p"))
print(x)
timeOfDay = x[9] + x[10]
hour = x[0] + x[1]
print(timeOfDay)
Day = calendar.day_name[my_date.weekday()] # gives you a day
if((timeOfDay == "AM" and (hour == "07" or hour == "08")) and (Day != "Saturday" or Day != "Sunday")):
    print("This should check you in the morning")
elif(timeOfDay == "PM" and hour == "04" and (Day != "Saturday" or Day != "Sunday")):
    print("This should check you out in the afternoon")

randomHour = random.randrange(7,9)
randomMin = random.randrange(30,59)
randomSecond = random.randrange(0,59)
if(randomHour > 7):
    randomMin = random.randrange(0, 15)
print(randomHour)
print(randomMin)
print(randomSecond)
# if(x[1] == "8" and )
# if(calendar.day_name[my_date.weekday() == 'Saturday'] or calendar.day_name[my_date.weekday() == 'Sunday']):
#     time.sleep(5) # we keep sleeping maybe?
#     driver.refresh() # we refresh maybe?
# else:
#

