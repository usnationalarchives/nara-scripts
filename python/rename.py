# -*- coding: utf-8 -*-

import os

def rename(folder='objects'):
    print ('Renaming files of ' + folder + ' and its subfolders...')
    for dirpath, _, filenames in os.walk(folder, topdown=True):
        print ('\nRenaming files from', dirpath, '\n')
        if filenames:
            for filename in filenames:
                replaced_name = filename.replace(",", "-")
                replaced_name = replaced_name.replace(u"\u2013", "-")
                replaced_name = replaced_name.replace(";", "-")
                replaced_name = replaced_name.replace("~", "-")
                replaced_name = replaced_name.replace("#", "-")
                replaced_name = replaced_name.replace("*", "-")
                replaced_name = replaced_name.replace("&", "-")
                replaced_name = replaced_name.replace("$", "-")
                replaced_name = replaced_name.replace("@", "-")
                replaced_name = replaced_name.replace("=", "-")
                replaced_name = replaced_name.replace(":", "-")
                replaced_name = replaced_name.replace("+", "-")
                replaced_name = replaced_name.replace("?", "-")
                replaced_name = replaced_name.replace("]", "-")
                replaced_name = replaced_name.replace("[", "-")
                replaced_name = replaced_name.replace("{", "-")
                replaced_name = replaced_name.replace("}", "-")
                replaced_name = replaced_name.replace("%", "-")
                replaced_name = replaced_name.replace("`", "-")
                replaced_name = replaced_name.replace("^", "-")
                replaced_name = replaced_name.replace("<", "-")
                replaced_name = replaced_name.replace("\"", "-")
                replaced_name = replaced_name.replace(">", "-")
                replaced_name = replaced_name.replace("|", "-")
                replaced_name = replaced_name.replace("\\", "-")              
                
                print (filename, "->", replaced_name)
                os.rename(
                    dirpath + '/' + filename, dirpath + '/' + replaced_name)
    print ('\nAll files renamed!')

if __name__ == "__main__":
    rename()
