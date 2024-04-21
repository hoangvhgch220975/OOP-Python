from film_draft import Film
from library_item import LibraryItem as item
import csv

class VideoLibrary:
    def __init__(self):
        self._films = self.load_films('films.csv')

    def load_films(self, file_name):
        films = []
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            # skip header
            next(reader)
            # scan each raw
            for row in reader:
                id = int(row[0])
                name = row[1]
                director = row[2]
                rating = float(row[3])
                f = Film(id, name, director, rating,play_count=0)
                films.append(f)

        return films
    
    def get_name(self):
        return (f.name for f in self._films)
    
    def get_film(self, index):
        # return self._films[index] => not safe, expose films info outside
        f = self._films[index] 
        # safe because we return a copy of film's info
        return f.id, f.name, f.director, f.rating
    
    
    
        