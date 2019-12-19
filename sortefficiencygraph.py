import matplotlib.pyplot as plt
import time
from src.abstractsort import AbstractSort
from src.bubblesort import BubbleSort
from src.quicksort import QuickSort
import random
import copy


class SortEfficiencyGraph:
    """
    This class is used to display on graph time complexity of two sorting algorithms.
    It takes 2 algorithms and creates 4 random lists to sort with given number of elements.
    Then it measures time of each algorithm when sorting those random lists.
    Lastly it displays graphs comparing time complexity of two sorting algorithms.
    """
    def __init__(self):
        self.algorithms_list = []
        self.list_to_sort_1 = []
        self.list_to_sort_2 = []
        self.list_to_sort_3 = []
        self.list_to_sort_4 = []
        self.sort_times_list = []

    def get_two_algorithms(self, algorithm1: AbstractSort, algorithm2: AbstractSort):
        """
        Method used to get two algorithms to compare later on.
        :param algorithm1:
        :param algorithm2:
        :return:
        """
        self.algorithms_list.append(algorithm1)
        self.algorithms_list.append(algorithm2)

    def create_data_to_sort(self, length1: int, length2: int, length3: int, length4: int):
        """
        This method creates 4 unsorted lists of random numbers that will be used as a template to sort
        :param length1:
        :param length2:
        :param length3:
        :param length4:
        :return:
        """
        self.list_to_sort_1, self.list_to_sort_2, self.list_to_sort_3, self.list_to_sort_4 = [], [], [], []
        for i in range(1, length1):
            self.list_to_sort_1.append(random.randint(1, 5000))
        for i in range(1, length2):
            self.list_to_sort_2.append(random.randint(1, 5000))
        for i in range(1, length3):
            self.list_to_sort_3.append(random.randint(1, 5000))
        for i in range(1, length4):
            self.list_to_sort_4.append(random.randint(1, 5000))

    def plot_chart(self, algorithm: AbstractSort):
        """

        :param algorithm: sorting algorithm
        :type algorithm: AbstractSort class
        :return:
        """
        plt.plot([len(self.list_to_sort_1),len(self.list_to_sort_2),
                  len(self.list_to_sort_3)],[self.get_algorithm_time(algorithm, self.list_to_sort_1),
                   self.get_algorithm_time(algorithm, self.list_to_sort_2),
                   self.get_algorithm_time(algorithm, self.list_to_sort_3)])
        plt.ylabel(['sorting time'])
        plt.xlabel(['sorted elements'])
        plt.legend(['hello'])
        plt.show()

    def get_algorithm_time(self, algorithm: AbstractSort, list_to_sort: list) -> float:
        """
        This method runs algorithms with a list to sort and returns time it took.
        :param algorithm:
        :param list_to_sort: list of numbers
        :type list_to_sort: list[int]
        :return:
        """
        temporary_list_to_sort = copy.deepcopy(list_to_sort)
        start = time.time()
        algorithm.get_numbers_list(temporary_list_to_sort)
        algorithm.sort_numbers()
        end = time.time()
        return end - start


if __name__ == '__main__':
    sort_me = SortEfficiencyGraph()
    sort_me.get_two_algorithms(BubbleSort(), QuickSort())
    sort_me.algorithms_list[0].print_sort_name()
    sort_me.algorithms_list[1].print_sort_name()
    sort_me.create_data_to_sort(100, 200, 300, 400)
    print(sort_me.get_algorithm_time(sort_me.algorithms_list[0], sort_me.list_to_sort_1))
    sort_me.plot_chart(sort_me.algorithms_list[0])