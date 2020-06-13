def writeHistoryCommand(command):
    # Наверное надо при инициализации скрипта программными средствами определять путь к корню приложения
    # и устанавливать какую-то константу, по которой будем дальше отслеживать файлы для записи
    filePath = '/home/surok/python_projects/files_python/data/commands'

    commandHistory = open(filePath, 'r+')

    # Смещаем указатель файла в конец, ибо открытие файла по r+ автоматом ставит указатель в начало
    # и write(), соответственно, пишет в начало
    commandHistory.seek(0, 2)
    commandHistory.writelines([command, '\n'])

    # Снова смещаем указатель файла, уже в начало, чтобы прочесть содержимое
    commandHistory.seek(0, 0)
    history = commandHistory.readlines()

    commandHistory.close()

    controlHistoryLen(filePath, history)


def controlHistoryLen(historyFilePath, history):
    if len(history) >= 5:
        history.pop(0)
        historyFile = open(historyFilePath, 'w')
        historyFile.writelines(history)
        historyFile.close()


def cleanHistory():
    paths = [
        '/home/surok/python_projects/files_python/data/commands',
    ]

    for path in paths:
        open(path, 'w').close()
