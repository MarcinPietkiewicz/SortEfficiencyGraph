import matplotlib.pyplot as plt
import time
from src.abstractsort import AbstractSort
from src.bubblesort import BubbleSort
from src.quicksort import QuickSort
import random
import copy

class SortEfficiencyGraph:
    def __init__(self):
        self.algorithms_list = []
        # self.bubble_sort = BubbleSort()
        # self.quick_sort = QuickSort()
        self.list_to_sort_1 = []
        self.list_to_sort_2 = []
        self.list_to_sort_3 = []
        self.list_to_sort_4 = []


    def get_two_algorithms(self, algorithm1: AbstractSort, algorithm2: AbstractSort):
        self.algorithms_list.append(algorithm1)
        self.algorithms_list.append(algorithm2)

    def create_data_to_sort(self, length1, length2, length3, length4):
        self.list_to_sort_1, self.list_to_sort_2, self.list_to_sort_3, self.list_to_sort_4 = [],[],[],[]
        for i in range(1, length1):
            self.list_to_sort_1.append(random.randint(1,5000))
        for i in range(1, length2):
            self.list_to_sort_2.append(random.randint(1,5000))
        for i in range(1, length3):
            self.list_to_sort_3.append(random.randint(1,5000))
        for i in range(1, length4):
            self.list_to_sort_4.append(random.randint(1,5000))



    def plot_chart(self):
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()


    def get_algorithm_time(self, algorithm: AbstractSort, list_to_sort: list) -> float:
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
    sort_me.create_data_to_sort(100,200,300,400)
    # print(sort_me.list_to_sort_1)
    # print(sort_me.list_to_sort_2)
    # print(sort_me.list_to_sort_3)
    # print(sort_me.list_to_sort_4)
    print(sort_me.list_to_sort_1)
    print(sort_me.get_algorithm_time(sort_me.algorithms_list[0], sort_me.list_to_sort_1))
    print(sort_me.list_to_sort_1)