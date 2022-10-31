# Process Matrix

This was a practical assignment for the Bootcamp Women In Tech by KeepCoding and Glovo.

__What it does?__

Takes a matrix as argument.
Returns a new matrix with the elements of its lists transformed
to the average of its inicial value and its neighbours values.


__What was my approach?__

I split the functionality in different functions.
The main functions are:

1. A process_matrix function that manages the call to _process_matrix.
Only the arguments that evaluate as being a numerical matrix with lists of the same lenght can be called on _process_matrix.

2. _process_matrix applies process_element in all the elements of the matrix and appends the new elements to a new column, and the new column to the new matrix.

3. process_element gets the value of the numbers that are side by side and up and down of the current index and returns its average.

__Where can this function be applied on?__

This function can be applied on images as a smooth filter.
