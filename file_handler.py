def import_data_from_file(filename):
    to_import=[]
    with open(filename,"r") as f:
        read_file = f.readlines()
        for i in read_file:
            to_import.append(i.rstrip().split(","))
    return(to_import)

def export_data_to_file(export_to_file,filename):
    pass

def main():
    print(import_data_from_file("text_albums_data.txt"))

main()