import os
import datetime

def printInfo(info):
    i = 1
    for elem in info:
        print('{i}. {elem}'.format(i=i, elem=elem))
        i += 1


def showAll():
    all = os.listdir()
    printInfo(all)

def getSize(name):
    return os.path.getsize(name)

def getCreateTime(name):

    return os.path.getmtime(name)

def getInfoFile(name):
    print('Размер составляет {bytes} байта'.format(bytes=getSize(name)))
    print('Дата создания: {time}'.format(time=getCreateTime(name)))



def getDetails(name):
    if os.path.isfile(name):
        getInfoFile(name)
    elif os.path.isdir(name):
        print('it is dir')
