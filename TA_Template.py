import pygame
pygame.init() 

#Create variables for storing car x and y location


screen = pygame.display.set_mode((600,600))
pygame.display.set_caption(" Racing Game")
carryOn = True
while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False
                  
    #Change location of background image according to the absolute path you have got in your computer
    bgImg_location= "C:/Users/dell/Documents/img/back_ground.jpg" 
    
    bgImg=pygame.image.load(bgImg_location).convert_alpha()
    bgImg_scaled=pygame.transform.smoothscale(bgImg,(600,600))
    screen.blit(bgImg_scaled,[0,0])
    
    #Change location of background image according to the absolute path you have got in your computer
    carImg_location="C:/Users/dell/Documents/img/car.png"
    
    carImg=pygame.image.load(carImg_location).convert_alpha()
    #Encode for user input
    
    
    
    
    pygame.display.flip()
    
pygame.quit()
