import speech_recognition as sr 
import webbrowser
import requests
import pyttsx3;
import time
import json
from weather import Weather, Unit
from geopy.distance import vincenty
from geopy.geocoders import Nominatim
import smtplib
import numpy as np


print("<<<<<<<<<<< STARTING ASSISTANT BOT >>>>>>>>>>>>>>>")
print("<<<<Coded by Sudesh Bhuju>>>>>")
time.sleep(2)
recognize = sr.Recognizer()  
engine = pyttsx3.init()
command=''
username_file =  open('username.txt','r')
user_name=username_file.read()
username_file.close()
query_history=open('old_queries.txt','r').readlines()
lastQuery= query_history[len(query_history)-1]

response ={
    
    'HI':'Hello there '+user_name,
    'HELLO':'Hello there '+user_name,
    'WHAT IS YOUR NAME':'You can call me NepBot Sir',
    'HOW OLD ARE YOU':'Haha I cant really tell you sir',        
    'I HATE YOU':'Sorry sir! But I work the best I can',
    'HOW ARE YOU':'Im fine sir and you',
    'I LOVE YOU':'Haha I am just a Bot. I have no feelings.',
    'YOU ARE AWESOME':'Thank you Sir. I feel honoured.',
    'NAMASTE':'NAMASTE Sir',
    'WHAT IS MY NAME':'You are '+user_name,
    'WHAT WAS MY LAST SEARCH QUERY':'Youre last search query was '+lastQuery,
    'THANK YOU':'My Pleasure Sir',
    'WHAT DO YOU LIKE':'I like serving you Sir.',
    'I AM FINE TOO':'GLAD TO HEAR THAT SIR',
    'BYE':'Bye Sir',
    'YES':'Thats cool sir',
    'YES I DID':'Thats cool sir',
    'GOODNIGHT':'Goodnight sir'
    
}

def numb_guess():
    randAns=np.random.randint(10)
    print (randAns)
    bot_speech("I got a number between 1-10 in my Bot Mind. Can you guess that number sir?")
    userGuess=input("Guess the number sir")
    life=3
    winCheck=True
    while (int(userGuess)!=randAns):
        if (int(userGuess)>randAns):
            print("HIGH")
            bot_speech("You got it a bit high sir")
        else:
            print("LOW")
            bot_speech("You got it a bit low sir")
        life=life-1
        print("LIFE REMAINING:"+str(life))
        userGuess=input("Try Again Sir")
        if life<=0:
            print("Sorry you lose")
            bot_speech("Sorry you lost. This is my first domination against human. Haha Just kidding.")
            winCheck=False
            break
    if (winCheck==True):
        print("Perfectly Guessed")
        bot_speech("oh wow! you guessed it right sir")
    else:
        print("You lost all the Life")

    

def send_Mail(reciever,content):
    user_cred = open("user_credentials.txt",'r')
    userCreds = user_cred.readlines()
    email = userCreds[0]
    password = userCreds[1]
    print(email,password)
    try:
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        print("Sending Mail.....Please wait")
        bot_speech('Sending Mail. Please wait sir.')
        mail.sendmail(email,reciever,content)
        mail.close()
        return "1 Mail Sent Successfully"
    except:
        return "Mail Sending Fail"

    
def weather_update():
    try:
        r = requests.get('http://freegeoip.net/json')
        j = json.loads(r.text)
        lat = j['latitude']
        long = j['longitude']
        print(lat,long)
        weather = Weather(Unit.CELSIUS)
        lookup = weather.lookup_by_latlng(lat,long)
        condition = lookup.condition
        weatherCondition = condition.text
        print(weatherCondition)
        return weatherCondition
    except:
        return "There seems to be a little problem getting the weather update sir"

def get_distance(req_location):
    try:
        r = requests.get('http://freegeoip.net/json')
        j = json.loads(r.text)
        lat = j['latitude']
        long = j['longitude']
        print(lat,long)
        geolocator = Nominatim()
        location = geolocator.geocode(req_location)
        print(location.latitude)
        print(location.longitude)
        req_coord = (location.latitude,location.longitude)
        user_coord = (lat,long)
        fetched_dist = vincenty(req_coord,user_coord).kilometers
        print(fetched_dist)
        return fetched_dist
    except:
        return "There seems to be a little problem identifying your location sir"

def get_location():
    try:
        r = requests.get('http://freegeoip.net/json')
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        print(lat,lon)
        geolocator = Nominatim()
        location = geolocator.reverse(str(lat)+", "+str(lon))
        current_location = location.address
        print(current_location)
        return current_location
    except:
        return "There seems to be a little problem identifying your location sir"
    
    
def add_userLike(newLike):
    usersLike=open('user_like.txt','a')
    usersLike.write("\n"+newLike)
    
def user_rename(new_name):
    username_file =  open('username.txt','w')
    username_file.write(new_name.lower())
    user_name=new_name
    response['WHAT IS MY NAME']='You are '+user_name
    response['HELLO']='You are '+user_name
    response['HI']='Hi there '+user_name

def google_search(u_query):
    print ("Search Query:"+u_query)
    write_history=open('old_queries.txt','a')
    write_history.write(u_query.lower()+'\n')
    write_history.close()
    lastQuery = u_query
    response['WHAT WAS MY LAST SEARCH QUERY']='Youre last search query was '+lastQuery
    webbrowser.open('https://www.google.com.np/search?q='+u_query) 

def bot_speech(response):
    engine.say(response)
    engine.runAndWait()
    

def respond(user_command):
    if(user_command in response):
        return response[user_command]
    
    elif("SEARCH" in user_command):
        user_query = user_command.split("SEARCH",2)
        uquery=user_query[1]
        google_search(uquery)
        return "Searching. Look what I have found sir:"
    
    elif("FIND" in user_command):
        user_query = user_command.split("FIND",2)
        uquery=user_query[1]
        google_search(uquery)
        return "Searching. Look what I have found sir:"
    
    elif("CALL ME" in user_command):
        Mnew_name = user_command.split("CALL ME ")[1]
        print(Mnew_name+"<<<<")
        user_rename(Mnew_name)
        return "Ok I will call you "+Mnew_name
    
    elif("MY NAME IS" in user_command):
        Mnew_name = user_command.split("MY NAME IS ")[1]
        print(Mnew_name+"<<<<")
        user_rename(Mnew_name)
        return "Ok I will call you "+Mnew_name
        
    elif("DO I LIKE" in user_command):
        like_query =  user_command.split("DO I LIKE ")[1]
        all_likes=open('user_like.txt','r').readlines()
        if(like_query in all_likes):
            print("You do like "+like_query+" Sir")
            return "You do like "+like_query+" Sir"
        else:
            print("I dont thik you like "+like_query+" Sir")
            return "I dont think you like "+like_query+" Sir"
        
    elif("I LIKE" in user_command):
        new_like = user_command.split("I LIKE ")[1]
        add_userLike(new_like)
        return "I'll remember that sir"
    
    elif("WHO IS" in user_command):
        search_query=user_command.split("WHO IS ")[1]
        google_search(search_query)
        return " I have found results about "+search_query+" online."
    
    elif("WHAT IS" in user_command):
        search_query=user_command.split("WHAT IS ")[1]
        google_search(search_query)
        return " I have found results about "+search_query+" online."
    
    elif("WHERE IS" in user_command):
        search_query=user_command.split("WHERE IS ")[1]
        google_search(search_query)
        return " I have found results about "+search_query+" online."
    
    elif("WHERE AM I" in user_command):
        getStreet = get_location()
        return "Your current position has been identified as "+getStreet
    
    elif("HOW FAR IS" in user_command):
        req_location = user_command.split("HOW FAR IS ")[1]
        getDistance = get_distance(req_location)
        return str(req_location).lower()+" is " + str(int(getDistance)) + " kilometers far from your current location"
   
    elif("HOW IS THE WEATHER" in user_command):
        getWeather = weather_update()
        return "The weather seems "+getWeather+" sir."
    
    elif("SEND MAIL" in user_command):
        bot_speech("Please input the email of the reciever Sir")
        ask_email = input("Email of the reciever:")
        bot_speech("Please input the contents of the Email Sir")
        ask_content = input("Content:")
        mail_send_status = send_Mail(ask_email,ask_content)
        return mail_send_status
    
    elif("LET'S PLAY GAMES" in user_command):
        numb_guess()
        return "Did you enjoy the game sir?"
        
    
    else:
        return "Oh Ok sir"
    
    
def rec_speech():     
    with sr.Microphone() as source:  
        print("Please wait. Calibrating microphone...")  
        recognize.adjust_for_ambient_noise(source, duration=1)  
        print("Say something!")  
        audio = recognize.listen(source) 
    try:  
        users_command=recognize.recognize_google(audio)
        print(users_command)
        return users_command
    except:
        print('There seems to be a little problem recognizing your voice Sir.')
        engine.say('There seems to be a little problem recognizing your voice Sir.')
        engine.runAndWait()


while(command!='exit' and command!="bye" and command!="good night" and command!="car"):
    command = rec_speech()
    if(command is not None):
        get_response = respond(command.upper())
        print(get_response)
        bot_speech(get_response)
        