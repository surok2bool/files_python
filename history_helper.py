def getHistoryCommand():
    return '/home/surok/python_projects/files_python/data/commands'

def getHistoryPaths():
    return '/home/surok/python_projects/files_python/data/paths'

def writeHistory(data, typeOfHistory):
    # Наверное надо при инициализации скрипта программными средствами определять путь к корню приложения
    # и устанавливать какую-то константу, по которой будем дальше отслеживать файлы для записи

    historyTypes = {
        'command': getHistoryCommand,
        'paths': getHistoryPaths,
    }

    filePath = historyTypes.get(typeOfHistory)()

    print(filePath)

    fileHistory = open(filePath, 'r+')

    # Смещаем указатель файла в конец, ибо открытие файла по r+ автоматом ставит указатель в начало
    # и write(), соответственно, пишет в начало
    fileHistory.seek(0, 2)
    fileHistory.writelines([data, '\n'])

    # Снова смещаем указатель файла, уже в начало, чтобы прочесть содержимое
    fileHistory.seek(0, 0)
    history = fileHistory.readlines()

    fileHistory.close()

    controlHistoryLen(filePath, history)


def controlHistoryLen(historyFilePath, history):
    if len(history) >= 5:
        history.pop(0)
        historyFile = open(historyFilePath, 'w')
        historyFile.writelines(history)
        historyFile.close()


def cleanHistory():
    paths = [
        getHistoryCommand(),
        getHistoryPaths()
    ]

    for path in paths:
        open(path, 'w').close()
