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
        return sets[1]
pass

def all_imported_release_year(list_of_data_import):
    for release_year in list_of_data_import:
        return release_year[2]
pass

def all_imported_genre(list_of_data_import):
    for genre in list_of_data_import:
        return genre[3]
pass

def all_imported_length(list_of_data_import):
    for lenght in list_of_data_import:
        return lenght[4]
pass

def search_by_artist(all_imported_artist):
    for by_artist in all_imported_artist:
        print(by_artist[0])
pass
#
#def search_by_album(all_imported_albums):
#    for by_album in all_imported_albums:
#        print(by_album[1])
#pass
#
#def search_by_release_year(all_imported_release_year):
#    for by_release_year in all_imported_release_year:
#        print(by_release_year[2])
#pass
#
#def search_by_genre(all_imported_genre):
#    for by_genre in all_imported_genre:
#        print(by_genre[3])
#pass
#
#def search_by_lenght(all_imported_length):
#    for by_lenght in all_imported_length:
#        print(by_lenght[4])

def main():
    data = fh.import_data_from_file("text_albums_data.txt")
    print(all_imported_artist(data))
    all_imported_albums(data)
    #print("---------")
    all_imported_release_year(data)
    all_imported_genre(data)
    all_imported_length(data)
    search_by_artist(data)

main()