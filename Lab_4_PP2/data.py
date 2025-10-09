#1
from datetime import date,  timedelta, datetime
current = date.today() - timedelta(5)
print("Current time: ", date.today())
print("Substact five days : ",current)



#2
from datetime import date,  timedelta, datetime
time = datetime.now()-timedelta(1)
yesterday = time.strftime("%d-%m-%Y")

print("Yesterday: ",yesterday)

time = datetime.now()
today = time.strftime("%d-%m-%Y")

print("Today: ",today)

time = datetime.now()+timedelta(1)
tomorrow = time.strftime("%d-%m-%Y")

print("Tomorrow: ", tomorrow)



#3
from datetime import date,timedelta,datetime
time = datetime.now()
withoutmiliseconds = time.strftime("%Y-%m-%d, %H:%M:%S")
print(withoutmiliseconds)



#4
from datetime import date,timedelta, datetime
yesterday = datetime.now()-timedelta(1)
tomorrow = datetime.now()+timedelta(1)


yesterday = datetime.timestamp(yesterday)
tomorrow = datetime.timestamp(tomorrow)

print(tomorrow-yesterday)