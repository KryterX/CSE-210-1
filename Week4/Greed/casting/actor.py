from shared.color import Color
from shared.point import Point


class Actor:

    def __init__(self):
        """Constructs a new Actor."""
        self._text = ""
        ### ADD POINTS
        self._points = 0
        ###
      
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
    
    ### ADD POINTS
    def get_points(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).
        """
        return self._points

    def set_points(self, points):
        """Updates the color to the given one.
        """
        self._points = points
    ###

    def get_color(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).
        """
        return self._color

    def get_font_size(self):
        """Gets the actor's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the actor's position.
        """
        return self._position
    
    ### Position bottom
    def get_position_bottom(self):
        x = self._position._x
        y = self._position._y + self._font_size
        return Point(x, y)
    ###
    
    def get_text(self):
        """Gets the actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        """
        return self._velocity
    
    def move_next(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def set_color(self, color):
        """Updates the color to the given one.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.
        """
        self._position = position
    
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the text to the given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        """
        self._velocity = velocity
