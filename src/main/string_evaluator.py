# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World"

    def concatenate(self, value_to_be_added_to, value_to_add):
        return str(value_to_be_added_to) + str(value_to_add)

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index:ending_index + 1]

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index + 1:ending_index]

    def compare(self, first_value, second_value):
        if first_value == second_value:
            return True
        negative_list = ["0", 0, None, False]
        positive_list = ["1", 1, True]

        is_first_value_positive = first_value in positive_list
        is_first_value_negative = first_value in negative_list
        is_second_value_positive = second_value in positive_list
        is_second_value_negative = second_value in negative_list

        are_both_positive = is_first_value_positive and is_second_value_positive
        are_both_negative = is_first_value_negative and is_second_value_negative

        return are_both_negative or are_both_positive

    def get_middle_character(self, string_to_fetch_from):
        return string_to_fetch_from[len(string_to_fetch_from)/2] # Round?

    def get_first_word(self, string_to_fetch_from):
        return string_to_fetch_from.split()[0]

    def get_second_word(self, string_to_fetch_from):
        return string_to_fetch_from.split()[1]

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1]
