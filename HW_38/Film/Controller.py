class Controller:
    def __init__(self, model):
        self.model = model

    def get_data(self):
        data = self.model.get_data()
        all_data = (f'Фильм :: {data['title']}\n'
                    f'Жанр :: {data['genre']}\n'
                    f'Режиссёр :: {data['director']}\n'
                    f'Год выпуска :: {data['release']}\n'
                    f'Длительность :: {data['duration']}\n'
                    f'Студия :: {data['studio']}\n'
                    f'Актёры :: {data['actors']}\n')
        return all_data

    def get_ad_info(self):
        '''Возвращает рекламный текст'''
        ad_text = f'Кинокартина "{self.model.get_data()['title']}" в жанре {self.model.get_data()['genre']} от режиссера {self.model.get_data()['director']}!'
        return ad_text

    def change_data(self, type_of_data, data):
        return self.model.change_data(type_of_data, data)

    def add_actors(self, actor, role):
        return self.model.add_actors(actor, role)
