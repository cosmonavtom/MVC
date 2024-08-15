class ArtController:
    def __init__(self, model):
        self.__model = model

    def get_default(self):
        return self.__model.get_article_data()

    def get_title(self):
        return self.__model.get_title()

    def get_author(self):
        return self.__model.get_author()

    def get_title_and_author(self):
        return self.__model.get_title(), self.__model.get_author()

    def change_title(self, new_title):
        return self.__model.change_title(new_title)