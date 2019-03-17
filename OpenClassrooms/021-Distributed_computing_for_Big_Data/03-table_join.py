# Problem: Given a table of movies and a table of movie directors,
# return a join of both tables on the director's ID.

example_input_1 = ('Movie', 123, 'Pulp Fiction')
example_input_2 = ('Director', 15, 'Martin Scorcese')


def map_function(key, value):
    map_result = []
    for val in value:
        map_result.append((val[1], (val[0], val[2])))
    return(map_result)


def reduce_function(key, values):
    name_list = []
    director = None
    for category, name in values:
        if category == 'Director':
            director = name
        else:
            name_list.append(name)
    reduce_result = list(map(lambda name: (director, name), name_list))
    return reduce_result


print(map_function(1, [example_input_1]))
print(reduce_function(123, [('Movie', 'Pulp Fiction'), ('Director', 'Q. Tarentino')]))