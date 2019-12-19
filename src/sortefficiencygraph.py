import matplotlib.pyplot as plt
import time
from src.abstractsort import AbstractSort
from src.bubblesort import BubbleSort
from src.quicksort import QuickSort
import random

class SortEfficiencyGraph:
    def __init__(self):
        self.algorithms_list = []
        # self.bubble_sort = BubbleSort()
        # self.quick_sort = QuickSort()

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


    def get_algorithm_time(self, algorithm: AbstractSort) -> float:
        start = time.time()
        algorithm.sortnumbers()
        end = time.time()
        return end - start