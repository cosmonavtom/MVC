class Recipe:
    '''Большинство полей класса являются списками. Потому что блюдо может иметь несколько
    названий, авторов и т.д. Для разных экземпляров может потребоваться несколько значений
    для разных полей, поэтому решил сразу списки делать. На примере в main это будет показано'''

    def __init__(self, name, cook, type_of_dish, description, ingredients, homeland, link):
        self.recipe_data = {
            'name': name,
            'cook': cook,
            'type_of_dish': type_of_dish,
            'description': description,
            'ingredients': ingredients,
            'homeland': homeland,
            'link': link
        }

    def get_data(self):
        '''Возвращаем все данные о рецепте'''
        return self.recipe_data

    def change_description(self, new_description):
        '''Изменяем описание блюда. Это можно было сделать и с помощью remove_data
        и add_ data, но решил один метод сделать таким ради разнообразия. Предполагается,
         что описание будет меняться чаще всего'''
        self.recipe_data['description'] = [new_description]
        return None

    def add_data(self, key, data):
        '''Добавляем значение в список параметров экземпляра. Принимаем параметр
        и его значение. Возвращаем ошибку если такого параметра нет'''
        if key in self.recipe_data:
            self.recipe_data[key].append(data)
            return None
        return 'Key error!'

    def remove_data(self, key, data):
        '''Так как у нас списки в значениях, то может потребоваться убрать один
        элемент из списка по значению. Функция принимает параметр и значение элемента
        из списка'''
        if key in self.recipe_data and data in self.recipe_data[key]:
            self.recipe_data[key].remove(data)
            return None
        return 'Key or value error!'

    def clear_data(self, key):
        '''Очищаем список целиком. Ускоряет процесс, когда надо поменять много элементов
        в списке. Например, убрать все ингредиенты'''
        if key in self.recipe_data:
            self.recipe_data[key].clear()
            return None
        return 'Key error!'

