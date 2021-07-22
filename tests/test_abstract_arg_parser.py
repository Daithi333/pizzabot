import unittest

from pizzabot.arg_parser.abstract_arg_parser import AbstractArgParser


class TestAbstractArgParser(unittest.TestCase):

    def test_subclass_instantiation_without_overridden_method_throws_error(self):
        with self.assertRaises(TypeError):
            test_arg_parser = InvalidArgParser()

    def test_subclass_instantiation_with_overridden_method_does_not_throw_error(self):
        try:
            test_arg_parser = ValidArgParser()
        except TypeError:
            self.fail('An Exception was raised!')


class InvalidArgParser(AbstractArgParser):
    pass


class ValidArgParser(AbstractArgParser):
    def extract_grid_and_coords(self, **args) -> ((int, int), list[(int, int)]):
        pass
