# pyAssistant

Interactive Voice Controlled Assistant BOT


The Python Assistant is dependent upon following Libraries
-------------------------------------------------------------
1> Google Speech Recognition
2> Webbrowser
3> GeoPy
4> Weather-api
5> NumPy
6> Pyttsx


The interactions given by the Bot can be furthur added by modifying the Dictionary

Default dictionary is given as:
---------------------------------
response ={<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'HI':'Hello there '+user_name,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'HELLO':'Hello there '+user_name,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'WHAT IS YOUR NAME':'You can call me NepBot Sir',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'HOW OLD ARE YOU':'Haha I cant really tell you sir',        
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'I HATE YOU':'Sorry sir! But I work the best I can',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'HOW ARE YOU':'Im fine sir and you',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'I LOVE YOU':'Haha I am just a Bot. I have no feelings.',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'YOU ARE AWESOME':'Thank you Sir. I feel honoured.',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'NAMASTE':'NAMASTE Sir',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'WHAT IS MY NAME':'You are '+user_name,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'WHAT WAS MY LAST SEARCH QUERY':'Youre last search query was '+lastQuery,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'THANK YOU':'My Pleasure Sir',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'WHAT DO YOU LIKE':'I like serving you Sir.',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'I AM FINE TOO':'GLAD TO HEAR THAT SIR',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'BYE':'Bye Sir',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'YES':'Thats cool sir',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'YES I DID':'Thats cool sir',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'GOODNIGHT':'Goodnight sir'<br>
}


I have added numerous actions that this Bot can perform

ACTIONS
------------
WHERE AM I: Gives your current location<br>
SEND MAIL: Send mail to someone<br>
HOW IS THE WEATHER: Gives the weather condition of current location<br>
HOW FAR IS (someplace): Calculates distance between your current position and the required place<br>
SEARCH (query here): Make a quick google search<br>
FIND (query here): Make a quick google search<br>
LET'S PLAY GAMES: A simple number guessing game<br>
CALL ME (your_name): Change your name. The bot calls you using this name.<br>
MY NAME IS (your_name): Change your name. The bot calls you using this name.<br>
I LIKE (something_you_like): By doing this the Bot records what you like.<br>
DO I LIKE (something_i_like): Aks the bot if you like something or not. The bot uses previous record.<br>
WHO IS (someone): Make a quick google search on someone.<br>
WHERE IS (place): Make a quick google search on some place.<br>
WHAT IS (something): Make a quick google search on some place.<br>
