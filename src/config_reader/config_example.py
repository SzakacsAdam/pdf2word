config_example: str = """
#     _  _  __   __                
#    |_)| \|_     _)   | | _  __ _|
#    |  |_/|     /__   |^|(_) | (_|


[CONVERT]
# The path where pdf_watch and word_output folders
# will be created for the pdf conversion (Full path)
# if empty it will create it next to the .exe
convert.path = A:\PDF_TEST

garbage.remove = true
garbage.remove.time = 1


[BACKUP]
# enable backup, where pdf files will be backed up (True/False)
backup.save = false

# set the path of the backup, where the backup folder will be created (Full path)
# if empty it will create it next to the .exe 
backup.path =  A:\PDF_TEST

# enable backup files to be removed automatically
backup.pdf.remove = true

# set the age of the files in days after they will be removed 
backup.pdf.remove.time = 0.01

[LOG]
# enable logs to be saved. (True/False)
log.save = True

# set the path of the log, where the log folder will be created, (Full path)
# if empty it will create it next to the .exe
log.path = A:\PDF_TEST

# create daily logs, next to the full log. (True/False)
log.daily = True

"""
