import pandas as pd
import statistics as st
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

data = pd.read_csv('medium.csv')['reading_time'].to_list()

population_mean = st.mean(data)

def sample():
    sample_list = []
    for a in range(0,29):
        sample_list.append(data[random.randint(0,len(data)-1)])

    return st.mean(sample_list)

def setup():
    mean_list = []
    for a in range(0,99):
        mean_list.append(sample())

    return mean_list

mean_list = setup()

samples = pd.read_csv('sample1.csv')['reading_time'].to_list()

z_score = (st.mean(samples)-st.mean(mean_list))/st.stdev(mean_list)

print(z_score)
