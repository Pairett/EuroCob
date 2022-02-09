import random
import math

from Combination import Combination

__author__ = "Pairett"

def initationSelect():
    rightSelect = list()

    combination = Combination()
    rightSelect = combination.selectValidCombination()
    print("All possible combinations")
    print("-----------------------------------------------------")
    printNumCombinations(rightSelect)
    rightSelect = combination.delValidConsecutive()
    print("Eliminated consecutive combinations")
    print("-----------------------------------------------------")
    printNumCombinations(rightSelect)
    rightSelect = combination.delValidEvenOdd()
    print("Eliminate the combinations that all numbers are even and odd")
    print("-----------------------------------------------------")
    printNumCombinations(rightSelect)
    rightSelect = combination.delValidDesviation()
    print("Eliminate the combinations that have a very small difference between the numbers")
    print("-----------------------------------------------------")
    printNumCombinations(rightSelect)
    print("How much random combinations do you want?")
    quantity = int(input("Enter a number: "))
    randomCombinations(quantity, rightSelect)




def printNumCombinations(selectedCombinations):
    numbers = len(selectedCombinations.numbers)
    stars = len(selectedCombinations.stars)
    combinations = numbers*stars
    print("Total numbers: ", f'{numbers:,}')
    print("Total stars: ", stars)
    print("Total combinations: ", f'{combinations:,}')
    print(" ")

def randomCombinations(quantiti, selectedCombinations):
    numbers = len(selectedCombinations.numbers)
    stars = len(selectedCombinations.stars)
    while 0<quantiti:
        number = selectedCombinations.numbers[random.randint(0, numbers-1)]
        star = selectedCombinations.stars[random.randint(0, stars-1)]
        print("-----------------------------------------------------")
        print("Numbers {0} / Stars {1}".format(number, star))
        print(" ")
        quantiti-=1





initationSelect()