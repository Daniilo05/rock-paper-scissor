import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera: ')
  user_option = user_option.lower()

  if not user_option in options:
    print('esa opcion no es valida')
    #continue
    return None, None

  computer = random.choice(options)

  print('User options =>', user_option)
  print('Computer options =>', computer)
  return user_option, computer  
  
def check_rule(user_options, computer, user_wins, computer_wins):
  if user_options == computer:
    print('Empate')
  elif user_options == 'piedra' and computer == 'tijera':
    print('Ganaste')
    user_wins += 1
  elif user_options == 'papel' and computer == 'piedra':
    print('Ganaste')
    user_wins += 1
  elif user_options == 'tijera' and computer == 'papel':
    print('Ganaste')
    user_wins += 1
  else:
    print('Perdiste')
    computer_wins += 1
  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  if computer_wins == 3:
    print('El ganador es la computadora')
    

  if user_wins == 3:
    print('El ganador es el usuario')
    

def run_game():
  Rounds = 1
  computer_wins = 0
  user_wins = 0
  
  while True:
    print('*' * 30)
    print('ROUND', Rounds)
    print('*' * 30)
  
    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    Rounds += 1
  
    user_options, computer = choose_options()
    if user_options is None:
      continue

    
    user_wins, computer_wins = check_rule(user_options, computer,user_wins,     computer_wins)

    if user_wins == 3 or computer_wins == 3:
      check_winner(user_wins, computer_wins)
      paly_again = input('Desea jugar otra vez? (si/no): ')
      if paly_again.lower() != 'si':
        print('Gracias por jugar. Hasta luego')
        break
    
    Rounds += 1
  
run_game()