def CheckSum(plate) -> str:
    
    multiplyprefix = [14, 2][::-1]
    multiplynumber = [12, 2, 11, 1][::-1]
    
    lettermap = {0: 'A', 1: 'Y', 2: 'U', 3: 'S', 4: 'P', 
                 5: 'L', 6: 'J', 7: 'G', 8: 'D', 9: 'B', 
                 10: 'Z', 11: 'X', 12: 'T', 13: 'R', 14: 'M',
                 15: 'K', 16: 'H', 17: 'E', 18: 'C'}
    
    if len(plate) < 2 or len(plate) > 8:
        return 'Invalid Input'
    
    prefix = ''
    number = ''
    for letter in plate:
        if letter.isalpha():
            prefix += letter.upper()
            if len(prefix) > 3:
                return 'Invalid Input'
        else:
            number = plate[len(prefix):len(plate)-1]
            checksum = plate[-1].upper()
            break
        
    if not prefix or not number or not number.isdigit() or len(number) > 4 or checksum.isdigit():
        return 'Invalid Input'
    
        
    while len(number) < 4:
        number = '0' + number
    
    result = 0
    prefix = prefix[-2:][::-1]
    for i in range(len(prefix)):
        letterasnum = ord(prefix[i]) - ord('A') + 1
        result += letterasnum * multiplyprefix[i]
        
    for i in range(4):
        result += int(number[::-1][i]) * multiplynumber[i]

    if lettermap[result % 19] == checksum:
        return 'Valid Plate'
    else:
        return 'Invalid Plate'