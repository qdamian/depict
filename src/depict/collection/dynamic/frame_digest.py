import os

class FrameDigest(object):

    def __init__(self, frame):
        self.frame = frame

    @property
    def function_name(self):
        return self.frame.f_code.co_name

    @property
    def module_name(self):
        return self.frame.f_globals['__name__']

    @property
    def file_name(self):
        return os.path.abspath(self.frame.f_code.co_filename)

    @property
    def line_number(self):
        return self.frame.f_lineno
