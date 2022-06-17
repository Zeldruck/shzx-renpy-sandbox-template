init -50 python:
    import random
    import math

    class Vector2:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def ChangePositionInArray(_array, lIndex, nIndex):
        if (lIndex == nIndex or lIndex >= len(_array) or nIndex >= len(_array)):
            return

        tempValue = _array.pop(lIndex)
        _array.insert(nIndex, tempValue)