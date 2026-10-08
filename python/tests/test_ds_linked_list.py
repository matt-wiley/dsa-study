from dsa.data_structures.linked_list import LinkedList

def test_add_item():
    item = dict(
        firstname="Matt",
        lastname="Wiley"
    )

    linked_list = LinkedList()
    linked_list.add(item)

    assert len(linked_list) == 1
    assert linked_list.peak() == item