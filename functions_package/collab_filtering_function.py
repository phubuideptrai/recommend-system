
#Content_base Recommendation
from functions_package import sort, functions


def collab_filtering_recommendation(products, users, user):

    results = []

    #Get best similar user
    bestSimilarUser = getBestSimilarUser(users, user)

    #Get History
    preference_defaultUser = user['preference']
    brandHistory_defaultUser = preference_defaultUser['brandHistory']
    skinTypeHistory_defaultUser = preference_defaultUser['skinTypeHistory']
    categoryHistory_defaultUser = preference_defaultUser['categoryHistory']
    sessionHistory_defaultUser = preference_defaultUser['sessionHistory']
    structureHistory_defaultUser = preference_defaultUser['structureHistory']

    #Get Top1 Brand History
    top1BrandHistory_temp = functions.getTop1History(brandHistory_defaultUser)
    top1BrandHistory_defaultUser = top1BrandHistory_temp[0]
    #Get Top1 Skin History
    top1SkinHistory_temp = functions.getTop1History(skinTypeHistory_defaultUser)
    top1SkinHistory_defaultUser = top1SkinHistory_temp[0]
    #Get Top1 Category History
    top1CategoryHistory_temp = functions.getTop1History(categoryHistory_defaultUser)
    top1CategoryHistory_defaultUser = top1CategoryHistory_temp[0]
    #Get Top1 Session History
    top1SessionHistory_temp = functions.getTop1History(sessionHistory_defaultUser)
    top1SessionHistory_defaultUser = top1SessionHistory_temp[0]
    #Get Top1 Structure History
    top1StructureHistory_temp = functions.getTop1History(structureHistory_defaultUser)
    top1StructureHistory_defaultUser = top1StructureHistory_temp[0]

    #Create criteria
    criteria_defaultUser = functions.createCriteria(top1BrandHistory_defaultUser, top1SkinHistory_defaultUser, top1CategoryHistory_defaultUser, top1SessionHistory_defaultUser, top1StructureHistory_defaultUser)
    criteria_bestSimilarUser = bestSimilarUser[0]['criteria']

    #Get 10 similar products with default user
    getSimilarProducts(products, criteria_defaultUser, results, 10)
    
    #Get 10 similar products with best similar user
    getSimilarProducts(products, criteria_bestSimilarUser, results, 20)
    
    return results

def getBestSimilarUser(users, user):
    result = {}
    temp = []

    preference_defaultUser = user['preference']
    brandHistory_defaultUser = preference_defaultUser['brandHistory']
    skinTypeHistory_defaultUser = preference_defaultUser['skinTypeHistory']
    categoryHistory_defaultUser = preference_defaultUser['categoryHistory']
    sessionHistory_defaultUser = preference_defaultUser['sessionHistory']
    structureHistory_defaultUser = preference_defaultUser['structureHistory']

    #Get Top1 Brand History
    top1BrandHistory_temp = functions.getTop1History(brandHistory_defaultUser)
    top1BrandHistory_defaultUser = top1BrandHistory_temp[0]
    #Get Top1 Skin History
    top1SkinHistory_temp = functions.getTop1History(skinTypeHistory_defaultUser)
    top1SkinHistory_defaultUser = top1SkinHistory_temp[0]
    #Get Top1 Category History
    top1CategoryHistory_temp = functions.getTop1History(categoryHistory_defaultUser)
    top1CategoryHistory_defaultUser = top1CategoryHistory_temp[0]
    #Get Top1 Session History
    top1SessionHistory_temp = functions.getTop1History(sessionHistory_defaultUser)
    top1SessionHistory_defaultUser = top1SessionHistory_temp[0]
    #Get Top1 Structure History
    top1StructureHistory_temp = functions.getTop1History(structureHistory_defaultUser)
    top1StructureHistory_defaultUser = top1StructureHistory_temp[0]

    #Create criteria
    criteria_defaultUser = functions.createCriteria(top1BrandHistory_defaultUser, top1SkinHistory_defaultUser, top1CategoryHistory_defaultUser, top1SessionHistory_defaultUser, top1StructureHistory_defaultUser)

    #Brand Criteria
    brandID_defaultUser = criteria_defaultUser['brand']['id']
    brandFrequency_defaultUser = criteria_defaultUser['brand']['frequency']
    brandPriority = 2
        
    #Skin Criteria
    skinID_defaultUser = criteria_defaultUser['skin']['id']
    skinFrequency_defaultUser = criteria_defaultUser['skin']['frequency']
    skinPriority = 2 

    #Category Criteria
    categoryID_defaultUser = criteria_defaultUser['category']['id']
    categoryFrequency_defaultUser = criteria_defaultUser['category']['frequency']
    categoryPriority = 3

    #Session Criteria
    sessionID_defaultUser = criteria_defaultUser['session']['id']
    sessionFrequency_defaultUser = criteria_defaultUser['session']['frequency']
    sessionPriority = 1

    #Structure Criteria
    structureID_defaultUser = criteria_defaultUser['structure']['id']
    structureFrequency_defaultUser = criteria_defaultUser['structure']['frequency']
    structurePriority = 1

    for User in users:
        #Get History
        User_ID = User['id']
        preference = User['preference']
        brandHistory = preference['brandHistory']
        skinTypeHistory = preference['skinTypeHistory']
        categoryHistory = preference['categoryHistory']
        sessionHistory = preference['sessionHistory']
        structureHistory = preference['structureHistory']

        #Get Top1 Brand History
        top1BrandHistory_temp = functions.getTop1History(brandHistory)
        top1BrandHistory = top1BrandHistory_temp[0]
        #Get Top1 Skin History
        top1SkinHistory_temp = functions.getTop1History(skinTypeHistory)
        top1SkinHistory = top1SkinHistory_temp[0]
        #Get Top1 Category History
        top1CategoryHistory_temp = functions.getTop1History(categoryHistory)
        top1CategoryHistory = top1CategoryHistory_temp[0]
        #Get Top1 Session History
        top1SessionHistory_temp = functions.getTop1History(sessionHistory)
        top1SessionHistory = top1SessionHistory_temp[0]
        #Get Top1 Structure History
        top1StructureHistory_temp = functions.getTop1History(structureHistory)
        top1StructureHistory = top1StructureHistory_temp[0]

        #Create criteria
        criteria = functions.createCriteria(top1BrandHistory, top1SkinHistory, top1CategoryHistory, top1SessionHistory, top1StructureHistory)

        #Calculate the similarity between two users
        #Brand Criteria
        brandID = criteria['brand']['id']
        brandFrequency = criteria['brand']['frequency']

        #Skin Criteria
        skinID = criteria['skin']['id']
        skinFrequency = criteria['skin']['frequency']

        #Category Criteria
        categoryID = criteria['category']['id']
        categoryFrequency = criteria['category']['frequency']

        #Session Criteria
        sessionID = criteria['session']['id']
        sessionFrequency = criteria['session']['frequency']

        #Structure Criteria
        structureID = criteria['structure']['id']
        structureFrequency = criteria['structure']['frequency']

        #Compare matching between two users
        #Matching Brand?
        if(brandID == brandID_defaultUser):  matching1 = 1
        else: matching1 = 0

        #Matching Skin?
        if(skinID == skinID_defaultUser): matching2 = 1
        else: matching2 = 0

        #Matching Category?
        if(categoryID == categoryID_defaultUser): matching3 = 1
        else: matching3 = 0

        #Matching Session?
        if(sessionID == sessionID_defaultUser): matching4 = 1
        else: matching4 = 0

        #Matching Structure?
        if(structureID == structureID_defaultUser): matching5 = 1
        else: matching5 = 0

        similarity = ((matching1*(brandFrequency+brandFrequency_defaultUser)*brandPriority)+(matching2*(skinFrequency+skinFrequency_defaultUser)*skinPriority)+(matching3*(categoryFrequency+categoryFrequency_defaultUser)*categoryPriority)+(matching4*(sessionFrequency+sessionFrequency_defaultUser)*sessionPriority)+(matching5*(structureFrequency+structureFrequency_defaultUser)*structurePriority)) / (((brandFrequency+brandFrequency_defaultUser)*brandPriority)+((skinFrequency+skinFrequency_defaultUser)*skinPriority)+((categoryFrequency+categoryFrequency_defaultUser)*categoryPriority)+((sessionFrequency+sessionFrequency_defaultUser)*sessionPriority)+((structureFrequency+structureFrequency_defaultUser)*structurePriority)) 
        result = {
            'id': User_ID,
            'similarity': similarity,
            'criteria': criteria
        }

        temp.append(result)

    n = len(temp)
    sort.quickSort(temp, 0, n-1)

    result = temp[:1]

    return result

def getSimilarProducts(products, criteria, results, limit):
    temp = []

    #Brand Criteria
    brandID = criteria['brand']['id']
    brandFrequency = criteria['brand']['frequency']
    brandPriority = 2

    #Skin Criteria
    skinID = criteria['skin']['id']
    skinFrequency = criteria['skin']['frequency']
    skinPriority = 2 

    #Category Criteria
    categoryID = criteria['category']['id']
    categoryFrequency = criteria['category']['frequency']
    categoryPriority = 3

    #Session Criteria
    sessionID = criteria['session']['id']
    sessionFrequency = criteria['session']['frequency']
    sessionPriority = 1

    #Structure Criteria
    structureID = criteria['structure']['id']
    structureFrequency = criteria['structure']['frequency']
    structurePriority = 1

    #Consider each product in products
    for product in products:
        #Get information of product to calculate
        productID = product['id']
        brandProductID = product['brandID']
        skinProductID = product['skinID']
        categoryProductID = product['categoryID']
        sessionProductID = product['sessionID']
        structureProductID = product['structureID']

        #Compare criteria and product's information
        #Matching Brand?
        if(brandID == brandProductID):  matching1 = 1
        else: matching1 = 0

        #Matching Skin?
        if(skinID == skinProductID): matching2 = 1
        else: matching2 = 0

        #Matching Category?
        if(categoryID == categoryProductID): matching3 = 1
        else: matching3 = 0

        #Matching Session?
        if(sessionID == sessionProductID): matching4 = 1
        else: matching4 = 0

        #Matching Structure?
        if(structureID == structureProductID): matching5 = 1
        else: matching5 = 0

        #Calculate similarity
        similarity = ((matching1*brandFrequency*brandPriority)+(matching2*skinFrequency*skinPriority)+(matching3*categoryFrequency*categoryPriority)+(matching4*sessionFrequency*sessionPriority)+(matching5*structureFrequency*structurePriority)) / ((brandFrequency*brandPriority)+(skinFrequency*skinPriority)+(categoryFrequency*categoryPriority)+(sessionFrequency*sessionPriority)+(structureFrequency*structurePriority)) 
        result = {
            'id': productID,
            'similarity': similarity
        }

        temp.append(result)

    n = len(temp)
    sort.quickSort(temp, 0, n-1)

    
    isFinished = False

    for element in temp:
        if (len(results) == 0):
            results.append(element)
        else:
            isNew = True
            for result in results:
                if(element['id'] == result['id']):
                    isNew = False
                    break
            if(isNew == True):
                results.append(element)
                if(len(results) == limit): isFinished = True  
        
        if(isFinished == True): break

    return results