##
## Name: Harshil Patel
## Course: Programming Languages CS 3003 - 001
## Assignment: Dynamo of Volition
##
## Implement a Dynamic Scope Class for Python

from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect

## Create Dynamic Scope Class and inherit from abc.Mapping abstract base class
class DynamicScope(abc.Mapping):
    ##Initializer
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}
        
    ##Set the provided item in the provided key in the dictionary
    def __setitem__(self, key, item):
        self.env[key] = item

    ##Get the item associated with given key    
    def __getitem__(self,key):
        if self.env.__contains__(key):
            return self.env[key]
        ##Raise NameError instead of KeyError if given key does not exist
        raise NameError(f"Name '{key}' is not defined.")

    ##Delete the given key, also will delete the item
    def __delitem__(self, key):
        if self.env.__contains__(key):
            del self.env[key]
        ##Raise NameError instead of KeyError if given key does not exist
        raise NameError(f"Name '{key}' is not defined.")
        
    def __iter__(self):
        return iter(self.env)

    def __len__(self):
        return len(self.env)

    ##Contains is used to check if given key exists in dictionary, returns boolean value
    def __contains__(self, key):
        return key in self.env


##The get_dynmaic_re class returns the dicti
def get_dynamic_re() -> DynamicScope:

    ##Create DynamicScope object which is a dictionary
    dictionary = DynamicScope()

    ##This is used to get the value 
    keyIndex = 1

    ##Get the stack info and store it in frame
    frame = inspect.stack(context=1)

    ## iterate through frame until it's length is equal to keyIndex(Incremented)
    while len(frame) != keyIndex:

        ##Declare the local variables and free variables
        localVarList = frame[keyIndex][0].f_locals
        freeVarList = list(frame[keyIndex][0].f_code.co_freevars)

        ##Iterate through all local variables
        for localVar in localVarList:
            
            ##If the dictionary does not contain the local variable,
            ## and the local variable is not in the list of free variables,
            ## add the local variable to the dictionary
            if dictionary.__contains__(localVar) == False:
                if (localVar in freeVarList) == False:
                    dictionary.__setitem__(localVar, localVarList[localVar])

        ##Increment keyIndex for next iteration
        keyIndex += 1

    ## return dictionary, which is a DynamicScope Object
    return dictionary
