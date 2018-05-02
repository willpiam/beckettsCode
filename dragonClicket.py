""" 
Program name:FinalProjectBeckett.py or .exe 
Creator:Beckett Smith 
Date Started:May 25 
Date finished:June 9 
help from: stackexchange, my old programs and many other small websites 
Description:this program, dragon fruit clicker not to be confused with the popular 
cookie clicker is where the player repeatedly clicks on the dragon fruit to get 
dragon fruits. The player can then spend their fruits on various other items in the shop. 
there is not a way to win at this game however they can save their progress and return 
later. 
what this program demonstrates 
the ability to use pygame to create a window 
the ability to use pygame to draw different images to the screen 
the ability to use pygame to get the players mouse position and do different things acordingly 
the ability to use varibles and write those variables to the screen 
the ability to declare which type a variable is 
the ability to make subrutines and call upon them  
""" 
 
 
import pygame#imports the libraries needed for the program 
import time 
import sys 
 
pygame.init() #starts pygame and the font engine 
pygame.font.init() 
 
myfont = pygame.font.SysFont('Microsoft Sans Serif', 15) #decares the font for the label of the cookies 
 
gamerunning=True #getting the loops to run at the right time 
updatescore=False 
 
cookies=0#declares the amount of resouces the player has 
becketts=False 
davids=False 
floyds=False 
sarki=False #is it sarkiss, sarkisus, sarkises or sarki 
williams=False 
 
becketts_num=0 
davids_num=0 
floyds_num=0 
sarki_num=0 #is it sarkiss, sarkisus, sarkises or sarki 
williams_num=0 
 
 
def menu():#defines the menu subroutine 
    print "welcome to dragonfruit clicker(not to be confused with cookie clicker)"#greets the user and prompts them to continue 
    print"to continue please type the word continue" 
    menucontinue=str(raw_input()) 
    if menucontinue== "c" or "Continue":#gets the user's input and compares it 
        display = pygame.display.set_mode((700,700))# set the program window to be 700 by 700 pixels 
        pygame.display.set_mode((700,700))# creates the 700x700 window 
         
        background_image = pygame.image.load("dragonfruit.jpg").convert()#loads the background image 
        display.blit(background_image, [0, 0])#places the image on the screen 
 
 
        beckett_shop = pygame.image.load("berket_icon.jpg").convert()#these name_icon images are the items you can buy 
        david_shop = pygame.image.load("david_icon.jpg").convert()             
        floyd_shop = pygame.image.load("floyd_icon.jpg").convert() 
        sarkis_shop = pygame.image.load("sarkis_icon.jpg").convert() 
        william_shop = pygame.image.load("william_icon.jpg").convert() 
        quit_icon = pygame.image.load("quit_icon.jpg").convert() 
        display.blit(beckett_shop, [0, 600])#placing all the shop images on screen 
        display.blit(david_shop, [100, 600]) 
        display.blit(floyd_shop, [200, 600]) 
        display.blit(sarkis_shop, [300, 600]) 
        display.blit(william_shop, [400, 600]) 
        display.blit(quit_icon, [500, 600]) 
         
        plrscore = myfont.render("cookies: " + str(cookies), 1, (0,0,0))#declaring the label, will be updated on mouse click 
        display.blit(plrscore, (0, 0))#placing the label on screen 
        pygame.display.update()#updates the display so that the user can see the image 
         
        gamerunning=True#changing variables to get the correct peices running 
        updatescore=True 
 
menu()#runs the menu subroutine 
 
while updatescore: #this loop constanly updates your score, a separate loop is needed because pygame will constalytry to draw over the score 
        plrscore = myfont.render("cookies: " + str(cookies), 1, (0,0,0)) 
        display.blit(plrscore, (0, 0)) 
        pygame.display.update() 
while gamerunning: #the main game loop 
 
    ev = pygame.event.get() #pygame.event.get is the way to get the user input with the GUI aswell we are giving it a variable to call upon 
    for event in ev: 
 
        if event.type == pygame.MOUSEMOTION:#setting to mouse position, the mousemotion command is basicly constanly tracking the players location  
            x, y = event.pos #also must be done before the mouse click because if it is in the mousebuttondown code then it would not work 
            print x 
            print y 
             
        elif event.type == pygame.MOUSEBUTTONDOWN:#when the mousebutton is down do this part of code 
            display = pygame.display.set_mode((700,700)) #these lines of code are called upon again so that they will not get drawn over 
            pygame.display.set_mode((700,700)) 
 
            background_image = pygame.image.load("dragonfruit.jpg").convert() 
            display.blit(background_image, [0, 0]) 
            beckett_shop = pygame.image.load("berket_icon.jpg").convert() 
            david_shop = pygame.image.load("david_icon.jpg").convert()             
            floyd_shop = pygame.image.load("floyd_icon.jpg").convert() 
            sarkis_shop = pygame.image.load("sarkis_icon.jpg").convert() 
            william_shop = pygame.image.load("william_icon.jpg").convert() 
            quit_icon = pygame.image.load("quit_icon.jpg").convert() 
            display.blit(beckett_shop, [0, 600]) 
            display.blit(david_shop, [100, 600]) 
            display.blit(floyd_shop, [200, 600]) 
            display.blit(sarkis_shop, [300, 600]) 
            display.blit(william_shop, [400, 600]) 
            display.blit(quit_icon, [500, 600]) 
             
            pygame.display.update()#updates the display so that the user can see the image 
            plrscore = myfont.render("cookies: " + str(cookies), 1, (0,0,0)) 
            display.blit(plrscore, (0, 0)) 
            pygame.display.update() 
            if y<601:# these next lines of code check for the position of the mouse cursor and do certain action depending on the mouse's position 
                cookies = cookies + 1 + becketts_num + davids_num + floyds_num + sarki_num + williams_num#the user will always get at least one cookie per click the "name"_num is just a vale that is explained below 
                print cookies 
            elif y>600 and x<=100 and cookies>=100:# the rest of the code is checking of the user already owns the upgrades 
                if becketts==False:#will make the variable becketts true  
                    cookies=cookies-100 #will remove the set amount of cookies from the user's reserves 
                    becketts=True #sets becketts to true so that you can't buy becketts again 
                    becketts_num=1 #this number is the bonus cookies thta you get per click it changes based on the upgrage 
                else:#if the user already owns becketts 
                    print "you already own beckett" 
 
            elif y>600 and x<=200 and x>=100 and cookies>=250: 
                if davids==False: 
                    cookies=cookies-250 
                    davids=True 
                    davids_num=2 
                else: 
                    print "you already own david" 
            elif y>600 and x<=300 and x>=200 and cookies>=500: 
                if floyds==False: 
                    cookies=cookies-500 
                    floyds=True 
                    floyds_num=3 
                else: 
                    print"you already own floyd" 
            elif y>600 and x<=400 and x>=300 and cookies>=750: 
                if sarki==False: 
                    cookies-cookies-750 
                    sarki=True 
                    sarki_num=4 
                else: 
                    print "you already own sarkis" 
            elif y>600 and x<=500 and x>=400 and cookies>=1000: 
                if williams==False: 
                    cookies=cookies-1000 
                    williams=True 
                    williams_num=5 
                else: 
                    print "you already own william" 
            elif y>600 and x<=700 and x>500: 
                sys.exit()#this checks for the user clicking on the quit button so that the program can exit normally 
 
 
 
