import os
import commands_executor as ce
import motion

currentDir = os.getcwd()
print('Текущий каталог:  {dir}'.format(dir=currentDir))

print(ce.commandExecutor('help'))

isRunning = True

null = None
if null == None:
    print('none')
else:
    print('yes')


def app(isRunning):
    command = input('Введите команду: ')
    ce.commandExecutor(command)
    if command == 'exit':
        needContinue = False
    else:
        needContinue = True
    return needContinue


while isRunning:
    isRunning = app(isRunning)









# files = os.listdir(path)

textFile = 'test_dir/some_text'
pdfFile = '/home/surok/books/books_programming/Big_data/9_Ethics_of_Big_Data_proglib.pdf'
pdfFile2 = '/home/surok/books/books_programming/Big_data/9_Ethics_of_/'
odtFile = '/home/surok/Документы/drd.txt.odt'
hardFile = '/etc/nginx/sites-available/echamps'

print(os.path.split(os.path.join(pdfFile2)))

# file1 = open(textFile, 'r')
# file2 = open(pdfFile, 'rb')
# file3 = open(odtFile, 'r')

# file4 = open(hardFile, 'r')

# print(file1.readline())
# print(file1.tell())

# str = file1.readline()

# print(file1.tell())

# print(file4.readline())


print(os.path)

# file4.close()
