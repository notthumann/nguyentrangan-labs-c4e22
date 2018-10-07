from matplotlib import pyplot
machine_counts = [18, 4 , 2]
machine_names = ['PC','Linux', 'MAC']
pyplot.pie(machine_counts, labels = machine_names, autopct='%.1f%%', shadow = True, explode=[0, 0.1, 0])
pyplot.axis('equal')
pyplot.title('PC vs MAC vs Linux Usage')
pyplot.show()