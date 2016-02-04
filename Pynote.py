import os
import fileinput, sys
import sys

from config import *

### date +%F #F N en ev. T

def rm_note(notes_folder, nr):
    os.system("if [ $(ls -l "+notes_folder+" | grep 'Nr"+nr+"---' | wc -l) = 1 ]; then mv -v "+notes_folder+"/$(ls "+notes_folder+" | grep 'Nr" +nr+"---') "+notes_folder+"/.archive; else echo 'Too much matching files'&& ls -l "+notes_folder+" | grep 'Nr"+nr+"---' ; fi")
    
def edit_note(notes_folder, nr):
    os.system("nano "+notes_folder+"/$(ls "+notes_folder+"|grep '^Nr"+nr+"---')")

def list_notes(notes_folder):
    os.system("clear")
    
    os.system("cd " + notes_folder +" && tail -n +1 $(ls -lt " + notes_folder+ " | awk '{print $9}') | less")
    print("")
    #Insert a cleanup here -> all files not matching nr datum etc etc

def add_note(notes_folder, name):
    os.system("nano "+ notes_folder+ "/Nr$(($(ls -l "+notes_folder+"| awk '{print $9}'|grep '^Nr[0-9]*---'|cut -c 3- | cut -f1 -d'-' |sort -g | tail -1)+1))---$(date +%F)_$(date +%T)" + name)
    
def search_note(notes_folder, searchterm):
    os.system("cd "+notes_folder+" && grep '"+searchterm+"' $(ls -l | awk '{print $9}')")
len_sysargv = len(sys.argv)
if len_sysargv == 1:
    #list command
    list_notes(notes_folder)
    #print today as in day format
    
elif sys.argv[1] == "ls":
    if len_sysargv == 2:
        list_notes(notes_folder)
    else:
        print("too much arguments")

elif sys.argv[1] == "a":
    name = ""
    if len_sysargv == 3:
        name = "_"+sys.argv[2]
    elif len_sysargv > 3:
        print ('No spaces allowed in name, resetting to blank...')
    add_note(notes_folder, name)
elif sys.argv[1] =="rm":
    if len_sysargv == 3:
        nr = sys.argv[2]
        rm_note(notes_folder, nr)
    else:
        print("incorrect number of arguments")
elif sys.argv[1] =="e":
    if len_sysargv == 3:
        nr = sys.argv[2]
        edit_note(notes_folder, nr)
        
elif sys.argv[1] =="search":
    if len_sysargv > 2:
        searchterm = sys.argv[2]
        arg_search=3
        while arg_search < len_sysargv:
            searchterm = searchterm + " " + sys.argv[arg_search]
            arg_search = arg_search+1
        search_note(notes_folder, searchterm)
    else:
        print ("define searchterm!'")
