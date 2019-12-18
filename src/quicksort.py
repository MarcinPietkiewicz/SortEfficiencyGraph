from src.abstractsort import AbstractSort

class QuickSort(AbstractSort):
    def __init__(self):
        super().__init__()
        sort_method_name = 'Quick sort'

    def get_numbers_list(self):
        print('I should get numbers list here')


    def sort_numbers(self):
        print("I should quick sort here")



if __name__ == '__main__':
    sortme = BubbleSort()
    sortme.get_numbers_list()
    sortme.sort_numbers()
