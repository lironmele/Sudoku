#importing
import pygame, sys, random

#setting up basic stuff and variables
pygame.init()
size = width, height = 504, 504
row, column = 9,9
screen = pygame.display.set_mode((width, height))
white = (255,255,255)
black = (0,0,0)

#draw the grid
def draw_grid(w=None):
    for x in range(column):
        if x == 3 or x == 6:
            w = 5
        else:
            w = 1
        pygame.draw.line(screen, black, (x*width//column, 0), (x*width//column, height),w)

    for y in range(row):
        if y == 3 or y == 6:
            w = 5
        else:
            w = 1
        pygame.draw.line(screen, black, (0, y*height//row), (width, y*height//row), w)

numbers = list()

def add_number(x,y,number):
    a = [x,y,number]
    for m in numbers:
        count = 0
        if m[0] == a[0] and m[1] == a[1]:
                return
        if m[0] == x or m[1] == y:
            if m[2] == number:
                return
        if 0 <= x <= 2 and 0 <= y <= 2 and 0 <= m[0] <= 2 and 0 <= m[1] <= 2 and number == m[2]: return
        if 0 <= x <= 2 and 3 <= y <= 5 and 0 <= m[0] <= 2 and 3 <= m[1] <= 5 and number == m[2]: return
        if 0 <= x <= 2 and 6 <= y <= 8 and 0 <= m[0] <= 2 and 6 <= m[1] <= 8 and number == m[2]: return
        #
        if 3 <= x <= 5 and 0 <= y <= 2 and 3 <= m[0] <= 5 and 0 <= m[1] <= 2 and number == m[2]: return
        if 3 <= x <= 5 and 3 <= y <= 5 and 3 <= m[0] <= 5 and 3 <= m[1] <= 5 and number == m[2]: return
        if 3 <= x <= 5 and 6 <= y <= 8 and 3 <= m[0] <= 5 and 6 <= m[1] <= 8 and number == m[2]: return
        #
        if 6 <= x <= 8 and 0 <= y <= 2 and 6 <= m[0] <= 8 and 0 <= m[1] <= 2 and number == m[2]: return
        if 6 <= x <= 8 and 3 <= y <= 5 and 6 <= m[0] <= 8 and 3 <= m[1] <= 5 and number == m[2]: return
        if 6 <= x <= 8 and 6 <= y <= 8 and 6 <= m[0] <= 8 and 6 <= m[1] <= 8 and number == m[2]: return
    numbers.append(a)

def draw_numbers():
    for num in numbers:        
        font = pygame.font.Font(None,60)
        mytextsurface = font.render(str(num[2]), True, black)
        screen.blit(mytextsurface, ((num[0]*width//column)+(width//column//4), (num[1]*height//row)+(height//row//4)))

def get_num(x, y):
    global c
    num = random.randint(1,9)
    for num2 in numbers:
        if num2[0] == x or num2[1] == y:
            if num2[2] == num:
                return
        #(x = 0-2, y = 0-8)
        if 0 <= x <= 2 and 0 <= y <= 2 and 0 <= num2[0] <= 2 and 0 <= num2[1] <= 2 and num == num2[2]: return
        elif 0 <= x <= 2 and 3 <= y <= 5 and 0 <= num2[0] <= 2 and 3 <= num2[1] <= 5 and num == num2[2]: return
        elif 0 <= x <= 2 and 6 <= y <= 8 and 0 <= num2[0] <= 2 and 6 <= num2[1] <= 8 and num == num2[2]: return
        #(x = 3-5, y = 0-8)
        elif 3 <= x <= 5 and 0 <= y <= 2 and 3 <= num2[0] <= 5 and 0 <= num2[1] <= 2 and num == num2[2]: return
        elif 3 <= x <= 5 and 3 <= y <= 5 and 3 <= num2[0] <= 5 and 3 <= num2[1] <= 5 and num == num2[2]: return
        elif 3 <= x <= 5 and 6 <= y <= 8 and 3 <= num2[0] <= 5 and 6 <= num2[1] <= 8 and num == num2[2]: return
        #(x = 6-8, y = 0-8)
        elif 6 <= x <= 8 and 0 <= y <= 2 and 6 <= num2[0] <= 8 and 0 <= num2[1] <= 2 and num == num2[2]: return
        elif 6 <= x <= 8 and 3 <= y <= 5 and 6 <= num2[0] <= 8 and 3 <= num2[1] <= 5 and num == num2[2]: return
        elif 6 <= x <= 8 and 6 <= y <= 8 and 6 <= num2[0] <= 8 and 6 <= num2[1] <= 8 and num == num2[2]: return
    c = False
    return num
c = True

def gen_board(limit):
    global c
    for i in range(limit):
        X = random.randint(0, 2) * 3 + random.randint(0, 2)
        Y = random.randint(0, 2) * 3 + random.randint(0, 2)
        c = True
        while c: Num = get_num(X, Y)
        else: add_number(X, Y, Num)

gen_board(50)
print(numbers)
cursor = pygame.Rect((0),(0),width//column,height//row)
# Game loop.
while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key >= 1073741913 and event.key <= 1073741921:
                add_number(cursor.left//(width//column), cursor.top//(height//row), event.key - 1073741912)
            if event.key == pygame.K_LEFT and cursor.left != 0: cursor.move_ip(-width//column, 0)
            elif event.key == pygame.K_RIGHT and cursor.right != width: cursor.move_ip(width//column, 0)
            elif event.key == pygame.K_UP and cursor.top != 0: cursor.move_ip(0, -height//row)
            elif event.key == pygame.K_DOWN and cursor.bottom != height: cursor.move_ip(0, height//row)
        elif event.type == pygame.QUIT:pygame.quit(), sys.exit()

    #draw stuff
    draw_grid()
    draw_numbers()
    pygame.draw.rect(screen,(0,255,0), cursor, 7)
    #mendatory display commands
    pygame.display.flip()
    pygame.time.Clock().tick(60)
