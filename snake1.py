import pygame
import random
import numpy as np

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
CELL_SIZE=10
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2

pygame.init()
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

class snake():
    def __init__(self,food):
        self.food=food
        self.head_x=5
        self.head_y=5
        self.direction=DOWN
        self.score=0
        self.score_rate=10
        self.body=[]        
        self.reset()
        self.update()        
    def reset(self):
        for i in range(4):
            self.body.append(((self.head_x+i)*CELL_SIZE,self.head_y*CELL_SIZE))
    def update(self):    
        self.show_score()
        pygame.draw.rect(screen,'red',(self.body[0][0],self.body[0][1],CELL_SIZE,CELL_SIZE))
        for i in range(1,len(self.body)):
            pygame.draw.rect(screen,'white',(self.body[i][0],self.body[i][1],CELL_SIZE,CELL_SIZE))
    def change_direction(self,key):
        action = { pygame.K_DOWN: self.move_down,
                   pygame.K_LEFT: self.move_left,
                   pygame.K_RIGHT: self.move_right,
                   pygame.K_UP: self.move_up }                                      
        action[key]()         
    def move_down(self):
        if self.direction!=UP:  #to avoid moving to the reverse direction
            self.direction=DOWN   
    def move_up(self):
        if self.direction!=DOWN:
            self.direction=UP      
    def move_left(self):
        if self.direction!=RIGHT:
            self.direction=LEFT         
    def move_right(self):    
        if self.direction!=LEFT:
            self.direction=RIGHT 
    def move(self):
        if self.direction==UP:self.head_y-=1
        if self.direction==DOWN:self.head_y+=1
        if self.direction==LEFT:self.head_x-=1
        if self.direction==RIGHT:self.head_x+=1
        
        self.body.insert(0,(self.head_x*CELL_SIZE,self.head_y*CELL_SIZE))                
        if (self.food.x==self.head_x and self.food.y==self.head_y):  
            self.score+=self.score_rate
            self.food.add()
        else:
            self.body.pop() 
        self.update()
    def draw_text(self,x,y,text,size):  
        font = pygame.font.SysFont('comicsans', size) 
        score_surface = font.render(text, True, 'white')
        screen.blit(score_surface,score_surface.get_rect(topleft=(x,y)))  
    def show_score(self):
        self.draw_text(0,0,"Score:  "+str(self.score),30)
    def lost_check(self):
        if self.hit_self() or self.hit_wall():
            self.draw_text(int(WINDOW_WIDTH/3), int(WINDOW_HEIGHT/2.5),"Game Over",60)
            pygame.display.update()
            pygame.time.delay(2000)    
            exit() 
    def hit_self(self):
        if ((self.head_x*CELL_SIZE,self.head_y*CELL_SIZE) in self.body[2:]):
            return True
    def hit_wall(self):
        if ((self.head_x*CELL_SIZE)>=WINDOW_WIDTH or  (self.head_x*CELL_SIZE)<=0 or   
           (self.head_y*CELL_SIZE)>=WINDOW_HEIGHT or  (self.head_y*CELL_SIZE)<=0 ) :  
               return True        
class food():
    def __init__(self):
        self.x=5
        self.y=5        
    def add(self):
        self.x=random.randint(1,int((WINDOW_WIDTH-2*CELL_SIZE)/CELL_SIZE))
        self.y=random.randint(1,int((WINDOW_HEIGHT-2*CELL_SIZE)/CELL_SIZE))
    def update(self):
        pygame.draw.rect(screen,'white',(self.x*CELL_SIZE,self.y*CELL_SIZE,CELL_SIZE,CELL_SIZE))
    
def checkEvents(snake):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()            
            if event.type==pygame.KEYDOWN:       
                if event.key in [pygame.K_LEFT, pygame.K_UP,pygame.K_RIGHT, pygame.K_DOWN]:
                    snake.change_direction(event.key)    
               
clock = pygame.time.Clock()
Food=food()  
Snake=snake(Food) 
Food.add()           
run=True
while run:
    checkEvents(Snake)
    screen.fill((0,0,0)) 
    Snake.lost_check()       
    Snake.move()
    Food.update()  
    pygame.display.update()
    clock.tick(15)
