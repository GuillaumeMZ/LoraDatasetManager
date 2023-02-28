class Taglist:
    def __init__(self, raw_content: str):
        self._tags = list(map(lambda tag: tag.strip(), raw_content.split(",")))
