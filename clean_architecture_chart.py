import matplotlib.pyplot as plt

original = ["Entities", "Use Cases", "Interface Adapters", "Frameworks & Drivers"]
mapped = ["Domain", "Application", "Presentation", "Infrastructure"]
colors = ["#FFD700", "#ADFF2F", "#87CEFA", "#FF6347"]
titles = ["Clean Architecture (Uncle Bob)", "Mappatura pratica (Flutter / .NET / ecc.)"]

canvas, charts = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'aspect': 'equal'})

size = 0.25

def create_chart(chart, labels, title):
    count = 0
    for label in reversed(labels):
        radius = 1 - count * size
        chart.pie([1], radius = radius, colors=[colors[len(labels)-1-count]],wedgeprops=dict(width=size, edgecolor='w'))
        count = count + 1
        text_position = radius - size/2 - 0.05
        if count == 4 :
            text_position = 0
        chart.text(0, text_position, label, ha='center', va='center',
                fontsize=9, weight='bold')
    chart.set_title(title, fontsize=12, pad=10)
    



create_chart(charts[0], original, titles[0])
create_chart(charts[1], mapped, titles[1])
plt.show()