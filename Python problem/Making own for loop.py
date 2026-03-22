#making own for loop
def making_own_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            element = next(iterator)
            print(element)
        except StopIteration:
            break
a = {1:"red",2:"green",3:"blue"}
b = (1,2,3,4)
# making_own_for_loop(b)
making_own_for_loop(a.values())