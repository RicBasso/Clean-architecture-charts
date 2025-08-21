import matplotlib.pyplot as plt

original = ["Entities", "Use Cases", "Interface Adapters", "Frameworks & Drivers"]
mapped = ["Domain", "Application", "Presentation", "Infrastructure"]
colors = ["#FFD700", "#ADFF2F", "#87CEFA", "#FF6347"]

canvas, charts = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'aspect': 'equal'})

size = 0.25

def create_chart(chart, labels):
    count = 0
    for label in reversed(labels):
        chart.pie([1], radius = 1 - count * size, colors=[colors[len(labels)-1-count]],wedgeprops=dict(width=size, edgecolor='w'))
        count = count + 1
     
    



create_chart(charts[0], original)
create_chart(charts[1], mapped)
plt.show()