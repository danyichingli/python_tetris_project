import constants as c

class Square:
    def __init__ (self, color, type):
        self.color = color
        self.type = type    # BLOCK, EMPTY, GHOST


    def get_color (self):
        return self.color

    def set_color (self, color):
        self.color = color

    def get_type (self):
        return self.type

    def set_type (self, type):
        self.type = type
