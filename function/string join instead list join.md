## Why is it string.join(list) instead of list.join(string)?

This is because join is a "string" method! It creates a string from any iterable. If we stuck the method on lists, what about when we have iterables that aren't lists?

What if you have a tuple of strings? If this were a list method, you would have to cast every such iterator of strings as a list before you could join the elements into a single string! For example:

some_strings = ('foo', 'bar', 'baz')

Let's roll our own list join method:

class OurList(list): 
    def join(self, s):
        return s.join(self)

And to use it, note that we have to first create a list from each iterable to join the strings in that iterable, wasting both memory and processing power:
```
>>> l = OurList(some_strings) # step 1, create our list
>>> l.join(', ') # step 2, use our list join method!
'foo, bar, baz'
```
So we see we have to add an extra step to use our list method, instead of just using the builtin string method:

```
>>> ' | '.join(some_strings) # a single step!
'foo | bar | baz'
```

Performance Caveat for Generators

The algorithm Python uses to create the final string with str.join actually has to pass over the iterable twice, so if you provide it a generator expression, it has to materialize it into a list first before it can create the final string.

Thus, while passing around generators is usually better than list comprehensions, str.join is an exception:
```
>>> import timeit
>>> min(timeit.repeat(lambda: ''.join(str(i) for i in range(10) if i)))
3.839168446022086
>>> min(timeit.repeat(lambda: ''.join([str(i) for i in range(10) if i])))
3.339879313018173
```
Nevertheless, the str.join operation is still semantically a "string" operation, so it still makes sense to have it on the str object than on miscellaneous iterables.

https://stackoverflow.com/questions/493819/python-join-why-is-it-string-joinlist-instead-of-list-joinstring