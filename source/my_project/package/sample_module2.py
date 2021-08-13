"""
Sample Module 2
---------------
sample module 2
"""


class SampleClass:
    def __init__(self, arg1: float, arg2: float):
        """[description of SampleClass]

        Args:
            arg1 ([type]): [description]
            arg2 ([type]): [description]
        """
        self.arg1 = arg1
        self.arg2 = arg2

    def sample_method(self, arg1: float, arg2: float) -> float:
        """[summary]

        Args:
            arg1 (float): [description]
            arg2 (float): [description]

        Returns:
            float: [description]
        Examples:

            how to use this method

            >>> sample_method(1.5, 2.5)
                4.
        """
        return arg1 + arg2

    @property
    def sample_property(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.arg1 + self.arg2
