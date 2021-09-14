import random
import sys

foodWords = ["Pineapple", "Toast", "Pasta", "Peach", "Pie", "Pizza", "Tomato"]

colorWords = ["Lime", "Magenta", "Yellow", "SkyBlue", "Grey", "Red"]

categories = ["foodWords", "colors"]

hints = ["It is a food", "It is a color"]

wrongLetters = []
strWrongLetters = ""

word = ""

categoryNum = 0

hiddenWord = []
strHiddenWord = ""

checkRepeat = False

index = 0

lives = 6

wrong = 0
    
def replay():
  global word
  global categoryNum
  global hiddenWord
  global strHiddenWord
  global checkRepeat
  global index
  global lives
  global wrongLetters
  global strWrongLetters
  
  
  word = ""

  categoryNum = 0

  hiddenWord = []
  strHiddenWord = ""

  checkRepeat = False

  index = 0
  
  lives = 6
  
  wrongLetters = []
  strWrongLetters = ""
  
  wordGen()
  
  
def wordGuess():
    global index
    global checkRepeat
    global lives
    global wrongLetters
    global wrong
    global wrongLetters
    global strWrongLetters
    
    if checkRepeat == False: 
      global hiddenWord
      
      global strHiddenWord
      
      print(hints[categoryNum - 1])
      for x in range(len(word)):
        hiddenWord.append("_ ")
        
      for x in hiddenWord:
        strHiddenWord += x  
        
    print(strHiddenWord)  
         
    wordI = input("\nLetter: \n")
      
    for x in word:
        
      if x.lower() == wordI:
          
          if index == 0:
            hiddenWord[index] = str(wordI).upper()  
          else:
            hiddenWord[index] = str(wordI).lower() 
         
      elif x.upper() == wordI:
          if index == 0:
            hiddenWord[index] = str(wordI).upper()  
          else:
            hiddenWord[index] = str(wordI).lower()  
       
      else:
          wrong += 1
      
      if wrong == len(word):
          wrongLetters.append(wordI)
          lives -= 1
         
      index += 1
    
    if lives == 0:
      sys.exit()   
    
    print("Lives: " + str(lives))
    
    for x in wrongLetters:
        strWrongLetters += x.lower() + " "
    
    print("\n" + strWrongLetters + "\n")    
    strWrongLetters = ""
    strHiddenWord = ""
    
    wrong = 0
      
    for x in hiddenWord:
      strHiddenWord += x  
         
    index = 0
    checkRepeat = True
    
    if strHiddenWord.upper() == word.upper():
        print(strHiddenWord)  
        print("\n" * 3)
        replay()
    else:
        wordGuess()


  
def wordGen():
  global word
  global categoryNum
  x = random.choice(categories)
  if x == categories[0]:
    word = random.choice(foodWords)
    categoryNum = 1
    
  if x == categories[1]:  
    word = random.choice(colorWords)
    categoryNum = 2
    
  wordGuess()
  
wordGen()  
