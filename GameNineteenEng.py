#The of the game "19"

a = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 1, 1, 2, 1, 3, 1, 4, 1],
     [5, 1, 6, 1, 7, 1, 8, 1, 9]]
len1 = a[0]
len2 = a[1]
len3 = a[2]



# the entered coordinates go to the input, and 2 points exit
def personal_coord(x1, y1, x2, y2):
    point_one1 = a[x1 - 1][y1 - 1]
    point_two2 = a[x2 - 1][y2 - 1]
    return point_one1, point_two2


# used when couples is 0
# make sure that in each line there are 9 characters, if possible.
def update_matrix():
    while ((len(len2) > 0) and len(len1) != 9) or ((len(len3) > 0) and (len(len2) != 9)):
        while (len(len3) > 0) and (len(len2) != 9):
            point_now1 = a[2][0]
            del a[2][0]
            a[1].extend([point_now1])
        while (len(len2) > 0) and (len(len1) != 9):
            point_now2 = a[1][0]
            del a[1][0]
            a[0].extend([point_now2])


# delete crossed out pairs
def delete_hyphen():
    for i in a:
        while '-' in i:
            i.remove('-')


# The intelligence of a computer counts how many various pairs are left.
# sum - number of couples
# j - meaningless variable indicating in which row the computer is now
# Iterates over the numbers from 0 to the penultimate one, and compares it with the right and the bottom.
def computer_intelligence():
    sum = 0
    j = 0
    while j == 0:
        try:
            for i, e in enumerate(a[j]):
                del e
                try:
                    b = a[j][i]
                    if (str(b).isdigit()) and (a[j][i+1] == '-'):
                        i += 1
                        while a[j][i] == '-':
                            i+=1
                        c = a[j][i]
                        if (b + c == 10) or (b == c):
                            sum += 1
                except IndexError:
                    continue
        except IndexError:
            continue
        try:
            for i, e in enumerate(a[j]):
                del e
                try:
                    if (a[j][i] == a[j][i + 1]) or (a[j][i] + a[j][i + 1] == 10):
                        if (a[j][i] == '-') or (a[j][i + 1] == '-'):
                            continue
                        else:
                            sum += 1
                except (IndexError, TypeError):
                    try:
                        if (a[j][i] == a[j + 1][i]) or (a[j][i] + a[j + 1][i] == 10):
                            if (a[j][i] == '-') or (a[j + 1][i] == '-'):
                                continue
                            else:
                                sum += 1
                    except (IndexError, TypeError):
                        continue
                    continue
                try:
                    if (a[j][i] == a[j + 1][i]) or (a[j][i] + a[j + 1][i] == 10):
                        if (a[j][i] == '-') or (a[j + 1][i] == '-'):
                            continue
                        else:
                            sum += 1
                except (IndexError, TypeError):
                    continue
            j += 1
        except IndexError:
            continue
    while j == 1:
        try:
            for i, e in enumerate(a[j]):
                del e
                try:
                    b = a[j][i]
                    if (str(b).isdigit()) and (a[j][i + 1] == '-'):
                        i += 1
                        while a[j][i] == '-':
                            i += 1
                        c = a[j][i]
                        if (b + c == 10) or (b == c):
                            sum += 1
                except IndexError:
                    continue
        except IndexError:
            continue
        try:
            for i, e in enumerate(a[j]):
                del e
                try:
                    if (a[j][i] == a[j][i + 1]) or (a[j][i] + a[j][i + 1] == 10):
                        if (a[j][i] == '-') or (a[j][i + 1] == '-'):
                            continue
                        else:
                            sum += 1
                except (IndexError, TypeError):
                    try:
                        if (a[j][i] == a[j + 1][i]) or (a[j][i] + a[j + 1][i] == 10):
                            if (a[j][i] == '-') or (a[j + 1][i] == '-'):
                                continue
                            else:
                                sum += 1
                    except (IndexError, TypeError):
                        continue
                    continue
                try:
                    if (a[j][i] == a[j + 1][i]) or (a[j][i] + a[j + 1][i] == 10):
                        if (a[j][i] == '-') or (a[j + 1][i] == '-'):
                            continue
                        else:
                            sum += 1
                except (IndexError, TypeError):
                    continue
            j += 1
        except IndexError:
            continue
    while j == 2:
        try:
            for i, e in enumerate(a[j]):
                del e
                try:
                    b = a[j][i]
                    if (str(b).isdigit()) and (a[j][i + 1] == '-'):
                        i += 1
                        while a[j][i] == '-':
                            i += 1
                        c = a[j][i]
                        if (b + c == 10) or (b == c):
                            sum += 1
                except IndexError:
                    continue
        except IndexError:
            continue
        try:
            for i, e in enumerate(a[j]):
                del e
                try:
                    if (a[j][i] == a[j][i + 1]) or (a[j][i] + a[j][i + 1] == 10):
                        if (a[j][i] == '-') or (a[j][i + 1] == '-'):
                            continue
                        else:
                            sum += 1
                except (IndexError, TypeError):
                    continue
            j += 1
        except IndexError:
            continue
    del j
    return sum


# just print the matrix
def print_matrix():
    print('')
    for i in a[0]:
        print(i, end=' ')
    print('')
    for i in a[1]:
        print(i, end=' ')
    print('')
    for i in a[2]:
        print(i, end=' ')
    print('')
    print('')


# checks if numbers suit us
def positive_couple(x1, y1, x2, y2):
    if (x1 == '-') or (x2 == '-') or (y1 == '-') or (y2 == '-'):
        return False
    if (x1 == x2) and (y1 == y2 - 1):
        return True
    elif (x1 == x2) and (y1 == y2 + 1):
        return True
    elif (x1 == x2 - 1) and (y1 == y2):
        return True
    elif (x1 == x2 + 1) and (y1 == y2):
        return True
    elif (x1 == x2) and (abs(y1-y2)>0) and (a[x1-1][y1-1] == a[x2-1][y2-1]):
        b = []
        c = 0
        if y1>y2:
            pass
        else:
            y1 , y2 = y2, y1
        while y2-1 != y1-2:
            b += str(a[x1-1][y2])
            y2 += 1
        for i in b:
            if str(i).isdigit():
                c += 1
        if c == 0:
            return True
    elif (x1 == x2) and (abs(y1 - y2) > 0) and (a[x1 - 1][y1 - 1] + a[x2 - 1][y2 - 1] == 10):
        b = []
        c = 0
        if y1 > y2:
            pass
        else:
            y1, y2 = y2, y1
        while y2 - 1 != y1 - 2:
            b += str(a[x1 - 1][y2])
            y2 += 1
        for i in b:
            if str(i).isdigit():
                c += 1
        if c == 0:
            return True
    elif (y1 == y2) and (abs(x1-x2)>0) and (a[x1-1][y1] == a[x2-1][y1]):
        b = []
        c = 0
        if x1>x2:
            pass
        else:
            x1, x2 = x2, x1
            while x2 - 1 != x1 - 2:
                b += str(a[x2][y1-1])
                x2 += 1
            for i in b:
                if str(i).isdigit():
                    c += 1
            if c == 0:
                return True
    elif (y1 == y2) and (abs(x1 - x2) > 0) and (a[x1 - 1][y1] + a[x2 - 1][y1] == 10):
        b = []
        c = 0
        if x1 > x2:
            pass
        else:
            x1, x2 = x2, x1
            while x2 - 1 != x1 - 2:
                b += str(a[x2][y1 - 1])
                x2 += 1
            for i in b:
                if str(i).isdigit():
                    c += 1
            if c == 0:
                return True
    else:
        return False


# main code block
start_game = 1
sum = computer_intelligence()
while start_game == 1:
    starting_program = str(input('Type start to start the game, or exit to exit: '))
    if starting_program.lower() == 'start':
        print('Hello, player.')
        print('The name of the game is "19".')
        print('Rules of the game: cross out identical pairs of numbers, or in total giving 10.')
        print('Condition: it is necessary that the pairs are near or through the blackened numbers. It is impossible to diagonally.')
        print('Numbering the rows from 1 to 3. Numbering the columns from 1 to 9.')
        print('Good luck!')
        print_matrix()
        while sum != 0:  # until the number of available pairs is 0
            if (a[2]) and (len(len3) == 0):
                del a[2]
            if (a[1]) and (len(len2)) == 0:
                del a[1]
            sum = computer_intelligence()
            print('Enter new coordinates for pairs of numbers.')
            # we enter and immediately check the row of the first number, that is, the first coordinate
            x1 = -1
            while (x1 == -1):
                x11 = input('Enter the row of the first number: ')
                try:
                    x11 = int(x11)
                except (ValueError, TypeError):
                    print('The expression you entered is not a decimal number.')
                    continue
                if len(len3) > 0:
                    if (x11 > 0) and (x11 < 4):
                        x1 = x11
                    else:
                        print('The entered number does not match.')
                        continue
                elif len(len2) > 0:
                    if (x11 > 0) and (x11 < 3):
                        x1 = x11
                    else:
                        print('The entered number does not match.')
                        continue
                else:
                    if (x11 > 0) and (x11 < 2):
                        x1 = x11
                    else:
                        print('The entered number does not match.')
                        continue
            # enter and immediately check the serial number of the first number, that is, the second coordinate
            y1 = -1
            while (y1 == -1):
                y11 = input('Enter the serial number of the first number: ')
                try:
                    y11 = int(y11)
                except (ValueError, TypeError):
                    print('The expression you entered is not a decimal number.')
                    continue
                if x1 == 3:
                    if (y11 <= len(len3)) and (y11 > 0):
                        y1 = y11
                    else:
                        print('The entered number does not match.')
                        continue
                elif x1 == 2:
                    if (y11 <= len(len2)) and (y11 > 0):
                        y1 = y11
                    else:
                        print('The entered number does not match.')
                        continue
                elif x1 == 1:
                    if (y11 <= len(len1)) and (y11 > 0):
                        y1 = y11
                    else:
                        print('The entered number does not match.')
                        continue
            # we enter and check a row of 2 numbers, i.e. 3 coordinate
            x2 = -1
            while (x2 == -1):
                x22 = input('Enter a row of the second number: ')
                try:
                    x22 = int(x22)
                except (ValueError, TypeError):
                    print('The expression you entered is not a decimal number.')
                    continue
                if len(len3) > 0:
                    if (x22 > 0) and (x22 < 4):
                        x2 = x22
                    else:
                        print('The entered number does not match.')
                        continue
                elif len(len2) > 0:
                    if (x22 > 0) and (x22 < 3):
                        x2 = x22
                    else:
                        print('The entered number does not match.')
                        continue
                else:
                    if (x22 > 0) and (x22 < 2):
                        x2 = x22
                    else:
                        print('The entered number does not match.')
                        continue
            # enter and check the serial number of the second number, i.e. 4 coordinate
            y2 = -1
            while (y2 == -1):
                y22 = input('Enter the serial number of the first number: ')
                try:
                    y22 = int(y22)
                except (ValueError, TypeError):
                    print('The expression you entered is not a decimal number.')
                    continue
                if x2 == 3:
                    if (y22 <= len(len3)) and (y22 > 0):
                        y2 = y22
                    else:
                        print('The entered number does not match.')
                        continue
                elif x2 == 2:
                    if (y22 <= len(len2)) and (y22 > 0):
                        y2 = y22
                    else:
                        print('The entered number does not match.')
                        continue
                elif x2 == 1:
                    if (y22 <= len(len1)) and (y22 > 0):
                        y2 = y22
                    else:
                        print('The entered number does not match.')
                        continue
            point_one, point_two = personal_coord(x1, y1, x2, y2)  # assign numbers to coordinates
            if positive_couple(x1, y1, x2, y2):
                try:
                    if (point_one == point_two) or (point_one + point_two == 10):
                        a[x1 - 1][y1 - 1] = '-'
                        a[x2 - 1][y2 - 1] = '-'
                        print_matrix()
                        print('The selected pair has been crossed out.')
                        print('Possible pairs of numbers: ', str(computer_intelligence()))
                    else:
                        print('The pair does not fit.')
                        continue
                except TypeError:
                    print('The number does not fit. You have selected strikethrough.')
                    continue
            else:
                print('You need to choose the numbers close to itself.')
                continue
            sum = computer_intelligence()
            if sum == 0:
                # we look again at how many pairs remain after deleting crossed out
                delete_hyphen()
                update_matrix()
                sum = computer_intelligence()
                # if 0, then the game is over, if! = 0, then update the field
                if (sum == 0):
                    start_game = 0
                    print('')
                    print('Game over. You won!!!')
                    print('Game over. You won!!!')
                    print('Game over. You won!!!')
                    print('Game over. You won!!!')
                    print('Game over. You won!!!')
                    delete_hyphen()
                    update_matrix()
                    print_matrix()
                    break
                else:

                    print('No more couples.')
                    print('Updating the field, please wait ...')
                    sum += 1
                    print_matrix()
                    print('Possible pairs of numbers: ', str(computer_intelligence()))
    elif starting_program.lower() == 'exit':
        print('We are exiting ...')
        break
    else:
        continue

