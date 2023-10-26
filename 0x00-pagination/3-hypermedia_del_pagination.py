#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary showing the current index, next_index,
           page_size and data of the requested page
        """
        dataset = self.dataset()
        assert index < len(dataset), 'Error in index range'
        next_idx = index + page_size
        indexed_dat = self.indexed_dataset()
        data_list = []
        for key in indexed_dat:
            value = indexed_dat[key]
            data_list.append(value)
        needed_data_dict = {m: data_list[m] for m
                            in range(index, next_idx)}
        needed_data = [data for data in needed_data_dict.values()]

        if index not in indexed_dat:
            next_idx += 1

        data = {'index': index, 'next_index': next_idx,
                'page_size': page_size, 'data': needed_data}
        return data
