def decimal():
    """
    this function will find the decimal value of an array given in binary format

    ex:
    [0,0,0,0,0,0,0,1] = 00000001 = 1
    [0,0,0,0,0,0,1,1] = 00000011 = 3
    [0,0,0,0,0,1,1,1] = 00000111 = 7

    """
    #add you own array in here
    array1 = [0, 0, 1, 1]

    #basePair array is the powers of 2 needed to calculate decimal value
    basePair = [128, 64, 32, 16, 8, 4, 2, 1]

    lengthOfLineOrder = array1.__len__()

    #if the length of array1 is less than 8, this while loop will add 0's until there are 8 items in array1
    while lengthOfLineOrder < basePair.__len__():
        array1.insert(0, 0)
        lengthOfLineOrder = array1.__len__()
    
    #loops through array1 to find all of the values that equal to 1 and prints out the index
    addedDecimal = 0
    for index, value in enumerate(array1):
        print('the value is ' + str(value) + '; index is: ' + str(index))
        if value == 1:
            addedDecimal = addedDecimal + basePair[index]
    
    #similar to above but uses a traditional for loop
    # x = 0
    # counter = 0
    # for value in array1:
    #     if value == 1:
    #         x = x + basePair[counter]
    #
    #     counter += 1

    #returns the decimal value of array1

    return addedDecimal

print(decimal())
