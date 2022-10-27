import pyttsx3 as p
import speech_recognition as sr
import datetime
import wikipedia as wiki
import webbrowser as wb

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.energy_threshold = 5000
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("You said: ", query)
          
    except Exception as e:
        print(e)
        print("Please, say that again .")
        return "None"
    
    return query


def speak(audio):
    engine = p.init()
    voices= engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(audio)
    engine.runAndWait()

 
def hello():
    speak("Hello, thankyou for coming to our shop if you have any concern free to ask me.")

def intro_self():
    speak("We are group 3, Your digital assistant at your service")

def how_much():
    speak("It's about 550,100 pesos. And of course it comes with a discount  if you'll instantly pay cash we'll give you a 15% discount.")
    
def machine():
    speak(" It's a low cost noise that you won't wake anyone if you'd wanted to leave in secret.")

def gas_use():
    speak("It uses bio-diesel, it may be a little bit more expensive than the others but it's high in lubricity that doesn't wear off the engine and of coursea little friendly to our environment.")
    
def warranty():
    speak(" We'll give you a 3 years warranty for investment and a 6 years warranty for a cash payment. You can contact us anytime if you need our service.")
    
def strong():
    speak("AC power a something that you'll love that can also make your hot coffee cold and will give a comfortable chill while driving.")    
    
def sport_car():
    speak("We have  Mazda MX-5, Porsche Taycan, BMW M3,Porsche 911,Nissan GT-RLexus LC Convertible, BMW M5.")  
    
def qualities_car():
    speak("The  car are safe, fast, affordable to purchase, economical to operate, reliable, capacious, comfortable, and attractive. ")     
    
def features():
    speak("A sports car's main emphasis is on performance by superior road holding, braking, maneuverability, low weight and power rather than comfort, passenger space, and econom") 
    
def special_about():
    speak("A sports car is a car designed with an emphasis on dynamic performance, such as handling,acceleration, top speed, the thrill of driving and racing capability.")
    
def most_comportable():
    speak(" If you're looking for the most comfortable seats in the sports car category look no further than the Nissan GT-R. This car puts comfort first, which is even more impressive when you consider that it is known for its performance on the track.")
             
def tell_day():
    day=datetime.datetime.today().weekday()+1
    Day_dict={ 1:'Monday', 2:'tuesday',3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week=Day_dict[day]
        print(day_of_the_week)
        speak("The say is" + day_of_the_week)


def give_info():
    speak("what informnation do you want?")
    query=take_command().lower()

    try:
        result=wiki.summary(query,sentences=2)
        speak("According to Wikipedia")
        print(result)
        speak(result)

    except Exception as e:
        print(e)
        print("Sorry, error found reading the topic. ")

def take_query():
    hello()
    while(True):
        query=take_command().lower()
        if "day" and "today" in query:
            tell_day()
            continue
        elif "open google" in query:
            speak("opening google")
            wb.open("www.google.com")
            speak("is there anything you want?")
            continue
        elif "your name" and "who are you" in query:
            intro_self()
            continue
        elif "how" and "much" in query:
            how_much()
            continue
        elif "machine" in query:
            machine()
            continue
        elif "gas" and "use" in query:
            gas_use()
            continue
        elif "warranty" in query:
            warranty()
            continue
        elif "strong" in query:
            strong()
            continue
        elif "sport" and "car" in query:
            sport_car()
            continue
        elif "qualities" and "car" in query:
            qualities_car()
            continue
        elif "features" in query:
            features()
            continue
        elif "special" and "about" in query:
             special_about()
             continue
        elif "most" and "comportable" in query:
            most_comportable()
            continue
        elif "stop" and "exit" and "nothing" in query:
            speak("Thank you and have a nice day.")
            exit()
        elif "information" in query:
            query = query.replace("information", "")
            give_info()
            speak("is there anything you want to know about are business?")
            continue
        else:
            speak("sorry, thats an unrecognized command")
            continue

if __name__ == '__main__':
         query = ""
         take_query()
            
       
    
        
             
    
            

