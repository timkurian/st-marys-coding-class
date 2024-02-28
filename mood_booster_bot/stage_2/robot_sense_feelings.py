name = input('What is your name?')
print(f'Hello {name}, I am Robot.')
feeling = input('How are you feeling?')

if feeling == 'good':
  print(f'Glad to see you are feeling {feeling}')
elif feeling == 'bad':
  print(f'Sorry to see you are feeling {feeling}')
else:
  print(f'Oh - you are feeling: {feeling}')
