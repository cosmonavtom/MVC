from Model import Recipe
from Controller import Controller
from View import View

name = ['Борщ']
cook = ['Народ']
type_of_dish = ['Первое']
description = ['Краткое описание, подробнее в ссылке']
ingredients = ['вода', 'свекла', 'мясо говядина', 'картофель', 'морковь']
homeland = ['Россия', 'Беларусь', 'Украина']
link = 'https://lifehacker.ru/classic-borshcht/'

recipe = Recipe(name, cook, type_of_dish, description, ingredients, homeland, link)
controller = Controller(recipe)
view = View(controller)


# ТЕСТ
# Смотрим краткое описание
view.print_base_data()
# Смотрим полное описание
view.print_all_data()
# Добавляем английское написание борща. Уж больно красивое написание
view.add_data('name', 'borscht')
# Удаляем из ингредиентов "воду".
view.remove_data('ingredients', 'water')
# Ошибка! Неправильное написание. Вторая попытка
view.remove_data('ingredients', 'вода')
# Смотрим на изменения
view.print_all_data()
# Полностью очищаем список стран
view.clear_data('homeland')
# Меняем описание
view.print_change_description('Новое описание')
# Смотрим на изменения
view.print_all_data()


