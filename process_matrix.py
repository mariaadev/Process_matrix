from functools import reduce

def process_element(row, index,elements): 
    """
    Gets an index, a row and a list of elements. Calculates the average of itself with its neighbours,
    and returns the average.
    """
    #Get left and right side neighbours
    indices = get_neighbours_indices(index,elements) 
    values = get_neighbours_values(indices,row, elements)
    
    #Get up and down neighbours
    indices_row = get_neighbours_indices_row(row,elements)
    values_row = get_neighbours_values_row(indices_row,index,elements)
    
    #Sum all the neighbours
    values = values + values_row 
    #Get average
    average = get_average(values) 
    
    return average

def get_neighbours_indices(index, elements):
    """
    Returns a list of the neighbours indices from the sides of the current index and the current index.
    """
    indices = []
 
    indices.append(index - 1)

    indices.append(index + 1) 

    indices.append(index)
    #Filter impossible indices, index >= 0 and index < lenght list
    indices = list(filter(lambda x: x >= 0 and x < len(elements[0]),indices)) 

    return indices

def get_neighbours_values(indices,row,elements):
    """
    Gets indices, current row and the matrix. Returns neighbours values from indices.
    """
    values = []

    for index in indices:
        values.append(elements[row][index]) 
    return values

def get_neighbours_indices_row(row,elements): 
    """
    Gets actual row and matrix. Returns list of indices of the neighbours row.
    """
    indices_row = []
 
    indices_row.append(row - 1)

    indices_row.append(row + 1) 

    #Filter impossible indices, row >= 0 and row < lenght matrix
    indices_row = list(filter(lambda x: x >= 0 and x < len(elements),indices_row))

    return indices_row

def get_neighbours_values_row(indices_row,index,elements):
    """
    Gets indices of the neighbours row, actual index and matrix. Returns values of up and down neighbours. 
    """
    values = []

    for row in indices_row:
        values.append(elements[row][index])
    return values

def get_average(numbers):
    """
    Gets a list of numbers and returns its average. 
    """
    return reduce(lambda x,y: x + y, numbers, 0) / (len(numbers)) 

def is_numerical_matrix(matrix):
    """
    Checks the following:   If matrix is list of lists | 
                            If all the lists inside are the same size
                            If the elements on the list are numerical
    """
    is_num = True
    is_list_of_lists = (type(matrix) == list) and (len(matrix) > 1)
    is_size = True

    if is_list_of_lists:
        for index,lista in enumerate(matrix): 
            is_size = is_size and (len(matrix[0]) == len(matrix[index]))
            for element in lista:
                if not is_num: #if not num go out
                    break
                else:       #if is num, continue checking other elements
                    is_num = is_num and (type(element) == int)

    return (is_num and is_size and is_list_of_lists)

def _process_matrix(matrix):
    """
    Gets a matrix and Returns a new matrix with the elements of its lists transformed
    to the average of its inicial value and its neighbours values.
    """
    processed_matrix = []
    processed_column = []
    for i, row in enumerate(matrix): 
        for j, element in enumerate(row): 
            new_value = process_element(i,j,matrix)
            processed_column.append(round(new_value,1))

        processed_matrix.append(processed_column)
        processed_column = []
        
    return processed_matrix

def process_matrix(matrix):
    if matrix == []:
        return []
    elif is_numerical_matrix(matrix): 
        return _process_matrix(matrix)
    else:
        raise ValueError('Only works on numerical matrices')


