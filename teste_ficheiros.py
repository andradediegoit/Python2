with open('teste_python.txt','r') as myFile:

    readLista = myFile.readlines()

print(readLista)

for i in readLista:
    print(i)

for i in readLista:
    print('programação' in i)

