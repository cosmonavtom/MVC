from Model import Film
from Controller import Controller
from View import View

film = Film('День сурка', 'фантастика', 'Гарольд Рамис', '1993', '101 минута', 'Columbia Pictures',
            {'Билл Мюррей': 'Фил Коннорс', 'Энди Макдауэлл': 'Рита Хансон'})
controller = Controller(film)
view = View(controller)

# Тестируем. Смотрим рекламное объявление вначале
view.print_ad_info()
# Смотрим полную информацию
view.print_data()
# Добавляем ещё одного актёра. Причём дважды
view.add_actors('Крис Эллиотт', 'Ларри, оператор')
view.add_actors('Крис Эллиотт', 'Ларри, оператор')
# Изменяем жанр фильма
view.change_data('genre', 'фантастика, комедия')
# Смотрим изменения
view.print_data()



