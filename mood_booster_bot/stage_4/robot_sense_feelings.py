feelings= {
        'good': ['good','fantastic', 'very well'],
        'bad': ['bad', 'not good', 'sad' , 'mad'],
        'ok': ['ok', 'fine', 'not sure']
    }

while True:
    name = input('What is your name?')
    print(f'Hello {name}, I am Robot.')
    feeling = input('How are you feeling?')
    
    if feeling in feelings['good']:
          print(f'Glad to see you are feeling {feeling}')
    elif feeling in feelings['ok']:
          print('Reach for the stars!' )
    elif feeling in feelings['bad']:
          print(f'Oh, sorry to hear you are feeling {feeling} , Lets check your temperature ')
          temperature = input('what is your temperature?')

          temp = float(temperature)
          
          if temp > 39:
              print(f'Oh No - you have a high temperature, you may need some medicine and rest')
          elif temp > 38:
              print(f'You have a mild temperature! Take Rest now')
          elif temp > 36.4:
              print('Your temperature is good')
          else:
              print('Your temperature is too cold?')
    else:
          category = input(f'I do not know what {feeling} is. Is it good / bad or ok ?')
          if category in feelings.keys():
               feelings[category].append(feeling)
          else:
                print(f'I did not understand')
           
   
