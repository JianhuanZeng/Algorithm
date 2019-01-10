########################################################
# iterable: __iter__, __getitem__
# iterator: __next
# generotor: a kind of iterator with yield

########################################################
# map: map(function_to_apply, list_of_inputs)
# filter: filter(lambda x: x < 0, number_list)
# reduce: reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

########################################################
# set
a_set = set([1])
b_set = set([2,4,6])

a_set.add(2)
a_set.intersection(b_set)
a_set.difference(b_set)
