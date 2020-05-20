# Importing some important libraries
from nltk.corpus import stopwords
from custom_map import PositionalIndex


# This class is built to read the given document and add it to the index_map object no more!!!
class FileReader(object):

    # Passing the required arguments
    def __init__(self, doc_id, should_remove, index_map):
        self.doc_id = doc_id
        self.doc_path = 'collection\\' + doc_id
        self.removable_words = set(stopwords.words("english"))
        self.should_remove = should_remove
        self.index_map = index_map
        self.position = -1

    # Calling the helper method "start_reading"
    def file_reader(self):
        self.more_removable_words()
        self.start_reading()

    # some removable words in my opinion
    def more_removable_words(self):
        self.removable_words.add('the')
        self.removable_words.add('The')
        self.removable_words.add('a')
        self.removable_words.add('A')
        self.removable_words.add('then')
        self.removable_words.add('Then')
        self.removable_words.add('that')
        self.removable_words.add('That')
        self.removable_words.add(' ')
        # we can add as much as we want that's my point
        pass

        # Open the document for reading and loop throw each line in that document

    # open the received document and open it for reading
    def start_reading(self):
        with open(self.doc_path, 'r', encoding="utf8") as file_to_read:
            for line in file_to_read:
                splitted_line = line.replace('\n', '').split(' ')
                self.index_words(splitted_line)

    # Receiving the line and loop throw each word in it and ignore the stopwords if needed
    def index_words(self, line):
        for word in line:
            self.position += 1
            if (self.should_remove == 'yes') and not (word in self.removable_words):
                self.add_to_index_map(word)
            elif self.should_remove != 'yes':
                self.add_to_index_map(word)

    # Add the word for the index_map object depending on it's own case the cases are explained in the method
    def add_to_index_map(self, word):
        # removing the punctuation marks from the word
        word = self.remove_punctuation_marks(word)
        if word == '':
            return
            # If the word does not exist in the map at all
        if not (word in self.index_map):
            self.index_map[word] = PositionalIndex()
            self.index_map[word].set_word(word)
            self.index_map[word].set_occurrence_times(1)
            self.index_map[word].set_positions_map(self.doc_id, [self.position])

        # If the word exist in the map and the document exist for that word
        elif word in self.index_map and self.doc_id in self.index_map[word].get_positions_map():
            self.index_map[word].increment_occurrence_times()
            current_map = self.index_map[word].get_positions_map()
            if self.position not in current_map[self.doc_id]:
                current_map[self.doc_id].append(self.position)

        # If the word exist in the map but it don't have this particular document in it's object (body)
        elif word in self.index_map and (self.doc_id not in self.index_map[word].get_positions_map()):
            self.index_map[word].increment_occurrence_times()
            current_map = self.index_map[word].get_positions_map()
            current_map[self.doc_id] = [self.position]

    # remove all unnecessary things from the word
    @staticmethod
    def remove_punctuation_marks(word):
        fixed_word = word
        fixed_word = fixed_word.replace(',', '')
        fixed_word = fixed_word.replace('\'', '')
        fixed_word = fixed_word.replace(':', '')
        fixed_word = fixed_word.replace(';', '')
        fixed_word = fixed_word.replace('.', '')
        fixed_word = fixed_word.replace('!', '')
        fixed_word = fixed_word.replace('?', '')
        fixed_word = fixed_word.replace('.', '')
        fixed_word = fixed_word.replace(' ', '')
        fixed_word = fixed_word.replace('/', '')
        fixed_word = fixed_word.replace('\\', '')
        fixed_word = fixed_word.replace('*', '')
        fixed_word = fixed_word.replace('(', '')
        fixed_word = fixed_word.replace(')', '')
        fixed_word = fixed_word.replace('#', '')
        fixed_word = fixed_word.replace('$', '')
        fixed_word = fixed_word.replace('%', '')
        fixed_word = fixed_word.replace('^', '')
        fixed_word = fixed_word.replace('&', '')
        fixed_word = fixed_word.replace('•', '')
        fixed_word = fixed_word.replace('”', '')
        fixed_word = fixed_word.replace('“', '')
        fixed_word = fixed_word.replace('"', '')
        for i in range(10):
            fixed_word = fixed_word.replace(str(i), '')
        return fixed_word.lower()
