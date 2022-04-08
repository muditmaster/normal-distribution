import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go
import pandas as pd

yoyo = pd.read_csv("data.csv")

mean = sum(yoyo) / len(yoyo)
median = statistics.median(yoyo)
mode = statistics.mode(yoyo)
std_deviation = statistics.stdev(yoyo)
print("Mean : ", mean)
print("Median :", median)
print("Mode :", mode)
print("Standard deviation :", std_deviation)


first_std_deviation_start,first_std_deviation_end = mean - std_deviation, mean+std_deviation

second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean+(2*std_deviation)

third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean+(3*std_deviation)


fig = ff.create_distplot([yoyo], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))

fig.show()