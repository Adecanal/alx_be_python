class Book:
    """A class representing a book with magic methods."""
    
    def __init__(self, title, author, year):
        """Initialize book attributes."""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Print message when book is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official string representation to recreate object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
