import os


requirements =  open('requirements.txt', 'r')
lines = requirements.readlines()

for requirement in lines :

    os.system('pip uninstall ' + str(requirement).replace('\n', ''))