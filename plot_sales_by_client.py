import pandas as pd
import matplotlib.pyplot as plt
import collections
import seaborn as sns


def generate_sales_vs_client(pd_data_object):
    """
    This function is responsible for returning an
    object that represents sales per state of Brazil
    :param pd_data_object:
    DataFrame containing values fromcsv file
    :return:
    sales_by_clients: amount of sales for each client
    not_sales_by_clients: amount of lost sales for each client
    """
    # Getting only those that did not lost the deal
    sales_made = [data for data in pd_data_object.values if data[6] is False]

    # Getting only those that did lose the deal
    sales_not_made = [data for data in pd_data_object.values if data[6] is True]

    # Listing all the states
    clients = set(pd_data_object['Client'].values)

    # Calculating value accomplished for state
    sales_by_clients = dict((el, 0) for el in clients)
    for sales in sales_made[:]:
        sales_by_clients[sales[4]] = sales_by_clients[sales[4]] + sales[5]

    # Calculating value lost for each state
    not_sales_by_clients = dict((el, 0) for el in clients)
    for not_sales in sales_not_made[:]:
        not_sales_by_clients[not_sales[4]] = not_sales_by_clients[not_sales[4]] + not_sales[5]

    # Ordering our results
    sorted_sales_by_clients = sorted(sales_by_clients.items(), key=lambda kv: kv[1])
    sorted_not_sales_by_clients = sorted(not_sales_by_clients.items(), key=lambda kv: kv[1])

    return collections.OrderedDict(sorted_sales_by_clients), \
           collections.OrderedDict(sorted_not_sales_by_clients)


if __name__ == '__main__':
    sns.set()

    csv_file = ".//data/Test_data.csv"
    data = pd.read_csv(csv_file)

    # Plotting graph: "Volume de vendas para cada cliente"
    sales_by_clients, not_sales_by_clients = generate_sales_vs_client(data)
    fig, ax = plt.subplots()
    plt.bar(sales_by_clients.keys(), list(sales_by_clients.values()), width=0.6)
    mean_sales_by_client = sum(list(sales_by_clients.values())) / len(list(sales_by_clients.values()))
    ax.axhline(mean_sales_by_client, color='green', linewidth=1)
    plt.title('Gráfico: Volume de vendas para cada cliente')
    plt.ylabel('Vendas (R$)')
    plt.xlabel('Clientes')
    plt.xticks(rotation=90, fontsize=6.5)
    # Plotting graph: "Volume de vendas/vendas perdidas por cliente"
    fig, ax = plt.subplots()
    p1 = plt.bar(sales_by_clients.keys(), list(sales_by_clients.values()), width=0.6)
    p2 = plt.bar(not_sales_by_clients.keys(), list(not_sales_by_clients.values()), width=0.6)
    mean_not_sales_by_client = sum(list(not_sales_by_clients.values())) / len(list(sales_by_clients.values()))
    ax.axhline(mean_sales_by_client, color='green', linewidth=1)
    ax.axhline(mean_not_sales_by_client, color='green', linewidth=1)
    plt.title('Gráfico: Volume de vendas e vendas perdidas por cliente')
    plt.ylabel('Vendas (R$)')
    plt.xlabel('Clientes')
    plt.legend((p1[0], p2[0]), ('Vendas', 'Vendas perdidas'))
    plt.xticks(rotation=90, fontsize=6.5)
    print("Volume de vendas/vendas perdidas por cliente")
    print("Media de vendas: " + str(mean_sales_by_client))
    print("Media de vendas perdidas: " + str(mean_not_sales_by_client))
    plt.show()
