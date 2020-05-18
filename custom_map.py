# Importing the needed classes for the fetching process
from index_object import PositionalIndex


# This class is built to extract the current index_map from the index file if it does exist
class IndexMap(object):

    # Passing the required arguments
    def __init__(self, index_path='collection\\index'):
        self.index_path = index_path
        self.index_map = {}
        self.times = True
        self.current_word = ''
        self.list_of_indexes = {}

    # Open the index file for reading and loop throw each to get the mapping for each word in it
    # If the file does not exist it returns an empty map
    def read_file(self):
        try:
            with open(self.index_path, 'r', encoding="utf8") as index:
                for line in index:
                    splitted_line = line.split(' ')
                    self.line_doctor(splitted_line)
                return self.list_of_indexes
        except FileNotFoundError:
            return {}

    def line_doctor(self, splitted_line):
        # in case we are at the beginning or at the end of the word indexing map
        if len(splitted_line) == 1:
            if splitted_line[0] == '}\n':
                self.times = True
            return

        # in case we are at the line were we should read the word and it'occurrence times
        if len(splitted_line) == 3 and ('=>' not in splitted_line) and self.times:
            self.current_word = splitted_line[0].replace('"', '').replace('”', '').replace('“', '')
            self.list_of_indexes[self.current_word] = PositionalIndex()
            self.list_of_indexes[self.current_word].set_word(self.current_word)
            self.list_of_indexes[self.current_word].set_occurrence_times(int(splitted_line[2]))
            self.times = False
            return

        # in case we are at the line were we should read the documentID and the list of positions
        positional_index_list = self.filter_list(splitted_line[2:])
        self.list_of_indexes[self.current_word].set_positions_map(splitted_line[0], positional_index_list)

    @staticmethod
    def filter_list(positional_index_list):
        filtered_list = []
        for element in positional_index_list:
            element = element.replace('\n', '').replace('[', '').replace(']', '').replace(',', '')
            if len(element) > 0:
                filtered_list.append(int(element))
        return filtered_list

    def write_to_index(self, index):
        with open(self.index_path, 'w', encoding="utf8") as index_file:
            for word in index:
                current_word = index[word]
                positions_map = current_word.get_positions_map()
                index_file.writelines(f'{current_word.get_word()} , {current_word.get_occurrence_times()}\n{"{"}\n')
                for doc in positions_map:
                    current_list = list(positions_map[doc])
                    index_file.writelines(f'{doc} => {current_list}\n')
                index_file.writelines('}\n\n')
