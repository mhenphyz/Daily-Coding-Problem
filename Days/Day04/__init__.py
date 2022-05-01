# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive
# integer in linear time and constant space. In other words,
# find the lowest positive integer that does not exist in the
# array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2.
# The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def day04(int_array):
    int_array.sort()

    max_positive_array = range(1, int(int_array[-1] + 2))
    
    print(max_positive_array)

    remove_negatives = [n for n in int_array if n > 0]

    remove_list_from_range = [
                              n for n in max_positive_array
                              if n not in remove_negatives
                             ]

    if len(remove_list_from_range) >= 1:
        return remove_list_from_range[0]

    return 1


if __name__ == '__main__':

    print(day04([3, 4, -1, 1]))
    print(day04([1, 2, 0]))
    print(day04(list(range(1, 1000))))
    print(day04([-3, -15, -167]))
    print(day04([-3, -15, -167, 158]))
