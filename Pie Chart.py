import matplotlib.pyplot as plt

    #create a list of values
valuesPie = [45, 24, 36, 10]
    

    #create pie chart from values
slice_labels = ['Q1', 'Q2', 'Q3', 'Q4']
titlePie = plt.title ('Sales Data')
colors = ['b', 'r', 'm', 'c']
def displayChart(title, label, values): 
    plt.pie(values, labels = slice_labels, colors = ['#008000', 'gold', 'indigo', 'black']) 
    #revised colors to green, gold, indigo, and black
    #https://matplotlib.org/stable/users/explain/colors/colors.html and https://proclusacademy.com/blog/customize_matplotlib_piechart/ 
    #display the pie chart
    plt.show()

displayChart(titlePie, slice_labels, valuesPie)  
