'''
Created on Jan 12, 2024

@author: NirajanMacPro
'''

if __name__ == '__main__':
    
    '''Create a dictonary of (key,value) set'''
    words = {"Dog":"Furry", "Cat":"Fuzzy"}
    
    if "DOG" in words:
        print(words["DOG"]) #accesses the dictonary using the key and returns value
    else:
        print("DOG is not a key in 'words'")
        
    words["Dog"] = "Has 4 legs"
    print(words["Dog"])
    
    del words["Dog"]
    print("Dog" in words) #Displays False because "Dog" was deleted in line prior
    
    print(len(words)) #1 remaining item "Cat"
    
    words["Ten"] = 10
    print(type(words["Ten"]))
    print(type(words["Cat"]))
    
    '''Both of below create empty dictionaries'''
    dictExmp = {}
    dictExmp2 = dict()
    
    dictExmp["Lambton College"] = "Sarnia, Ontario"
    dictExmp["St. Clair College"] = "Windsor, Ontario"
    dictExmp["Fanshawe College"] = "London, Ontario"
    
    
    for key in dictExmp:
        print(key + "->" + dictExmp[key])
        
    print(dictExmp.get("ZZZ", "Not found!"));
    
    print(dictExmp.items()) #displays list of (key,value) pairs
    
    for (_,value) in dictExmp.items():
        print(value)
    
    print(dictExmp.keys()) #Just gives a list of key values
    
    inventory = { 'apple': 2, 'orange': 3, 'grapes': 4 }

    element = inventory.pop('apple', 0) #removes apples from the list and returns value
    print(element)
    print(inventory.items()) #RECALL pop() removes apple
    
    print("POP ITEM:", inventory.popitem())
    print(inventory.items())
    
    