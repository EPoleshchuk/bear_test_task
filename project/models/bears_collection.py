from project.models.bear import Bear


class BearsCollection:
    def __init__(self, bear_objects: list = None):
        """
        BearsCollection initializer
        :param bear_objects (optional, list): list with bear objects
        """
        self.bear_objects = [Bear(**bear_data) for bear_data in bear_objects] \
            if bear_objects else []

    def __add__(self, bear: Bear) -> None:
        """
        Add new bear to bear collection
        :param bear (Bear): object to be added
        :return: None
        """
        self.bear_objects.append(bear)

    def __contains__(self, bear: Bear) -> bool:
        """
        Check if bear in bear collection or not
        :param bear (Bear): bear object
        :return: is bear object in collection or not
        :rtype: bool
        """
        for bear_obj in self.bear_objects:
            if bear_obj == bear:
                return True
        else:
            return False

    def __eq__(self, bears_collection: 'BearsCollection') -> bool:
        """
        Compare bear collection with other bear collection
        :param bears_collection (BearsCollection): bear collection to compare
        :return: equal or not
        :rtype: bool
        """
        if len(self.bear_objects) != len(bears_collection):
            return False

        for bear_obj in self.bear_objects:
            if bear_obj not in bears_collection:
                return False
        return True

    def __str__(self) -> str:
        """
        Get str representation of bear collection
        :return: string representation
        :rtype: str
        """
        return "\n".join([str(bear_obj) for bear_obj in self.bear_objects])

    def __len__(self) -> int:
        """
        Get bear collection length
        :return: collection length
        :rtype: int
        """
        return len(self.bear_objects)
