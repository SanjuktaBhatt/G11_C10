import pygame
pygame.init() 

#Create variables for storing car x and y location
carx=130
cary=500
#create background variable


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
    bgImg_scaled=pygame.transform.smoothscale(bgImg,(600,800))
    screen.blit(bgImg_scaled,[0,0])
    
    #Change location of background image according to the absolute path you have got in your computer
    carImg_location="C:/Users/dell/Documents/img/car.png"
    
    carImg=pygame.image.load(carImg_location).convert_alpha()
    #Encode for user input
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_UP:
        #decrement background
        
          cary-=2
      if event.key==pygame.K_DOWN:
        #increment background 
        
          cary+=2
      if event.key==pygame.K_LEFT:
          carx-=10
      if event.key==pygame.K_RIGHT:
          carx+=10
    screen.blit(carImg,[carx,cary])
    #reset car and screen
    
    
    pygame.display.flip()
    
pygame.quit()
