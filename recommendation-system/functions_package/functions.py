#Get Top 2 Brand History
from numpy import append
from functions_package import sort


def getTop2History(History):
    result = []
    defaultElement = {
        'id': 0,
        'frequency': 0
    }
    temp = [defaultElement]

    for history in History:
        isNew = True
        for element in temp:
            if(element['id'] == history):
                element['frequency']+=1
                isNew = False
                break
        if(isNew == True): 
            newElement = {
                'id': history,
                'frequency': 1
            }
            temp.append(newElement)

    sort.insertionSort(temp)
    result = temp[:2]
    return result

def getTop1History(History):
    result = {}
    defaultElement = {
        'id': 0,
        'frequency': 0
    }
    temp = [defaultElement]

    for history in History:
        isNew = True
        for element in temp:
            if(element['id'] == history):
                element['frequency']+=1
                isNew = False
                break
        if(isNew == True): 
            newElement = {
                'id': history,
                'frequency': 1
            }
            temp.append(newElement)

    sort.insertionSort(temp)
    result = temp[:1]
    return result

def createCriteria(brand, skin, category, session, structure):
    criteria = {
        'brand': {
            'id': brand['id'],
            'frequency': brand['frequency']
        },
        'skin': {
            'id': skin['id'],
            'frequency': skin['frequency']
        },
        'category': {
            'id': category['id'],
            'frequency': category['frequency']
        },
        'session': {
            'id': session['id'],
            'frequency': session['frequency']
        },
        'structure': {
            'id': structure['id'],
            'frequency': structure['frequency']
        },
    }
    return criteria

