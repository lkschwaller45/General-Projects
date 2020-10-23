import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set_style("ticks")



def main():
    '''
    df = pd.read_csv('biggestcap')
    df1 = pd.read_csv('2ndbiggestcap')
    df2 = pd.read_csv('datacorrect')
    graph_data(df)
    graph_data(df1)
    graph_data(df2)
    '''
    df3 = pd.read_csv('shorts')
    file_name1 = '2ndcap-input'
    file_name2 = '2ndcap-Capacitance'
    graph_data(df3,file_name1,file_name2)
    '''
    df4 = pd.read_csv('v2.1.5')
    file_name1 = '2V.1.5-input'
    file_name2 = '2V.1.5-Capacitance'
    graph_data(df4,file_name1,file_name2)

    df4 = pd.read_csv('v5')
    file_name1 = 'v5-input'
    file_name2 = 'v5-Capacitance'
    graph_data(df4,file_name1,file_name2)

    df4 = pd.read_csv('v5.1.5')
    file_name1 = '5V.1.5-input'
    file_name2 = '5V.1.5-Capacitance'
    graph_data(df4,file_name1,file_name2)
    
    df4 = pd.read_csv('v7')
    file_name1 = 'v7-input'
    file_name2 = 'v7-Capacitance'
    graph_data(df4,file_name1,file_name2)

    df4 = pd.read_csv('v7.1.5')
    file_name1 = '7V.1.5-input'
    file_name2 = '7V.1.5-Capacitance'
    graph_data(df4,file_name1,file_name2)

    df4 = pd.read_csv('v10')
    file_name1 = 'v10-input'
    file_name2 = 'v10-Capacitance'
    graph_data(df4,file_name1,file_name2)

    df4 = pd.read_csv('v10.1.5')
    file_name1 = '10V.1.5-input'
    file_name2 = '10V.1.5-Capacitance'
    graph_data(df4,file_name1,file_name2)
    '''

def graph_data(df,file_name1,file_name2):

    fig1 = sns.lineplot(x="Time", y="Voltage",  data=df,label='Input')
    fig1.set(xlabel='Time(ms)', ylabel='Voltage(Volts)')
    ax = plt.gca()
    ax.get_legend().remove()


    plt.savefig(file_name1+'.png')
    #plt.close()
    fig1 = sns.lineplot(x="Time", y="Voltage",  data=df,label='Capacitance',color='Red')
   # fig2.set(xlabel='Time(ms)', ylabel='Voltage(Volts)')
    ax = plt.gca()
    ax.get_legend()
    plt.savefig(file_name2+'.png')
    #plt.close()
    plt.show()


main()

