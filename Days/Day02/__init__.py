# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the
# original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output
# would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected
#  output would be [2, 3, 6]

def day02(number_list):

    print(f'\nList: {number_list}')

    new_list = list()

    for i, number in enumerate(number_list):
        product = 1

        for n in number_list[i+1:] + number_list[:i]:
            product = product * n

        new_list.append(product)

    print(f'Product List: {number_list}')

    return new_list


if __name__ == '__main__':
    print(day02([1, 2, 3, 4, 5]))
    print(day02([3, 2, 1]))
