from src.abstractsort import AbstractSort

class BubbleSort(AbstractSort):
    def __init__(self):
        super().__init__()
        self.sort_method_name = 'Bubble sort'

    def get_numbers_list(self):
        print('I should get numbers list here')


    def sort_numbers(self):
        print("I should bubble sort here")


if __name__ == '__main__':
    sortme = BubbleSort()
    sortme.get_numbers_list()
    sortme.sort_numbers()
    sortme.print_sort_name()