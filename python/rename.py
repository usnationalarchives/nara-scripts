# -*- coding: utf-8 -*-

import os
def renameFiles(folder='specialCharFix'):
    print 'Renaming files of ' + folder + ' and its subfolders...'
    for dirpath, _, filenames in os.walk(folder, topdown=True):
        print '\nRenaming files from', dirpath, '\n'
        if filenames:
            for filename in filenames:
                replaced_name = filename.replace(",", "-")
                replaced_name = replaced_name.replace("~", "-")
                replaced_name = replaced_name.replace(";", "-")
                replaced_name = replaced_name.replace("#", "-")
                replaced_name = replaced_name.replace("*", "-")
                replaced_name = replaced_name.replace("–", "-") #this is the long dash
                replaced_name = replaced_name.replace("ca.", "ca-")
                replaced_name = replaced_name.replace("[", "-")
                replaced_name = replaced_name.replace("]", "-")
                replaced_name = replaced_name.replace("(", "-")
                replaced_name = replaced_name.replace(")", "-")
                print filename, "->", replaced_name
                os.rename(
                    dirpath + '/' + filename, dirpath + '/' + replaced_name)
    print '\nAll files renamed!'

if __name__ == "__main__":
    renameFiles()

def rename(folder='specialCharFix'):
    print 'Renaming folders'
    for root, dirs, files in os.walk(folder):
        for directory in dirs:
            replaced_name = directory.replace("‚Äì", "-")
            replaced_name = replaced_name.replace("–","-")
            replaced_name = replaced_name.replace(",", "-")
            replaced_name = replaced_name.replace("~", "-")
            replaced_name = replaced_name.replace(";", "-")
            replaced_name = replaced_name.replace("#", "-")
            replaced_name = replaced_name.replace("*", "-")
            replaced_name = replaced_name.replace("ca.", "ca-")
            replaced_name = replaced_name.replace("[", "-")
            replaced_name = replaced_name.replace("]", "-")
            replaced_name = replaced_name.replace("(", "-")
            replaced_name = replaced_name.replace(")", "-")
            print(directory, "->"), replaced_name
            os.rename(
                root + '/' + directory, root + '/' + replaced_name)
    print 'All folders renamed!'
    

if __name__ == "__main__":
    rename()
