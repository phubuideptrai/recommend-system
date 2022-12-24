

from functions_package import sort, functions

#Content_base Recommendation
def content_base_recommendation(products, user):

    results = []

    #Get History
    preference = user['preference']
    brandHistory = preference['brandHistory']
    skinTypeHistory = preference['skinTypeHistory']
    categoryHistory = preference['categoryHistory']
    sessionHistory = preference['sessionHistory']
    structureHistory = preference['structureHistory']

    
    #brandHistory = [1,2,2,3,4,5,1,5,3,1]
    #skinTypeHistory = [2,3,4,5,3,2,5,7,3,5]
    #categoryHistory = [1,2,3,1,2,3,5,6,3,5]
    #sessionHistory = [1,5,5,4,4,4,4,3,4,4]
    #structureHistory = [2,3,4,1,2,2,2,1,5,3]

    #Get Top2 Brand History
    top2BrandHistory = functions.getTop2History(brandHistory)
    #Get Top2 Skin History
    top2SkinHistory = functions.getTop2History(skinTypeHistory)
    #Get Top2 Category History
    top2CategoryHistory = functions.getTop2History(categoryHistory)
    #Get Top2 Session History
    top2SessionHistory = functions.getTop2History(sessionHistory)
    #Get Top2 Structure History
    top2StructureHistory = functions.getTop2History(structureHistory)

    #Create 5 criterion
    criteria1 = functions.createCriteria(top2BrandHistory[0], top2SkinHistory[0], top2CategoryHistory[0], top2SessionHistory[0], top2StructureHistory[0]) #get 10 products with criteria1
    criteria2 = functions.createCriteria(top2BrandHistory[1], top2SkinHistory[1], top2CategoryHistory[0], top2SessionHistory[0], top2StructureHistory[0]) #get 5 products with criteria2
    criteria3 = functions.createCriteria(top2BrandHistory[0], top2SkinHistory[0], top2CategoryHistory[1], top2SessionHistory[0], top2StructureHistory[0]) #get 3 products with criteria3
    criteria4 = functions.createCriteria(top2BrandHistory[1], top2SkinHistory[0], top2CategoryHistory[1], top2SessionHistory[0], top2StructureHistory[0]) #get 1 products with criteria4
    criteria5 = functions.createCriteria(top2BrandHistory[1], top2SkinHistory[1], top2CategoryHistory[1], top2SessionHistory[0], top2StructureHistory[0]) #get 1 products with criteria5

    #Get 10 similar products with criteria1
    getSimilarProducts(products, criteria1, results, 10)
    
    #Get 5 similar products with criteria2
    getSimilarProducts(products, criteria2, results, 15)
    
    #Get 3 similar products with criteria3
    getSimilarProducts(products, criteria3, results, 18)
    
    #Get 1 similar products with criteria4
    getSimilarProducts(products, criteria4, results, 19)
    
    #Get 1 similar products with criteria5
    getSimilarProducts(products, criteria5, results, 20)
    
    return results

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

def getSimilarProductsBySelectedProduct(products, product):
    
    results = []
    temp = []

    #Brand 
    brandID = product['brandID']
    brandPriority = 2

    #Skin
    skinID = product['skinID']
    skinPriority = 2 

    #Category 
    categoryID = product['categoryID']
    categoryPriority = 3

    #Session
    sessionID = product['sessionID']
    sessionPriority = 1

    #Structure
    structureID = product['structureID']
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
        similarity = ((matching1*brandPriority)+(matching2*skinPriority)+(matching3*categoryPriority)+(matching4*sessionPriority)+(matching5*structurePriority)) / (brandPriority+skinPriority+categoryPriority+sessionPriority+structurePriority) 
        
        result = {
            'id': productID,
            'similarity': similarity
        }

        temp.append(result)

    n = len(temp)
    sort.quickSort(temp, 0, n-1)

    results = temp[:20]

    return results