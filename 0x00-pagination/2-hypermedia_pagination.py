#!/usr/bin/env python3
"""This module contains a function that that takes two integer arguments
   page and page_size, and returns tuple of size two containing
   a start index and an end index corresponding to the range of indexes
   to return in a list for those particular pagination parameters.
"""

from typing import Tuple
import csv
from math import floor, ceil
from typing import List, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''returs a tuple'''
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "./Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''gives the correct page index and reads the page'''

        assert isinstance(page, int) and page > 0, "page \
                must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size \
                must be a positive integer"

        idx_range = index_range(page, page_size)
        dataset = self.dataset()

        if (idx_range[0] > len(dataset)
                or idx_range[1] > len(dataset)):
            correct_data = []
        correct_range = self.__dataset[idx_range[0]:idx_range[1]]
        return correct_range

    def get_hyper(self, page: int = 1, page_size: int = 10) ->\
            Dict[str, Union[List[List]]]:
        """returns a dictionary with the following key, value pair...
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """

        data = self.get_page(page, page_size)
        dataset = self.dataset()
        page_number = len(dataset) / page_size

        if ceil(page_number) >= page:
            next_page = page + 1
        else:
            next_page = None

        if (page - 1) == 0:
            prev_page = None
        else:
            prev_page = page - 1

        total_pages = len(dataset[1:]) / page_size

        if isinstance(total_pages, float):
            total_pages = ceil(total_pages)

        dict_obj = {'page_size': len(data), 'page': page, 'data': data,
                    'next_page': next_page, 'prev_page': prev_page,
                    'total_pages': total_pages}
        return dict_obj
