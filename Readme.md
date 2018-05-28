# Taskfile-scheduler
A simple python script that parses a taskfile and creates a apple script dialog.  
The are currently three features to be used. The script will check @today tasks in the evening and assemble all the tasks that are not @done.  
In the morning of a new day it checks the file for any @tomorrow tags, alters them to @today and presents them.  

