"""Top-Down-parsing tree

This script builds a tree with a top down parsing method and validating
if a string is accepted or not in the parsing tree

This tool accepts text files (.txt) with the correct syntax to build a 
parsing tree from a grammar.

This script requires `pptree` be installed within the Python
environment you are running this script in. 

You can install pptree using command `pip install pptree` in your terminal
in case you do not have it.


"""
from pptree import *

def TopDownParsing(nonTerminal,terminal,initialState,productions,string,depth):
    """Top down parsing method to build the parsing Tree

    Parameters
    ----------
    nonTerminal : list
        All the non Terminal symbols in the .txt file
    terminal : list
        All the terminal symbols in the .txt file
    initialState: str
        Initial state in the grammar
    productions: dict
        All the productions of the grammar
    string: str
        Input string to validate
    depth: int
        Input max depth the tree must go   

    Returns
    -------
    Printed Tree and string validation 
    """ 

    print("TopDownParsing Method")
    queue = []
    devide = []

    Tree = {}
    dicDepth = {}

    found = False
    uwv = ""

    queue.append(initialState)
    dicDepth[initialState] = 0

    while queue and not found:
        q = queue.pop(0)

        if dicDepth[q] + 1 > depth:
            break

        done = False

        for x in range(len(q)):
            if q[x].isupper():
                q = q.partition(q[x])
                break      
        while not done and not found:

            for j in productions[q[1]]:
                devide.clear()
                w = j
                checkIfmatches = q[0]
                devide.append(q[0])
                devide.append(w)
                devide.append(q[2])
                uwv = listToString(devide)

                allTerminal = 0
                for minus in range(len(uwv)):
                    if uwv[minus] in terminal:
                        allTerminal = allTerminal + 1

                matches = True
                for x in range(len(checkIfmatches)):
                    if len(checkIfmatches) > len(string):
                        matches = False
                        break
                    elif checkIfmatches[x] != string[x]:
                        matches = False
                        break        

                if allTerminal < len(uwv) and matches:
                    queue.append(uwv)
                    append_value(Tree,listToString(q),uwv)
                    dicDepth[uwv] = dicDepth[listToString(q)] + 1
                    if uwv == string:
                        found = True

                elif matches:
                    append_value(Tree,listToString(q),uwv)
                    if uwv == string:
                        found = True          
            done = True  
                   
    if found:
        print("------------------String " +string + " Accepted------------------")
    else:
        print("----------------String " +string + " NOT Accepted----------------")   

    tempRoot = Node(initialState)
    print_tree_method_recursive(Tree,initialState,tempRoot)

    if depth <= 5:
        print_tree(tempRoot,horizontal=False)
    else:
        print_tree(tempRoot,horizontal=True)
    
    if found:
        print("------------------String " +string + " Accepted------------------")
    else:
        print("----------------String " +string + " NOT Accepted----------------")


def listToString(devide): 
    """Simple list to string converter

    Parameters
    ----------
    devide : list
        The list wanted to construct a str

    Returns
    -------
    string constructed 
    """ 
    str1 = ""    
    for x in devide:  
        str1 += x    
    return str1

def append_value(dict_obj, key, value):
    """Insert values to a dict in order to have list inside

    Parameters
    ----------
    dict_obj : dict
        The dictionary with current elements
    key : string
        The key we want to assign the value
    value : string
        The value we want to assign to the key

    Returns
    -------
    Dictionary with value added 
    """ 
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = [value]

def print_tree_method_recursive(Tree,key,parent):
    """Print Tree using pprint import

    Parameters
    ----------
    Tree : dict
        Dictionary with all nodes and children
    key : str
        String representing a node
    parent : node
        The parent to assign children  
    

    Expected value
    -------
    built complete tree 
    """
    for x in Tree:
        for j in Tree[x]:
            if x == key:
                nod = Node(j,parent)
                print_tree_method_recursive(Tree,j,nod)


repeat = True

while repeat:
    print("Select the text file (e.g. test1, test2,test3,test4)")
    txtVal = input()
    print("String to evaluate")
    string = input()
    print("indicate the maximun depth")
    depth = int(input())

    productions = {}

    with open(txtVal + ".txt") as f:
        nonTerminal = f.readline().split(",")
        nonTerminal[len(nonTerminal)-1] = nonTerminal[len(nonTerminal)-1].strip()
        terminal = f.readline().split(",")
        terminal[len(terminal)-1] = terminal[len(terminal)-1].strip()
        initialState = f.readline().strip() 
        for i in range(len(nonTerminal)*3):
                ste = f.readline()
                if not ste:
                    break
                ste = ste.split("->")
                ste[len(ste)-1] = ste[len(ste)-1].strip()
                if ste[0].isupper():
                    append_value(productions,ste[0],ste[1])
                ste.clear()

    TopDownParsing(nonTerminal,terminal,initialState,productions,string,depth)

