import pandas as pd
import matplotlib.pyplot as plt
import collections
import seaborn as sns

def generate_sales_vs_sales_executive(pd_data_object):
    """
    This function is responsible for returning an
    object that represents sales per state of Brazil
    :param pd_data_object:
    DataFrame containing values fromcsv file
    :return:
    sorted_sales_by_sales_executive: amount of sales for each executive ordered
    sorted_not_sales_by_sales_executive: amount of lost sales for each executive
    """
    # Getting only those that did not lost the deal
    sales_made = [data for data in pd_data_object.values if data[6] is False]

    # Getting only those that did lose the deal
    sales_not_made = [data for data in pd_data_object.values if data[6] is True]

    # Listing all the states
    sales_executive = set(pd_data_object['Sales_Executive'].values)

    # Calculating value accomplished for sales executive
    sales_by_sales_executive = dict((el, 0) for el in sales_executive)
    for sales in sales_made[:]:
        sales_by_sales_executive[sales[3]] = sales_by_sales_executive[sales[3]] + sales[5]

    # Calculating value lost for each sales executive
    not_sales_by_sales_executive = dict((el, 0) for el in sales_executive)
    for not_sales in sales_not_made[:]:
        not_sales_by_sales_executive[not_sales[3]] = not_sales_by_sales_executive[not_sales[3]] + not_sales[5]

    # Ordering our results
    sorted_sales_by_sales_executive = sorted(sales_by_sales_executive.items(), key=lambda kv: kv[1])
    sorted_not_sales_by_sales_executive = sorted(not_sales_by_sales_executive.items(), key=lambda kv: kv[1])

    return collections.OrderedDict(sorted_sales_by_sales_executive), \
           collections.OrderedDict(sorted_not_sales_by_sales_executive)

if __name__ == '__main__':
    sns.set()

    csv_file = ".//data/Test_data.csv"
    data = pd.read_csv(csv_file)

    # Plotting graph: "Volume de vendas/vendas perdidas por vendedor"
    sales_by_sales_executive, not_sales_by_sales_executive = generate_sales_vs_sales_executive(data)
    my_range = range(1, len(sales_by_sales_executive)+1)
    fig, ax = plt.subplots()
    xmin = []
    for index in sales_by_sales_executive.keys():
        xmin.append(not_sales_by_sales_executive[index])

    plt.hlines(y=sales_by_sales_executive.keys(), xmin=xmin, xmax=sales_by_sales_executive.values(), colors='grey')
    ax.scatter(list(sales_by_sales_executive.values()), sales_by_sales_executive.keys(), color='green',
               label='Vendas', alpha=0.3, edgecolors='none')
    ax.scatter(list(not_sales_by_sales_executive.values()), not_sales_by_sales_executive.keys(), color='red',
               label='Vendas perdidas', alpha=0.3, edgecolors='none')

    ax.legend()
    plt.title('Gráfico: Volume de vendas e vendas perdidas por empregado')
    plt.xlabel('Vendas (R$)')
    plt.ylabel('Empregados')
    plt.show()