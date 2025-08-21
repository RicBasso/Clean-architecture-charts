import matplotlib.pyplot as plt

original = ["Entities", "Use Cases", "Interface Adapters", "Frameworks & Drivers"]
mapped = ["Domain", "Application", "Presentation", "Infrastructure"]
colors = ["#FFD700", "#ADFF2F", "#87CEFA", "#FF6347"]

canvas, charts = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'aspect': 'equal'})

def create_chart(chart):
    chart.pie([1], radius = 1 )



create_chart(charts[0])
create_chart(charts[1])
plt.show()