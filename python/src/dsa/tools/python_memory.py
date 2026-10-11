import sys
import json

from dataclasses import dataclass

class MemoryFootprintOfList():

    def __init__(self, input: list):
        self._list = input
        self.list_length = len(input)
        self.list_container_ref_total = self._size_of_list()
        self.list_stored_data_total = self._size_of_stored_data()
        self.total = self.list_container_ref_total+self.list_stored_data_total
        self.average_per_element: float | None = self._calculate_average_per_element()

    def _size_of_list(self) -> int:
        return sys.getsizeof(self._list)

    def _size_of_stored_data(self) -> int:
        total_stored_data = 0
        for i in range(len(self._list)):
            total_stored_data += sys.getsizeof(self._list[i])
        return total_stored_data

    def _calculate_average_per_element(self) -> float | None:
        if self.list_length > 0:
            return float(self.total - 56) / self.list_length
        return None

    def __repr__(self):
        self_dict = {}
        for k in self.__dict__.keys():
            if not k.startswith("_"):
                self_dict[k] = self.__dict__.get(k)
        return f"{json.dumps(self_dict, indent=2)}"




# def size_of_list(input: list) -> MemoryFootprintOfList:
#     total_container_size = sys.getsizeof(input)
#     total_stored_data = 0
#     for i in range(len(input)):
#         total_stored_data += sys.getsizeof(input[i])

#     return MemoryFootprintOfList(
#         total=total_container_size+total_stored_data,
#         list_length=len(input),
#         list_container_ref_total=total_container_size,
#         list_stored_data_total=total_stored_data,
#     )




def main():
    empty_list = []

    print(sys.getsizeof(''))
    print(sys.getsizeof(""))
    print(sys.getsizeof("a"))
    print(sys.getsizeof("b"))
    print(sys.getsizeof("ab"))

    # print(MemoryFootprintOfList(empty_list))
    # print(MemoryFootprintOfList(["graham"]))
    # print(MemoryFootprintOfList(["graham", 123]))

    # print(size_of_list(empty_list).__dict__)
    # print(size_of_list(["graham", 123]).__dict__)


if __name__ == '__main__':
    main()