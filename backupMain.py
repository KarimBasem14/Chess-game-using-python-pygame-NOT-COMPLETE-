
import pygame
from typing import Tuple

pygame.init()
timer = pygame.time.Clock()
fps = 60
# Set display dimensions
WIDTH, HEIGHT = 1000, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set title
pygame.display.set_caption("Chess Game")

# Colors
WHITE =(255,255,255)
BLACK = (0,0,0)
GOLD= (255,215,0)

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]


black_turn = True # Is it black's turn?
selected = False # Did he select a piece?
selected_piece_coords = ()
turn_text = ["Black's turn: select a piece", "Black's turn: choose a tile to move to", "White's turn: select a piece", "White's turn: choose a tile to move to"]

# Font
font = pygame.font.Font('freesansbold.ttf', 32)

# LOAD GAME IMAGES
# r"" is used to make it a raw string so the \ doesn't give error inside the string
black_queen = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load(r'C:\Users\Cyber\Desktop\Code\Python\Task4MIA\Chess game\assets\images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
white_images = [white_rook,white_knight,white_bishop,white_king,white_queen,white_bishop,white_knight,white_rook,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn]
black_images = [black_rook,black_knight,black_bishop,black_king,black_queen,black_bishop,black_knight,black_rook,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']



def draw_board(): # Draws the board on the screen
    for x in range(8):
        for y in range(8):
            if (y+x) % 2 ==0: # This (x+y) % 2 == 0 is generally used if you want to generate a grid of any size
                pygame.draw.rect(screen,(0,0,0),( x*100,y*100, 100, 100))
            
    pygame.draw.line(screen, GOLD , (0, 8*100),(8*100,8*100),width=5) # horizontal line under the board
    pygame.draw.line(screen, GOLD ,(8*100,8*100),(8*100,0),width=5)  # Vertical line beside the board
def ingrid_range(x,y): # Returns true if position is inside the grid else returns false
    # Uses x,y insted of pos so i can easily edit them but now you have to unpack the args when you call the function using * 
    return (x<8 and x>=0) and (y<8 and y>=0)

def is_piece(pos): # Returns True if the position given is the position of a piece
    if pos in white_locations or pos in black_locations :
        return True

def highlight_square(square_pos):
    x,y = square_pos
    pygame.draw.rect(screen, (255,0,0), (x*100,y*100,100,100),2 ) # Highlights a square in red when that square is clicked, 2 is the width it makes it so that the rectangle doesn't fill the entire tile
    
def move_to_tile(initial_pos: Tuple[int, int], target: Tuple[int, int]): # The different syntax is used to make the fn only accept 2 tuples
    if black_turn:
        index = black_locations.index(initial_pos)
        black_locations[index] = target
    elif black_turn == False:
        index = white_locations.index(initial_pos)
        white_locations[index] = target

def show_turn_text():
    text = ""
    if black_turn:
        if selected == False:
            text= turn_text[0]
        elif selected == True:
            text = turn_text[1]
    elif black_turn == False:
        if selected == False:
            text= turn_text[2]
        elif selected == True:
            text = turn_text[3]
    
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 850))
    screen.blit(text_surface, text_rect)
    

def draw_pieces():
    for i,(x,y) in enumerate(white_locations):
        screen.blit(white_images[i], (x*100,y*100))
    for i,(x,y) in enumerate(black_locations):
        screen.blit(black_images[i], (x*100,y*100))
    

    pygame.display.flip()
# Main game loop

running = True
while running:
    timer.tick(fps)
    
    screen.fill('dark gray')
    show_turn_text() # Putting this under draw_pieces() makes it flash from time to time
    draw_board()
    if selected_piece_coords: # Before this the red highlight used to flash
        highlight_square(selected_piece_coords)
    draw_pieces()
    


    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if ingrid_range(*click_coords) and is_piece(click_coords) and selected == False: 
                """First condition is to make sure that you clicked somewhere on the board.
                   Second condition is to make sure you clicked on a tile with a piece on it
                   Third condition is to make sure you only select one piece at a time"""
                selected_piece_coords = click_coords
                selected = True 
                if selected_piece_coords in black_locations and black_turn == False: 
                    selected = False
                    # These 2 conditions makes it so that if i for example select a black piece i can't select a black one right after it
                    # I feel that these is something wrong though or it is a lil bit slow there might be unnoticable bugs but i can ignore them for now ig
                if selected_piece_coords in white_locations and black_turn == True:
                    selected = False
            elif selected == True: # If you have selected a piece
                move_to_tile(selected_piece_coords, click_coords) # Move the piece to whatever place you click on YOU STILL HAVE TO MAKE SURE YOU CAN ONLY PLACE IT IN VALIDMOVES AND INSIDE THE GRID
                selected = False # Return to the nothing selected state
                selected_piece_coords = () 
                black_turn = not black_turn # switches turns
            print(click_coords)
            print(ingrid_range(*click_coords))
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
                
    

    pygame.display.flip()
pygame.quit()