import csv
from pg_utils.utils import pg_connection, pg_close_connection, pg_insert


def data_from_csv(csv_path, encoding='windows-1251'):
    """Создает список из данных CSV"""
    try:
        csv_list = []

        with open(csv_path, 'r', encoding=encoding) as file:
            csv_file = csv.DictReader(file)
            # записываем данные из файла
            for line in csv_file:
                csv_list.append(line)

        return csv_list

    except FileNotFoundError:
        raise FileNotFoundError(f'Отсутствует файл {csv_path}')


if __name__ == '__main__':
    #Подключаемся к БД
    connection = pg_connection()

    #Создаем списки с данным для инсерта в таблицы
    customers_data = data_from_csv('north_data/customers_data.csv')
    employees_data = data_from_csv('north_data/employees_data.csv')
    orders_data = data_from_csv('north_data/orders_data.csv')

    # Инсертим данные в customers_data
    for i in customers_data:
        pg_insert(connection=connection, table_name='customers_data',\
                  customer_id=i['customer_id'],
                  company_name=i['company_name'],
                  contact_name=i['contact_name']
                  )

    #Инсертим данные в employees_data
    for i in employees_data:
        pg_insert(connection=connection, table_name='employees_data',\
                  first_name=i['first_name'],
                  last_name=i['last_name'],
                  title=i['title'],
                  birth_date=i['birth_date'],
                  notes=i['notes'],
                  )

    #Инсертим данные в orders_data
    for i in orders_data:
        pg_insert(connection=connection, table_name='orders_data',\
                  order_id=i['order_id'],
                  customer_id=i['customer_id'],
                  employee_id=i['employee_id'],
                  order_date=i['order_date'],
                  ship_city=i['ship_city'],
                  )

    pg_close_connection(connection)
