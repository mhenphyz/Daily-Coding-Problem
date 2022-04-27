# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers
# from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.


def long(numbers, k):

    sum_of_members = set()  # avoid duplicated numbers with set instead list

    for index, number in enumerate(numbers):

        for member in numbers[:index] + numbers[index+1:]:

            sum_of_members.add(number + member)

    if k in sum_of_members:
        return True

    return False


def short(numbers, k):
    return True if k in set((n + j for i, n in enumerate(numbers) for j in
                            numbers[:i] + numbers[i+1:])) else False


def day01(numbers, k, short_version=True):
    '''
     I need loop over the list and sum
     with all the members in the list except
     the current member.
    '''

    return short(numbers, k) if short_version is True else long(numbers, k)


if __name__ == '__main__':

    numbers = [10, 15, 3, 7]
    k = 17,

    # long version
    print(day01(numbers, k, False))

    # short version
    print(day01(numbers, k))
