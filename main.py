from utils import *
pygame.init()
WND = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Drawing Console")
icon = pygame.image.load('src/icon.png')
pygame.display.set_icon(icon)
def init_grid(row,col,color):
    grid = []
    for i in range(row):
        grid.append([])
        for _ in range(col):
            grid[i].append(color)
    return grid
def draw_grid(win,grid):
    for i,row in enumerate(grid):
        for j,pixel in enumerate(row):
            pygame.draw.rect(win,pixel,(j*PIXEL_SIZE,i*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE),)     # pygame.draw.rect(surface,color,(x_position, y_position, breadth_of_rect, height_of_rect))             --> rect() means it draws a rectangle -->x_position is x-coordinate where rectangle should be drawn similarly y_position  -->breadth_rect is breadth of rectangle to be drawn similarly height_rect
    if DRAW_GRID_LINES:
        for i in range(ROWS):
            pygame.draw.line(win,LIGHT_BLACK,(0,i*PIXEL_SIZE),(WIDTH,i*PIXEL_SIZE))
    if DRAW_GRID_LINES:
        for i in range(COLS):
            pygame.draw.line(win,LIGHT_BLACK,(i*PIXEL_SIZE,0),(i*PIXEL_SIZE,HEIGHT-TOOLBAR_HEIGHT))
def get_coordinate(co):
    x , y = co
    col = x // PIXEL_SIZE
    row = y // PIXEL_SIZE
    if row >= ROWS-1:
        raise IndexError 
    return (row,col)
def draw(win, grid, butt):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    for b in butt:
        b.draw(win)
    pygame.display.update()
clock = pygame.time.Clock()
run = True
grid = init_grid(ROWS,COLS,BG_COLOR)
draw_color = BLACK
but_y = HEIGHT - TOOLBAR_HEIGHT/2 -25
butt =  [
    Button(10,but_y,50,50,BLACK),
    Button(10+60,but_y,50,50,RED),
    Button(10+(2*60),but_y,50,50,GREEN),
    Button(10+(3*60),but_y,50,50,BLUE),
    Button(10+(4*60),but_y,50,50,LIGHT_BLACK),
    Button(10+(5*60),but_y,50,50,WHITE,'Erase',BLACK),
    Button(10+(6*60),but_y,50,50,WHITE,'Clr All',BLACK)
]
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            do_pos = pygame.mouse.get_pos()
            try:
                row,col = get_coordinate(do_pos)
                grid[row][col] = draw_color
            except IndexError:
                for b in butt:
                    if not b.clicked(do_pos):
                        continue
                    if b.text == 'Clr All':
                        grid = init_grid(ROWS,COLS,BG_COLOR)
                        draw_color = BLACK
                    else:
                        draw_color = b.color
    draw(WND,grid,butt)
    pygame.display.update()
pygame.quit()