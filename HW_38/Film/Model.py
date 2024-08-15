class Film():
    '''В общем мне шаблон MVC понравился. Нормально его заботали. Уже даже какой-то день Сурка появился
    по последним заданиям. В хорошем смысле, конечно'''
    def __init__(self, title, genre, director, release, duration, studio, actors: dict):
        self.film_data = {
            'title': title,
            'genre': genre,
            'director': director,
            'release': release,
            'duration': duration,
            'studio': studio,
            'actors': actors
        }

    def get_data(self):
        return self.film_data

    def change_data(self, type_of_data, data):
        '''Изменяем выбранное поле'''
        if type_of_data in self.film_data.keys():
            self.film_data[type_of_data] = data
            return None
        else:
            return 'Type error!'

    def add_actors(self, actor, role):
        '''Добавляем актёра'''
        if actor in self.film_data['actors']:
            return 'This actor already exists'
        self.film_data['actors'][actor] = role
