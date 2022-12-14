config_example: str = """
#     _  _  __   __                
#    |_)| \|_     _)   | | _  __ _|
#    |  |_/|     /__   |^|(_) | (_|



[CONVERT]
convert.path =

backup.remove = true
backup.remove.time = 1

junk_files.remove = true
junk_files.remove.time = 1

output.remove = true
output.remove.time = 1

error.remove = true
error.remove.time = 1


[API]
post = 53814

[LOG]
# enable logs to be saved. (True/False)
log.save = True

# set the path of the log, where the log folder will be created, (Full path)
# if empty it will create it next to the .exe
log.path =

# create daily logs, next to the full log. (True/False)
log.daily = True

"""
