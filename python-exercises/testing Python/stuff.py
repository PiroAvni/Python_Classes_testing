class ThrowError(Exception):
    pass


def do_maths(x, y):
    try:
        return x+y
    except:
        raise ThrowError(f'Notpossible to add {x} and {y}')

def add_fruit(fruit):
    salad = ['banana', 'apple']
    salad.append(fruit)
    return salad

class StuffError(Exception):
    pass

def how_many_sweets(sweets, people):
    if not people:
        raise StuffError('We need some people to share sweets with!')
    return len(sweets) / len(people)

def greeting(name):
    print(f'Hello, {name}!')
    
    

# cat represents each dictionary element within the list cats.
# for cat in cats iterates over each dictionary in cats.
# if cat['id'] == cat_id checks if the value of the 'id' key in the current cat dictionary matches the given cat_id.
# The generator expression (cat for cat in cats if cat['id'] == cat_id) generates a sequence of dictionaries that meet the condition.
# Finally, next() is used to retrieve the next item from the generator expression. In this case, it returns the first dictionary where the 'id' matches cat_id.

# Note that if there is no match found in the list of dictionaries, a StopIteration exception will be raised. To handle this, you can provide a default value to next() by using next(..., default).

cats =[]

def find_cat_by_id(cat_id):
    return next(cat for cat in cats if cat['id'] == cat_id)