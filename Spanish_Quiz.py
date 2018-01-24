#Link to website : http://rdominguez.pythonanywhere.com/quizzes/confirmation/8/31#
#Login needed!
#Imports

import config
import requests
import re
from robobrowser import RoboBrowser
import urllib.request
import urllib.parse

#Lists
questions=config.questions
answers=config.answers
#Getting the HTML

Times = int( input("HOW MANY TIMES WOULD YOU LIKE TO RUN THE PROGRAM? "))

a = Times
print("<======================BEGIN====================>")
while  a >0:

    print(str(a) + " Times Remaining")
    s = requests.Session()
    s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36" 
    br = RoboBrowser(session = s, history =True,parser='html.parser')
    br.open("http://rdominguez.pythonanywhere.com/login")
    login_form = br.get_form()
    login_form["email"]= "config.username"
    login_form["password"]="config.password"
    br.submit_form(login_form)


    #GET TO THE QUIZ
    br.open("http://rdominguez.pythonanywhere.com/quizzes/confirmation/8/31#")
    confirmation_form= br.get_form()
    confirmation_form["on_or_off"].value=["y"]
    br.submit_form(confirmation_form)
    question_link = br.get_link("Let's Play Siglo XV!")
    br.follow_link(question_link)
    #FIND THE QUESTION

    i = 20
    while i>0:
        print("Number "+str(i))
        src = str(br.parsed())
        start1 ="¿"
        end1 = "?<"
        result = re.search('%s(.*)%s' % (start1,end1), src).group(1) 
        print(str(result))
        question_index=questions.index(result)
        print("The answer is " + answers[question_index])
        question_form = br.get_form()
        question_form["user_answer"]=answers[question_index]
        br.submit_form(question_form)
        i=i-1 
    print("<=============END OF QUIZ==============>")
    a=a-1
print("You earned "+str(Times*20) +" points!")
print("Success! You are free now!")
