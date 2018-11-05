"""
Тут написати умову до завдання
"""

from example.Tereshchenko_Igor.workshop1.source.inputpkg.inputter import inputFloat
from

def summ(a, b):
    """
        This fucntion add two floats which belongs to [-100,100]

        Args:
            a:   float number
            b:   float number


        Returns:
            A float number is the result.

        Raises:
            AssertionError, ValueError.

        Examples:
            >>> print(sum(11.5,0.5))
            12.0

            >>> print(sum(100.5,1.5))
            Traceback (most recent call last):
                ...
            ValueError:<unprintable ValueError object>

            >>> print(sum(100,1.5))
            Traceback (most recent call last):
                ...
                assert isinstance(a, float)
            AssertionError:AssertionError

            >>> print(sum(1.5,"a"))
            Traceback (most recent call last):
                ...
                assert isinstance(b, float)
            AssertionError:AssertionError
        """
    assert isinstance(a, float)
    assert isinstance(b, float)

    if (a > 100.0) | (a < -100.0) | (b > 100.0) | (b < -100.0):
        raise ValueError

    return a + b


if __name__ == "__main__":
    a = inputFloat("Enter float: ")
    b = inputFloat("Enter float: ")
    print(sum(a, b))
