# LISTS
# FIRST TASK
elements = [1,4,234,65,43,467,357,31,21]
sort = min(elements)
sort2 = max(elements)
print(f"Наименьший элемент в списке {elements} это {sort}")
print(f"Наибольший элемент в списке {elements} это {sort2}")
# SECOND TASK
names = ['Roy', 'Arif', 'Dima', 'Krissanto']
names.sort()
print(names)
# THIRD TASK
def concatLists(firstList, secondList):
    thirdList = []
    for i in firstList:
        if i in secondList:
            thirdList.append(i)
    print(thirdList)
firstList = [1,6,2,6,8,2,5,74,8,0,5]
secondList = [5,7,1,2,6,8,5,73,6,4,7]
concatLists(firstList, secondList)