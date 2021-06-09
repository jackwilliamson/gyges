import os

class File:
    def __init__(self, file_loc):
        filename, file_ext = os.path.splitext(file_loc)
        self.name = filename
        self.ext = file_ext

        self.date_created = ''
        self.date_last_modified = ''

