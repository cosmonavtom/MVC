class Controller:
    def __init__(self, model):
        self.model = model

    def get_base_data(self):
        data = self.model.get_data()
        base_data = f'Блюдо {' '.join(data['name'])} от {data['cook']}!!! Родина: {data['homeland']}'
        return base_data

    def get_data(self):
        all_data = self.model.get_data()
        return all_data

    def change_description(self, new_description):
        self.model.change_description(new_description)
        return None

    def add_data(self, key, data):
        if self.model.add_data(key, data) == 'Key error!':
            return 'Key error!'
        # else:
        #     self.model.add_data(key, data)

    def remove_data(self, key, data):
        if self.model.remove_data(key, data) == 'Key or value error!':
            return 'Key or value error!'
        self.model.remove_data(key, data)
        return None

    def clear_data(self, key):
        if self.model.clear_data(key) == 'Key error!':
            return 'Key error!'





