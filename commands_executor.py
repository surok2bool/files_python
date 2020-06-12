import file_checker
import os


"""

Список всех команд с описанием. Необходимо для вывода информации о командах и проверке на корректность
TODO надо изменить проверку, а то криво как-то выходит

"""
commandsDescription = dict(
    help='показать справку по программе',
    up='подняться на папку выше',
    back='вернуться назад',
    go='переместиться по пути',
    show_files='показать все файлы',
    show_dirs='показать все папки',
    show_all='показать все содержимое',
    details='показать детальную информацию о файле или папке',
    exit='выход из программы'
)

"""
Вывод текущего каталога, необходимо для функций перемещения по каталогам
"""
def showCurrentPath():
    currentDir = os.getcwd()
    print('Текущий каталог:  {dir}'.format(dir=currentDir))


"""

Выводит в консоль все команды + описание к ним

"""
def showAllCommands():
    print('Возможные команды: ')
    for key in commandsDescription:
        print('{command} => {description}'.format(command=key, description=commandsDescription[key]))


def goUp():
    showCurrentPath()


def goBack():
    print('go back')

def goTo():
    print('go to ...')

def showFiles():
    print('files')

def showDirs():
    print('dirs')

def showAll():
    print('start show all')
    file_checker.showAll()

def stopProgramm():
    print('stop')

def details():
    print('details')

"""

Проверяем, корректная ли команда

"""
def checkCommand(command):
    for key in commandsDescription:
        if key == command:
            return key
    return None


"""

Словарь всех доступных команд + функции, которые вызываются по данныой команде

"""
functions = {
    'help': showAllCommands,
    'up': goUp,
    'back': goBack,
    'go': goTo,
    'show_files': showFiles,
    'show_dirs': showDirs,
    'show_all': showAll,
    'details': details,
    'exit': stopProgramm
}



def commandExecutor(command, history):
    # Устанавливаем максимальную длину истории и удаляем первый элемент при необходимости, дабы не переполнять буфер
    if len(history) == 20:
        history.pop(0)
    history.append(command)
    functionName = checkCommand(command)
    if functionName is not None:
        functions[functionName]()
    else:
        print('Неверно введена команда, повторите попытку')
