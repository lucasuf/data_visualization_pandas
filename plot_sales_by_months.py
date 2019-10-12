import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_sales_vs_month(pd_data_object):
    """
    This function receives a dataframe object and returns all values for each year,
    separating in not_sales and sales
    :param pd_data_object:
    :return:
    values_by_months_sales_2017, values_by_months_sales_2018, values_by_months_sales_2019, \
    values_by_months_not_sales_2017, values_by_months_not_sales_2018, values_by_months_not_sales_2019
    """
    values_by_months = pd_data_object.groupby(['Month', 'Year', 'Lost_Deal'], as_index=False)['Value'].sum()

    # Cleaning and organizing data: Replacing month names by values
    values_by_months['Month'].replace(['January', 'February', 'March', 'April', 'May', 'June',
                                       'July', 'August', 'September', 'October', 'November', 'December'],
                                      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], inplace=True)
    # Sorting by year and month
    values_by_months = values_by_months.sort_values(['Year', 'Month'], ascending=[1, 1])  # Sorting by year

    values_by_months_sales = values_by_months[values_by_months['Lost_Deal'] == False]
    values_by_months_not_sales = values_by_months[values_by_months['Lost_Deal'] == True]

    # One dataframe for each year: Sales
    values_by_months_sales_2017 = values_by_months_sales[values_by_months_sales['Year'] == 2017]
    values_by_months_sales_2018 = values_by_months_sales[values_by_months_sales['Year'] == 2018]
    values_by_months_sales_2019 = values_by_months_sales[values_by_months_sales['Year'] == 2019]

    # One dataframe for each year: Not Sales
    values_by_months_not_sales_2017 = values_by_months_not_sales[values_by_months_not_sales['Year'] == 2017]
    values_by_months_not_sales_2018 = values_by_months_not_sales[values_by_months_not_sales['Year'] == 2018]
    values_by_months_not_sales_2019 = values_by_months_not_sales[values_by_months_not_sales['Year'] == 2019]

    return values_by_months_sales_2017, values_by_months_sales_2018, values_by_months_sales_2019, \
           values_by_months_not_sales_2017, values_by_months_not_sales_2018, values_by_months_not_sales_2019


if __name__ == '__main__':
    sns.set()

    csv_file = ".//data/Test_data.csv"
    data = pd.read_csv(csv_file)

    # Plotting graph: "Meses por volume de vendas por ano"
    values_by_months_sales_2017, values_by_months_sales_2018, values_by_months_sales_2019, \
    values_by_months_not_sales_2017, values_by_months_not_sales_2018, values_by_months_not_sales_2019 = \
        generate_sales_vs_month(data)
    # Plotting results: Sales
    ax1 = plt.subplot(231)
    ax1.plot(values_by_months_sales_2017['Month'], values_by_months_sales_2017['Value'], color='orange')
    ax1.set_ylabel('Vendas (R$)', fontsize=9)
    ax1.set_xlabel('Meses', fontsize=9)
    ax1.set_title('Grafico: Vendas 2017')

    ax2 = plt.subplot(232)
    ax2.plot(values_by_months_sales_2018['Month'], values_by_months_sales_2018['Value'])
    ax2.set_ylabel('Vendas (R$)', fontsize=9)
    ax2.set_xlabel('Meses', fontsize=9)
    ax2.set_title('Gráfico: Vendas 2018')

    ax3 = plt.subplot(233)
    ax3.plot(values_by_months_sales_2019['Month'], values_by_months_sales_2019['Value'], color='green')
    ax3.set_ylabel('Vendas (R$)', fontsize=9)
    ax3.set_xlabel('Meses', fontsize=9)
    ax3.set_title('Gráfico: Vendas 2019')

    ax4 = plt.subplot(212)
    ax4.plot(values_by_months_sales_2017['Month'][:6], values_by_months_sales_2017['Value'][:6], color='orange',
             label='2017')
    ax4.plot(values_by_months_sales_2018['Month'][:6], values_by_months_sales_2018['Value'][:6], label='2018')
    ax4.plot(values_by_months_sales_2019['Month'], values_by_months_sales_2019['Value'], color='green', label='2019')
    ax4.set_ylabel('Vendas (R$)', fontsize=10)
    ax4.set_xlabel('Meses', fontsize=10)
    ax4.set_title('Gráfico: Vendas para os primeiros semestres de 2019, 2018 e 2017')
    plt.show()
    # Plotting results : Not Sales
    ax1 = plt.subplot(231)
    ax1.plot(values_by_months_not_sales_2017['Month'], values_by_months_not_sales_2017['Value'], color='orange')
    ax1.set_ylabel('Vendas perdidas(R$)', fontsize=9)
    ax1.set_xlabel('Meses', fontsize=9)
    ax1.set_title('Grafico: Vendas perdidas 2017')

    ax2 = plt.subplot(232)
    ax2.plot(values_by_months_not_sales_2018['Month'], values_by_months_not_sales_2018['Value'])
    ax2.set_ylabel('Vendas perdidas(R$)', fontsize=9)
    ax2.set_xlabel('Meses', fontsize=9)
    ax2.set_title('Gráfico: Vendas perdidas 2018')

    ax3 = plt.subplot(233)
    ax3.plot(values_by_months_not_sales_2019['Month'], values_by_months_not_sales_2019['Value'], color='green')
    ax3.set_ylabel('Vendas perdidas(R$)', fontsize=9)
    ax3.set_xlabel('Meses', fontsize=9)
    ax3.set_title('Gráfico: Vendas perdidas 2019')

    ax4 = plt.subplot(212)
    ax4.plot(values_by_months_not_sales_2017['Month'][:6], values_by_months_not_sales_2017['Value'][:6], color='orange',
             label='2017')
    ax4.plot(values_by_months_not_sales_2018['Month'][:6], values_by_months_not_sales_2018['Value'][:6], label='2018')
    ax4.plot(values_by_months_not_sales_2019['Month'], values_by_months_not_sales_2019['Value'], color='green',
             label='2019')
    ax4.legend(loc="upper right")
    ax4.set_ylabel('Vendas perdidas(R$)', fontsize=10)
    ax4.set_xlabel('Meses', fontsize=10)
    ax4.set_title('Gráfico: Vendas perdidas para os primeiros semestres de 2019, 2018 e 2017')
    plt.show()
