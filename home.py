# importing the needed stuff
from custom_map import IndexMap
from file_reader import FileReader

# creating an instance of the indexMap map > and read the index file to extract the map from it
current_index_map = IndexMap()
index_map = current_index_map.read_file()

# ask the user what document he wants to use ** the user must have added the document to the file collection  or it
# wont work > then ask the user if he want the document with stopwords or not
# I have added some documents to the collection if you want to try them out
document_name = input('what is the name of the document that you want to index? ')
should_remove = str.lower(input('should I index with the stop words pls answer with yes or no? '))

# creating an instance of the FileReader
files = FileReader(doc_id=document_name, should_remove=should_remove, index_map=index_map)
# read the file
files.file_reader()

# write it back to the index document
current_index_map.write_to_index(index_map)
