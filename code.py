import random

foodWords = ["Pineapple", "Toast", "Pasta", "Orange"]

categories = ["foodWords"]

hints = ["It is a food"]

word = ""

categoryNum = 0

hiddenWord = ""

index = 0
  
def wordGuess():
  global hiddenWord
  global index
  print(hints[categoryNum - 1])
  for x in range(len(word)):
    hiddenWord += "_ "

  print(hiddenWord)
  wordI = input("Letter: \n")
  
  for x in word:
     if x.upper() == wordI:
         hiddenWord[index] = str(wordI)
         
     elif x.lower() == wordI:
         hiddenWord[index] = str(wordI)
     index += 1
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
