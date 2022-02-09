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



def printNumCombinations(selectedCombinations):
    numbers = len(selectedCombinations.numbers)
    stars = len(selectedCombinations.stars)
    combinations = numbers*stars
    print("Total numbers: ", f'{numbers:,}')
    print("Total stars: ", stars)
    print("Total combinations: ", f'{combinations:,}')
    print(" ")




initationSelect()