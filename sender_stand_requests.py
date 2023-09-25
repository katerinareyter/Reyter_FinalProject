import configuration
import requests

# Запрос на создание заказа
def create_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

# Запрос на получение данных о заказе по треку заказа
def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_INFO + str(track))