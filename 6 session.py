'''مقداری تمرین برای حلقه ها
*
**
***
****
*****
******
خروجی به این شکل باشد'''

for i in range(1,7):
    for j in range(i):
        print('*',end='')
    print() 

#--------------------------------
'''عکس مثال بالا:
******
*****
****
***
**
*'''
for i in range(6,0,-1):
    for j in range(i):
        print('*',end='')
    print() 

#------------------------------
'''درست کردن بازی حدس عدد به روش دودویی
استفاده از کتابخانه random'''
import random 
r=random.randint(1,100)
for i in range(10):
    guss_number=int(input("Enter guss number 1_100 :"))
    if guss_number==r:
        print('you win')
        break
    elif guss_number>r:
        print ('big')
    else:
        print ('small')
        
'''درست کردن بازی حدس از بین حیوانات با کلمه '''
import random

animal = ['dog','panda','cow','tiger','zebra','horse','cat','eagle']
print(animal)
word = random.choice(animal)
l = len(word)*2 - 1
blank_word = list('_' * len(word))
wrong = 0

for i in range(l):
    guess = input('Enter your guess: ')
    if guess in word:
        for j in range(len(word)):
            if guess == word[j]:
                blank_word[j] = guess
    else:
        wrong += 1
        print('Wrong guess! Total wrong guesses:', wrong)
    print('Current word:', ' '.join(blank_word))
    if '_' not in blank_word:
        print('You win!')
        break
if '_' in blank_word:
    print('You lose! The word was:', word)

#_____________________________________________
'''دستور وایل تروwhile true'''
while True:
    n=int(input("Enter n for n^2:"))
    print(n**2)
    answer=input("(y/n)ایا همچنان بازی میکنی با خیر")
    if answer=='n' or answer=='N':
        break
    
#__________________________&_____________________

    