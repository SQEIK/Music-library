import file_handler as fh
def all_imported_artist(list_of_data_import):
    for artist in list_of_data_import:
        print(artist[0])
pass 
#return i pomyśleć w jakiej formie chce to zwrócić
#czy jako gotowy string czy coś po czym jeszcze
#możemy iterować

def all_imported_albums(list_of_data_import):
    for sets in list_of_data_import:
        print(sets[1])
pass

def all_imported_release_year(list_of_data_import):
    for release_year in list_of_data_import:
        print(release_year[2])
pass

def all_imported_genre(list_of_data_import):
    for genre in list_of_data_import:
        print(genre[3])
pass

def all_imported_length(list_of_data_import):
    for lenght in list_of_data_import:
        print(lenght[4])
pass

def main():
    data = fh.import_data_from_file("text_albums_data.txt")
    all_imported_albums(data)
    print("---------")
    all_imported_artist(data)
    print("---------")
    all_imported_release_year(data)
    print("---------")
    all_imported_genre(data)
    print("---------")
    all_imported_length(data)

main()