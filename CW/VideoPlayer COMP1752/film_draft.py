class Film:
    def __init__(self, id, name, director, rating, play_count):
        if not isinstance(id,int) or id < 0:
            raise ValueError('Id must me a number and not negative')
        if name == '':
            raise ValueError('Name cannot be empty')
        if director == '':
            raise ValueError('Director cannot be empty')
        if not isinstance(rating, float) or rating <= 0:
            raise ValueError('Rating cannot be negative')
        self._id = id
        self._name = name
        self._director = director
        self._rating = rating
        self._play_count = play_count

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self._name = value

    @property
    def director(self):
        return self._director
    
    @director.setter
    def director(self, value):
        if value == '':
            raise ValueError('Director cannot be empty')
        self._director = value

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        if not (isinstance(value, float) or isinstance(value, int)) or value <= 0:
            raise ValueError('Rating cannot be negative')
        self._rating = value

    @property
    def play_count(self):
        return self._play_count
    
   
    
   

    
    

    
        
    