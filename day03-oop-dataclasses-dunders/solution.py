class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height
