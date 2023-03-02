class Taglist:
    """
    An ordered set of tags, without any duplicates.
    """
    def __init__(self, raw_content: str):
        """
        Creates a Taglist from a string containing tags separated by commas. For instance, the string "a, b, c" yields
        the dataset ["a", "b", "c"].
        """
        self._tags = list(map(lambda tag: tag.strip(), raw_content.split(",")))

    def add_tag(self, tag: str, position: int = -1):
        """
        Add a tag to the tag list.
        :param tag: the tag to add
        :param position: the position where the tag should be
        added. Starts at 0; -1 corresponds to the end of the taglist, -2 corresponds to the element before the last,
        and so on.
        """
        if tag in self._tags:  # No duplicate allowed
            return

        if position < 0:
            position = len(self._tags) + position + 1

        self._tags.insert(position, tag)

    def remove_tag(self, tag: str):
        """
        Removes the tag if it is present in the taglist; does nothing otherwise
        :param tag: the tag to remove
        """
        try:
            self._tags.remove(tag)
        except ValueError:
            pass
