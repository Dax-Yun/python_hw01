# Simple game in python

print('Hi, welcome to the python game class!')
print('Try to get as many questions correct as possible...')

totalQuestions = 22
score = 0

ans = input('1. What is the name of my class? ')

if ans.lower() == 'imagination lab':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('2. What is my age? ')

if ans == "42":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('3. What is my favourite sport? ')

if ans.lower() == "basketball":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('4. What is my favourite food? ')

if ans.lower() == "pizza":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('5. What is 12x14? ')
if ans.lower() == "168":
    print('Correct!')
    score += 1
else:
    print('incorrect')

ans = input('6. mm pizza ')

if ans.lower() == "pizza":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('7. what is the name of this question? ')

if ans.lower() == "7":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('8. what is a  ? ')

if ans.lower() == "space":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('9. Lets play simon says! simon says the answer to this question is lveel? ')

if ans.lower() == "level":
    print('Correct!')
    score += 1
else:
    print('HAHAHA GET TRICKED IT WAS LEVEL')

ans = input('10. Simon says the answer to this question is not to answer it. ')

if ans.lower() == "not to answer it.":
    print('Correct!')
    score += 1
else:
    print('HOW did you get this incorrect')

ans = input('11. What was the answer to problem 7? ')

if ans.lower() == "7":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('12. What was the answer to question 6? ')

if ans.lower() == "pizza":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('13. what was the secret code in question 9? ')

if ans.lower() == "lveel":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('say pizza ')

if ans.lower() == "pizza":
    print('Correct!yay!!!!                                                ')
    score += 1
else:
    print('Incorrect')

ans = input('the answer of last questions 6,7,9,10 and 13 will be the correct answers from here to the next 5 questions ')

if ans.lower() == "pizza":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
ans = input('16. what can be the result of a 4+3? ')

if ans.lower() == "7":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
ans = input('24. what is a different word for stage? ')

if ans.lower() == "level":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
ans = input('14. What should you do to this question? ')

if ans.lower() == "not to answer it.":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
ans = input('17. What is a anagram for level? ')

if ans.lower() == "lveel":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
ans = input('what is the answer to 2034x301924? i bet its not pizza! ')

if ans.lower() == "pizza":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
ans = input('what is the number of this question? ')

if ans.lower() == "21":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('NOW FOR THE FINAL QUESTION. THE ANSWER MIGHT BE IN PLAIN SIGHT. ')

if ans.lower() == "in plain sight.":
    print('Correct!')
    score += 1
else:
    print('WRONG')


if score >= 10:
    print('your score was over 10!!')
else:
    print('Better luck next time! your score was less then 10.')

print("Thank you for playing, you got " + str(score) + ' questions correct!')
percent = (score / totalQuestions) * 100
print("Mark: " + str(int(percent)) + '%')

if percent >= 50:
    print('Nice! You passed!')
else:
    print('Better luck next time')













