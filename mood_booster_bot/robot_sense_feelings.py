feelings= {
        'good': ['good','fantastic', 'very well'],
        'bad': ['bad', 'not good', 'sad' , ' mad'],
        'ok': ['ok', 'fine', 'not sure']
    }
   
def y_or_n():
        carry_on = input(f'do you want to go again [Y/N]?')
       
        if carry_on == 'Y' or carry_on == 'y':
            print('Yay! I am so glad we can continue playing')
        else:
            print('Sorry to see you go')
            exit()
   
def handle_new_feeling(feeling, category ):

        if category in feelings.keys():
            feelings[category].append(feeling)
        else:
            print(f'I did not understand')
   
   
def handle_feeling(feeling):
        if feeling in feelings['good']:
            print(f'Glad to see you are feeling {feeling}')
        elif feeling in feelings['ok']:
            print('Reach for the stars!' )
        elif feeling in feelings['bad']:
             print(f'Oh, sorry to hear you are feeling {feeling} , Lets check your temperature ')
             temperature = input('what is your temperature?')
             check_temperature(temperature)
        else:
            category = input(f'I do not know what {feeling} is. Is it good / bad or ok ?')
            handle_new_feeling(feeling, category)

def check_temperature(temperature)  :
          temp = float(temperature)
          
          if temp > 39:
              print(f'Oh No - you have a high temperature, you may need some medicine and rest')
          elif temp > 38:
              print(f'You have a mild temperature! Take Rest now')
          elif temp > 36.4:
              print('Your temperature is good')
          else:
              print('Your temperature is too cold?')
   
while True:
        name = input('> What is your name?')
        print(f'Hello {name}, I am Robot.')
        feeling = input('> How are you feeling?')
        handle_feeling(feeling)
       
        y_or_n()
