from collections import namedtuple


class Allergies(object):
    Allergen = namedtuple('Allergen', ['score', 'name'])

    ALLERGENS = [
        Allergen(score=1, name='eggs'),
        Allergen(score=2, name='peanuts'),
        Allergen(score=4, name='shellfish'),
        Allergen(score=8, name='strawberries'),
        Allergen(score=16, name='tomatoes'),
        Allergen(score=32, name='chocolate'),
        Allergen(score=64, name='pollen'),
        Allergen(score=128, name='cats'),
    ]

    def __init__(self, total_score):
        self._lst = [
            name for score, name in self.ALLERGENS
            if (score & total_score) == score
        ]

    def __bool__(self):
        return bool(self._lst)

    def __len__(self):
        return len(self._lst)

    def __getitem__(self, postion):
        return self._lst[postion]
