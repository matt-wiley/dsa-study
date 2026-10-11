from typing import List, Any

class LinkedList:

    class Node:
        def __init__(self, parent: LinkedList.Node | None, data: Any):
            self._parent: LinkedList.Node | None = parent
            self._data: Any = data

    def __init__(self):
        self._items: List[LinkedList.Node] = []

    def add(self, item: Any) -> None:
        parent = None
        data = item

        if len(self._items) > 0:
            parent = self._items[-1]

        new_node = LinkedList.Node(parent,data)
        self._items.append(new_node)

    def peak(self) -> Any | None:
        if len(self) > 0:
            return self._items[-1]._data
        return None

    def __len__(self):
        return len(self._items)


