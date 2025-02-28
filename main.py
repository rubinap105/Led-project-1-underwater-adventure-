#imported necessary modules
import pygame, random
from pygame.locals import *
import sqlite3

#function named game where all codes of main program is stored so it can be access easily fromm other place
def game():
    #initialized Pygame
    pygame.init()
    #stored values into WIDTH and HEIGHT
    WIDTH, HEIGHT = 330, 500
    #Set Geometry of Pygame Window
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    #Set Title of Pygame Window
    pygame.display.set_caption("Underwater Adventure")
    #changed Icon of Pygame window to fish2.png
    pygame_icon = pygame.image.load('images/fish2.png')
    pygame.display.set_icon(pygame_icon)

    #Provided R G B for BLUE color so can be called later to use
    BLUE=(0,105,148)

    #Runs the program at 60 frames
    clock = pygame.time.Clock()
    fps = 60

    #define game variables
    ground_scroll = 0
    scroll_speed = 2

    #Displays Base and background of game
    ground_img = pygame.image.load(r'images/base.png')
    bg_img = pygame.image.load(r"images/bg.png")

    #displays fish
    fish_img = pygame.image.load(r'images/fish2.png')
    #transformed fish into 40x40
    fish = pygame.transform.scale(fish_img, (40,40))

    #provided values to var_x as where var_x act as X axis point where base is displayed
    var_x = 0
    #Provided value to fish_x and fish_y which is X and Y position of fish
    fish_x=30
    fish_y=200
    #Value of fish_y_change as 0 which is value by which fish changes its y axis
    fish_y_change=0
    #g_force as 0.5 which is by how much fish is attracted downward
    g_force = 0.5

    #Width of obstacle that will be generated
    obstacle_width = 60
    #height of Obstacles from top
    obstacle_height = random.randint(120,250)
    #color of Obstacles
    obstacle_color = (211,253,117)
    #obstacle_x-change which is value by which X position of obstacles changes
    obstacle_x_change = -4
    #X position of obstacles when it first appears
    obstacle_x = 330


    TIMER = pygame.USEREVENT
    pygame.time.set_timer(TIMER, 1000)

    #function named base_movement which  displays Base as parameter is provided
    def base_movement(WIN, ground_img,var_x):
        #displays base so blit is used
        WIN.blit(ground_img, (var_x,430))
        WIN.blit(ground_img, (var_x + 240,430))

    #function named display_fish that displays fish at position where paramater is provided
    def display_fish(x,y):
        #blit to display fish
        WIN.blit(fish,(x,y))

    #function named display_obstacles which displays obstacles with provided height
    def display_obstacle(height):
        #draws a rectangle with obstacle_x as x position and 0 as Y position with obstacle_width as width and provided argument as height
        pygame.draw.rect(WIN, obstacle_color, pygame.Rect(obstacle_x, 0, obstacle_width, height))
        #Added 130 to bottom_y and subtract that value from 430 and stored to bottom_obstacle
        bottom_y = height + 130
        bottom_obstacle_height = 430 - bottom_y
        # draws a rectangle with obstacle_x as x position and obstacle_y as Y position with obstacle_width as width and bottom_obstacle_height as height
        pygame.draw.rect(WIN, obstacle_color, pygame.Rect(obstacle_x, bottom_y, obstacle_width, bottom_obstacle_height))

    #function named collision_detection with 4 parameter
    def collision_detection(obstacle_x, obstacle_height, fish_y , bottom_obstacle_height):
        #if statement to check conditions
        if obstacle_x >=30 and obstacle_x <= (50 + 40):
            #returns True of again provided Condition satisfies or returns false
            if fish_y <= obstacle_height or fish_y >= (bottom_obstacle_height - 40):
                return True
            return False

    #point as 0
    point = 0
    #Font to be used while Displaying Score
    point_font = pygame.font.Font('freesansbold.ttf',26)
    #function named point_display with point as one parameter
    def point_display(point):
        #displays the point
        display = point_font.render(f"Score: {point}", True, (255,255,255))
        WIN.blit(display, (10, 10))

    #Stored run as True
    run = True
    #Infinite While loop for now until some statemt fulfills to cancel it
    while run:
        #Runs program at 60 fps
        clock.tick(fps)

        #Displays bg_img at 0,0 position
        WIN.blit(bg_img, (0,0))

        #changed var_x to -1
        var_x -= 1

        #calls base_movement with WIN,ground_img and var_x as 3 arguments
        base_movement(WIN, ground_img,var_x)
        #looks whether var_x is less then -180 then changes value to 0
        if var_x <= -180:
            var_x=0

        #Looks for user input
        for event in pygame.event.get():
            #if user pressed Crossed or Quit then It Stops Infinite Loop
            if event.type == pygame.QUIT:
                run = False

            #if user pressed a key and that is Space Key then it changes y-axis position of fish by moving 6 upward
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fish_y_change = -6
            #if user removes hand from a key and that is Space Key then it changes y-axis position of fish by going 5 downward
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    fish_y_change = 5

        #changes fish _y position by adding fish_y_change infish_y
        fish_y += fish_y_change


        if fish_y <= 0 or fish_y >= 370:
            from game_over import game_finish as end_game
            end_game()

        #changes X position of Fish by fish_x_change
        obstacle_x += obstacle_x_change
        #changes obstacles_x location if it is <= -50 then to 330 and a random height adding 1 as point
        if obstacle_x <= -50:
            obstacle_x = 330
            obstacle_height = random.randint(100, 300)
            point += 1

        #calls display_obstacle function with one parameter named obstacle_height
        display_obstacle(obstacle_height)

        #Calls Collision_detection function which return True or False and Stores in collision
        collision = collision_detection(obstacle_x, obstacle_height, fish_y, obstacle_height + 130)

        #if collision is found
        if collision:
            #connect with player_details database and stores all data of profile data into recordsprofile
            conn = sqlite3.connect('player_details.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM profile")
            recordsprofile = c.fetchall()
            conn.commit()
            conn.close()

            #connect with current_user database and stores all data of user_data Table into recordsuser
            conn = sqlite3.connect('current_user.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM user_data")
            recordsuser = c.fetchall()
            conn.commit()
            conn.close()

            #looks which user data matches in profile table and update its score if it is greater than before
            for record_user in recordsuser:
                for record_profile in recordsprofile:
                    if str(record_user[0]) == str(record_profile[2]):
                        record_id = record_profile[5]
                        previous_score = record_profile[4]
                        if point>previous_score:
                            conn = sqlite3.connect('player_details.db')
                            c = conn.cursor()
                            data_to_be_updated = '''UPDATE profile
                                                    SET score = ?
                                                    WHERE oid = ?'''
                            data = (point,record_id)
                            c.execute(data_to_be_updated, data)
                            conn.commit()
                            conn.close()
            #Quit the Pygame Window
            pygame.quit()
            #calls function end_game i.e. game_finish from game_over
            from game_over import game_finish as end_game
            end_game()

        #calls function to display fish
        display_fish(fish_x,fish_y)
        #call function to sisplay point
        point_display(point)
        #upates everything into pygame Window
        pygame.display.update()

    #quit Pygame Window
    pygame.quit()

#call game function
game()