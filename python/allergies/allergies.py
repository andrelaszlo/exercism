"""Given a person's allergy score, this program can tell whether or not they're
allergic to a given item, and their full list of allergies.
"""

class Allergies(object):
    """Manages an allergy score."""

    ITEMS = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes",
             "chocolate", "pollen", "cats"]

    def __init__(self, score):
        self._score = score

    def _item_value(self, item):
        """Get the value of an item."""
        return 1 << self.ITEMS.index(item.lower())

    def is_allergic_to(self, item):
        """See if the item is included in this allergy score."""
        return self._item_value(item) & self._score != 0

    @property
    def list(self):
        """List all the allergies included in this allergy score."""
        return filter(self.is_allergic_to, self.ITEMS)
