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
                self (Self): An object.
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
                cls (Type[Self]): A class object.
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
            Args:
                self (Self): An object.
            Returns:
                Self | None: Return the reference to next node object in singly
                linked list if exists, None otherwise.
            """
            return self.__link

        @_link.setter
        def _link(self: Self, link: Self | None) -> None:
            """Mutate the property self._link before validating it.
            Args:
                self (Self): An object
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
