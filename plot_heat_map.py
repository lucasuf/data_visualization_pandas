import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import seaborn as sns

def generate_sales_vs_state(pd_data_object):
    """
    This function is responsible for returning an
    object that represents sales per state of Brazil
    :param pd_data_object:
    DataFrame containing values fromcsv file
    :return:
    states: list with states on data
    sales_by_state: amount of sales for each state
    not_sales_by_state: amount of lost sales for each state
    """
    # Getting only those that did not lost the deal
    sales_made = [data for data in pd_data_object.values if data[6] is False]

    # Getting only those that did lose the deal
    sales_not_made = [data for data in pd_data_object.values if data[6] is True]

    # Listing all the states
    states = set(pd_data_object['State'].values)

    # Calculating value accomplished for state
    sales_by_state = dict((el, 0) for el in states)
    for sales in sales_made[:]:
        sales_by_state[sales[0]] = sales_by_state[sales[0]] + sales[5]

    # Calculating value lost for each state
    not_sales_by_state = dict((el, 0) for el in states)
    for not_sales in sales_not_made[:]:
        not_sales_by_state[not_sales[0]] = not_sales_by_state[not_sales[0]] + not_sales[5]

    return list(states), sales_by_state, not_sales_by_state


if __name__ == '__main__':
    sns.set()

    csv_file = ".//data/Test_data.csv"
    fp = './/data//Brasil//UFEBRASIL.shp'
    data = pd.read_csv(csv_file)
    map_df = gpd.read_file(fp)

    states, sales_by_state, not_sales_by_state = generate_sales_vs_state(data)

    # Ploting graph: "Mapa de calor do Brasil"
    df = pd.DataFrame([['SANTA CATARINA', sales_by_state['SC']],
                       ['SÃO PAULO', sales_by_state['SP']],
                       ['RIO DE JANEIRO', sales_by_state['RJ']],
                       ['PERNAMBUCO', sales_by_state['PE']],
                       ['RONDÔNIA', 0],
                       ['ACRE', 0],
                       ['AMAZONAS', 0],
                       ['RORAIMA', 0],
                       ['PARÁ', 0],
                       ['AMAPÁ', 0],
                       ['TOCANTINS', 0],
                       ['MARANHÃO', 0],
                       ['PIAUÍ', 0],
                       ['CEARÁ', 0],
                       ['RIO GRANDE DO NORTE', 0],
                       ['PARAÍBA', 0],
                       ['ALAGOAS', 0],
                       ['SERGIPE', 0],
                       ['BAHIA', 0],
                       ['MINAS GERAIS', 0],
                       ['ESPIRITO SANTO', 0],
                       ['PARANÁ', 0],
                       ['RIO GRANDE DO SUL', 0],
                       ['MATO GROSSO DO SUL', 0],
                       ['MATO GROSSO', 0],
                       ['GOIÁS', 0],
                       ['DISTRITO FEDERAL', 0]], columns=['State', 'Value'])
    merged = map_df.set_index('NM_ESTADO').join(df.set_index('State'))
    variable = 'Value'
    # create figure and axes for Matplotlib
    fig, ax = plt.subplots(1, figsize=(10, 6))
    ax.axis('off')
    ax.set_title('Grafico: Mapa de calor para o volume de vendas no Brasil')
    merged.plot(column=variable, cmap='BuGn', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    plt.show()