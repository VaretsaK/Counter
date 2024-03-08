class Counter:
    """
        A class that maintains a global count across all instances.

        Attributes:
            count (int): A class-level attribute that tracks the total number of
                         Counter instances that have been created.
            method_called (int): An instance-level attribute that counts the number
                                 of times the get_count method is called on the instance.

        Methods:
            __init__: Initializes a new Counter instance, incrementing the global count.
            get_count: Returns the number of Counter instances and increments the
                       method call count for the instance.
        """
    count = 0

    def __init__(self) -> None:
        """
        Initialize a new Counter instance, incrementing the class-wide count.
        """
        Counter.count += 1
        self.method_called = 0

    def get_count(self) -> int:
        """
        Increment the method call count and return the number of Counter instances.
        """

        # increments the instance variable 'method_called' by 1 each time
        # it is called, tracking how many times this particular method has been used
        # for the instance.
        self.method_called += 1
        return Counter.count
