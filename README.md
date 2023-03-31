# divide_and_conquer_algorithm
This is an implementation of the Karatsuba algorithm for multiplying large numbers. It is a recursive algorithm that uses a divide and conquer strategy to reduce the number of multiplication operations needed.

The code takes two command-line arguments, which are the two numbers to be multiplied. If the numbers are negative, the code will print a negative sign before the result if only one of them is negative.

The code works by breaking the two input numbers into three pieces and recursively calling the Karatsuba algorithm on those pieces. Once the pieces are small enough, the algorithm uses ordinary multiplication to compute the result.

The main challenge with implementing the Karatsuba algorithm is handling the "padding" of zeros that is required to ensure that the two input numbers have the same length. The code includes a function called "zeroPad" that adds zeros to the beginning or end of a string. The code also uses the built-in Python function "ord" to convert characters to ASCII codes and "chr" to convert ASCII codes back to characters.
