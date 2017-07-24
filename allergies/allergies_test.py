import unittest

from allergies import Allergies

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class AllergiesTests(unittest.TestCase):
    def test_no_allergies_means_not_allergic(self):
        allergies = Allergies(0)
        self.assertNotIn('peanuts', allergies)
        self.assertNotIn('cats', allergies)
        self.assertNotIn('strawberries', allergies)

    def test_is_allergic_to_eggs(self):
        self.assertIn('eggs', Allergies(1))

    def test_allergic_to_eggs_in_addition_to_other_stuff(self):
        allergies = Allergies(5)
        self.assertIn('eggs', allergies)
        self.assertIn('shellfish', allergies)
        self.assertNotIn('strawberries', allergies)

    def test_no_allergies_at_all(self):
        self.assertFalse(Allergies(0))

    def test_allergic_to_just_eggs(self):
        self.assertCountEqual(Allergies(1), ['eggs'])

    def test_allergic_to_just_peanuts(self):
        self.assertCountEqual(Allergies(2), ['peanuts'])

    def test_allergic_to_just_strawberries(self):
        self.assertCountEqual(Allergies(8), ['strawberries'])

    def test_allergic_to_eggs_and_peanuts(self):
        self.assertCountEqual(Allergies(3), ['eggs', 'peanuts'])

    def test_allergic_to_more_than_eggs_but_not_peanuts(self):
        self.assertCountEqual(Allergies(5), ['eggs', 'shellfish'])

    def test_allergic_to_lots_of_stuff(self):
        self.assertCountEqual(
            Allergies(248),
            ['strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats'])

    def test_allergic_to_everything(self):
        self.assertCountEqual(
            Allergies(255), [
                'eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes',
                'chocolate', 'pollen', 'cats'
            ])

    def test_ignore_non_allergen_score_parts_only_eggs(self):
        self.assertCountEqual(Allergies(257), ['eggs'])

    def test_ignore_non_allergen_score_parts(self):
        self.assertCountEqual(
            Allergies(509), [
                'eggs', 'shellfish', 'strawberries', 'tomatoes', 'chocolate',
                'pollen', 'cats'
            ])


if __name__ == '__main__':
    unittest.main()
