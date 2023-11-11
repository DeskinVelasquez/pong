import pygame
pygame.init()

#difinir variables y constantes
black = (0,0,0)
white = (255,255,255)
screen_size = (800,600)
player_width = 5
player_height = 90
speed_players = 6

#coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - (player_height/2)
player1_y_speed = 0
(player1_x_coor, player1_y_coor, player_width, player_height) # (posicion x, posicion Y, ancho, alto) | 300 es la mitad del la pantalla y 45 es la mitad del alto   

#coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - (player_height/2)
player2_y_speed = 0
(player2_x_coor, player2_y_coor, player_width, player_height) # (posicion x, posicion Y, ancho, alto) | 300 es la mitad del la pantalla y 45 es la mitad del alto   

#coordenadas de la pelota
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3
ball_radius = 10

screen = pygame.display.set_mode(screen_size) #crear la pantalla de pygame
clock = pygame.time.Clock() #se crea el reloj

game_over = False

#para ingresar una imagen de fondo
bacground = pygame.image.load("universo.png").convert() #el metodo convert facilita el trabajo a pygame para trabajar con imagenes

while not game_over:
    #para detectar los eventos
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            game_over = True
        #eventos de teclado
        #al presionar la tecla
        if event.type == pygame.KEYDOWN:
            #jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = speed_players*-1
            if event.key == pygame.K_s:
                player1_y_speed = speed_players
            #jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = speed_players*-1
            if event.key == pygame.K_DOWN:
                player2_y_speed = speed_players
        
        #al soltar la tecla
        if event.type == pygame.KEYUP:
            #jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            #jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    #rebote de pelota
    if ball_y > 590 or ball_y < 10:
        ball_speed_y *= -1

    #revisa si la pelota sale del lado derecho o izquierdo
    if ball_x >800 or ball_x < 0:
        ball_x = 400
        ball_y = 300
        ball_speed_x = 3
        ball_speed_y = 3
        #si sale de la pantalla invierte la direccion
        ball_speed_x *= -1
        ball_speed_y *=-1

    #modifica las coordenadas para dar moviniemto a la pelota y jugadores
    #jugador1
    player1_y_coor += player1_y_speed
    #jugador2
    player2_y_coor += player2_y_speed

    #movimiento pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    screen.blit(bacground, [0,0]) #dar el color a la pantalla

    #dibujando rectangulo player 1
    jugador_1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height)) #(contenedor del rectangulo, color, dimension)

    #dibujando rectangulo player 2
    jugador_2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height)) #(contenedor del rectangulo, color, dimension)

    #dibujando la pelota
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)

    #colisiones
    if ball.colliderect(jugador_1) or ball.colliderect(jugador_2):
        if ball_speed_x > 0 :
            ball_speed_x+=1
            ball_speed_y+=1
        else:
            ball_speed_x-=1
            ball_speed_y-=1
        player1_y_speed+=1
        player2_y_speed+=1
        ball_speed_x *= -1

    pygame.display.flip() #para actualizar la pantalla
    clock.tick(60) #esto le da los frames por segundo (fps)


pygame.quit()
