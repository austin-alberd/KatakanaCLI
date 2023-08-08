#library imports
from time import sleep as s
import random

#functions
def Convert(string):
    li = list(string.split(" "))
    return li

#initial game setup
print("________________________________________________________")
print("               Katakana Practice Application            ")
print(                    "By:Austin Alberd                    ")
print("________________________________________________________")
#print game instructions
print("Select your game mode  (flashcards or quiz)")

#set Data Structures for the Lists
KatakanaChars = ['ア a','カ ka','サ sa','タ ta','ナ na','ハ ha','マ ma','ヤ ya','ラ ra','ワ wa','ン n','ガ ga','ザ za','ダ da','バ ba','パ pa','ファ fa','ツァ tsa','イ i','キ ki','シ shi','チ chi','ニ ni''ヒ hi','ミ mi','リ ri','ギ gi','ジ ji','ヂ ji','ビ bi''ピ pi','フィ fi','ティ ti','ウ u','ク ku','ス su','ツ tsu','ム mu','ヌ nu','フ fu','ユ yu','ル ru','グ gu','ズ zu','ヅ zu','ブ bu','プ pu','トゥ tu','エ e','ケ ke','セ se','テ te','ネ ne','ヘ he','デ de','ベ be','メ me','レ re','ゲ ge','ゼ ze','ペ pe','フェ fe','ウェ we','オ o','コ ko','ソ so','ト to','ノ no','ホ ho','モ mo','ヨ yo','ロ ro','ゴ go','ゾ zo','ド do','ボ bo','ポ po','フォ fo','ウォ wo','キャ kya','シャ sha','チャ cha','ニャ nya','ヒャ hya','ミャ mya','リャ rya','ギャ gya','ジャ ja','ビャ bya','ピャ pya','キュ kyu','シュ shu','チュ chu','ニュ nyu','ヒュ hyu','ミュ myu','リュ ryu','ギュ guy','ジュ ju','ビュ byu','ピュ pyu','キョ kyo','ショ sho','チョ cho','ニョ nyo','ヒョ hyo','ミョ myo','リョ ryo','ギョ gyo','ジョ jo','ビョ byo','ピョ pyo']

#get the game mode from the player
gameMode = input("Select your game mode :>")
gameMode=gameMode.lower()



#flashcard game modes
if gameMode == "flashcards":
    #set game state
    gameIsPlaying=True
    #keep the totals
    correctCount=0
    wrongCount=0
    charCount=0
    while gameIsPlaying == True:
        for x in range(0,len(KatakanaChars)):
            #get the carecter answer combo , split it, and display it
            current = Convert(KatakanaChars[x])
            print(current[0])
            #get user input and process it
            action=input("Type the english translation of this charecter or select quit to leave the game. Select end to end the flashcards set :>")
            action = action.lower()
            #respond to the action
            if action == "quit":
                break
            if action == "end":
                correctCount= str(correctCount)
                wrongCount=str(wrongCount)
                charCount=str(charCount)
                print("You ended the game")
                print(f"You got {correctCount} correct")
                print(f"You got {wrongCount} wrong")
                break
            if action != "quit":
                if action == current[1]:
                    print("Yay! You got it correct!")
                    correctCount = correctCount+1
                    charCount=charCount+1
                if action !=current[1]:
                    print("You got it wrong. The right answer was "+current[1])
                    wrongCount=wrongCount+1
                    charCount=charCount+1
        print("Thank you for playing")
        break

#quiz game mode
if gameMode=="quiz":
    gameIsPlaying = True
    correct=0
    wrong=0
    print("Quiz Mode: Answer the questions and get your score type end to end the quiz early")
    for x in range (0,len(KatakanaChars)):
        current = Convert(KatakanaChars[x])
        print(current[0])
        answer = input("Type the english translation of this charecter :> ")
        if answer == current[1]:
            correct= correct+1
        if answer != current[1]:
            wrong = wrong+1
        if answer == "end":
            break
    total = correct+wrong
    percent = correct/total
    percent = percent*100
    print("Your Quiz results are ")
    print(f"Your score is {percent}%")