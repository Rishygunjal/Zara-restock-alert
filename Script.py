import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
import re
import datetime
from selenium.webdriver.chrome.options import Options
import time

from twilio.rest import Client
# Import required libraries
import os
# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

# Access the password from the environment variable


# Use the password in your code
# For example, you might use it to authenticate to a service:
# authenticate(username, password)

# account_sid = 'ACc8d4c3ce0323020a4780104867bf8183'
# auth_token = '54f0ade3d768ed01c3b363944effe51d'

client = Client(os.getenv("account_sid"), os.getenv("auth_token"))




def your_task():
    # Replace this with the code for your task
    
        # Open the website
    driver.get(url1)
    button = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/main/article/div/div/div[2]/div/div[3]")
    print(button.text)
    now = datetime.datetime.now()
    now = now + datetime.timedelta(minutes=2)
    print(now.hour, now.minute)

    # pywhatkit.sendwhatmsg("+919175418951", button.text, now.hour, now.minute)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=button.text,
        to='whatsapp:+919657413031'
    )


    print(message.sid)

    # You can add more actions here, like clicking on elements, filling out forms, etc.


    






# Get the current date and time

# Send a WhatsApp Message to a Contact at 1:30 PM
# #Enter Your Credentials for login purposes
# USERNAME = "username" #Ldap Id
# PASSWORD = "passsword" #Ldap Password
# OTP = "OTP" #SSO OTP

# Function to remove unnecessary space from text
# def remove(string):
#     pattern = re.compile(r'\s+')
#     return re.sub(pattern, '', string)

# Data will be stored here
# all_details = []

# # setting up webdriver
# Path = "D: \softwares\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=Path)
# driver.get("https://www.zara.com/IN/en/sweatshirt-with-embroidered-slogan-p01131340.html?v1=251352804&utm_campaign=productShare&utm_medium=mobile_sharing_Android&utm_source=red_social_movil")

from selenium import webdriver

# Specify the path to your ChromeDriver executable
# Make sure you have the compatible ChromeDriver version for your Chrome browser
chromedriver_path = "C:\Program Files (x86)\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--user-agent=Your-User-Agent-String")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=chrome_options)

# Website URL to open
# Replace this with the URL of the site you want to open
url1 = 'https://www.zara.com/IN/en/sweatshirt-with-embroidered-slogan-p01131340.html?v1=251352804&utm_campaign=productShare&utm_medium=mobile_sharing_Android&utm_source=red_social_movil'
url2 = "https://www.zara.com/in/en/refill-bronzing-powder-p24130836.html?v1=277697091"





# Schedule the task to run every 1 minute
# schedule.every(1).minutes.do(your_task)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

while True:
    your_task()
    time.sleep(3600)  # Sleep for 1 hour (3600 seconds)

# finally:
    # Close the browser window
    # driver.quit()


# user_name = driver.find_element_by_id("username")
# pw = driver.find_element_by_id("password")

# user_name.send_keys(USERNAME)
# pw.send_keys(PASSWORD)

# otp = driver.find_element_by_name("totp")

# driver.implicitly_wait(3) #Waiting to avoid slow Network Issues
# otp.send_keys(OTP)

# driver.implicitly_wait(3)
# driver.implicitly_wait(3)

# login = driver.find_elements_by_name("/html/body/div[2]/div/form/input[6]")

# rem = driver.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/label/span[1]")
# rem.click()
# driver.implicitly_wait(3)

# otp.send_keys(Keys.RETURN)
# driver.switch_to.frame("rightPage")
# user_name = driver.find_element_by_name("UserName")
# pw = driver.find_element_by_name("UserPassword")
# user_name.send_keys(USERNAME)
# pw.send_keys(PASSWORD)

# pw.send_keys(Keys.RETURN)
# driver.implicitly_wait(1)


# ele = driver.find_elements_by_tag_name("frame")
# driver.switch_to.frame("leftPage") #Switching Frames
# acad = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div[1]/table/tbody/tr/td[2]/a")
# acad.click()
# abc = driver.find_element_by_partial_link_text("All About")
# abc.click()
# run = driver.find_element_by_partial_link_text("Course Syllabus")
# run.click()
# driver.implicitly_wait(5)
# run = driver.find_element_by_partial_link_text("Course Syllabus")

# driver.switch_to.default_content()
# ele = driver.find_elements_by_tag_name("frame")

# driver.switch_to.default_content()
# driver.switch_to.frame("rightPage")

# for i in range(2,36):
#  if i-1<10:
#         k = ("0"+str(i-1))
#  else :
#     k = str(i-1)
#  i = str(i)

#  driver.switch_to.default_content()
#  driver.switch_to.frame("rightPage")
#  dept = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(i)+"]")
#  print(dept.text)
#  branch = (((dept.text)).split(" ("))[0]
#  driver.implicitly_wait(2)
#  dep = driver.find_element_by_partial_link_text(dept.text)
#  driver.implicitly_wait(2)
#  dep.click()
#  driver.implicitly_wait(2)

#  for j in range(2,1111): #The number "1111" can be changed to any large number as long as it is greater than 200

#     driver.switch_to.default_content()
#     driver.switch_to.frame("rightPage")
#     try:
#         info = driver.find_element_by_xpath("/html/body/form/table/tbody/tr["+str(j)+"]/td[1]/a")
#         CourseCode = info.text
#     except:
#         break
#     info.click()
#     # CourseCode = info.text
#     CourseCode = remove(CourseCode)

#     CourseName = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]").text
#     TotalCredits = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[2]").text
#     Type = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[2]").text
#     Lecture = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[5]/td[2]").text
#     Tutorial = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[6]/td[2]").text
#     Practical = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[7]/td[2]").text
#     Selfstudy = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[8]/td[2]").text
#     HalfSemester = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[9]/td[2]").text
#     TextReference= driver.find_element_by_xpath("/html/body/form/table/tbody/tr[10]/td[2]").text
#     Description = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[11]/td[2]").text
#     LastUpdate = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[12]/td[2]").text

#     #Seperating to obtain only the date of LastUpdate
#     try:
#         LastUpdate = (LastUpdate.split())[0]
#     except:
#         LastUpdate = LastUpdate


#     #Changing the Type to conventional notations
#     if Type == "Theory":
#         Type = "T"
#     if Type == "Lab":
#         Type = "L"
#     if Type == "Other Project":
#         Type = "L"

#     Structure ={
#             "Type":Type,
#             "HalfSemester":HalfSemester,
#         }

#     WorkLoad ={

# 	        "Lecture":Lecture,
#             "Tutorial":Tutorial,
# 	        "Practical":Practical,
#             "Selfstudy":Selfstudy,

#         }

#     course_info = {
#         "Code":CourseCode,
#         "Department":branch,
#         "Title":CourseName,
#         "TotalCredits":TotalCredits,
#         "Description":Description,
# 	    "TextReference":TextReference,
#         "LastUpdate":LastUpdate,
#         }
#     course_info['Structure']= Structure

#     all_details.append(course_info)


#     driver.back()

#     driver.implicitly_wait(1)

#  driver.back()

# #Creating a function to save the data in Json Format in a file
# def writeToJSONFile(path, fileName, data):
#     filePathNameWExt = './' + path + '/' + fileName + '.json'
#     with open(filePathNameWExt, 'w') as fp:
#         json.dump(data, fp)

# path = './' #'./' means that the file will be stored in the current location
# fileName = 'all_details'
# data = all_details

# writeToJSONFile('./',fileName,data)
