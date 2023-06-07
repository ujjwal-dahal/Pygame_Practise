# Importing the library
import pygame


# Initializing Pygame
pygame.init()


#Game Variable
screen_width=800
screen_height=450
rect_width=100
rect_height=100
FPS=50

#initilizing color --> range from 0 to 255 ---> RGB

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)



# Initializing surface
screen = pygame.display.set_mode((screen_width,screen_height))
title= pygame.display.set_caption("HellO UjjwaL")

'''
To set the FPS (frames per second) of a Pygame game, you can use the 'pygame.time.Clock()' object to create
a clock object, and then use the 'tick()' method of the clock object to set the maximum FPS for your game loop.
'''
clock=pygame.time.Clock()


"""
To fill an image onto a Pygame screen, you need to first load the image into memory using the "pygame.image.load()" 
function. Then, you can use the "screen.blit()" function to draw the image onto the screen.
"""

# image=pygame.image.load("snake_game.png")


'''
the "pygame.transform.scale()" function is used to scale the image to match the size of the screen. 
The 'screen_width' and 'screen_height' variables are used as the dimensions of the scaled image. 
Once the image is scaled, it is filled onto the screen using the "screen.blit()" function.

'''
# image_size=pygame.transform.scale(image,(screen_width,screen_height))


'''
Set the font and size of the text.

The None argument le chai Pygame ko default font use garcha, and
 35 specifies the font size.
'''
# font=pygame.font.Font(None,35)

#Afnai Font use garna

font=pygame.font.Font("font/SuperMario256.ttf",35)


'''
Create a surface object containing the rendered text.

The first argument specifies the text to render, 
the second argument specifies whether or not to use anti-aliasing (smoothing), 
and the third argument specifies the color of the text.
'''

text_surface=font.render("My GamE",False,'black')
text_surf_rect=text_surface.get_rect(center=(400,50))

"""
--> Creating Text <---

1. Create a font (text style and size)

2. Write text on a surface 

3. blit the text surface

"""


'''
Surfaces can be created in different ways, such as by loading an image file using 'pygame.image.load()', 
or by creating an empty surface with a specified width and height using 'pygame.Surface((width, height))'.

'''
# image_surface=pygame.Surface((130,30))  
# image_surface.fill(white)


sky_surface=pygame.image.load("sky.png")#.convert()
#convert() function --> converts image that pygame can work easily and game is going run faster
ground_surface=pygame.image.load("ground.png")#.convert()

snail_surface=pygame.image.load("snail1.png")#.convert_alpha()
#convert_alpha(), which is used to convert an image with transparency
snail_x_pos=300
snail_y_pos=300


player_surface=(pygame.image.load("player_walk_1.png"))
player_surface_size=pygame.transform.scale(player_surface,(50,60))

player_rect=player_surface_size.get_rect(midbottom=(500,300))
snail_rect=snail_surface.get_rect(midbottom=(snail_x_pos,snail_y_pos))

score_text=pygame.font.Font(None,35)


player_gravity=0  

game_active=True

game_over=pygame.font.Font(None,150)
game_over_surface=game_over.render("Game Over",True,"black")
game_over_surface_rect=game_over_surface.get_rect(center=(400,225))

#Screen ko surface ma aru k k halnu i.e text,image,color box cha bhane blit() function use garincha


'''
We use rectangle for positioning and collisions but it also use to draw.

'''



def draw_window(i,start_time):
    '''
    'screen.blit()' function is used to fill an image onto the screen.
    'screen.blit()' function is used to fill the images, text, and color boxes onto the screen.

    'pygame.time.Clock()' function creates a clock object that can be used to set the maximum FPS for the game loop.
    'clock.tick()' function sets the maximum FPS for the game loop.

    'pygame.font.Font()' function sets the font and size of the text.
    'font.render()' function creates a surface object containing the rendered text.
    
    '''
    # screen.blit(image_size,(0,0))  #(0,0) chai kun position ma image rakhne ho coordinate system.
    # screen.blit(image_surface,(0,0))


    current_time=pygame.time.get_ticks()//1000 - start_time
    time_surface=score_text.render(f"{current_time}",False,"black")
    time_surface_rect=time_surface.get_rect(center=(700,50))

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))

    '''
    Animation ma lana ko lagi hamile (x,y) ko value change garnu parcha i.e tini haruko position change garnu parcha.
    '''
    

    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface_size,player_rect)

    pygame.draw.rect(screen,'#87CEFA',text_surf_rect)
    screen.blit(text_surface,text_surf_rect)  #blit() function le duita arguments lincha
    #one is Kun surface ma lagaune and another is tesko position.
    
    #pygame.draw.rect(screen,red,(50,50,rect_width,rect_height))  #(x, y, width, height)
    
    score_surface=score_text.render(f"SCORE : {i} ",False,"black")
    score_surface_rect=score_surface.get_rect(topleft=(5,10))
    
    screen.blit(score_surface,score_surface_rect)
    # pygame.draw.line(screen,"gold",(0,0),(800,450),5) #here 5 is thickness
    #pygame.draw.line(ke_ma_banaune,coloue,start_point,end_point)
    screen.blit(time_surface,time_surface_rect)
    pygame.display.update()

"""
In Pygame, '.x' is an attribute that represents the x-coordinate of a rectangle, 
and '.y' represents the y-coordinate of a rectangle.

'.left' and '.right' are attributes that represent the left and right edges of a rectangle, respectively. 

For example, if rect is a rectangle object, then rect.left represents the x-coordinate of the left edge of the rectangle,
and rect.right represents the x-coordinate of the right edge of the rectangle.

"""

def main():
    
    start_time=0
    i=0
    global game_active
    global player_gravity

    clock.tick(FPS) #Game lai kati fps ma chalauna ko lagi pygame.time.Clock.tick() function use garne
    while True:

       
        
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if game_active:
                if event.type==pygame.KEYDOWN: #KEYDOWN le kunai pani key dabiyo ki dabiyena check garcha
                    if event.key == pygame.K_SPACE: #K_SPACE le spacebar click bhayo ki bhaena hercha
                        if player_rect.bottom == 300:
                            player_gravity = -6


                        if player_rect.colliderect(snail_rect)==False:
                            i+=1
            else:
                if event.type==pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE:
                        game_active=True
                        snail_rect.right=800
                        i=0
                        start_time=pygame.time.get_ticks()//1000
                    
                        
                
            
        #event.key le value of the key that was pressed or released on the keyboard during the event.

            
                

            #mouse ko position tha paune event loop ko maddat le

            # if event.type==pygame.MOUSEMOTION:
            #     if player_rect.collidepoint(event.pos): #the event.pos attribute is used to get the x and y coordinates 
            #         #of a mouse or joystick event.
            #         pygame.quit()
            #         quit()

        
        if game_active:    
            snail_rect.x -=2
    #snail_rect.x le snail ko x tira ko coordinate.
    #snail_rect.right bhaneko snail ko right side ko point eddi 0 bhanda kam bhayo bhane 
    # tesko left side lai 800 bata suru garde matlab eddi smail ko position 0 bhayo bhane 800 parde

            if snail_rect.right <=-10:
                snail_rect.left = screen_width


        #if the snail goes off the left edge of the screen, its rectangle will be positioned at the right edge of the screen 
        # (700 pixels from the left edge). 
        

                
            
            # #Basic Animation garna
            # snail_x_pos-=1
            # if snail_x_pos<=-50: #snail ko x position 1 le ghatdai jancha ani eddi -50 bhanda kam bhayo bhane 
            #     #tesko value 800 huncha ani feri ghatdai jancha
            #     snail_x_pos=screen_width


            
            # mouse_position=pygame.mouse.get_pos()

            # if player_rect.collidepoint(mouse_position): #Eddi mouse ko position tyo image ma gayo bhane loop exit huncha.
            #     pygame.quit()
            #     quit()


            

            player_gravity +=0.1

            player_rect.y += player_gravity

            
            if player_rect.bottom >300:
                player_rect.bottom=300 

            if player_rect.colliderect(snail_rect):
                game_active=False
    
            
            draw_window(i,start_time)
        else:
            screen.fill("white")
            screen.blit(game_over_surface,game_over_surface_rect)
            pygame.display.update()
'''
'collidepoint()' is a Pygame function that checks if a point (specified by its x and y coordinates) 
is inside a rectangle.

It can be used to check if a mouse click or other event is occurring inside a particular area on the screen.

Syntax --> rect1.collidepoint((x,y))

-> To get mouse position we have two method:
1. pygame.mouse  -> gives mouse position,clicks button,visibility etc

2. event loop

'''



"""
colliderect is a method in Pygame used to detect collisions between two rectangular objects. 
It is a very useful method in game development for collision detection between game objects.

The colliderect() method checks if two rectangular objects collide with each other. 
It takes one argument, which is another rectangle object, and 
returns a boolean value of True if the two rectangles collide, and False if they do not.
 
"""       

if __name__ =="__main__":
    main()