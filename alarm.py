import schedule
import time
import webbrowser
def job():
    url = 'https://www.youtube.com/watch?v=3Y5GDoLbeBs'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

def strconverter(num):
    if(num>=0 and num <10):
        return "0"+str(num)

    else:
         return str(num)


while True:
    try:
        hour = int(input("Enter alarm hour(0-23): "))
    except ValueError:
        print("That entry was not valid. Please enter a number between 0 and 24 valer")

    if(hour<24 and hour >=0 ):
        break
    else:
        print("That entry was not valid. Please enter a number between 0 and 24")

while True:
    try:
        minute = int(input("Enter alarm minute (0-60): "))
    except ValueError:
        print("That entry was not valid. Please enter a number between 0 and 60")

    if(minute<60 and hour >=0 ):
        break
    else:
        print("That entry was not valid. Please enter a number between 0 and 60")


#minute = input("Enter alarm minute(0-59)")

str = strconverter(hour)+":"+strconverter(minute)

print("alarm set for: " + str)

schedule.every().day.at(str).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
