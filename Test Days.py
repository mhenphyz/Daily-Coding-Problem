import unittest
import random

from Days import day01


class Test_Every_Day(unittest.TestCase):

    def test_01_suggested(self):
        self.assertEqual(day01([10, 15, 3, 7], 17), True,
                         "There is no two numbers that can be add up to k")

    def test_01_stress(self):
        random_lists = (
            random.choices(range(0, 100), k=random.choice(range(2, 6)))
            for x in range(100)
            )

        for number_list in random_lists:

            sum_members = sum(random.sample(number_list, 3))

            self.assertEqual(day01(number_list, sum_members), True,
                             "There is no two numbers that can be add up to k")


if __name__ == '__main__':
    unittest.main()
