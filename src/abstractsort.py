from abc import ABC, abstractmethod


class AbstractSort(ABC):
    def __init__(self):
        self.sort_method_name = None

    @abstractmethod
    def get_numbers_list(self):
        raise NotImplementedError('get_list method not implemented!')

    @abstractmethod
    def sort_numbers(self):
        raise NotImplementedError('Sorting mechanism not implemented!')

    def print_sort_name(self):
        print(self.sort_method_name)