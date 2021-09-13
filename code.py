import random

foodWords = ["Pineapple", "Toast", "Pasta", "Orange"]

categories = ["foodWords"]

hints = ["It is a food"]

word = ""

categoryNum = 0

hiddenWord = []
strHiddenWord = ""

checkRepeat = False

index = 0
    
  
def wordGuess():
    global index
    global checkRepeat
    
    if checkRepeat == False: 
      global hiddenWord
      
      global strHiddenWord
      
      print(hints[categoryNum - 1])
      for x in range(len(word)):
        hiddenWord.append("_ ")
        
      for x in hiddenWord:
        strHiddenWord += x  
        
    print(strHiddenWord)  
         
    wordI = input("Letter: \n")
      
    for x in word:
    #   if x.upper() == wordI:
    #      hiddenWord[index] = str(wordI)
    #      index += 1
             
      if x.lower() == wordI:
         hiddenWord[index] = str(wordI)
         
      index += 1
         
    strHiddenWord = ""
      
    for x in hiddenWord:
      strHiddenWord += x  
         
    index = 0
    checkRepeat = True
    wordGuess()


  
def wordGen():
  global word
  global categoryNum
  x = random.choice(categories)
  if x == categories[0]:
    word = random.choice(foodWords)
    categoryNum = 1
    
  wordGuess()
  
wordGen()  
