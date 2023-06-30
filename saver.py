def import_to_file(name:str, info_to_save:tuple):
    file = open(name, "w")
    file.write('')
    file.close()
    file = open(name, "a")
    for i in range (0, len(info_to_save)):
        for a in range (0, len(info_to_save[i])):
            for b in range (0, len(info_to_save[i])):
                file.write(str(info_to_save[i][a][b]) + ', ')
            file.write(' / ')
        file.write('\n')
""" 
Need to be finished export_out_of_file
"""

