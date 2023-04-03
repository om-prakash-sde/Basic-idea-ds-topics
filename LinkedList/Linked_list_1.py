# Representation of Singly Linked Lists
class Node:
    # Function to initialize the node object
    def __init__(self,data) -> None:
        self.data=data
        self.node=None

class LinkedList:
    def __init__(self) -> None:
        # Function to initialize the Linked
        # List object
        self.head=None