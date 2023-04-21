from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import *
import sys
from letterDrawer import setLetterRadius, drawOuterCircle, drawTypeOne, drawTypeTwo, drawTypeThree, drawTypeFour
import turtle as t
import math


##  WINDOW PARAMETERS
xpos = 50
ypos = 50
width = 400
height = 300

ERROR_MESSAGE = ""

class GallifreyanTranslator(QMainWindow):
    def __init__(self):
        super(GallifreyanTranslator, self).__init__()
        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle('Circular Gallifreyan Generator')
        self.initUI()

    def initUI(self):
        self.enterWord = QtWidgets.QLabel(self)
        self.enterWord.setText('Enter Word:')
        self.enterWord.move(50, 25)
        self.enterWord.adjustSize()

        self.wordEntry = QtWidgets.QLineEdit(self)
        self.wordEntry.move(75, 55)
        self.wordEntry.setMinimumWidth(250)

        self.doubleConsonants = QtWidgets.QCheckBox(self)
        self.doubleConsonants.setText('Doubled Consonants?')
        self.doubleConsonants.move(100, 100)
        self.doubleConsonants.adjustSize()

        self.attachedVowels = QtWidgets.QCheckBox(self)
        self.attachedVowels.setText('Attached Vowels?')
        self.attachedVowels.setChecked(True)
        self.attachedVowels.move(100, 125)
        self.attachedVowels.adjustSize()

        self.goButton = QtWidgets.QPushButton(self)
        self.goButton.setText('GO!')
        self.goButton.move(100, 150)
        self.goButton.clicked.connect(self.getData)

    def getData(self):
        global WORD
        WORD = self.wordEntry.text()
        WORD = WORD.lower()
        letterList = []
        outputList = []
        global ERROR_MESSAGE
        ERROR_MESSAGE = ""

        allLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        vowels = ['a', 'e', 'i', 'o', 'u']
        specials = ['ch', 'ph', 'wh', 'sh', 'th', 'qu', 'ng', 'gh']
        errors = [' ', 'c']

        for letter in WORD:
            letterList.append(letter)

        n = 0
        wordLength = len(letterList)
        while n < wordLength:
            letter = letterList[n]
            if n < wordLength - 1:
                nextLetter = letterList[n + 1]
            else:
                nextLetter = 'null'
            specialCheck = letter + nextLetter

            if letter in vowels:
                if self.attachedVowels.isChecked():
                    if n >= 1:
                        previousLetter = letterList[n - 1]
                        if previousLetter in vowels:
                            outputList.append(letter)
                else:
                    outputList.append(letter)
            elif specialCheck in specials:
                outputList.append(specialCheck)
                letterList.pop(n + 1)
                wordLength -= 1
            elif letter == nextLetter and self.doubleConsonants.isChecked():
                outputList.append(specialCheck)
                letterList.pop(n + 1)
                wordLength -= 1
            
            elif letter in errors or (letter not in allLetters):
                if letter == "c":
                    ERROR_MESSAGE = "Please use 's' or 'k' instead of 'c'."
                elif letter == " ":
                    ERROR_MESSAGE = "Please enter a single word."
                else:
                    ERROR_MESSAGE = "Please do not enter numbers or special characters."     
               
            else:
                outputList.append(letter)
            n += 1
        if ERROR_MESSAGE == "":
            self.writeWord(outputList)
        else:
            self.pop = ErrorMessage()
            self.pop.show()

    def getListWithVowels(self, LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE):
        global WORD
        WORD = self.wordEntry.text()
        WORD = WORD.lower()
        letterList = []
        outputListVowel = []
        errorMessage = ""

        allLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        vowels = ['a', 'e', 'i', 'o', 'u']
        specials = ['ch', 'ph', 'wh', 'sh', 'th', 'qu', 'ng', 'gh']
        errors = [' ', 'c']

        for letter in WORD:
            letterList.append(letter)

        n = 0
        wordLength = len(letterList)
        while n < wordLength:
            letter = letterList[n]
            if n < wordLength - 1:
                nextLetter = letterList[n + 1]
            else:
                nextLetter = 'null'
            specialCheck = letter + nextLetter

            if letter in vowels:
                outputListVowel.append(letter)
            elif specialCheck in specials:
                outputListVowel.append(specialCheck)
                letterList.pop(n + 1)
                wordLength -= 1
            elif letter == nextLetter and self.doubleConsonants.isChecked():
                outputListVowel.append(specialCheck)
                letterList.pop(n + 1)
                wordLength -= 1
                        
            else:
                outputListVowel.append(letter)
            n += 1
        if errorMessage == "":
            self.writeVowels(outputListVowel, LETTERRADIUS, LETTERANGLE, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE)

    def writeWord(self, outputList):
        OUTERRADIUS = 200
        NUMCONSONANTS = len(outputList)
        LETTERRADIUS = setLetterRadius(OUTERRADIUS, NUMCONSONANTS)
        LETTERANGLE = 360 / NUMCONSONANTS
        TYPEONEDISTANCE = OUTERRADIUS + LETTERRADIUS / 20
        TYPETWODISTANCE = OUTERRADIUS + (-15)
        TYPETHREEFOURDISTANCE = (math.sqrt(OUTERRADIUS ** 2 - LETTERRADIUS ** 2)) + LETTERRADIUS
        typeOne = ['b', 'ch', 'd', 'g', 'h', 'f']
        doubleOne = ['bb', 'dd', 'gg', 'hh', 'ff']
        typeTwo = ['j', 'ph', 'k', 'l', 'n', 'p', 'm']
        doubleTwo = ['jj', 'kk', 'll', 'nn', 'pp', 'mm']
        typeThree = ['t', 'wh', 'sh', 'r', 'v', 'w', 's']
        doubleThree = ['tt', 'rr', 'vv', 'ww', 'ss']
        typeFour = ['th', 'gh', 'y', 'z', 'qu', 'x', 'ng']
        doubleFour = ['yy', 'zz', 'xx']
        drawOuterCircle()
        n = 0
        while n < NUMCONSONANTS:
            letterRing = t.Turtle()
            letterRing.width(6)
            letterRing.hideturtle()
            letterRing.speed(0)
            letterRing.penup()
            letterRing.seth(n * LETTERANGLE - 90)
            marker = t.Turtle()
            marker.width(6)
            marker.color('red')
            marker.speed(0)
            marker.hideturtle()
            marker.penup()
            marker.seth(n * LETTERANGLE - 90)
            if outputList[n] in typeOne:
                drawTypeOne(letterRing, marker, TYPEONEDISTANCE, LETTERRADIUS, False)
                self.consonantAccent(outputList[n], n, LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE)
            elif outputList[n] in typeTwo:
                drawTypeTwo(letterRing, TYPETWODISTANCE, LETTERRADIUS, False)
                self.consonantAccent(outputList[n], n, LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE)
            elif outputList[n] in typeThree:
                drawTypeThree(letterRing, marker, TYPETHREEFOURDISTANCE, LETTERRADIUS, False)
                self.consonantAccent(outputList[n], n, LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE)
            elif outputList[n] in typeFour:
                drawTypeFour(letterRing, TYPETHREEFOURDISTANCE, LETTERRADIUS, False)
                self.consonantAccent(outputList[n], n, LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE)
            elif outputList[n] in doubleOne:
                drawTypeOne(letterRing, marker, TYPEONEDISTANCE, LETTERRADIUS, True)
                self.consonantAccent(outputList[n], n, LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE)
            elif outputList[n] in doubleTwo:
                drawTypeTwo(letterRing, TYPETWODISTANCE, LETTERRADIUS, True)
                self.consonantAccent(outputList[n], n, LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE)
            elif outputList[n] in doubleThree:
                drawTypeThree(letterRing, marker, TYPETHREEFOURDISTANCE, LETTERRADIUS, True)
                self.consonantAccent(outputList[n], n, LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE)
            elif outputList[n] in doubleFour:
                drawTypeFour(letterRing, TYPETHREEFOURDISTANCE, LETTERRADIUS, True)
                self.consonantAccent(outputList[n], n, LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE)
            n += 1

        self.getListWithVowels(LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE)


        screen = t.Screen()
        screen.exitonclick()

    def consonantAccent(self, letter, consonantNumber,LETTERANGLE, LETTERRADIUS, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE):
        typeOne = ['b', 'ch', 'd', 'g', 'h', 'f', 'bb', 'dd', 'gg', 'hh', 'ff']
        typeTwo = ['j', 'ph', 'k', 'l', 'n', 'p', 'm', 'jj', 'kk', 'll', 'nn', 'pp', 'mm']
        typeThree = ['t', 'wh', 'sh', 'r', 'v', 'w', 's', 'tt', 'rr', 'vv', 'ww', 'ss']
        typeFour = ['th', 'gh', 'y', 'z', 'qu', 'x', 'ng', 'yy', 'zz', 'xx']
        empty = ['b', 'j', 't', 'th']
        oneDot = ['ph', 'wh', 'gh']
        twoDot = ['ch', 'k', 'kk', 'sh', 'y', 'yy']
        threeDot = ['d', 'dd', 'l', 'll', 'r', 'rr', 'z', 'zz']
        oneLine = ['g', 'gg', 'n', 'nn', 'v', 'vv', 'qu']
        twoLine = ['h', 'hh', 'p', 'pp', 'w', 'ww', 'x', 'xx']
        threeLine = ['f', 'ff', 'm', 'mm', 's', 'ss', 'ng']

        accentArtist = t.Turtle()
        accentArtist.width(6)
        accentArtist.hideturtle()
        accentArtist.speed(0)
        accentArtist.penup()

        
        if letter in typeOne:
            dotDistance = TYPEONEDISTANCE + 10 - (2 * LETTERRADIUS)
            lineDistance = TYPEONEDISTANCE - (2 * LETTERRADIUS)
        elif letter in typeTwo:
            dotDistance = TYPETWODISTANCE + 10 - (2 * LETTERRADIUS)
            lineDistance = TYPETWODISTANCE - (2 * LETTERRADIUS)
        else:
            dotDistance = TYPETHREEFOURDISTANCE + 10 - (2 * LETTERRADIUS)
            lineDistance = TYPETHREEFOURDISTANCE - (2 * LETTERRADIUS)

        if letter in oneDot or letter in twoDot or letter in threeDot:
            accentArtist.seth(consonantNumber * LETTERANGLE - 90)
            accentArtist.forward(dotDistance)
            accentArtist.pendown()
            accentArtist.circle(3)
            if letter in twoDot or letter in threeDot:
                accentArtist.penup()
                accentArtist.forward(LETTERRADIUS - 20)
                accentArtist.right(180 + 45)
                accentArtist.forward(LETTERRADIUS - 20)
                accentArtist.pendown()
                accentArtist.circle(3)
                if letter in threeDot:
                    accentArtist.penup()
                    accentArtist.backward(LETTERRADIUS - 20)
                    accentArtist.right(38)
                    accentArtist.forward(LETTERRADIUS - 20)
                    accentArtist.pendown()
                    accentArtist.circle(3)
        
        if letter in oneLine or letter in twoLine or letter in threeLine:
            accentArtist.seth(consonantNumber * LETTERANGLE - 90)
            accentArtist.forward(lineDistance)
            accentArtist.pendown()
            accentArtist.circle(1.5)
            if letter in twoLine or letter in threeLine:
                accentArtist.penup()
                accentArtist.forward(LETTERRADIUS)
                accentArtist.right(180 + 25)
                accentArtist.forward(LETTERRADIUS)
                accentArtist.pendown()
                accentArtist.circle(1.5)
                if letter in threeLine:
                    accentArtist.penup()
                    accentArtist.backward(LETTERRADIUS)
                    accentArtist.left(50)
                    accentArtist.forward(LETTERRADIUS)
                    accentArtist.pendown()
                    accentArtist.circle(1.5)
       
    def writeVowels(self, outputListVowel, LETTERRADIUS, LETTERANGLE, TYPEONEDISTANCE, TYPETWODISTANCE, TYPETHREEFOURDISTANCE):
        vowels = ['a', 'e', 'i', 'o', 'u']
        typeOne = ['b', 'ch', 'd', 'g', 'h', 'f', 'bb', 'dd', 'gg', 'hh', 'ff']
        typeTwo = ['j', 'ph', 'k', 'l', 'n', 'p', 'm', 'jj', 'kk', 'll', 'nn', 'pp', 'mm']
        typeThree = ['t', 'wh', 'sh', 'r', 'v', 'w', 's', 'tt', 'rr', 'vv', 'ww', 'ss']
        typeFour = ['th', 'gh', 'y', 'z', 'qu', 'x', 'ng', 'yy', 'zz', 'xx']
        letterArtist = t.Turtle()
        letterArtist.hideturtle()
        letterArtist.width(5)
        letterArtist.speed(0)
        letterArtist.penup()

        n = 0
        c = 0
        listLength = len(outputListVowel)
        vowelDistance = 0

        while n < listLength:
            if outputListVowel[n] in vowels:
                if self.attachedVowels.isChecked():
                    if n >= 1:
                        previousLetter = outputListVowel[n-1]
                        if previousLetter not in vowels:
                            if previousLetter in typeOne:
                                vowelDistance = TYPEONEDISTANCE - LETTERRADIUS
                            elif previousLetter in typeTwo:
                                vowelDistance = TYPETWODISTANCE - LETTERRADIUS
                            else:
                                vowelDistance = 200
                            if outputListVowel[n] == 'a':
                                vowelDistance = 220
                                letterArtist.seth((c - 1) * LETTERANGLE - 90)
                                letterArtist.forward(vowelDistance)
                                letterArtist.pendown()
                                letterArtist.circle(10)
                                letterArtist.penup()
                                letterArtist.home()
                            elif outputListVowel[n] == 'e':
                                letterArtist.seth((c - 1) * LETTERANGLE - 90)
                                letterArtist.forward(vowelDistance)
                                letterArtist.pendown()
                                letterArtist.circle(10)
                                letterArtist.penup()
                                letterArtist.home()
                            elif outputListVowel[n] == 'i':
                                letterArtist.seth((c - 1) * LETTERANGLE - 90)
                                letterArtist.forward(vowelDistance)
                                letterArtist.pendown()
                                letterArtist.circle(10)
                                letterArtist.penup()
                                letterArtist.left(90)
                                letterArtist.forward(10)
                                letterArtist.left(90)
                                letterArtist.forward(10)
                                letterArtist.pendown()
                                letterArtist.circle(2)
                                letterArtist.penup()
                                letterArtist.home()
                            elif outputListVowel[n] == 'o':
                                letterArtist.seth((c - 1) * LETTERANGLE - 90)
                                letterArtist.forward(vowelDistance)
                                letterArtist.left(120)
                                letterArtist.forward(LETTERRADIUS)
                                letterArtist.pendown()
                                letterArtist.circle(10)
                                letterArtist.penup()
                                letterArtist.home()
                            elif outputListVowel[n] == 'u':
                                letterArtist.seth((c - 1) * LETTERANGLE - 90)
                                letterArtist.forward(vowelDistance)
                                letterArtist.pendown()
                                letterArtist.circle(10)
                                letterArtist.penup()
                                letterArtist.left(90)
                                letterArtist.forward(10)
                                letterArtist.left(90)
                                letterArtist.backward(10)
                                letterArtist.pendown()
                                letterArtist.circle(2)
                                letterArtist.penup()
                                letterArtist.home()
                        if outputListVowel[n] in vowels and previousLetter in vowels:
                            c += 1
                            if outputListVowel[n] == 'a':
                                vowelDistance = 220
                                letterArtist.seth((c - 1) * LETTERANGLE - 90)
                                letterArtist.forward(vowelDistance)
                                letterArtist.pendown()
                                letterArtist.circle(10)
                                letterArtist.penup()
                                letterArtist.home()
                            elif outputListVowel[n] == 'e':
                                vowelDistance = 200
                                letterArtist.seth((c - 1) * LETTERANGLE - 90)
                                letterArtist.forward(vowelDistance)
                                letterArtist.pendown()
                                letterArtist.circle(10)
                                letterArtist.penup()
                                letterArtist.home()
                            elif outputListVowel[n] == 'i':
                                vowelDistance = 200
                                letterArtist.seth((c - 1) * LETTERANGLE - 90)
                                letterArtist.forward(vowelDistance)
                                letterArtist.pendown()
                                letterArtist.circle(10)
                                letterArtist.penup()
                                letterArtist.left(90)
                                letterArtist.forward(10)
                                letterArtist.left(90)
                                letterArtist.forward(10)
                                letterArtist.pendown()
                                letterArtist.circle(2)
                                letterArtist.penup()
                                letterArtist.home()
                            elif outputListVowel[n] == 'o':
                                vowelDistance = 180
                                letterArtist.seth((c - 1) * LETTERANGLE - 90)
                                letterArtist.forward(vowelDistance)
                                letterArtist.left(120)
                                letterArtist.forward(LETTERRADIUS)
                                letterArtist.pendown()
                                letterArtist.circle(10)
                                letterArtist.penup()
                                letterArtist.home()
                            elif outputListVowel[n] == 'u':
                                vowelDistance = 200
                                letterArtist.seth((c - 1) * LETTERANGLE - 90)
                                letterArtist.forward(vowelDistance)
                                letterArtist.pendown()
                                letterArtist.circle(10)
                                letterArtist.penup()
                                letterArtist.left(90)
                                letterArtist.forward(10)
                                letterArtist.left(90)
                                letterArtist.backward(10)
                                letterArtist.pendown()
                                letterArtist.circle(2)
                                letterArtist.penup()
                                letterArtist.home()
                        
                    else:
                        c += 1
                else:
                    vowelDistance = 200
                    c += 1
                    if outputListVowel[n] == 'a':
                        vowelDistance = 220
                        letterArtist.seth((c - 1) * LETTERANGLE - 90)
                        letterArtist.forward(vowelDistance)
                        letterArtist.pendown()
                        letterArtist.circle(10)
                        letterArtist.penup()
                        letterArtist.home()
                    elif outputListVowel[n] == 'e':
                        vowelDistance = 200
                        letterArtist.seth((c - 1) * LETTERANGLE - 90)
                        letterArtist.forward(vowelDistance)
                        letterArtist.pendown()
                        letterArtist.circle(10)
                        letterArtist.penup()
                        letterArtist.home()
                    elif outputListVowel[n] == 'i':
                        vowelDistance = 200
                        letterArtist.seth((c - 1) * LETTERANGLE - 90)
                        letterArtist.forward(vowelDistance)
                        letterArtist.pendown()
                        letterArtist.circle(10)
                        letterArtist.penup()
                        letterArtist.left(90)
                        letterArtist.forward(10)
                        letterArtist.left(90)
                        letterArtist.forward(10)
                        letterArtist.pendown()
                        letterArtist.circle(2)
                        letterArtist.penup()
                        letterArtist.home()
                    elif outputListVowel[n] == 'o':
                        vowelDistance = 180
                        letterArtist.seth((c - 1) * LETTERANGLE - 90)
                        letterArtist.forward(vowelDistance)
                        letterArtist.left(120)
                        letterArtist.forward(LETTERRADIUS)
                        letterArtist.pendown()
                        letterArtist.circle(10)
                        letterArtist.penup()
                        letterArtist.home()
                    elif outputListVowel[n] == 'u':
                        vowelDistance = 200
                        letterArtist.seth((c - 1) * LETTERANGLE - 90)
                        letterArtist.forward(vowelDistance)
                        letterArtist.pendown()
                        letterArtist.circle(10)
                        letterArtist.penup()
                        letterArtist.left(90)
                        letterArtist.forward(10)
                        letterArtist.left(90)
                        letterArtist.backward(10)
                        letterArtist.pendown()
                        letterArtist.circle(2)
                        letterArtist.penup()
                        letterArtist.home()
            else:
                c += 1
            n +=1
    

class ErrorMessage(QWidget):
    def __init__(self):
        super(ErrorMessage, self).__init__()
        self.setGeometry(100, 100, 300, 50)
        self.setWindowTitle('Error')
        self.Error_initUI()
    
    def Error_initUI(self):
        global ERROR_MESSAGE
        localErrorMessage = ERROR_MESSAGE
        self.errorMessageLabel = QtWidgets.QLabel(self)
        self.errorMessageLabel.setText(localErrorMessage)
    
       


def window():
    app = QApplication(sys.argv)
    win = GallifreyanTranslator()

    win.show()

    sys.exit(app.exec_())

window()