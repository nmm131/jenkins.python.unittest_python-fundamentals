# Created by Leon Hunter at 3:56 PM 10/23/2020
class Predicator(object):
    def is_greater_than_5(self, some_value):
        return bool(some_value > 5)

    def is_greater_than_8(self, some_value):
        return bool(some_value > 8)

    def is_less_than_4(self, some_value):
        return bool(some_value < 4)

    def is_less_than_1(self, some_value):
        return bool(some_value < 1)