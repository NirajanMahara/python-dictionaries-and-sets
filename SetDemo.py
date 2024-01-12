'''
Created on Jan 12, 2024

@author: NirajanMacPro
'''

if __name__ == '__main__':
    
    
    setOfNumbers = set() #creates an empty set
    setOfNumbers2 = set([1, 3, 5, 3, 7]) #creates an empty set
    
    print(setOfNumbers)
    print(setOfNumbers2)
    
    print(len(setOfNumbers2))
    
    '''add item to empty set'''
    setOfNumbers.add(6);
    setOfNumbers.update("Aaron")
    setOfNumbers.discard("Z")
    
    for item in setOfNumbers:
        print(item)
    
    
    A = set([1, 10, 3, 7])
    B = set([12, 1, 7, 4])
    
    C = A | B #union
    D = A & B #intersection
    E = A - B #difference
    F = B - A #difference
    print("Union:", C) #all items in two sets
    print("Intersection:", D) #same items in two sets
    print("Difference:", E) #same items in two sets
    print("Difference:", F) #same items in two sets
    
    G = A ^ B #symmetric difference
    print("Symmetric Difference:", G) #same items in two sets