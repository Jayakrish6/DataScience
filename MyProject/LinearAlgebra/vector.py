# -*- coding: utf-8 -*-
height_weight_age = [70, # inches,
    170, # pounds,
    40 ] # years
grades = [95, # exam1
    80, # exam2
    75, # exam3
    62 ] # exam4

def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]
    
def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]
    
def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0] # start with the first vector
    for vector in vectors[1:]: # then loop over the others
        result = vector_add(result, vector) # and add them to the result
    return result

def vector_sum1(vectors):
    return reduce(vector_add, vectors)

vector_sum = partial(reduce, vector_add)