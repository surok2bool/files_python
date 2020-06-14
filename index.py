import os
import commands_executor as ce


ce.showCurrentPath()
ce.commandExecutor('help')


def app():
    command = input('Введите команду: ')
    ce.commandExecutor(command)
    if command == 'exit':
        needContinue = False
    else:
        needContinue = True
    return needContinue

isRunning = True

while isRunning:
    isRunning = app()

