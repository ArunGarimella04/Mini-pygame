import pygame
import random

#main parameters
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner Game")
clock=pygame.time.Clock()
test_font=pygame.font.Font('font/Pixeltype.ttf',50)
in_game=False
login=False
score=0
start_time=pygame.time.get_ticks()
jump_sound=pygame.mixer.Sound('audio/jump.mp3')
jump_sound.set_volume(0.1)
death_sound=pygame.mixer.Sound('audio/roblox-death-sound-effect.mp3')
death_sound.set_volume(0.5)
login_bgm=pygame.mixer.Sound('audio/dances-with-kittens-216892.mp3')
login_bgm.set_volume(0.4)
run_bgm=pygame.mixer.Sound('audio/cool-jazz-1-166406.mp3')
run_bgm.set_volume(0.2)

#function to move obstacles
def obstacle_movement(obstacle_rect_list):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            obstacle_rect.x-=5
            if obstacle_rect.bottom==300:
                screen.blit(snail_surface,obstacle_rect)
            else:   
                screen.blit(fly_surface,obstacle_rect)
        
        #remove obstacles that are out of screen
        obstacle_rect_list=[obstacle for obstacle in obstacle_rect_list if obstacle.x>-100]
            
        return obstacle_rect_list
    else:
        return []

#collision function
def collision(player_rect,obstacle_rect_list):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            if player_rect.colliderect(obstacle_rect):
                death_sound.play()
                return False
    return True

#player animation function
def player_animation():
    global player_index,player_surface,player_image_surface
    if player_rect.bottom<300:
        player_image_surface=player_jump
    else:
        player_index+=0.1
        if player_index>=len(player_style):
            player_index=0
        player_surface=player_style[int(player_index)]

#game objects
sky=pygame.image.load('graphics\Sky.png').convert()
ground=pygame.image.load('graphics\ground.png').convert()

#login screen
login_screen_font=pygame.font.Font('font/Pixeltype.ttf',70)
login_text_surface=login_screen_font.render('RUN-MAXXER',False,'black')
login_text_rect=login_text_surface.get_rect(center=(400,100))

player_image_stand=pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_image_stand=pygame.transform.rotozoom(player_image_stand,0,2)

game_start_text_surface=test_font.render('Press Enter to Start',False,(139,69,19))
game_start_text_rect=game_start_text_surface.get_rect(center=(400,330))

#game text
text_surface=test_font.render('My Game',False,(64,64,64))
text_rect=text_surface.get_rect(center=(400,50))

#score display
score_disp_surface=test_font.render(f'Score: {score}',False,'black')
score_disp_rect=score_disp_surface.get_rect(center=(400,80))

#snail object
snail_1=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_2=pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames=[snail_1,snail_2]
snail_index=0
snail_surface=snail_frames[snail_index]

#fly object
fly_1=pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly_2=pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
fly_frames=[fly_1,fly_2]
fly_index=0
fly_surface=fly_frames[fly_index]

#player object
player_walk_1=pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2=pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_jump=pygame.image.load('graphics/Player/jump.png').convert_alpha()
player_style=[player_walk_1,player_walk_2]
player_index=0
player_surface=player_style[player_index]
player_rect=player_surface.get_rect(midbottom=(80,300))
player_gravity=0
player_velocity_x=0

#obsatales
obstacle_rect_list=[]

#timer
obstacle_timer=pygame.USEREVENT+1
pygame.time.set_timer(obstacle_timer,1500)
snail_animation_timer=pygame.USEREVENT+2
pygame.time.set_timer(snail_animation_timer,250)
fly_animation_timer=pygame.USEREVENT+3
pygame.time.set_timer(fly_animation_timer,500)

#game loop/main loop
while True:
    #start screen
    if not login:
        if not pygame.mixer.get_busy():
            login_bgm.play(-1)
        #login screen
        player_rect=player_surface.get_rect(center=(350,170))
        login_screen=screen.fill((94,129,162))
        screen.blit(login_text_surface,login_text_rect)
        screen.blit(player_image_stand,player_rect)
        screen.blit(game_start_text_surface,game_start_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                login_bgm.stop()
                run_bgm.play(-1)
                login=True
                in_game=True
                score=0
                player_rect.x=80
                player_rect.y=300
                player_gravity=0
                text_surface=test_font.render('My Game',False,(64,64,64))
                text_rect=text_surface.get_rect(center=(400,50))
                score_disp_surface=test_font.render(f'Score: {score}',False,'black')
                score_disp_rect=score_disp_surface.get_rect(center=(400,80))
                screen.blit(text_surface,text_rect)
                screen.blit(score_disp_surface,score_disp_rect)
        
        pygame.display.update()
        clock.tick(60)
    
    #successful login
    if login:
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 500 and in_game:
            if(score>100):
                score+=2
            elif(score>500):
                score+=5
            else:
                score+=1
            start_time = current_time  
        score_disp_surface=test_font.render(f'Score: {score}',False,'black')

        #in-game event handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if in_game:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos) and player_rect.bottom>=300:
                        player_gravity=-20

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.bottom>=300:
                        player_gravity=-20
                        jump_sound.play()
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                        player_velocity_x+=5
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                        player_velocity_x-=5
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player_gravity+=10

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player_velocity_x = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player_velocity_x = 0 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    login=False
                    in_game=False
                if event.type == obstacle_timer:
                    if random.randint(0,2):
                        obstacle_rect_list.append(snail_surface.get_rect(midbottom=(random.randint(1000,1200),300)))
                    else:
                        obstacle_rect_list.append(fly_surface.get_rect(midbottom=(random.randint(1000,1200),200)))
                if event.type == snail_animation_timer:
                    if snail_index == 0:
                        snail_index = 1
                    else:
                        snail_index = 0
                    snail_surface=snail_frames[snail_index]
                if event.type == fly_animation_timer:
                    if fly_index == 0:
                        fly_index = 1
                    else:
                        fly_index = 0
                    fly_surface=fly_frames[fly_index]
            
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    in_game=True
                    score=0
                    player_rect.x=80
                    player_rect.y=300
                    # snail_rect.x=800
                    player_gravity=0
                    text_surface=test_font.render('My Game',False,(64,64,64))
                    text_rect=text_surface.get_rect(center=(400,50))
                    score_disp_surface=test_font.render(f'Score: {score}',False,'black')
                    score_disp_rect=score_disp_surface.get_rect(center=(400,80))
                    screen.blit(text_surface,text_rect)
                    screen.blit(score_disp_surface,score_disp_rect)
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    login=False
                    in_game=False

        #game logic
        if in_game:
            if 0 <= player_rect.x + player_velocity_x <= 340:    
                player_rect.x += player_velocity_x
            
            #loading screen
            screen.blit(sky, (0,0))
            screen.blit(ground, (0,300))
            screen.blit(text_surface,text_rect)
            
            #loading scoreboard
            screen.blit(score_disp_surface,score_disp_rect)

            #player movement
            player_animation()
            player_gravity+=1 
            player_rect.y+=player_gravity
            
            if player_rect.bottom>=300:
                player_rect.bottom=300
            screen.blit(player_surface,player_rect)

            #obstacle movement
            obstacle_rect_list=obstacle_movement(obstacle_rect_list)

            #collision
            in_game=collision(player_rect,obstacle_rect_list)
            
        else:
            #clear obsatacle list
            obstacle_rect_list.clear()
            run_bgm.stop()

            #game over screen
            screen.blit(sky, (0,0))
            screen.blit(ground, (0,300))
            screen.blit(text_surface,text_rect)
            screen.blit(player_surface,player_rect)

            #game over text
            GO_font=pygame.font.Font('font/Pixeltype.ttf',70)
            text_surface=GO_font.render('GAME OVER!!!',False,(64,64,64))
            text_rect=text_surface.get_rect(center=(400,100))

            final_score_font=pygame.font.Font('font/Pixeltype.ttf',90)
            score_disp_surface=final_score_font.render(f'Your Score: {score}',False,'black')
            score_disp_rect=score_disp_surface.get_rect(center=(400,150))

            GO_restart_text_surface=test_font.render('Press Space to Restart',False,(64,64,64))
            GO_restart_text_rect=GO_restart_text_surface.get_rect(center=(400,190))
            go_to_login_text_surface=test_font.render('Press Esc to go to Login',False,(64,64,64))
            go_to_login_text_rect=go_to_login_text_surface.get_rect(center=(400,230))
            screen.blit(score_disp_surface,score_disp_rect)
            screen.blit(GO_restart_text_surface,GO_restart_text_rect)
            screen.blit(go_to_login_text_surface,go_to_login_text_rect)
    
        pygame.display.update()
        clock.tick(60)