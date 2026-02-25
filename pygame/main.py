import pygame 
pygame.init() 

win = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption("Moving rectangle") 

x = 200
y = 200

width = 20
height = 20

isjump = False
v = 5
m = 1

vel = 10
run = True

# infinite loop 
while run: 
	
	pygame.time.delay(10)
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False
	keys = pygame.key.get_pressed() 
	
	if keys[pygame.K_LEFT] and x>0: 
		x -= vel 
		
	if keys[pygame.K_RIGHT] and x<500-width: 
		x += vel 
		
	if keys[pygame.K_UP] and y>0: 
		y -= vel 
		
	if keys[pygame.K_DOWN] and y<500-height:
		y += vel
	if isjump == False:
		if keys[pygame.K_SPACE]:
			isjump = True			
	if isjump :
		# calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
		F =(1 / 2)*m*(v**2)
		 
		# change in the y co-ordinate
		y-= F
		 
		# decreasing velocity while going up and become negative while coming down
		v = v-1
		 
		# object reached its maximum height
		if v<0:
			 
			# negative sign is added to counter negative velocity
			m =-1
 
		# objected reaches its original state
		if v ==-6:
 
			# making isjump equal to false 
			isjump = False

   
			# setting original values to v and m
			v = 5
			m = 1

			
	 
	# creates time delay of 10ms

	win.fill((0, 0, 0))
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.update()
	
		# it refreshes the window