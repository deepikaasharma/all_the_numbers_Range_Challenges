# Create a list (using range()) named all_the_numbers that has the numbers from 500 up to and including 1000.

# all_the_numbers = list(range(500, 1001))

# print(all_the_numbers)


# You want to create a list of all the numbers between 100 and 1000 (including 1000) that are evenly divisible by 10. How should you do this?

# list_of_all_numbers = list(range(100, 1001,10 ))

# print(list_of_all_numbers)


"""In this challenge, you will create four range objects (not list objects), each assigned to a variable according to the following specifications:

    zero_to_fifty - all of the numbers from zero to fifty (inclusive)
    zero_to_fifty_evens - all of the even numbers from zero to fifty (inclusive)
    zero_to_fifty_odds - all of the odd numbers from zero to fifty (zero is an even number)
    zero_to_fifty_by_threes - every third number from zero to fifty (0, 3, ...)

Note: This challenge is not looking for lists, but rather the range objects themselves."""

zero_to_fifty = range(0, 51)

zero_to_fifty_evens = range(0,51, 2)

zero_to_fifty_odds = range(1, 50, 2)

zero_to_fifty_by_threes = list(range(0, 50, 3))

# print(zero_to_fifty)

print(zero_to_fifty_by_threes)