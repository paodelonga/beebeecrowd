game_time = str(input())
game_hour = int(game_time.split(' ')[2]) - int(game_time.split(' ')[0])
game_min = int(game_time.split(' ')[3]) - int(game_time.split(' ')[1])

print(f"O JOGO DUROU {game_hour} HORA(S) E {game_min} MINUTO(S)")
