class Article:
    '''Это задание делал на уроке "у доски". Добавил метод изменения названия статьи'''

    def __init__(self, title, author, signs, publication, description):
        self.__title = title
        self.__author = author
        self.__signs = signs
        self.__publication = publication
        self.__description = description

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_signs(self):
        return self.__signs

    def get_article_data(self):
        article_data = {
            'title': self.__title,
            'author': self.__author,
            'signs': self.__signs,
            'publication': self.__publication,
            'description': self.__description
        }
        return article_data

    def change_title(self, new_title):
        self.__title = new_title


