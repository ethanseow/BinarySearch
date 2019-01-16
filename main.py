import random

min = 0
max = 100
while True:
  randNumber = random.randint(min,max)
  guess = input("Is your number " + str(randNumber) + ':')

  if guess == 'too small':
    min = randNumber + 1
    max = max
  elif guess == 'too big':
    max = randNumber - 1
    min = min
  elif guess == 'yes':
    break