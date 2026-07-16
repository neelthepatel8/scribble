# Parse words.csv to list of words
# allow a new session creator, I think can just be a class instance.
# allow one method to generate()
# for each session should track words used and never show those. Can just be linear lookup since each game is 24 ish rounds
import random


class WordGeneratorService:

    WORD_LIST_FILE = "static/words.csv"

    def __init__(self) -> None:
        self.word_list: list[str] = []
        self._parse_word_list()

    def _parse_word_list(self):
        with open(self.WORD_LIST_FILE, "r") as f:
            for line in f.readlines()[1:]:
                if line.strip():
                    # cols = ["word", "count", ""]
                    cols: list[str] = line.split(",")
                    self.word_list.append(cols[0])

        random.shuffle(self.word_list)

    def generate(self):
        return self.word_list.pop()
