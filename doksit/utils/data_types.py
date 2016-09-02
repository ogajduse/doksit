import collections


class OrderedDict(collections.OrderedDict):
    """Upgraded 'OrderedDict' from module 'collections'."""

    def last(self):
        """Get the name of the last inserted key."""
        return next(reversed(self))
