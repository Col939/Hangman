import random

foodWords = ["Pineapple", "Toast", "Pasta", "Orange"]

categories = ["foodWords"]

hints = ["It is a food"]

word = ""

categoryNum = 0

hiddenWord = []
strHiddenWord = ""

index = 0
  
def wordGuess():
  global hiddenWord
  global index
  global strHiddenWord
  print(hints[categoryNum - 1])
  for x in range(len(word)):
    hiddenWord.append("_ ")
  for x in hiddenWord:
    strHiddenWord += x  
    
  print(strHiddenWord)    
  wordI = input("Letter: \n")
  
  for x in word:
     if x.upper() == wordI:
         hiddenWord[index] = str(wordI)
         
     elif x.lower() == wordI:
         hiddenWord[index] = str(wordI)
     index += 1
     strHiddenWord = ""
  for x in hiddenWord:
    strHiddenWord += x  
    
  print(strHiddenWord)    

  
def wordGen():
  global word
  global categoryNum
  x = random.choice(categories)
  if x == categories[0]:
    word = random.choice(foodWords)
    categoryNum = 1
    
  wordGuess()
  
wordGen()  
