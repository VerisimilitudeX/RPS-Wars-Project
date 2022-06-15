"""
RPS Wars Project

1. Make this a 2-player game (Player 1: A [rock], S [paper], D [scissors] | Player 2: J [rock], K [paper], L [scissors])
2. Keep Score: The number of times a player wins will be displayed at the end
3. Each player gets a screen-clearing special move every 20 seconds (Player 1 KEY: Q | Player 2 KEY: O)
4. Multi-language support so that all can enjoy
5. Random player colors and fill window with the victorious player's random color
"""

import tsk, pygame, random

pygame.init()
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()
background = tsk.Sprite("TowerSiege.jpg", 0, 0)

player1 = []
player2 = []

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 255, 255), (132, 32, 21), (123, 43, 43), (212, 243, 121)]

index1 = random.randint(0, len(colors) - 1)
color_player_1 = colors[index1]

index2 = random.randint(0, len(colors) - 1)
color_player_2 = colors[index2]

player1_score = 0
player2_score = 0

player1_timer = 0
player2_timer = 0
time_limit = 2000

player1_move_timer = 0
player2_move_timer = 0
move_limit = 10000

player1_delete_timer = 0
player2_delete_timer = 0

del_limit = 5000

language = input("Please set the default language of this game (English, Spanish, Chinese, Hindi): ")

if language == "English" or language == "english":
    intro_y_n = input("Would you like to get a quick overview of RPS Wars? y/n ")

    if intro_y_n == "y" or intro_y_n == "Y" or intro_y_n == "yes" or intro_y_n == "Yes":
        print("Welcome to RPS Wars!")
        pygame.time.wait(2000)
        print("RULES AND FEATURES:")
        pygame.time.wait(2000)
        print("1. Player 1: A [rock], S [paper], D [scissors] | Player 2: J [rock], K [paper], L [scissors]")
        pygame.time.wait(6000)
        print("2. The number of times a player wins will be displayed at the end")
        pygame.time.wait(6000)
        print("3. Each player gets a special screen-clearing move every 20 seconds (Player 1 KEY: Q | Player 2 KEY: O")
        pygame.time.wait(6000)
        print("4. Multi-language support so that all can enjoy")
        pygame.time.wait(6000)
        print("5. Randomize player colors and fill window with the victorious player's random color")
        pygame.time.wait(6000)

    player1name = input("Please enter your name, Player 1: ")
    print("Welcome to the games, " + player1name)
    player2name = input("Please enter your name, Player 2: ")
    print("Welcome to you as well, " + player2name)
    print("Let the games begin!")

if language == "Spanish" or language == "spanish":
    intro_y_n = input("¿Te gustaría obtener una visión general rápida de RPS Wars? y/n ")
    
    if intro_y_n == "y" or intro_y_n == "Y" or intro_y_n == "Sí" or intro_y_n == "sí" or intro_y_n == "si":
        print("¡Bienvenido a RPS Wars!")
        pygame.time.wait(2000)
        print("REGLAS Y CARACTERÍSTICAS:")
        pygame.time.wait(2000)
        print("1. Jugador 1: A [roca], S [papel], D [tijeras] | Jugador 2: J [roca], K [papel], L [tijeras]")
        pygame.time.wait(6000)
        print("2. El número de veces que un jugador gana se mostrará al final")
        pygame.time.wait(6000)
        print("3. Cada jugador recibe un movimiento especial de limpieza de pantalla cada 20 segundos (Jugador 1 CLAVE: Q | Jugador 2 CLAVE: O")
        pygame.time.wait(6000)
        print("4. Soporte multilingüe para que todos puedan disfrutar")
        pygame.time.wait(6000)
        print("5. 5. Colores de jugador personalizados")
        pygame.time.wait(6000)

    player1name = input("Por favor, introduzca su nombre, Jugador 1:")
    print("Bienvenidos a los juegos, " + player1name)
    player2name = input("Por favor, introduzca su nombre, Jugador 2:")
    print("Bienvenido a usted también," + player2name)
    print("¡Que empiecen los juegos!")
    
if language == "Chinese" or language == "chinese":
    intro_y_n = input("您想快速了解RPS战争吗？ y/n ")
    
    if intro_y_n == "y" or intro_y_n == "Y" or intro_y_n == "yes" or intro_y_n == "Yes":
        print("欢迎来到RPS大战！")
        pygame.time.wait(2000)
        print("规则和功能：")
        pygame.time.wait(2000)
        print("1.玩家1：A[石头]，S[纸]，D[剪刀]|玩家 2： J [岩石]， K [纸]， L [剪刀]")
        pygame.time.wait(6000)
        print("2. 玩家获胜的次数在最后显示")
        pygame.time.wait(6000)
        print("3. 每个玩家每20秒获得一次特殊的屏幕清除动作（玩家1键：Q|玩家 2 键： O")
        pygame.time.wait(6000)
        print("4.多语言支持，让所有人都能享受")
        pygame.time.wait(6000)
        print("5. 个性化玩家颜色")
        pygame.time.wait(6000)
    
    player1name = input("请输入您的姓名，玩家 1：")
    print("欢迎来到游戏，" + player1name)
    player2name = input("请输入您的姓名，玩家 2: ")
    print("也欢迎您，" + player2name)
    print("让游戏开始吧！")
    
if language == "Hindi" or language == "hindi":
    intro_y_n = input("क्या आप आरपीएस युद्धों का एक त्वरित अवलोकन प्राप्त करना चाहेंगे? y/n ")
    
    if intro_y_n == "y" or intro_y_n == "Y" or intro_y_n == "yes" or intro_y_n == "Yes":
        print("आरपीएस युद्धों में आपका स्वागत है!")
        pygame.time.wait(2000)
        print("नियम और सुविधाएँ:")
        pygame.time.wait(2000)
        print("1. खिलाड़ी 1: एक [रॉक], एस [कागज], डी [कैंची] | खिलाड़ी 2: जे [रॉक], कश्मीर [कागज], एल [कैंची]")
        pygame.time.wait(6000)
        print("2. एक खिलाड़ी जीत की संख्या अंत में प्रदर्शित किया जा सकता है")
        pygame.time.wait(6000)
        print("3. प्रत्येक खिलाड़ी एक विशेष स्क्रीन समाशोधन हर 20 सेकंड (खिलाड़ी 1 कुंजी: क्यू | कदम हो जाता है खिलाड़ी 2 कुंजी: O")
        pygame.time.wait(6000)
        print("4. बहु भाषा समर्थन ताकि सभी का आनंद ले सकते हैं")
        pygame.time.wait(6000)
        print("5. खिलाड़ी रंग निजीकृत करें")
        pygame.time.wait(6000)
    
    player1name = input("कृपया अपना नाम दर्ज करें, प्लेयर 1: ")
    print("खेलों में आपका स्वागत है, " + player1name)
    player2name = input("कृपया अपना नाम दर्ज करें, प्लेयर 2: ")
    print("आपका भी स्वागत है, " + player2name)
    print("चलो खेल शुरू करते हैं!")

else:
    intro_y_n = input("Would you like to get a quick overview of RPS Wars? y/n ")

    if intro_y_n == "y" or intro_y_n == "Y" or intro_y_n == "yes" or intro_y_n == "Yes":
        print("Welcome to RPS Wars!")
        pygame.time.wait(2000)
        print("RULES AND FEATURES:")
        pygame.time.wait(2000)
        print("1. Player 1: A [rock], S [paper], D [scissors] | Player 2: J [rock], K [paper], L [scissors]")
        pygame.time.wait(6000)
        print("2. The number of times a player wins be displayed at the end")
        pygame.time.wait(6000)
        print("3. Each player gets a special screen-clearing move every 20 seconds (Player 1 KEY: Q | Player 2 KEY: O")
        pygame.time.wait(6000)
        print("4. Multi-language support so that all can enjoy")
        pygame.time.wait(6000)
        print("5. Randomize player colors and fill window with the victorious player's random color")
        pygame.time.wait(6000)
    
    player1name = input("Please enter your name, Player 1: ")
    print("Welcome to the games, " + player1name)
    player2name = input("Please enter your name, Player 2: ")
    print("Welcome to you as well, " + player2name)
    print("Let the games begin!")

playing = True
player1_win = False

while playing:
    player1_timer += c.get_time()
    player2_timer += c.get_time()
    player1_move_timer += c.get_time()
    player2_move_timer += c.get_time()
    player1_delete_timer += c.get_time()
    player2_delete_timer += c.get_time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.KEYDOWN:
            if player1_timer > time_limit:

                if event.key == pygame.K_a:
                    player1.append(tsk.Sprite("RPSRock.png", 100, 573//2))
                    player1_timer = 0

                if event.key == pygame.K_s:
                    player1.append(tsk.Sprite("RPSPaper.png", 100, 573//2))
                    player1_timer = 0

                if event.key == pygame.K_d:
                    player1.append(tsk.Sprite("RPSScissors.png", 100, 573//2))
                    player1_timer = 0

            if player2_timer > time_limit:
                if event.key == pygame.K_j:
                    player2.append(tsk.Sprite("RPSRock.png", 1018 - 200, 573//2))
                    player2_timer = 0

                if event.key == pygame.K_k:
                    player2.append(tsk.Sprite("RPSPaper.png", 1018 - 200, 573//2))
                    player2_timer = 0

                if event.key == pygame.K_l:
                    player2.append(tsk.Sprite("RPSScissors.png",  1018 - 200, 573//2))
                    player2_timer = 0         

                if len(player2) > 0:
                    player2[-1].flip_x = True          

            if player1_move_timer > move_limit:
                if event.key == pygame.K_q:
                    player1 = []
                    player2 = []
                    player1_move_timer = 0        

            if player2_move_timer > move_limit:
                if event.key == pygame.K_o:
                    player1 = []
                    player2 = []
                    player2_move_timer = 0

    background.draw()

    for i in player1:
        i.x += 0.15 * c.get_time()
        i.draw()
        if i.x > 1018:
            playing = False
            player1_win = True

        pygame.draw.circle(w, color_player_1, (i.center_x, i.center_y - 125), 25)  

    for j in player2:
        j.x -= 0.15 * c.get_time()
        j.draw()
        if j.x < 0 - 130:
            playing = False
            player1_win = False     
        
        pygame.draw.circle(w, color_player_2, (j.center_x, j.center_y - 125), 25)   

    player1_removal = None
    player2_removal = None

    for i in player1:
        for j in player2:
            if pygame.sprite.collide_rect(i, j):
                if i.image == "RPSPaper.png" and j.image == "RPSRock.png":
                    player2_removal = j
                    player1_score += 1

                elif i.image == "RPSRock.png" and j.image == "RPSPaper.png":
                    player1_removal = i
                    player2_score += 1

                elif i.image == "RPSScissors.png" and j.image == "RPSPaper.png":
                    player2_removal = j
                    player1_score += 1

                elif i.image == "RPSPaper.png" and j.image == "RPSScissors.png":
                    player1_removal = i
                    player2_score += 1

                elif i.image == "RPSRock.png" and j.image == "RPSScissors.png":
                    player2_removal = j
                    player1_score += 1

                elif i.image == "RPSScissors.png" and j.image == "RPSRock.png":
                    player1_removal = i
                    player2_score += 1 

    if not player1_removal == None:
        player1.remove(player1_removal)

    if not player2_removal == None:
        player2.remove(player2_removal)  

    pygame.display.flip()
    c.tick(30)

if language == "English" or language == "english":
    print(player1name + "'s Score: " + str(player1_score))
    print(player2name + "'s Score: " + str(player2_score))
    if player1_win:
        print("Congratulations " + player1name + "!")
        print("You won!")
        background.visible = False
        w.fill(color_player_1)
        input()
    else:
        print("Congratulations " + player2name + "!")
        print("You won!")
        background.visible = False
        w.fill(color_player_2)
        input()
        
if language == "Spanish" or language == "spanish":
    print(player1name + "'s Puntuación: " + str(player1_score))
    print(player2name + "'s Puntuación: " + str(player2_score))
    if player1_win:
        print("Congradaciones " + player1name + "!")
        print("¡Ganaste!")
        background.visible = False
        w.fill(color_player_1)
        input()
    else:
        print("Congradaciones " + player2name + "!")
        print("¡Ganaste!")
        background.visible = False
        w.fill(color_player_2)
        input()

if language == "Chinese" or language == "chinese":
    print(player1name + "'s 标点: " + str(player1_score))
    print(player2name + "'s 标点: " + str(player2_score))
    if player1_win:
        print("祝贺 " + player1name + "!")
        print("赢得！")
        background.visible = False
        w.fill(color_player_1)
        input()
    else:
        print("祝贺 " + player2name + "!")
        print("赢得！")
        background.visible = False
        w.fill(color_player_2)
        input()

if language == "Hindi" or language == "hindi":
    print(player1name + "'s अंक: " + str(player1_score))
    print(player2name + "'s अंक: " + str(player2_score))
    if player1_win:
        print("बधाइयाँ " + player1name + "!")
        print("आप जीत गए!")
        background.visible = False
        w.fill(color_player_1)
        input()
    else:
        print("बधाइयाँ " + player2name + "!")
        print("आप जीत गए!")
        background.visible = False
        w.fill(color_player_2)
        input()

else:
    print(player1name + "'s Score: " + str(player1_score))
    print(player2name + "'s Score: " + str(player2_score))
    if player1_win:
        print("Congratulations " + player1name + "!")
        print("You won!")
        background.visible = False
        w.fill(color_player_1)
        input()
    else:
        print("Congratulations " + player2name + "!")
        print("You won!")
        background.visible = False
        w.fill(color_player_2)
        input()
