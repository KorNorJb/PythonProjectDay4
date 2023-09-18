dict = {
    'Казахстан': "Астана",
    'Норвегия': "Осло",
    'Южная Корея': "Сеул"
}
c = str(input("Введите страну(Казахстан, Норвегия, Южная Корея): "))
if c in dict:
    Fdict = dict[c]
    print(f"Столица страны {c} является {Fdict}")
else: 
    print("Страна не найдена!")
k = dict.keys()
print(k)


def funcDict(dict):
    keyList = list(dict.keys())
    print(keyList)
funcDict(dict)


dict2 = {
    'Помидоры': '10шт',
    'Огурцы': '5шт',
    'Бананы': '12шт',
    'Клубника': '9шт',
}
sold = int(input("Товар был продан? \n1) Да \n2) Нет \n"))
if(sold == 1):
    item = str(input("Какой товар продан? : "))
    if (item == "Помидоры" or "Огурцы" or "Бананы" or "Клубника" ):
        del dict2[item]
        print(dict2)
    else:
        print("Такого товара не найдено")
else:
    print("Пока)")
