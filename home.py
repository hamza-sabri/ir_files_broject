from custom_map import IndexMap
from file_reader import FileReader

currentMap = IndexMap()
index_map = currentMap.read_file()

documentName = input('what is the name of the document that you want to index? ')
shouldRemove = str.lower(input('should I index with the stop words pls answer with yes or no? '))

files = FileReader(doc_id=documentName, should_remove=shouldRemove, index_map=index_map)
files.file_reader()

currentMap.write_to_index(index_map)

# add comments to the project
# try to make the index file more beautiful to look at
# add the choice to loop throw all the files in the collection but the index itself
# you should also filter the words from the " or the one for coats and the dots : and = and > and < and => and ; and •
# and , etc...
# in short build another method and make sure to clean the delivered word from those things
# in the assignment he is saying "positional index written" does that mean we should store the position of the word too?
