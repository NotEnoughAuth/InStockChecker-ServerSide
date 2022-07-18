import time
ThreadReading = False
ThreadWriting = False


def strToBool(str):
    if str == "True":
        return True
    else:
        return False


def readProducts():
    closeBrac = 1
    temp = []
    global ThreadReading
    while ThreadWriting:
        time.sleep(1)
    ThreadReading = True
    file = open('C:/Users/opryga/Documents/GitHub/InStockChecker-ServerSide/prodLookUp', 'r')
    hold = file.read()
    while closeBrac < hold.__len__()-2:
        openBrac = hold.find('[', closeBrac) + 1
        closeBrac = hold.find(']', closeBrac + 1)
        temp.append(hold[openBrac:closeBrac])
    temp2d = [[]] * temp.__len__()
    for i in range(0, temp.__len__()):
        temp2d[i] = temp[i].split(',')
        temp2d[i][0] = temp2d[i][0].split('\'')[1]
        temp2d[i][1] = strToBool(temp2d[i][1])
        temp2d[i][2] = strToBool(temp2d[i][2])
    ThreadReading = False
    return temp2d


def logProduct(productsAry):
    global ThreadWriting
    while ThreadReading:
        time.sleep(1)
    ThreadWriting = True
    file = open('C:/Users/opryga/Documents/GitHub/InStockChecker-ServerSide/prodLookUp', 'w+')
    file.write(productsAry.__str__())
    ThreadWriting = False
