'''Syntax for recursion-
def function_name(parameters):
        if base_condition:
            return result
        return function_name(modified_parameters)'''

'''write a python program to print the summation of list elements using 
recursion'''
List=[1,2,3,4,5]
def Add_List(List,Sum):
        if bool(List[len(List)-1]):
            Sum=Sum+List[len(List)-1]
            return Add_List(List.pop(),sum)
        return Sum
print(Add_List[List,0])

