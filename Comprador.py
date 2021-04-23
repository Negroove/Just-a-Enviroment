import json
from tkinter import messagebox

def Lectura1():
    jsonstring1= list()
    with open('Json_1.json') as json_file:
        data = json.load(json_file)
        for k,v in data.items():
            jsonstring1.append(list((k,v)))            
    return jsonstring1

def Lectura2():
    jsonstring2 = list()
    with open('Json_2.json') as json_file:
        data = json.load(json_file)
        for k,v in data.items():
            jsonstring2.append(list((k,v)))            
    return jsonstring2

texto1 = Lectura1()

texto2 = Lectura2()

def compare():
    differences = list()
    same = True
    while same:
        for i in range(len(texto1)):
                if texto1[i]!= texto2[i]:
                    differences.append(texto1[i])
                    same = False
    print(differences)
    return same

if compare():
    messagebox.showinfo(message="Son iguales",title="Resultados")
else:
    messagebox.showinfo(message="solo tenias que precionar una tecla",title="Shit bro")
