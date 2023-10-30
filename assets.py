"""A test module"""
import pandas as pd

print( "this is a new file I added")

print( "to make it to git I need to go to SOURCE CONTROL")
print( "the file should have a U (Untrack) next to it")
print( "Hit the + and it becomes A (Add) then M (Modified)")

def my_func( x, y):
    """simple add func"""
    return x+y

print( my_func(3,2 ))
print( my_func(4,5 ))

a = pd.DataFrame()
b = pd.DataFrame()
