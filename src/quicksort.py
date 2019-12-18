from src.abstractsort import AbstractSort

class QuickSort(AbstractSort):
    def __init__(self):
        super().__init__()
        self.sort_method_name = 'Quick sort'


    def get_numbers_list(self, numbers: list):
        print('I should get numbers list here ', numbers)


    def sort_numbers(self):
        print("I should quick sort here and return sorted list")
        return self.numbers


if __name__ == '__main__':
    sortme = QuickSort()
    sortme.get_numbers_list([1,2,3])
    sortme.sort_numbers()
    sortme.print_sort_name()