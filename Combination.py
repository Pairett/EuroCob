import itertools

class Combination:
    "EuroMillones combination"
    TOTAL_NUMBERS = 5
    TOTAL_STARS = 2
    SMALL_NUMBER = 1
    BIG_NUMBER = 50
    SMALL_STAR = 1
    BIG_STAR = 12

    def __init__(self):
        self.numbers = list()
        self.stars = list()
        self.value = 0
        self.values = list()
        self.desviation = 5
        
    #Select an Euromillones combination
    def selectValidCombination(self):
        self.numbers = self._selectCreat(self.SMALL_NUMBER, self.BIG_NUMBER, self.TOTAL_NUMBERS)
        self.stars = self._selectCreat(self.SMALL_STAR, self.BIG_STAR, self.TOTAL_STARS)
        return self
    
    #Creat al of combinations

    def _selectCreat(self, small, big, total):
        selecto = list()
        rango = range(small, big+1)

        selecto = itertools.combinations(rango, total)

        return list(selecto)
    
    #Delete all combination with a consecutive number

    def delValidConsecutive(self):
        self.numbers = self._delConsecutive(self.numbers)
        self.stars = self._delConsecutive(self.stars)
        return self

    def _delConsecutive(self, selecto):
        i = 0
        selecto_ = list()

        for selNum in selecto:
        
            noConseq = True
            y = 0

            while y<len(selNum)-1 and noConseq:
                if (selNum[y] - selNum[y+1]) == -1: #Check for consecutive numbers
                    noConseq = False
                else:
                    y+=1
            
            if noConseq == True:
                selecto_.append(selNum)                                

            i+=1
        
        return selecto_

    #Delete all even and odd combinations 

    def delValidEvenOdd(self):
        self.numbers = self._delEvenOdd(self.numbers, self.TOTAL_NUMBERS)
        self.stars = self._delEvenOdd(self.stars, self.TOTAL_STARS)
        return self

    def _delEvenOdd(self, selecto, total):
        selecto_ = list()
        
        for selNum in selecto:
            odd = 0
            even = 0

            for i in range(0, len(selNum)):
                if selNum[i]%2==0:
                    even+=1
                else:
                    odd+=1
            
            if even != total and odd != total:
                selecto_.append(selNum)
        
        return selecto_
            
    #Delete all combinations with his deviation of all numbers is less of 5

    def delValidDesviation(self):
        self.numbers = self._delDesviation(self.numbers, self.desviation)
        return self

    def _delDesviation(self, selecto, desviation):
        selecto_ = list()

        for selNum in selecto:
            c = (selNum[4] + selNum[3]) - (selNum[1] + selNum[0]) #I'm sure that is not the correct form to do this. But it works for me
            x = c/selNum[2]

            if x > desviation:
                selecto_.append(selNum)
            
        return selecto_


    def printAll(self):
        print("Total numbers: ", len(self.numbers))
        print("Total stars: ", len(self.stars))
        print("Numbers: ")
        for number in self.numbers:
            print("N")
            print(str(number[0]) + "+" + str(number[1])+ "+" + str(number[2])+ "+" + str(number[3])+ "+" + str(number[4]))

        print("Stars: ")
        for star in self.stars:
            print(str(star[0]) + "+" + str(star[1]))

        print("Value: ", self.value)
        print("Values: ", self.values)