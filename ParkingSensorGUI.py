import pygame, sys

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
    #dist = sensor1()
    dist = 87

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
    #dist = sensor2()
    dist = 30

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
    # s3 = sensor3()
    # s4 = sensor4()
    #
    # dist = (s3 + s4)/2

    dist = 23

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
    # s4 = sensor4()
    # s5 = sensor5()
    #
    # dist = (s4 + s5)/2

    dist = 23

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
    # s5 = sensor5()
    # s6 = sensor6()
    #
    # dist = (s5 + s6)/2

    dist = 23

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

def main_screen():
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
        mainClock.tick(60)

        #sets background of screen to white using RGB
        screen.fill((255,255,255))
        #background image
        screen.blit(background, (160, 0))
        # car image
        screen.blit(supra,(317, 50))
        # display rectangles
        createLF()
        createRF()
        createLB()
        createMB()
        createRB()


# call screen function to display when code is run

main_screen()
