import os
import commands_executor as ce


currentDir = os.getcwd()

ce.showCurrentPath()
ce.commandExecutor('help')

isRunning = True


def app():
    command = input('Введите команду: ')
    ce.commandExecutor(command)
    if command == 'exit':
        needContinue = False
    else:
        needContinue = True
    return needContinue


while isRunning:
    isRunning = app()

