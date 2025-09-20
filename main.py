# Simple game in python

print('Hi, welcome to the python game class!')
print('Try to get as many questions correct as possible...')

totalQuestions = 100
score = 0

ans = input('1. What is my name? ')

if ans.lower() == 'max':
    print('ur cooking')
    score += 10
else:
    print('ur autistic')

ans = input('2. What is my age? ')

if ans == "12":
    print('oh ur frying')
    score += 20
else:
    print('u special')

ans = input('3. What is my favourite sport? ')

if ans.lower() == "soccer":
    print('oh my goodness u r boiling')
    score += 30
else:
    print('u have down syndrome')

ans = input('4. What is my favourite food? ')

if ans.lower() == "pasta":
    print('yeaaaaahhhh')
    score += 40
else:
    print('ur selling so hard')

print("Thanks for grinding this game " + str(score) + ' questions correct!')
percent = (score / totalQuestions) * 100
print("Max: " + str(int(percent)) + '% hooray u finished')

if percent >= 50:
    print('Great!ur not sped!')
else:
    print('U sold')













