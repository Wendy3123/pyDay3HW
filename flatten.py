def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)
print(flatten_and_sort(['hello','bye']))

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?
we append only data structures so it remains unchanged once its written

Is this solution a pure function? Why or why not?
our functions output value follows only from its input values and has no side effects

Is this solution a higher order function? Why or why not?
no because our function is not taking another function as a argument

Would it have been easier to solve this problem using a different programming style?
I think this way is the easiest way.

Why in particular is functional programming a helpful paradigm when solving this problem?
using functional programming is helpful because it is easier to debug because it has no side effects
'''