#! /usr/bin/env bash                     
#tells os to run script using bash shell

script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)

pyuic4 "$project_dir/ui/mainwindow.ui" -o "$project_dir/ui/mainwindow.py"

# After running this script, you’ll get a mainwindow.py file that contains Python classes corresponding to the GUI you designed in Qt Designer.
