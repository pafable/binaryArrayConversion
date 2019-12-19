class Conversion:
    def __init__(self):
        """
        this function will find the decimal value of an array given in binary format
        ex:
        [0,0,0,0,0,0,0,1] = 00000001 = 1
        [0,0,0,0,0,0,1,1] = 00000011 = 3
                  [1,1,1] = 00000111 = 7
        """
        #add you own array in here
        self.array1 = [1, 0, 0, 0, 0, 0, 1, 1]

        #basePair array is the powers of 2 needed to calculate decimal value
        self.basePair = [128, 64, 32, 16, 8, 4, 2, 1]

        self.lengthOfLineOrder = self.array1.__len__()

        #if the length of array1 is less than 8, this while loop will add 0's until there are 8 items in array1
        while self.lengthOfLineOrder < self.basePair.__len__():
            self.array1.insert(0, 0)
            self.lengthOfLineOrder = self.array1.__len__()

        #loops through array1 to find all of the values that equal to 1 and prints out the index
        self.addedDecimal = 0
        for index, value in enumerate(self.array1):
            #print('the value is ' + str(value) + '; index is: ' + str(index))
            if value == 1:
                self.addedDecimal = self.addedDecimal + self.basePair[index]

def Func1():
    return Conversion()

print("Binary = " + str(Func1().array1) + "  ==  " + "Decimal = " + str(Func1().addedDecimal))
