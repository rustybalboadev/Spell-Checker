from spellchecker import SpellChecker
import os
spell = SpellChecker()
choice = input("Use a [F]ile or input [T]ext? ").lower()
correctList = []
fileList = []
rightCounter = 0
wrongCounter = 0
total = 0
if choice == "t":
    text = str(input("Input the words "))
    textList = text.split(' ')
    for each in textList:
        print("Testing '{}'".format(each))
        correct = spell.correction(each)
        if each == correct:
            print("'{}' Is spelt correctly \n".format(each))
            correctList.append(each)
        elif each != correct:
            print("'{}' Is not spelt correctly. I think you meant '{}' \n".format(each, correct))
            print("Possible canidates: \n {} \n".format(spell.candidates(each)))
            correctList.append(correct)
    
    print("Corrected output: \n" + ' '.join(correctList))
#When done testing you can look at discord and replace
elif choice == "f":
    file_name = input("What is the name of the file? (include .txt)")
    output_name = input("output file name ") #keep this though
    testing = input("Is it seperated by [S]paces or [E]nters (New lines)? ").lower()
    f = open(file_name)
    if testing == "e":
        for each in f:
            fileList.append(each[0:-1])
    elif testing == "s":
        for each in f:
            fileList = each.split(' ')
    total = len(fileList)
    f.close()
    for word in fileList:
        print("Testing '{}'".format(word))
        correct = spell.correction(word)
        if word == correct:
            print("'{}' Is spelt correctly \n".format(word))
            correctList.append(word)
            wrongCounter += 1
        elif word != correct:
            print("'{}' Is not spelt correctly. I think you meant '{}' \n".format(word, correct))
            print("Possible canidates: \n {}".format(spell.candidates(word)))
            correctList.append(correct)
            rightCounter += 1
    f.close()
    os.system("rm {}".format(output_name))
    f = open(output_name,"w+")
    for each in correctList:
        f.writelines(each + "\n")
    f.close()
    print("Output: {} Misspelled: {} Spelled Correctly: {} Total Words: {}\n".format(output_name,rightCounter,wrongCounter,total))
    print("Corrected output: \n" + ' '.join(correctList))

