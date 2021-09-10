import random

foodWords = ["Pineapple", "Toast", "Pasta", "Orange"]

categories = ["foodWords"]

hints = ["It is a food"]

word = ""

categoryNum = 0

hiddenWord = ""
  
def wordGuess():
  global hiddenWord
  print(hints[categoryNum - 1])
  for x in range(len(word)):
    hiddenWord += "_ "

  wordI = input("Letter: \n")
  
  for x in word:
     if x.upper() == wordI:
         hiddenWord[x] = wordI
         
     elif x.lower() == wordI:
         print("hi")
         
  print(hiddenWord)
  
  
def wordGen():
  global word
  global categoryNum
  x = random.choice(categories)
  if x == categories[0]:
    word = random.choice(foodWords)
    categoryNum = 1
    
  wordGuess()
  
wordGen()  
