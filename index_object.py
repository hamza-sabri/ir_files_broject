# This class is to represent what each word would look like in the index file
class PositionalIndex(object):

    # Passing the values for each object or setting them to default
    def __init__(self, word='', occurrence_times=0):
        self.word = word
        self.occurrence_times = occurrence_times
        self.positions_map = {}

    # A getter method for the occurrence_times attribute
    def get_occurrence_times(self):
        return self.occurrence_times

    # A getter method for the word attribute
    def get_word(self):
        return self.word

    # A getter method for the positions_map attribute
    def get_positions_map(self):
        return self.positions_map

    # Adding a new position to the map when ever we come across the same word as self.word in the same doc
    def add_to_positions_map(self, doc_id, position):
        self.positions_map[doc_id].append(position)

    # incrementing the occurrence_times attribute when ever we come across the same word as self.word in the same doc
    def increment_occurrence_times(self):
        self.occurrence_times = self.occurrence_times + 1

    # A setter for the word attribute
    def set_word(self, word):
        self.word = word

    # A setter for the occurrence_times attribute
    def set_occurrence_times(self, occurrence_times):
        self.occurrence_times = occurrence_times

    # A setter for the positions_map attribute
    def set_positions_map(self, doc_id, positions_map):
        self.positions_map[doc_id] = positions_map
