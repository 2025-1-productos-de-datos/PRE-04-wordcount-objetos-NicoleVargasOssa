class TextProcessor:
    """Class to preprocess text lines and split them into words."""

    def preprocess_lines(self, lines):
        """Preprocess lines by normalizing and cleaning text."""
        return [line.lower().strip() for line in lines]

    def split_into_words(self, lines):
        """Split lines into individual words and clean puntuaction."""
        words = []
        for line in lines:
            words.extend(word.strip(",.!?") for word in line.split())
        return words
