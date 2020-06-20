import file_helper
import os
import history_helper

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
    history_helper.writeHistory(currentDir, 'paths')
    print('Текущий каталог:  {dir}'.format(dir=currentDir))


"""

Выводит в консоль все команды + описание к ним

"""
def showAllCommands():
    print('Возможные команды: ')
    for key in commandsDescription:
        print('{command} => {description}'.format(command=key, description=commandsDescription[key]))


def goUp():
    os.chdir('../')
    showCurrentPath()


def goBack():
    path = history_helper.getPrevPath()
    os.chdir(path)
    showCurrentPath()


def goTo():
    print('go to ...')

def showFiles():

    print('files')

def showDirs():
    print('dirs')

def showAll():
    print('start show all')
    file_helper.showAll()

def stopProgramm():
    history_helper.cleanHistory()


def repeat_command(command):
    need_repeat = input('Повторить команду? (y/n) ')

    if need_repeat == 'y':
        return True
    elif need_repeat == 'n':
        return False
    else:
        print('Пожалуйста, введите y или n')
        repeat_command(command)


def details():
    need_repeat = True
    while need_repeat:
        name = input('Введите название объекта для детальной информации о нем: ')
        if not os.path.exists(name):
            print('Такого файла/папки не существует!')
        else:
            file_helper.getDetails(name)
        need_repeat = repeat_command('details')

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



def commandExecutor(command):
    history_helper.writeHistory(command, 'command')

    functionName = checkCommand(command)
    if functionName is not None:
        functions[functionName]()
    else:
        print('Неверно введена команда, повторите попытку')
