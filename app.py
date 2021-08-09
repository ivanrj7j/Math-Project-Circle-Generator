import pygame
import math
import sys


pygame.init()
# initiaing pygame 
pygame.mixer.init()
# initialising the mixer 
pygame.font.init()
# initialising the font 

PI = 3.1415926535
# pi value 

try:
    arguments = sys.argv
    argument_type = arguments[1]
    argument = arguments[2]
    if argument_type == '-r' or argument_type == '--r' or argument_type == '-radius' or argument_type == '--radius':
        print("Running in Radius Mode")
        r = int(argument)
    elif argument_type == '-p' or argument_type == '--p' or argument_type == '-perimeter' or argument_type == '--perimeter':
        print("Running in Perimeter Mode")
        perimeter = int(argument)
        diameter = perimeter / PI
        r = diameter / 2
        
    elif argument_type == '-a' or argument_type == '--a' or argument_type == '-area' or argument_type == '--area':
        print("Running in area Mode")
        area = int(argument)
        r_square = area / PI
        r = math.sqrt(r_square)
        
    elif argument_type == '-d' or argument_type == '--d' or argument_type == '-diameter' or argument_type == '--diameter':
        print("Running in Diameter Mode")
        diameter = int(argument)
        r = diameter / 2
    
    else:
        print("No arguments were given, So taking radius as 15")
        
    
except Exception as e:
    print("OOpsie, Big OOpsie")
    print(e)
    r = 15
    
window = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
# initialising the window 

'''Colors'''
red = (166,3,63)
grey_border = (88,85,90)
black = (0,0,0)
white = (250,250,250)
'''Colors end.'''

pygame.display.set_caption("Math Project")
# setting the caption of the screen 

class Pixel:
    def __init__(self, color:tuple = white, position:tuple = (0,0) , border:bool = False):
        '''Returns a box representing a pixel, not an actual pixel.
        Use for demonstration purpose only.'''
        self.color = color
        # setting the color 
        self.x = position[0]
        self.y = position[1]
        # setting the position 
        self.width = 8
        self.height = 8
        # setting the dimension 
        self.has_border = border
        self.entity = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def render(self):
        pygame.draw.rect(window, self.color, self.entity, 1)

def get_center(width, height):
    '''Gives the dead center position of the thing.'''
    center = (((window.get_width() / 2) - (width / 2)), ((window.get_height() / 2) - (height / 2)))
    return center

def circle_positions(width , height, radius):
    '''Returns a list of the positions of where to render the pixels'''
    PI = 3.1415926535
    # value of pi 
    center_x = (window.get_width() / 2)
    center_y = (window.get_height() / 2)
    # the center cordinates 
    render_list = []
    # gives the cordinates of where to render the pixel 
    new_render_list = []
    # gives the cordinates of where to render the pixel 
    radius = radius * 8
    for angle in range(0, 360):
        x1 = radius * math.cos(angle * PI / 180)
        y1 = radius * math.sin(angle * PI / 180)
        new_x = int((x1 + center_x) - (width / 2))
        new_y = int((y1 + center_y) - (height / 2))
        render_list.append((new_x , new_y))
    
    for item in range(0, len(render_list), width):
        new_render_list.append(render_list[item])
    
    return new_render_list

def main():
    running = True
    # true if the game is running   
    clock = pygame.time.Clock()
    # initialising the clock object 
    
    while running:
        clock.tick(60)
        # setting the fps cap 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # quitting the game when quitted 
        window.fill((255,255,255)) 
        # filling the window with white
        center = Pixel(color=red, position=get_center(8, 8))
        positions = circle_positions(8, 8, r)
        pixel_list = []
        for pos in positions:
            pixel = Pixel(color=black, position=pos)
            pixel_list.append(pixel) 
        center.render()
        for pixel in pixel_list:
            pixel.render()
        if pygame.display:
            pygame.display.update()
        # updating the display 
    pygame.quit()
    
if __name__ == "__main__":
    main()