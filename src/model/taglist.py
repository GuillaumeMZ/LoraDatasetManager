class Taglist:
    def __init__(self, tags):
        self.tags = tags

    def add_tag(self, tag, position):
        self.tags.insert(position, tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)

    def add_tags(self, tags, position):
        self.tags = self.tags[:position] + tags + self.tags[position:] #??

    def remove_tags(self, tags):
        for tag in tags:
            self.tags.remove(tag)