from typing_extensions import Self
from typing import Any, Type


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Non-public class for storing a singly linked list node."""

        def __init__(self: Self, val: Any, link: Self | None = None) -> None:
            """Create and initilize an object that can be used as node to build
            a singly linked list.
            Args:
                val (Any): The data object stored inside the node.
                link (Self, optional): Reference to next node object in singly
                linked list. Defaults to None.
            """
            self._val = val
            self._link = link

        @classmethod
        def _valid_link(cls: Type[Self], link: Self | None) -> bool:
            """Validate the link.
            Args:
                link (Self | None): This is link that need be validate. In order
                link to be valid it need to be either LinkedStack._Node or None
                type.
            Returns:
                bool: Return True, when link is valid, False otherwise.
            """
            return isinstance(link, cls) or link is None

        @property
        def _link(self: Self) -> Self | None:
            """The property, reference to next node object.
            Returns:
                Self | None: Return the reference to next node object in singly
                linked list if exists, None otherwise.
            """
            return self.__link

        @_link.setter
        def _link(self: Self, link: Self | None) -> None:
            """Mutate the property self._link before validating it.
            Args:
                link (Self | None): Mutate property with this.
            Raises:
                TypeError: If link is not valid. In order link to be valid it
                need to be either LinkedStack._Node or None type.
            """
            if not self._valid_link(link):
                cls_name = self.__class__
                link_cls_name = link.__class__
                raise TypeError(
                    f"inappropriate type for the '_link': expecting either \
                    '{cls_name}' or '{None}' but got '{link_cls_name}'"
                )
            self.__link = link

        def __str__(self) -> str:
            """Implements str(self).
            Returns:
                str: Return the string representation of an object
            """
            cls_name = self.__class__.__name__
            return f"<{cls_name} contains {self._val}>"

    def __init__(self: Self) -> None:
        """Create an empty queue."""
        self._head: LinkedQueue._Node | None = None  # Reference to the head node.
        self._tail: LinkedQueue._Node | None = None  # Reference to the tail node.
        self._size: int = 0  # Number of queue items.

    def __len__(self: Self) -> int:
        """Return length of queue.

        Time complexity: O(1)

        Returns:
            int: Number of items in the queue.
        """
        return self._size

    def is_empty(self: Self) -> bool:
        """Return True when queue is emtpy, False otherwise.

        Returns:
            bool: True when queue is emtpy, False otherwise.
        """
        return self._head is None

    def enqueue(self: Self, value: Any) -> None:
        """Add an item to the back of queue.

        Time complexity: O(1)

        Args:
            value (Any): The value that need to be added.
        """
        new_tail_node = self._Node(value)
        if self._tail is None:  # Or self.is_empty()
            self._head = new_tail_node  # Special case: previously empty
        else:
            self._tail._link = new_tail_node  # Link to the tail node
        self._tail = new_tail_node  # Update referece to tail node
        self._size += 1

    def dequeue(self: Self) -> Any:
        """Remove and return the first item of the queue (i.e. FIFO)

        Time complexity: O(1)

        Raises:
            Exception: Trying to dequeue from empty queue.

        Returns:
            Any: The first item of the queue.
        """
        if self._head is None:
            raise Exception("trying to dequeue in empty queue")
        value = self._head._val  # The value that need be return.
        self._head = self._head._link  # Update head to refer to next node.
        self._size -= 1
        if self._head is None:
            self._tail = None  # Since no node present tail must be None.
        return value

    def first(self: Self) -> Any:
        """Return (but do not remove) the item at the front of the queue.

        Time Complexity: O(1)

        Raises:
            Exception: Trying to perform operation on empty queue.

        Returns:
            Any: Return item at the front of the queue.
        """
        if self._head is None:
            raise Exception("trying to return item from emtpy queue")
        return self._head._val
