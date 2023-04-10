import random

#Player guessing the number
def guess_random_number(tries, start, stop):
    random_number = random.randint(0, 10) 
    while True:
        if tries != 0:
            print("The number of tries remaining :", tries)
        interger = input("Guess a number betweeen 0 and 10: ")
        guess = int(interger)
        
        #Guessing random number
        if guess == random_number:
            print("You guessed correctly!")
            return
        if guess < random_number:
            tries -= 1
            print("You guessed :", guess)
            print("Guess higher!")
            
        if guess > random_number:
            tries -= 1
            print("You guessed :", guess)
            print("Guess lower!")
           
        if tries == 0:
            print("Failure")
            print("Target number is:", random_number)
            break

            
#Computer guessing the number                       
def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(0, 10)
    for _ in range(0,10):
        guess = random.randint(0, 10)
        if tries != 0:
            print("The number of tries remaining :", tries)
            
        #Guessing random number
        if guess == random_number:
            print("Target number", random_number)
            print ("Computer guessed:", guess)
            print("Computer guessed correctly!")
        if guess < random_number:
            print ("Computer guessed:", guess)
            print("Guess higher!")
            tries -= 1
        if guess > random_number:
            print ("Computer guessed:", guess)
            print("Guess lower!")
            tries -= 1 
         
        if tries == 0:
            print("Number of tries:", tries)
            print("Target number", random_number)
            print("No more tries, computer has failed")
            break

#Binary guessing
def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(0, 100)
    lower_bound = 0
    upper_bound = 100
    print("Random number to find:", random_number)
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound)// 2
        pivot_value = pivot
    
        # guessing if pivot = random number
        if pivot_value == random_number:
            print("Found it!", random_number)
            print("Number was found ")
        if pivot_value > random_number:
            print("Guess lower!")
            upper_bound = pivot - 1
            tries -= 1
        if pivot_value < random_number:
            tries -= 1
            print("Guess higher!")
            lower_bound = pivot + 1
        if tries == 0:
            print("Number of tries:", tries)
            print("No more tries")
            break
    
        
   

guess_random_num_binary(5, 0, 100)
guess_random_number(5, 0, 10)
guess_random_num_linear(5, 0, 10)




    