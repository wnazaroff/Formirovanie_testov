import numpy as np

def open_file(x):
    x = str(x)
    a = 'data (' + x + ').txt'
    file = open(a, 'r', encoding="utf-8")
    text = file.read().strip()
    file.close()
    return text

def w_file(x):
    x = str(x)
    txt = 'test ' + x + '.txt'
    with open(txt, "a", encoding="utf-8") as result:
        print("Варинт №", x, file=result)

def w_file_test(x):
    x = str(x)
    txt = 'test ' + x + '.txt'
    otvety = 'otvet' + x + '.txt'
    #выбираем 25 из 50 рандомных элементов
    a = np.random.permutation(50)
    b = a[0:25]
    
    with open(txt, "a", encoding="utf-8") as vopros: #запись результата в тест
        print("Варинт №", x, file=vopros)
        n = 0
        for i in b:
            n = n + 1
            print(n, file=vopros)
            print(open_file(i+1), file=vopros)
    with open(otvety, "a", encoding="utf-8") as otv: #запись результата в ответ
        print("Варинт №", x, file=otv)
        n = 0
        for j in b:
            n = n + 1
            print(n, otvet[j], file=otv)




otvet = ['а','в','б','б','г','абв','г','в','а','б',
         'б','б','а','а','в','в','б','а','а','в',
         'б','аб','в','абвг','авг','г','г','г','ав','в',
         'а','г','в','в','г','г','б','а','г','б',
         'б','г','а','г','б','б','г','а','б','а']

for i in range(27):
    w_file_test(i+1)
