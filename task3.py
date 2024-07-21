from typing import List
import matplotlib.pyplot as plt


def read_sales_data(file_path: str) -> List[dict]:
    """Get list of sales from .txt file"""
    sales = []
    keys = ['product_name', 'quantity', 'price', 'date']

    with open(file_path, 'r', encoding='utf8') as file:
        for line in file:
            values = line.strip().split(', ')
            sales.append(dict(zip(keys, values)))

    return sales


def total_sales_per_product(sales_data: List[dict]) -> dict:
    """Calculate total_sum sales per each product"""
    sum_per_item = {}

    for item in sales_data:
        cur_sum = int(item['quantity']) * int(item['price'])
        sum_per_item[item['product_name']] = sum_per_item.get(item['product_name'], 0) + cur_sum

    return sum_per_item


def sales_over_time(sales_data: List[dict]) -> dict:
    """Calculate total_sum sales per each date"""
    sum_per_date = {}

    for item in sales_data:
        cur_sum = int(item['quantity']) * int(item['price'])
        sum_per_date[item['date']] = sum_per_date.get(item['date'], 0) + cur_sum

    return sum_per_date


def plot_sales_per_items(sales: dict):
    fig = plt.figure(figsize=(8, 4))

    plt.title('Общая сумма продаж по каждому продукту (руб)')
    plt.bar(list(sales.keys()), list(sales.values()))
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()


def plot_sales_per_dates(sales: dict):
    #  сортируем по возрастанию даты, расщипляем список кортежей [(date, sum), ...] =>
    #  в 2 списка [date1, date2,...] и [sum1, sum2, ...] для построения графика
    dates, total_sum = list(zip(*sorted(sales.items(), key=lambda x: x[0])))

    fig = plt.figure(figsize=(8, 4))

    plt.title('Общая сумма продаж по дням (руб)')
    plt.plot(dates, total_sum)
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()


if __name__ == '__main__':
    # получаем список продаж
    sales_lst = read_sales_data('sales.txt')

    # получаем общую сумму продаж по каждому товару
    total_sales_per_item = total_sales_per_product(sales_lst)

    # получаем общую сумму продаж по каждой дате
    total_sales_per_date = sales_over_time(sales_lst)

    best_item = sorted(total_sales_per_item.items(), key=lambda x: x[1])[-1][0]
    best_date = sorted(total_sales_per_date.items(), key=lambda x: x[1])[-1][0]

    print(f'Продукт с максимальной выручкой: {best_item}')
    print(f'Дата с наибольшей суммой продаж: {best_date}')

    plot_sales_per_items(total_sales_per_item)
    plot_sales_per_dates(total_sales_per_date)
