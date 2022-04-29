import pygame, sys

import RPi.GPIO as GPIO
import time
#set gpio pin numbering
GPIO.setmode(GPIO.BCM)


    
        

#set up pygame window
mainClock = pygame.time.Clock()
from pygame.locals import *
#initiate pygame
pygame.init()
#name of window
pygame.display.set_caption('SensorGUI')
#window size
screen = pygame.display.set_mode((800,480))
#font type
font = pygame.font.SysFont(None, 20)

#load background image
background = pygame.image.load('background.png')
#load car image
supra = pygame.image.load('topSupra.png')

#define colours
green = pygame.color.Color(0, 190, 0)
orange = pygame.color.Color(255, 153, 51)
red = pygame.color.Color(255, 0, 0)
grey = pygame.color.Color(192, 192, 192)
white = pygame.color.Color(255, 255, 255)

class button():
    
    clicked = 1
    #function to set up button object
    def __init__(self, color, x,y,width,height, text= ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    #method to draw button on screen
    def draw(self, win, outline = None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    #method to check if mouse position is over the button
    def isOver(self, pos):
        #pos is the mouse position
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


def sensor1():
    #define trig and echo pins on gpio
    TRIG = 15
    ECHO = 14
    #set up input/output pins
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    #set trig to low after 0.01 ms
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    #save time that pulse went out
    while GPIO.input(ECHO)==0:
        pulseStart = time.time()
        
    #save time that pulse was received
    while GPIO.input(ECHO)==1:
        pulseEnd = time.time()
    try:
        #calculate length of pulse
        pulse = pulseEnd - pulseStart
    except UnboundLocalError:
        pass
    
    #calculate distance from pulse
    distance = pulse * 17150
    
    
    distance = round(distance, 2)
    
    return distance


def sensor2():
    
    #define trig and echo pins on gpio
    TRIG = 23
    ECHO = 18
    #set up input/output pins
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    #set trig to low after 0.01 ms
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    #save time that pulse went out
    while GPIO.input(ECHO)==0:
        pulseStart = time.time()
        
    #save time that pulse was received
    while GPIO.input(ECHO)==1:
        pulseEnd = time.time()
    try:
        #calculate length of pulse
        pulse = pulseEnd - pulseStart
    except UnboundLocalError:
        pass

    #calculate distance from pulse
    distance = pulse * 17150
    
    
    distance = round(distance, 2)
    
    return distance
    

def sensor3():
    #define trig and echo pins on gpio
    TRIG = 25
    ECHO = 24
    #set up input/output pins
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    #set trig to low after 0.01 ms
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    #save time that pulse went out
    while GPIO.input(ECHO)==0:
        pulseStart = time.time()
        
    #save time that pulse was received
    while GPIO.input(ECHO)==1:
        pulseEnd = time.time()
    
    try:
        #calculate length of pulse
        pulse = pulseEnd - pulseStart
    except UnboundLocalError:
        pass
    
    #calculate distance from pulse
    distance = pulse * 17150
    
    
    distance = round(distance, 2)
    
    return distance


def sensor4():
    #define trig and echo pins on gpio
    TRIG = 7
    ECHO = 8
    #set up input/output pins
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    #set trig to low after 0.01 ms
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    #save time that pulse went out
    while GPIO.input(ECHO)==0:
        pulseStart = time.time()
        
    #save time that pulse was received
    while GPIO.input(ECHO)==1:
        pulseEnd = time.time()
    
    try:
        #calculate length of pulse
        pulse = pulseEnd - pulseStart
    except UnboundLocalError:
        pass
    
    #calculate distance from pulse
    distance = pulse * 17150
    
    
    distance = round(distance, 2)
    
    return distance




def sensor5():
    #define trig and echo pins on gpio
    TRIG = 19
    ECHO = 26
    #set up input/output pins
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    #set trig to low after 0.01 ms
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    #save time that pulse went out
    while GPIO.input(ECHO)==0:
        pulseStart = time.time()
        
    #save time that pulse was received
    while GPIO.input(ECHO)==1:
        pulseEnd = time.time()
    
    try:
        #calculate length of pulse
        pulse = pulseEnd - pulseStart
    except UnboundLocalError:
        pass
    
    #calculate distance from pulse
    distance = pulse * 17150
    
    
    distance = round(distance, 2)
    
    return distance

def sensor6():
    #define trig and echo pins on gpio
    TRIG = 5
    ECHO = 6
    #set up input/output pins
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    #set trig to low after 0.01 ms
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    #save time that pulse went out
    while GPIO.input(ECHO)==0:
        pulseStart = time.time()
        
    #save time that pulse was received
    while GPIO.input(ECHO)==1:
        pulseEnd = time.time()
    
    try:
        #calculate length of pulse
        pulse = pulseEnd - pulseStart
    except UnboundLocalError:
        pass
    
    #calculate distance from pulse
    distance = pulse * 17150
    
    
    distance = round(distance, 2)
    
    return distance


def createLF():

    #set angle of rotation
    angle = 192
    #create lf1
    lf1 = pygame.Surface((60,10), pygame.SRCALPHA)
    #create lf2
    lf2 = pygame.Surface((70,10), pygame.SRCALPHA)
    #create lf3
    lf3 = pygame.Surface((80,10), pygame.SRCALPHA)

    #set distance equal to distance recorded from sensor on front left of vehicle
    dist = sensor1()
    #dist = 87

    if dist <= 25:
        lf1.fill(red)
        lf2.fill(orange)
        lf3.fill(green)
    elif 25 < dist <= 60:
        lf1.fill(white)
        lf2.fill(orange)
        lf3.fill(green)
    elif 60 < dist <= 90:
        lf1.fill(white)
        lf2.fill(white)
        lf3.fill(green)
    else:
        lf1.fill(white)
        lf2.fill(white)
        lf3.fill(white)

    #rotate each  rectangle
    lf1 = pygame.transform.rotate(lf1, angle)
    lf2 = pygame.transform.rotate(lf2, angle)
    lf3 = pygame.transform.rotate(lf3, angle)
    #display each rectangle
    screen.blit(lf1, (320, 65))
    screen.blit(lf2, (312, 45))
    screen.blit(lf3, (302, 25))





def createRF():

    #set angle of rotation
    angle = 172
    #create rf1
    rf1 = pygame.Surface((60,10), pygame.SRCALPHA)
    #create rf2
    rf2 = pygame.Surface((70,10), pygame.SRCALPHA)
    #create rf3
    rf3 = pygame.Surface((80,10), pygame.SRCALPHA)
    #set distance equal to distance recorded from sensor on front right of vehicle
    dist = sensor2()
    #dist = 30

    if dist <= 25:
        rf1.fill(red)
        rf2.fill(orange)
        rf3.fill(green)
    elif 25 < dist <= 60:
        rf1.fill(white)
        rf2.fill(orange)
        rf3.fill(green)
    elif 60 < dist <= 90:
        rf1.fill(white)
        rf2.fill(white)
        rf3.fill(green)
    else:
        rf1.fill(white)
        rf2.fill(white)
        rf3.fill(white)
    #rotate and display each rectangle
    rf1 = pygame.transform.rotate(rf1, angle)
    screen.blit(rf1, (420, 65))
    rf2 = pygame.transform.rotate(rf2, angle)
    screen.blit(rf2, (417, 45))
    rf3 = pygame.transform.rotate(rf3, angle)
    screen.blit(rf3, (415, 25))


def createLB():

    #set angle of rotation
    angle = 172
    #create lb1
    lb1 = pygame.Surface((60,10), pygame.SRCALPHA)
    #create lb2
    lb2 = pygame.Surface((70,10), pygame.SRCALPHA)
    #create lb3
    lb3 = pygame.Surface((80,10), pygame.SRCALPHA)

#    set distance equal to average distance recorded from sensor on back left and mid - left
    s3 = sensor3()
    s4 = sensor4()
    #
    dist = (s3 + s4)/2

    #dist = 23

    if dist <= 25:
        lb1.fill(red)
        lb2.fill(orange)
        lb3.fill(green)
    elif 25 < dist <= 60:
        lb1.fill(white)
        lb2.fill(orange)
        lb3.fill(green)
    elif 60 < dist <= 90:
        lb1.fill(white)
        lb2.fill(white)
        lb3.fill(green)
    else:
        lb1.fill(white)
        lb2.fill(white)
        lb3.fill(white)

    #rotate and display rectangles
    lb1 = pygame.transform.rotate(lb1, angle)
    screen.blit(lb1, (310, 400))
    lb2 = pygame.transform.rotate(lb2, angle)
    screen.blit(lb2, (297, 425))
    lb3 = pygame.transform.rotate(lb3, angle)
    screen.blit(lb3, (285, 450))



def createMB():
    #create mb1
    mb1 = pygame.Surface((50,10), pygame.SRCALPHA)
    #create mb2
    mb2 = pygame.Surface((60,10), pygame.SRCALPHA)
    #create mb3
    mb3 = pygame.Surface((70,10), pygame.SRCALPHA)

    #set distance equal to the average of distance collected by the two back middle sensors
    s4 = sensor4()
    s5 = sensor5()
    #
    dist = (s4 + s5)/2

    #dist = 23

    if dist <= 25:
        mb1.fill(red)
        mb2.fill(orange)
        mb3.fill(green)
    elif 25 < dist <= 60:
        mb1.fill(white)
        mb2.fill(orange)
        mb3.fill(green)
    elif 60 < dist <= 90:
        mb1.fill(white)
        mb2.fill(white)
        mb3.fill(green)
    else:
        mb1.fill(white)
        mb2.fill(white)
        mb3.fill(white)


    #display rectangles
    screen.blit(mb1, (373, 410))
    screen.blit(mb2, (368, 435))
    screen.blit(mb3, (364, 460))




def createRB():

    #set angle of rotation
    angle = 192
    #create rb1
    rb1 = pygame.Surface((60,10), pygame.SRCALPHA)
    #create rb2
    rb2 = pygame.Surface((70,10), pygame.SRCALPHA)
    #create rb3
    rb3 = pygame.Surface((80,10), pygame.SRCALPHA)

    #set distance equal to average of that recorded by sensor on back mid- right and back right
    s5 = sensor5()
    s6 = sensor6()
    #
    dist = (s5 + s6)/2

    #dist = 23

    if dist <= 25:
        rb1.fill(red)
        rb2.fill(orange)
        rb3.fill(green)
    elif 25 < dist <= 60:
        rb1.fill(white)
        rb2.fill(orange)
        rb3.fill(green)
    elif 60 < dist <= 90:
        rb1.fill(white)
        rb2.fill(white)
        rb3.fill(green)
    else:
        rb1.fill(white)
        rb2.fill(white)
        rb3.fill(white)

    #set rotation and display all rectangles
    rb1 = pygame.transform.rotate(rb1, angle)
    screen.blit(rb1, (426, 397))
    rb2 = pygame.transform.rotate(rb2, angle)
    screen.blit(rb2, (429, 420))
    rb3 = pygame.transform.rotate(rb3, angle)
    screen.blit(rb3, (433, 445))
    

    

parkingButton = button((0,255,0), 15, 390, 150, 75, 'Parking On')



def main_screen():
    sensing = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
        mainClock.tick(20)
        

        #sets background of screen to white using RGB
        screen.fill((255,255,255))
        #background image
        screen.blit(background, (160, 0))
        # car image
        screen.blit(supra,(317, 50))
        
        
        
        #parkingButton.draw(screen, (0,0,0))
        
        pos = pygame.mouse.get_pos()
        
        

        if event.type == pygame.MOUSEBUTTONUP:
            parkingButton.color = (0,255,0)
            parkingButton.text = 'Parking On'
            sensing = True

                
        if event.type == pygame.MOUSEBUTTONUP and parkingButton.isOver(pos):

            parkingButton.color = (255,0,0)
            parkingButton.text = 'Parking Off'
            sensing = False


        
        parkingButton.draw(screen, (0,0,0))
        
        
        
        
                
        
        
        if sensing:
            # display rectangles
            createLF()
            createRF()
            createLB()
            createMB()
            createRB()


# call screen function to display when code is run

main_screen()
GPIO.cleanup()