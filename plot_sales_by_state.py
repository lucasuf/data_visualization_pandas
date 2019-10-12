import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plot_heat_map import generate_sales_vs_state

if __name__ == '__main__':
    sns.set()
    width = 0.35

    csv_file = ".//data/Test_data.csv"
    data = pd.read_csv(csv_file)
    states, sales_by_state, not_sales_by_state = generate_sales_vs_state(data)

    # Plotting graph: "Volume de vendas por estado"
    plt.figure()
    plt.bar(states, list(sales_by_state.values()), width=0.35)
    plt.title('Gráfico: Volume de vendas por estado')
    plt.ylabel('Vendas (R$)')
    plt.xlabel('Estados')
    plt.show()
    # Plotting graph: "Volume de vendas/vendas perdidas por estado"
    plt.figure()
    menStd = [i * 0.03 for i in list(sales_by_state.values())]  # cosidering possible error rate
    p1 = plt.bar(states, list(sales_by_state.values()), width=0.35, yerr=menStd)
    p2 = plt.bar(states, list(not_sales_by_state.values()), width=0.35, yerr=menStd)
    plt.title('Gráfico: Volume de vendas e vendas perdidas por estado')
    plt.ylabel('Vendas (R$)')
    plt.xlabel('Estados')
    plt.legend((p1[0], p2[0]), ('Vendas', 'Vendas perdidas'))
    plt.show()

    mean_sales_by_state = sum(list(sales_by_state.values())) / len(list(sales_by_state.values()))
    print("Volume de vendas/vendas perdidas por estados")
    print("Media de vendas: " + str(mean_sales_by_state))
