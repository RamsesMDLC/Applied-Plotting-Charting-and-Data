# -*- coding: utf-8 -*-
"""
Created on Tue May 24 21:34:45 2022
a
@author: USUARIO
"""

#MATPLOLIB ARCHITECTURE (Topic 1)

#Matplotlib Definitions and Concepts (Topic 1.1)

#Matplotlib is:
    #A Python-based plotting library with full support for 2D and limited..
    #...support for 3D graphics.
    #Provides a stateful "Scripting Layer" for quick and...
    #...easy generation of graphics similar to MATLAB's. (this tool is based..
    #...in MATLAB).
    #It is called “plt” because most Python programmers like to import...
    #..."Matplotlib" and make an alias called “plt” (it is just like "np"...
    #...for "Numpy" or "pd" for "Pandas")
    
import matplotlib.pyplot as plt

#"IPython" allow us to deploy all the functionalities of Matplotlib in...
#...Jupyter (i.e., with Jupyter we are working in a "web environment" with...
#...Matplotlib). Despite the fact that this is the approach of the course....
#...we can use Matplotlib outside the "web environment" (like Spyder...
#...environment).

#Matplotlib Architecture (Topic 1.2)

#The architecture of Matplotlib is separated into three layers, which can...
#...be viewed as a stack. Each layer that sits above another layer knows..
#...how to talk to the layer below it, but the lower layer is not aware of...
#...the layers above it. The three layers from bottom to top are: 
    #1.Backend Layer
    #2.Artist Layer
    #3.Scripting Layer

#1. The first layer is the "Backend" (Topic 1.2.1):
    #At the bottom of the stack is the backend layer, which provides concrete...
    #...implementations of the abstract interface classes:
        #FigureCanvas: encapsulates the concept of a surface to draw onto...
        #....(e.g. "the paper").
        #Renderer: does the drawing (e.g. "the paintbrush").
        #Event: handles user inputs such as keyboard and mouse events.
        
    #Matplotlib is renderized into the browser thanks to a "backend"..
    #...(which is layer that allow the code interact with the...
    #...operative system or in this case the browser).    

    #There are several types of "backends" (we need to call one of this...
    #...in Jupyter).
    
#2. The second layer is the "Artist Layer" (Topic 1.2.2):
    #The "Artist" is the middle layer of the matplotlib stack, and...
    #...is the place where much of the heavy lifting happens. 
    
    #The "Artist" is the object that knows how to take the "Renderer"..
    #...(the paintbrush) and put ink on the "FigureCanvas" (e.g. "the paper").

    #There are two types of "Artists" in the hierarchy. These are:
        #1."Primitive Artists": represent the kinds of objects you see in a..
        #...plot like: "Line2D, Rectangle, Circle, and Text". 
        #2."Composite Artists": are collections of Artists such as the "Axis,...
        #...Tick, Axes, and Figure". Each "composite artist" may contain ...
        #...other "composite artists" as well as "primitive artists". 
     
    #The most important "composite artist" are: 
        
    #Figure: <--IMPORTANT. 
        #As I understand a "figure" is like the big container of the "axes"...
        #...(i.e. inside the "figure" we have "axes" and inside "axes"...
        #...we have most of the graphical elements that make up the...
        #...background of the plot).   
        
        #It is a Top level "Artist" which holds all plot elements and also...
        #...control the default spacing of the subplots.
        
        #When we plot something using "plt"...
        #...,we implicitly created a "Figure" object instance and an...
        #..."Axes" object (inside the "Figure" object). This is totally...
        #...fine and very convenient when we just want to draw a single graph.
        
        #A “figure” in matplotlib means the whole window in the user....
        #...interface.  

        #We create a "figure" object with the code:
plt.figure()
        
    #Axes: <--IMPORTANT.
        #An "Axes" object is generated "implicitly" with the plotted...
        #...chart (line, scatterplot, bars, radial,...)
        
        #Based in what we described in the previous two lines we create...
        #...an "Axes" object with the code:
            #"plt.plot()"
        
        #Is where most of the matplotlib plotting methods are defined. Is..
        #...the region where the plots and graphs are drawn. 
        
        #Not only does the "Axes" contain most of the graphical elements...
        #...that make up the background of the plot (for instance: the ticks,..
        #...the axis lines [x-axis and y-axis], the grid, the patch of color..
        #...which is the plot background, etc.) it also contains numerous...
        #...helper methods that create "primitive artists" and add them to...
        #...the "Axes" instance. 
                        
        #The main difference between the "axes" and the "subplot" is the...
        #...following: <--EXTREMELY IMPORTANT
            #While "subplot" positions the plots in a regular grid, "axes"...
            #...allows free placement within the "figure". Both can be...
            #...useful depending on your intention. 
                #With "subplot" you can arrange plots in a regular grid...
                #...You need to specify the number of "rows and columns"...
                #...and the number of the plot. Note that the "gridspec"...
                #...command is a more powerful alternative.
                
                #"Axes" are very similar to "subplots" but allow...
                #...placement of plots at any location in the "figure". So...
                #...if we want to put a smaller plot inside a bigger one...
                #...we do so with "axes".
        
        #A Matplotlib "figure" object can have one or many "axes". Therefore,...
        #...using some kind of metaphor here:
            #"Figure" object is like a paper that you can draw anything...
            #...you want.
            #We have to draw a chart in a “cell”, which is "Axes" object in...
            #...this context. 
            #If we’re drawing only one graph, we don’t have to draw a..
            #...“cell” first, just simply draw on the paper anyway. Then, we..
            #...have the following instance:
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.random.rand(20))
plt.title('test title')
plt.show()
            #Although we can explicitly draw a “cell” on the...
            #...“paper”, to tell "Matplotlib" that we’re gonna draw a...
            #...chart inside this cell. Then, we have the following...
            #...instance:  
                #Using the "subplot" codes.
                #Establishing the "graph" and also the "title of the graph"...
                #...that we wnat inside the "subplot".
import matplotlib.pyplot as plt
import numpy as np

    #Create "fig" and "ax" variables using subplots method.
fig, ax = plt.subplots()
ax.plot(np.random.rand(20))
ax.set_title('test title')
plt.show()
                #We can check what we describe in the previous 4 lines...
                #...print the type of the data, in this case the code...
                #..."fig" is a "figure object" (for this reason we can see...
                #...in the printed output the text...
                #...<class 'matplotlib.figure.Figure'> ) and the code...
                #..."ax" is an "axes object" that represent explicitly...
                #...a “cell” of the "figure object" (for this reason we...
                #...can see in the printed output the text of "subplot"
                #...<class 'matplotlib.axes._subplots.AxesSubplot'> ).
print(type(fig))
print(type(ax))
        
    #Axis: <--IMPORTANT. 
        #"Axis" is not equal to "Axes".
        #The axis in Matplotlib refers to the scale of the graph (for...
        #...instance a two-dimensional graph has an x-axis and a y-axis,...
        #...whereas a three-dimensional graph has an x-axis, a y-axis,..
        #...and a z-axis).
        
    #Subplot: <--IMPORTANT. 
        #it means a group of smaller "axes" (where each "axes"...
        #...is a plot) that can exist together within a single "figure"...
  
            #We can plot several data on the the same "figure". Also, we can...
            #...split a "figure" in several "subplots" (named "Axes").
        
            #"Subplots()" function in the matplotlib library, helps in...
            #...creating multiple layouts of subplots. It provides control..
            #...over all the individual plots that are created.
        
            #When analyzing data you might want to compare multiple plots...
            #...placed side-by-side. Matplotlib provides a convenient...
            #...method called "subplots" to do this.
            
            #There are 3 different ways (at least) to create subplots (called..
            #..."axes") in matplotlib. They are:
                #1. plt.axes()
                #2. figure.add_axis()
                #3. plt.subplots()
                
                #Of those ways (listed previously) "plt.subplots" is the...
                #...most commonly used. However, the first two approaches...
                #...are more flexible and allows you to control where...
                #...exactly on the figure each plot should appear.
                
                #If we need to add a "subplot", which exists inside another...
                #...axes, then you can specify the [bottom, left, width, ...
                #...height] to create an axis covering that region.
                
                #"plt.subplots()"
                    #Rather than creating a single "axes", this function...
                    #...creates a full grid of equal-sized "axes" in a ...
                    #...single line, returning them in a NumPy array.
                    
                    #We need to specify the numbers of "rows and columns" as...
                    #...an argument (i.e., we are putting the graphs in...
                    #...a specific array. For instance, several graphs...
                    #...one at the side of the other like a one row with...
                    #...several columns) to the "subplots()" function.
                   
#3. The third layer is the "Scripting Layer" (Topic 1.2.3):
    #We can create graphs with matplotlib using the previous two layers...
    #...if we are professional programmers.
    
    #The "Scripting Layer" is very useful for everyday purposes, particularly..
    #...for scientists who are not professional programmers. The "Scripting..
    #...Layer" it is easier to use than the "Artist layer". <--IMPORTANT.

    #The "Scripting layer" is the "matplotlib.pyplot" that automates...
    #...the process of putting everthing together. <--IMPORTANT.
    
        #"pyplot": is a stateful interface that handles much of the ...
        #...boilerplate (i.e. is any written text that can be reused in..
        #...new contexts or applications without significant changes to....
        #...the original) for creating "figures" and "axes" and connecting..
        #...them to the "backend" of your choice, and maintains module-level...
        #...internal data structures representing the current "figure" and...
        #..."axes" to which to direct plotting commands. <--IMPORTANT.
        
        #"pyplot": is mainly intended for interactive plots and simple cases...
        #...of programmatic plot generation.
      
    #In the "scripting layer" when we call the "pyplot" "plt.plot", the...
    #..."scripting layer" actually looks to see if there's a "figure" that...
    #...currently exists, and if not, it creates a new one. It then returns...
    #...the "axes" for this "figure". <--IMPORTANT.

#To sum ump:
    #There's a "backend", which deals with actual drawing.
    #A bunch of "artists" on top of the "backend", which describe how data is...
    #...arranged.
    #And a "scripting layer", which actually creates those "artists" and...
    #...choreographs them all together. 

###############################################################################

#TEN SIMPLE RULES FOR BETTER FIGURES (Topic 2)
    #https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833
    
    #Rule 1: Know Your Audience
    #Rule 2: Identify Your Message
    #Rule 3: Adapt the Figure to the Support Medium
    #Rule 4: Captions Are Not Optional
    #Rule 5: Do Not Trust the Defaults
    #Rule 6: Use Color Effectively
    #Rule 7: Do Not Mislead the Reader
    #Rule 8: Avoid “Chartjunk”
    #Rule 9: Message Trumps Beauty
    #Rule 10: Get the Right Tool (Matplotlib and R)

###############################################################################

#BASIC PLOTTING WIHT MATPLOTLIB (Topic 3)
#Some "backends" update our visualization (this is a particular feature...
#...that other backends might not).
    #This code is not necessary in the context of "Sypder" environment..
    #....<--IMPORTANT    
import matplotlib as mpl
mpl.get_backend()                                 
      
#Instance 3.1.1

#First, let's input the "pyplot" "scripting layer" as "plt". 

#We put the arguments that will be interpreted as "x, y" pairs. So let's...
#...try with just one data point at position (3,2).
    #Here, we see that the code return a draw (i.e. a blank space with...
    #...the axis) that does not has the data point (3,2) because it turns ...
    #...out that we omit to put the third argument inside the code...
    #..."plt.plot(3, 2)". This third argument allow us to draw the graph.  
    
    #It is important to say that the "axis´s limits" adapt to the "x, y" pair...
    #...that we want to graph. However, we can manually adjust or put those...
    #...values.
import matplotlib.pyplot as plt
plt.plot(3, 2)

#Instance 3.1.2
#To solve the situation described in the "Instance 3.1.1" we put a third...
#...argument inside the code "plt.plot(3, 2, "*")". In this case a string...
#...which signifies how we want that data point to be rendered. For this ...
#...case let's use an asterisk (*) as marker.                                                   
import matplotlib.pyplot as plt
plt.plot(3, 2, "*")

#Instance 3.1.3
#Is a variant of the "Instance 3.1.2".
import matplotlib.pyplot as plt
plt.plot(1.5, 1.5, 'o')

import matplotlib.pyplot as plt
plt.plot(5, 2.9, '.')

#Instance 3.2
#Let's create a new "figure" with "pyplot" (this step is not necessarily;...
#..i.e., we can omit this line of code "plt.figure()" without problem...
#...with our plot). Then, let's make a plot, grab the current "axes",...
#...and set the "x and y" axis´s limits for the current "axes" that we..
#...have just gotten.

#EXTREMELY IMPORTANT:
    #It is important to recall that when we plot something using "plt"...
    #...we implicitly created a "Figure" object instance and an Axes"...
    #...object (inside the "Figure" object). This is totally fine and...
    #...very convenient when we just want to draw a single graph.
    
    #It is important to recall that an "Axes" object is generated...
    #..."implicitly" with the plotted chart (line, scatterplot, bars,...)

    #"matplotlib.pyplot.figure" code create a new "figure", or activate an...
    #...existing "figure". Also allow us to add subplot to a "figure"...
    #...(through "axes" code) that has been create. <-IMPORTANT
    
    #We can actually get access to the "figure" using the "GCF function",...
    #...which stands for " Get Current "Figure" of "pyplot" ".
        #Stands for get "current figure".
        #Gives the reference of the "current figure".

    #We can actually get access to the "axes" using the "GCA function", which...
    #...means "Get Current Axes". 
        #“Current” means that it provides a handle to the last active...
        #..."axes".If there are no "axes" yet, axes will be created (For...
        #...instance, if you create two subplots, then the subplot that...
        #...is created last is  the "current" one). <-IMPORTANT
    
    #We set the "x and y" limits using the "axes" function. This function...
    #...takes four parameters (i.e. we limits some parameters of the...
    #..."axes"):
        #A minimum value for "x" which we'll put it zero (0),
        #A maximum value for "x" which we'll put at six (6).
        #A minimum value for "y" which we'll put it zero (0),
        #A maximum value for "y" which we'll put at ten (10).

#Creation of a new "figure"
import matplotlib.pyplot as plt
plt.figure()
#Plotting the point (5,5) using the "sigle pint marker".
plt.plot(5, 5, '.')
#Getting the current "axes".
ax = plt.gca()
#Setting axis properties [xmin, xmax, ymin, ymax]
ax.axis([0,6,0,10])

#Instance 3.3
#We can add "Artists" instances to an "Axes" object at any time through..
#...the "plot function". We are going to determine what..
#...shape we want from the string (i.e. for the third argument of our graph...
#...represented by a "dot" or "asterisk" or the lowercase letter "o"), the...
#...location associated with that shape, etc.

#In this case we make subsequent calls to the "plot" function, adding as a...
#...consequence more data to our chart (in this case 3 points with differents...
#...coordinates). When this is done, the points are rendered in different...
#...colors (this different colors were selected by the machine in an automatic...
#...way without the user help) as the "axes" recognizes them as different...
#...data series. 

    #IMPORTANT: It is necessary to run the "code of 3 plots" at the...
    #...same time and as a consequence we are going to see in the...
    #...same "Axe" the result of the "code of 3 plots".

#In addition we go further with the "axes" object to the point where we...
#...actually get all of the child objects that that "axes" contains (i.e. we...
#...get a list of all elements that are part of our current "Axes").
#We do this with the "axes" "get_children" function.
    #Here, we can see that output describe when we applied the code of..
    #..."get_children":
        #Three lines of code, each line for one 2D object contained in...
        #...this "axes" (these are our data points).
        #A number of spines (which are actual renderings of the borders of...
        #...the frame including tic markers)
        #Two axis objects (X and Y axis)
        #A bunch of text which are the labels for the chart.
        #A rectangle which is the background for the "axes".

import matplotlib.pyplot as plt
#Plot the point (1.5, 1.5) using the circle marker
plt.plot(1.5, 1.5, 'o')
#Plot the point (2, 2) using the circle marker
plt.plot(2, 2, '+')
#Plot the point (2.5, 2.5) using the circle marker
plt.plot(2.5, 2.5, '*')
#Get current axes
ax = plt.gca()
#Get all the child objects the axes contains
ax.get_children()

#############################################################################
                                 
#SCATTERPLOTS (Topic 4)

#The scatter function takes an "x-axis" value as a first argument and...
#..."y-axis" value as the second to graph multiples values at the same time.

#Instance 4.1
#In a scatterplot if the two arguments are the same, we get a nice diagonal...
#...alignment of points. 

    #I'll create a short numpy array for "x" and make "y" the same.

    #Then create a new "figure" (this step is not necessarily;...
    #..i.e., we can omit this line of code "plt.figure()" without problem...
    #...with our plot) and "scatterplot". We can see in this plot a...
    #...nice diagonal line and matplotlib has sized our axises accordingly. 
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

plt.figure()
plt.scatter(x, y)
plt.show()

    #EXTREMELY IMPORTANT:
    #It is important to recall that when we plot something using "plt"...
    #...we implicitly created a "Figure" object instance and an Axes"...
    #...object (inside the "Figure" object). This is totally fine and...
    #...very convenient when we just want to draw a single graph.
    
        #A great proof of that is that we can turn off or even delete the...
        #....code "plt.figure()" and we are going to get the same answer...
        #...and graph.
    
    #It is important to recall that an "Axes" object is generated...
    #..."implicitly" with the plotted chart (line, scatterplot, bars,...)
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

plt.scatter(x, y)

#Instance 4.2
#Create a "scatterplot" but with different colors in the....
#...data points and also with a different size for the marker (in contrast...
#...with the other instances showed previously). We can see...
#...in this plot a nice diagonal line and matplotlib has sized our...
#...axises accordingly.

#Syntax:
    #matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)
    
    #Parameters:
        #x,y: float or array-like, shape (n, )
            #The data positions.
        #s: float or array-like, shape (n, ), optional.
            #The marker size in points**2. Default is rcParams...
            #....['lines.markersize'] ** 2.
        #c: array-like or list of colors or color, optional
            #The marker colors. Possible values:
                #A scalar or sequence of "n" numbers to be mapped to colors...
                #...using cmap and norm.
                #A 2D array in which the rows are RGB or RGBA.
                #A sequence of colors of length n.
                #A single color format string.
            #If you wish to specify a single color for all points prefer...
            #...the color keyword argument.
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

# create a list of colors for each point to have
# ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'purple']
    #We can see how the last point change its color.
colors = ['green']*(len(x)-1)
colors.append('purple')

# plot the point with size 300 and chosen colors
plt.scatter(x, y, s=300, c=colors)

#Instance 4.3
#Zip Method:
    #The "zip method" takes a number of iterables and creates "tuples" out of...
    #...them, matching elements based on index. 
        #So if we have two lists of numbers, zip will take the first element...
        #...from each list and create a tuple, then the second element from...
        #...each and create a tuple, and so on.
    #The "zip method" has lazy evaluation because it's actually a "generator...
    #...in Python 3" (which means we need to use the "list" function if...
    #...we want to see the results of iterating over zip (similar when we...
    #...work with "list" function or "lambdas").
        #When we convert this "generator" to a list, we see there's a list...
        #...of pairwise tuples. 

#Use "zip" to convert the two lists into a pairwise tuples.
zip_generator1 = zip([1,2,3,4,5], [600,700,800,900,100])
print(list(zip_generator1))

#Instance 4.4
#The single asterisk " * " in the "Zip Method":
    #Unpacks a collection into positional arguments (i.e. it will show us...
    #...several tuples that are not inside a final list [i.e. square brackets]).
    #When you pass "lists" or an "intervals" more generally to a function...
    #...and prepend it with an asterisk, each item is taken out of the...
    #...iterable and passed as a separate argument (i.e. it will show us...
    #...several tuples that are not inside a final list [i.e. square brackets]).

#Use "zip" to convert the two lists into a separate argument of...
#...pairwise tuples.
    #In this case with the "zip method" we takes a number of iterables...
    #...(lists) and creates "tuples", then we passed as a separate argument...
    #...each tuple (i.e. we do not take the tuples to make a "final list" [..
    #...something that by default needs to be done considering the...
    #...."zip method" has lazy evaluation]).
        #It is important to take into account that in this intance we do not...
        #...create a "final list" because we are "unpacking a collection...
        #...into positional arguments" .
    
    #If we contrast the "Instance 4.3" and "Instance 4.4" we can see that in...
    #..."Instance 4.3" we transform our number of iterables (lists) and...
    #...creates "tuples" and finally create a "final list" formed by tuples [..
    #...something that by default needs to be done considering the...
    #...."zip method" has lazy evaluation]).
zip_generator2 = zip([1,2,3,4,5], [6100,7100,8100,9100,1100])
print(*zip_generator2)

#Instance 4.5
#Use "zip" to convert 5 tuples with 2 elements each, to 2 tuples with...
#...5 elements each. Then we create a "final list" formed by the 2 tuples [..
    #...something that by default needs to be done considering the...
    #...."zip method" has lazy evaluation]).
    #In some way it is like the inverse version of "Instance 4.3".
print(list(zip((1, 60), (2, 70), (3, 80), (4, 90), (5, 100))))

#Instance 4.6
#If we want to turn the data back, one with the "x" component and one with...
#...the "y" component, we can use parameter unpacking with "zip".
    #Step 1:First, we do something similar of what we did in Instance 4.3..
    #...(i.e. we pack the data of lists in tuples).
        #Is like calling zip((1, 6), (2, 7), (3, 8), (4, 9), (5, 10))
    #Step 2:Then we unpack the result of "Step 1" with a new "zip" code...
    #...in two variables (in this case the variables "x" and "y"). In other...
    #...words is like generate similar beginning conditions for data.

zip_generator = zip([1,2,3,4,5], [67,77,87,97,107])
# let's turn the data back into 2 groups of data.
x, y = zip(*zip_generator) 
print(x)
print(y)

#Instance 4.7
#We use as a conceptual base the code of "Instance 4.6"

#It is important to run all the code at the same time if we want to see...
#...all changes or transformations (that produces the code) in the same...
#...graph. <--IMPORTANT

#In this instance we create a single graph created from 2 different datasets..
#...(in this case the values of the groups of data "x" and "y" had...
#...been packed and then unpacked before been used in the graph).

import matplotlib.pyplot as plt
import numpy as np

zip_generator = zip([1,2,3,4,5], [67,77,87,97,107])
x, y = zip(*zip_generator) 
print(x)
print(y)

# Plot a data series 'Tall students' in red using the first two elements...
#...(this count of elements is based in the Python; therefore, we start with..
#...the elements located in the position 0 and 1, but element located in...
#...the position 2 is not included) of "x" and "y".

     #It is interesting to see that we have very different scales for the...
     #..."x" and "y" axis.
     
     #It is interesting to remark that the label "Tall students" (as a...
     #..."legend") does not appear in the graph.
     
     #Syntax:
     #matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)
    
     #Parameters:
        #label: I think it belongs to the parameter "**kwargs" and allow us..
        #...use that "string" described as label in the "legend".                                                                                                                               
plt.scatter(x[:2], y[:2], s=100, c='red', label='Tall students')

#Plot a second data series 'Short students' in blue using the last three...
#...elements (this count of elements is based in the Python; therefore, we...
#...start with the elements located in the position 2 until end) of "x"...
#...and "y".

     #It is interesting to see that we have very different scales for the...
     #..."x" and "y" axis.
     
     #It is interesting to remark that the label "Short students" (as a...
     #..."legend") does not appear in the graph.
plt.scatter(x[2:], y[2:], s=100, c='blue', label='Short students')

#Instance 4.8
#We use as a conceptual base the code of "Instance 4.7"

#It is important to run all the code at the same time if we want to see...
#...all changes or transformations (that produces the code) in the same...
#...graph. <--IMPORTANT

#Now we are interested in:
    #1.Put a label to the "x" axis and to the "y" axis.
    #2.Put a title to the graph
    #3.Put a legend to the graph
  
#1.1.Label:
   #Set the label for the x-axis (i.e. title of x-axis).
   #Syntax:
       #matplotlib.pyplot.xlabel(xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)
       #Parameters (some of them):
           #xlabel: str
               #The label text.
           #labelpad: float, default: rcParams["axes.labelpad"] (default: 4.0)
               #Spacing in points from the Axes bounding box including ticks...
               #...and tick labels. If None, the previous value is left as is.
           #loc: {'left', 'center', 'right'}, default: rcParams["xaxis.labellocation"] (default: 'center')
               #The label position. This is a high-level alternative...
               #...for passing parameters x and horizontalalignment.

#1.2.Label:
   #Set the label for the y-axis (i.e. title of y-axis).
   #Syntax:
       #matplotlib.pyplot.ylabel(ylabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)
       #Parameters (some of them):
           #ylabel: str
               #The label text.
           #labelpad: float, default: rcParams["axes.labelpad"] (default: 4.0)
               #Spacing in points from the Axes bounding box including ticks...
               #...and tick labels. If None, the previous value is left as is.
           #loc: {'bottom', 'center', 'top'}, default: rcParams["yaxis.labellocation"] (default: 'center')
               #The label position. This is a high-level alternative...
               #...for passing parameters x and horizontalalignment.            

#2.Title:
   #Set a title for the Axes.
   #Set one of the three available "Axes titles". The available titles...
   #...are positioned above the Axes:
       #In the center
       #Flush (i.e. "alinedados") with the left edge.
       #Flush (i.e. "alinedados") with the right edge.
   #Syntax:
       #matplotlib.pyplot.title(label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs)
       #Parameters (some of them):
           #label: str
               #Text to use for the title.
           #fontdict: dict
               #A dictionary controlling the appearance of the title text.
           #loc: {'center', 'left', 'right'}, default: rcParams["axes.titlelocation"] (default: 'center')
               #Which title to set.
            
#3.Legend:
    #The "legend module" defines the "Legend class", which is responsible...
    #....for drawing legends associated with "axes and/or figures".
    
        #The "Legend class" is a container of "legend handles" and "legend..
        #...texts".
    
        #The "legend handler" map specifies how to create "legend handles"...
        #...from "artists" (lines, patches, etc.) in the "axes" or "figures". 
    
    #Syntax:
        #class matplotlib.legend.Legend(parent, handles, labels, loc=None, numpoints=None, markerscale=None, markerfirst=True, scatterpoints=None, scatteryoffsets=None, prop=None, fontsize=None, labelcolor=None, borderpad=None, labelspacing=None, handlelength=None, handleheight=None, handletextpad=None, borderaxespad=None, columnspacing=None, ncol=1, mode=None, fancybox=None, shadow=None, title=None, title_fontsize=None, framealpha=None, edgecolor=None, facecolor=None, bbox_to_anchor=None, bbox_transform=None, frameon=None, handler_map=None, title_fontproperties=None)
        #Parameters (some of them):
            #label: list of str
               #A list of labels to show next to the "artists". The length...
               #...of "handles" and "labels" should be the same. If they are...
               #...not, they are truncated to the smaller of both lengths.
           #loc: str or pair of floats, default: rcParams["legend.loc"] (default: 'best') ('best' for axes, 'upper right' for figures)
               #The location of the legend.
                   #1.The strings 'upper left', 'upper right', 'lower left',...
                   #...'lower right' place the legend at the corresponding...
                   #...corner of the "axes/figure".
                   
                   #2.The strings 'upper center', 'lower center',...
                   #...'center left', 'center right' place the legend at...
                   #...the center of the corresponding edge of the..
                   #..."axes/figure".
                   
                   #3.The string 'center' places the legend at the center...
                   #...of the "axes/figure".
                   
                   #4.The string 'best' places the legend at the location,...
                   #...among the nine locations defined so far, with the...
                   #...minimum overlap with other drawn artists. This...
                   #:..option can be quite slow for plots with large..
                   #...amounts of data; your plotting speed may benefit...
                   #...from providing a specific location.
                   
                   #4.Each "string" locations can also be given as a..
                   #...numeric value.
                       #Location String - Location Code
                       #'best'- 0
                       #'upper right'- 1
                       #'upper left'- 2
                       #'lower left'- 3
                       #'lower right'- 4
                       #'right'- 5
                       #'center left'- 6
                       #'center right'- 7
                       #'lower center'- 8
                       #'upper center'- 9
                       #'center'- 10
            #frameon: bool, default: rcParams["legend.frameon"] (default: True)
                #Whether the legend should be drawn on a patch (frame); (i.e....
                #...if it is necessary to put the legend inside of a...
                #...very thin frame).
            #title: str or None
                #The legend's title. Default is no title (None).	
   #Label: I think it belongs to the parameter "**kwargs" of code..
   #..."matplotlib.pyplot.figure" and allow us use that "string"...
   #...described as "label" in the "legend". 
import matplotlib.pyplot as plt
import numpy as np

zip_generator = zip([1,2,3,4,5], [67,77,87,97,107])
x, y = zip(*zip_generator) 
print(x)
print(y)

plt.scatter(x[:2], y[:2], s=100, c='green', label='Tall students')
plt.scatter(x[2:], y[2:], s=100, c='chocolate', label='Short students')

#Add a label to the x axis
plt.xlabel('The number of times the child kicked a ball')
#Add a label to the y axis
plt.ylabel('The grade of the student')
#Add a title
plt.title('Relationship between ball kicking and grades')
#Add a legend (uses the "labels" from plt.scatter)
plt.legend()

#Instance 4.9
#We use as a conceptual base the code of "Instance 4.8".In this case we just...
#...modify a little the position and title of the "legend" of the graph.
#Those changes are:
    #1. Locate the "legend" in the 'lower right' position of the ...
    #...corresponding corner of the "axes/figure" using the code "loc=4".
    #2. I turn off the very thin gray frame that is by default around...
    #...the legend.
    #3. I put the title of the "legend": "Leyend X"

import matplotlib.pyplot as plt
import numpy as np

zip_generator = zip([1,2,3,4,5], [67,77,87,97,107])
x, y = zip(*zip_generator) 
print(x)
print(y)

plt.scatter(x[:2], y[:2], s=100, c='green', label='Tall students')
plt.scatter(x[2:], y[2:], s=100, c='chocolate', label='Short students')

plt.xlabel('The number of times the child kicked a ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')

#Add the legend to "loc = 4" (the lower right hand corner), also gets rid...
#:..of the frame and adds a "title".
plt.legend(loc=4, frameon=False, title='Legend X')

#Instance 4.10
#We use as a conceptual base the code of "Instance 4.9".

#The "legend" itself is an "artist", which means it can contain "children".

#Let's take advantage of this and write a little routine to recursively...
#...go through the "list of children" of all elements of the graph...
#...(including the "legend"). 

#It is important to run all the code at the same time if we want to see...
#...all changes or transformations (that produces the code) <--IMPORTANT.

import matplotlib.pyplot as plt
import numpy as np

zip_generator = zip([1,2,3,4,5], [67,77,87,97,107])
x, y = zip(*zip_generator) 
print(x)
print(y)

plt.scatter(x[:2], y[:2], s=100, c='green', label='Tall students')
plt.scatter(x[2:], y[2:], s=100, c='chocolate', label='Short students')

plt.xlabel('The number of times the child kicked a ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')

plt.legend(loc=4, frameon=False, title='Legend X')

    #We get "children" " from current "axes" ". In this case we can see that...
    #...the "legend" appears described in the "children's list" as the...
    #...second to last item in this list.
    
    #We get "children" from current "axes" with a code that is shorter than...
    #...the code used to get childrens Instance 3.3 
plt.gca().get_children()

#Instance 4.11
#We use as a conceptual base the code of "Instance 4.10".

#It is important to run all the code at the same time if we want to see...
#...all changes or transformations (that produces the code) <--IMPORTANT.

import matplotlib.pyplot as plt
import numpy as np

zip_generator = zip([1,2,3,4,5], [10,20,30,40,50])
x, y = zip(*zip_generator) 
print(x)
print(y)

plt.scatter(x[:2], y[:2], s=100, c='green', label='Tall students')
plt.scatter(x[2:], y[2:], s=100, c='chocolate', label='Short students')

plt.xlabel('The number of times the child kicked a ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')

plt.legend(loc=4, frameon=False, title='Legend X')

plt.gca().get_children()

    #We can get with a positional argument (based in the "children's list")...
    #...the type of "children" that we are handling. In this case:
        #Position [-2] = We get as answer "Legend"
        #Position [-5] = We get as answer "text" (in this case this is...
        #...the title of the graph)    
Argument1 = plt.gca().get_children()[-2]
print(Argument1)

Argument2 = plt.gca().get_children()[-5]
print(Argument2)

#Instance 4.12
#We use as a conceptual base the code of "Instance 4.11".

#The "legend" itself is an "artist", which means it can contain "children"...
#...Let's take advantage of this and write a little routine to recursively...
#...go through the list of "children" in an "artist" with the following...
#...steps:
    #Step 1. Import the "artist class" from "matplotlib".
    # Step2. Then we'll make a recursive "function" which takes in an "artist"...
    #...and some "depth" parameter.
    #Step 3. Then checks if the object is an "artist" and if so, prints out...
    #...its string name.
    #Step 4. Then we apply a "for loop" to recurse and increase the depth...
    #...for pretty printing (i.e. after we confirmed in the previous steps...
    #...that we are dealing with an "artist", we are going to get the...
    #..."children" of it).
    #Step 5. Finally, we can call this on the "legend" object itself.
    
#An an answer we can see the "legend" artist is just made up of a number of...
#...different "offsetboxes" for drawing, as well as "TextAreas" and...
#..."PathCollections. 

import matplotlib.pyplot as plt
import numpy as np

zip_generator = zip([1,2,3,4,5], [10,20,30,40,50])
x, y = zip(*zip_generator) 
print(x)
print(y)

plt.scatter(x[:2], y[:2], s=100, c='green', label='Tall students')
plt.scatter(x[2:], y[2:], s=100, c='chocolate', label='Short students')

plt.xlabel('The number of times the child kicked a ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')

plt.legend(loc=4, frameon=False, title='Legend X')

#Step 1: Importing the "artist class" from "matplotlib".
from matplotlib.artist import Artist

#Steps 2,3 and 4:
def rec_gc(art, depth=0):
    if isinstance(art, Artist):
        print("  " * depth + str(art))
        for child in art.get_children():
            rec_gc(child, depth+2)

#Step 5: Calling this function on the "legend" artist to see what the...
#..."legend" is made up of
rec_gc(plt.legend())

#To sum up:
    #We basically calls to the "scripting interface", just create "figures,...
    #...and axes". Then load those "axes" up with various...
    #..."artists", which the "backend layer" renders to the screen or some...
    #...other medium like a file.        

    #While we spend 95% of our time at the "scripting layer", creating...
    #...graphs and charts, it's important to understand how the library works..
    #...underneath for the other 5% of the time, because having control over
    #...it will allow us to create our own "charting functions".

#############################################################################
                                 
#LINE PLOTS (Topic 5)    

#Instance 5.1
#We create two groups of data, in this case a "Linear Data" and...
#..."Exponential Data" (based in "Linear Data"). Then we plot both groups...
#...of data in the same graph.

    #It is important to take into account that we are going to plot "X" data...
    #...vs "Y" data as "lines and/or markers".
    
    #It is important to remark that we are going to get as an answer a...
    #...Line or Lines in 2D (a list of lines representing the plotted data).
        
    #Syntax:
        #matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)    #Parameters (some of them):
        #Parameters (some of them):
            #fmt = Format Strings "[marker][line][color]" (optional)
                #This parameter is a convenient way for...
                #...defining basic formatting like "color, marker and...
                #...linestyle". It's a shortcut string notation.
                #If not provided, the value from the style cycle is used....
                #...Exception: If line is given, but no marker, the data...
                #...will be a line without markers.
                #Other combinations such as [color][marker][line] are...
                #...also supported, but note that their parsing may be...
                #:..ambiguous.    
            #x,y: array-like or scalar
                #The horizontal / vertical coordinates of the data points. 
                #Commonly, these parameters are 1D arrays.
                #They can also be scalars, or two-dimensional (in that case,...
                #...the columns represent separate data sets).
            #data: indexable object (optional).
                #An object with labelled data. If given, provide the...
                #...label names to plot in x and y.
    
    #In this case we use the following format for the lines (using a brief...
    #...notation called "fmt" [discussed in the previous lines] to...
    #...modify format features):
        #In this brief notation to modify format features we put the...
        #..."Line style" together to the "Line color"

        #"Linear Data": 
            #Lines color: "m" for magenta. 
            #Lines style: --
        #"Exponential Data": 
            #Lines color: "b" for blue. 
            #Lines style: - 
import matplotlib.pyplot as plt
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2
plt.plot(linear_data, '--m', exponential_data, '-b')
    
#Instance 5.2
#We based the main code (an its concetps in Instance 5.1).

#We plot another series, in this case we use only "Linear Data"

    #In this case the "data" [22,44,55] plot "y" axis, meanwhile the "x"...
    #...axis is an index array (For instance: 0,1,2,3...N-1).
        #In this case because we are working only with 3 terms in the...
        #..."y" axis, we are going to work with 3 index values in the...
        #..."x" axis (i.e. 0, 1 and 2).

    #In this case we use the following format for the lines (using a brief...
    #...notation called "fmt" [discussed in the previous lines] to...
    #...modify format features):
        #In this brief/formal notation to modify format features we put the...
        #..."Line style" together to the "Line color", and also we add the...
        #...linewidth
        
        #"Linear Data": 
            #Lines color: "C1" for orange
            #Lines style: :
            #Linewidth: 3
import matplotlib.pyplot as plt
import numpy as np
plt.plot([22,44,55], ':C1', linewidth=3)

#Instance 5.3
#We based the main code (an its concetps in "Instance 5.1" and "Instance 5.2").

#We plot three another series, in this case all "Linear Data".

    #In this case we use the following format for the lines (using a formal...
    #...notation to modify format features):
        #In this formal notation to modify format features we put the...
        #..."Line style", "Line color", "marker" and "linewidth" in a very...
        #...explicty way.
import matplotlib.pyplot as plt
import numpy as np
plt.plot([22,44,66], linestyle="--", color="greenyellow", marker="s", linewidth=2)
plt.plot([11,55,77], linestyle=":", color="darkviolet", marker=".", linewidth=2)
plt.plot([33,88,99], linestyle="-", color="cadetblue", marker="3", linewidth=2)

    #In this case we also add:
        #Y Label, X Label, Title of the Plot and a Legend (as we did in...
        #...Instance 4.8 and Instance 4.9)
plt.xlabel('Countries')
plt.ylabel('Money')
plt.title('Gross Domestic Product')
plt.legend(['Panama', 'Colombia', 'USA'],loc=4, frameon=False)

#Instance 5.4.1
#We are going to learn hoy to fill the space between two horizontal curves.

    #The curves are defined by the points (x, y1) and (x, y2). This...
    #...creates one or multiple polygons describing the filled area.
        #We are establishing the upper bound (y1) and the lower...
        #...bound (y2).

    #We can exclude some horizontal sections from filling using "where".

    #By default, the edges connect the given points directly. We can use...
    #..."step" if the filling should be a "step function".
                                                                                                                                  
    #Syntax:
        #matplotlib.pyplot.fill_between(x, y1, y2=0, where=None, interpolate=False, step=None, *, data=None, **kwargs)
        #Parameters (some of them):
            #x: array (length N)
                #The x coordinates of the nodes defining the curves.
            #y1: array (length N) or scalar
                #The y coordinates of the nodes defining the first curve.
            #y2: array (length N) or scalar, default: 0
                #The y coordinates of the nodes defining the second curve.
            #facecolor: it is the color of the fill.
            #alpha: it is used to established the transparency of the fill.

#We based the main code (an its concetps in "Instance 5.1",...
#..."Instance 5.2" and "Instance 5.3").

#Our main purpuse is to fill the area between the group of data (in this...
#...case [22,44,66]) and the axis "x" in the following way:
    
    #Step 1: It is important to remark that we are plotting a grap that...
    #...only have "y" axis data points [22,44,66] as we had in...
    #.. "Instance 5.2" and "Instance 5.3".
    
    #Step 2:
    #The code "(range(len([22,44,66]))" in "plt.gca().fill_between"...
    #...represents the parameters of "x" axis of the fill (in this case...
    #...they are the lower bound).
        #Those parameters are the same index array points 
        #...of the plot of graph of Step 1.
    #The code [22,44,66] in "plt.gca().fill_between" represents the...
    #...parameter "y1" of "y" axis of the fill. (in this case...
    #...they are the upper bound).
        #Those parameters match exactly with the parameters of "y"
        #...of the plot of graph of Step 1.
    
    #As a result of use the same data points for the "x" and "y" axis...
    #...in the exact way described in the code "plt.gca().fill_between"...
    #...we can see clearly in the plot that the fill is exactly below the...
    #...line's graph of "y" axis data points [22,44,66].                                    
import matplotlib.pyplot as plt
import numpy as np
plt.plot([22,44,66], linestyle="--", color="greenyellow", marker="s", linewidth=2)

plt.gca().fill_between(range(len([22,44,66])),[22,44,66], facecolor='blue', alpha=0.15)


#Instance 5.4.2
#We based the main code (an its concetps in "Instance 5.4.1").

#In this case:
#Our main purpuse is to fill the area between the group of data (in this...
#...case [1,2,3]) and the axis "x" in the following way:
    
    #Step 1: It is important to remark that we are plotting a grap that...
    #...only have "y" axis data points [1,2,3] as we had in...
    #.. "Instance 5.2" and "Instance 5.3".
    
    #Step 2:
    #The code "[1,2,3]" in "plt.gca().fill_between"...
    #...represents the parameter of "x" axis of the fill. (in this case...
    #...they are the lower bound).
        #Those parameters are not the same index array points 
        #...of the plot of graph of Step 1.        
    #The code [8,10,12] in "plt.gca().fill_between" represents the...
    #...parameter "y1" of "y" axis of the fill. (in this case...
    #...they are the upper bound).
        #Those parameters do not match with the parameters of "y"
        #...of the plot of graph of Step 1.
    
    #As a result of use different data points for the "x" and "y" axis (for...
    #...the line graph and the fill) we can see clearly in the plot that...
    #...the fill is not exactly below the line's graph of "y" axis...
    #...data points [1,2,3].
import matplotlib.pyplot as plt
import numpy as np
plt.plot([1,2,3], linestyle="--", color="greenyellow", marker="s", linewidth=2)

plt.gca().fill_between([1,2,3],[8,10,12], facecolor='blue', alpha=0.25)

#Instance 5.4.3
#We based the main code (an its concetps in "Instance 5.4.1").

#In this case:
#Our main purpuse is to fill the area between the group of data (in this...
#...case [22,44,66]) and the axis "x" in the following way:
    
    #Step 1: It is important to remark that we are plotting a grap that...
    #...only have "y" axis data points [22,44,66] as we had in...
    #.. "Instance 5.2" and "Instance 5.3".
    
    #Step 2:
    #The code "range(len([22,44,66]))" in "plt.gca().fill_between"...
    #...represents the parameter of "x" axis of the fill. 
        #Those parameters are the same index array points 
        #...of the plot of graph of Step 1.        
    #The code [3],[50] in "plt.gca().fill_between" represents the...
    #...parameter "y1" of "y2" (for the second curve that does not...
    #...exist) axis of the fill. (in this case...
    #...the [3] is the lower bound and the [50] is the upper bound).
        #Those parameters do not match with the parameters of "y"
        #...of the plot of graph of Step 1.
    
    #As a result of use different data points for the "x" and "y" axis (for...
    #...the line graph and the fill) we can see clearly in the plot that...
    #...the fill is not exactly below the line's graph of "y" axis...
    #...data points [22,44,66].
import matplotlib.pyplot as plt
import numpy as np
plt.plot([22,44,66], linestyle="--", color="greenyellow", marker="s", linewidth=2)

plt.gca().fill_between(range(len([22,44,66])),3,50,facecolor='blue', alpha=0.25)

#Instance 5.4.4
#We based the main code (an its concetps in "Instance 5.4.1").

#In this case:
#Our main purpuse is to fill the area between the group of data (in this...
#...case [22,44,66] and [11,55,77]) and the axis "x" in the following way:
    
    #Step 1: It is important to remark that we are plotting a grap that...
    #...only have "y" axis data points [22,44,66] and [11,55,77] as we...
    #...had in "Instance 5.2" and "Instance 5.3".
    
    #Step 2:
    #The code "range(len([22,44,66]))" in "plt.gca().fill_between"...
    #...represents the parameter of "x" axis of the fill. 
        #Those parameters are the same index array points 
        #...of the plot of graph of Step 1.        
    #The code [22,44,66],[11,55,77] in "plt.gca().fill_between"...
    #...represents the parameter "y1" of "y2" (where the first curve is...
    #...[22,44,66] and the second curve is [11,55,77]) axis of the fill...
    #...(in this case the [11,55,77] is the lower bound and the [22,44,66]...
    #...is the upper bound).
        #Those parameters do match with the parameters of "y"
        #...of the plot of graph of Step 1.
    
    #As a result of use different data points for the "x" and "y" axis (for...
    #...the line graph and the fill) we can see clearly in the plot that...
    #...the fill is exactly up and below the line's graph of "y" axis...
    #...data points [22,44,66] and [11,55,77].
import matplotlib.pyplot as plt
import numpy as np
plt.plot([22,44,66], linestyle="--", color="greenyellow", marker="s", linewidth=2)
plt.plot([11,55,77], linestyle="-", color="cadetblue", marker="3", linewidth=2)

plt.gca().fill_between(range(len([22,44,66])),[22,44,66],[11,55,77], facecolor='blue', alpha=0.25)

#Instance 5.5
#Let's try working with dates! (using Numpy)

#In this case we plot a graph with two lines:
    
    #It is very interesting to see that in just one line of code I wrote...
    #...the code for 2 graps that belong to same axes.
    
    #Step 1: taking as a "x axis" the values of range of dates from....
    #...'2017-01-01' to '2017-01-09'.
    
    #Step 2.1: We use as a "y axis" for the curve 1 the values of...
    #..."linear_data".
    
    #Step 2.2: We use as a "y axis" for the curve 2 the values of...
    #..."exponential_data". 

#Some of the code is (from Numpy):
    #"arange"
        
    #"arange": Return evenly spaced values within a given interval.
    #"arange" can be called with a varying number of positional arguments:
        #arange(stop): Values are generated within the half-open...
        #...interval [0, stop) (in other words, the interval including...
        #...start but excluding stop).
        #arange(start, stop): Values are generated within the half-open...
        #...interval [start, stop).
        #arange(start, stop, step): Values are generated within the...
        #....half-open interval [start, stop), with spacing between...
        #...values given by step.

    #Syntax:
        #numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
        #Parameters (some of them):
            #start: integer or real (optional).
                #Start of interval. The interval includes this value...
                #...The default start value is 0.
            #stop: integer or real.
                #End of interval. The interval does not include this...
                #...value, except in some cases where step is not an...
                #...integer and floating point round-off affects the...
                #...length of out.
            #step: integer or real (optional)
                #Spacing between values. 
            #dtype: dtype (optional)
                #The type of the output array. If dtype is not given,...
                #...infer the data type from the other input arguments.
import matplotlib.pyplot as plt
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
plt.plot(observation_dates, linear_data, '-o',  observation_dates, exponential_data, '-o')

#Instance 5.6.1
#Let's try working with dates! (using Numpy and Pandas) to convert "Numpy...
#...array of dates" into "Standard Library Dates" (the latter easily...
#...handled by Matplotlib) thanks to "Pandas" (to be specific, using the...
#...code "pandas.to_datetime").

#We based the main code (an its concetps in "Instance 5.5").

#In this case we plot a graph with two lines:
    
    #It is very interesting to see that in just one line of code I wrote...
    #...the code for 2 graps that belong to same axes.
    
    #Step 1.1: taking as a "x axis" the values of range of dates from....
    #...'2017-01-01' to '2017-01-09' (until now those dates values are...
    #... in a Numpy array).
    
    #Step 1.2: we apply a "map function" over the range of dates using the...
    #...specific function of "pandas.to_datetime" (i.e., the dates values in...
    #...the Numpy array are converterd into a new format of dates thanks to...
    #...the Pandas code).
    
    #Step 2.1: We use as a "y axis" for the curve 1 the values of...
    #..."linear_data".
    
    #Step 2.2: We use as a "y axis" for the curve 2 the values of...
    #..."exponential_data".
    
    #Step 3: Trying to plot a "map" will result in an error because we...
    #...forget to convert this "map" object into a "list" to make it readable.
        #To be specific: "map function" returns an "iterator" and Matplotlib...
        #...can't handle the "iterator", so we need to convert the...
        #..."interator" to a "list".

#Some of the code is (from Pandas and Python):  
    #"Map function"
    
    #The "map function" is one of the basis for "functional programming" in..
    #...Python.
        #"Functional programming" is a programming paradigm in which you...
        #...explicitly declare all parameters which could change through...
        #...execution of a given function.
    #It is a way of making lists.
    #You pass inside "map()" a "function and an iterable", then "map()" will...
    #...create an object. This "object" contains the output you would get...
    #...from running each iterable element through the supplied function.
    #The map function signature looks like this "map(function, iterable)":
        #The first parameter, the function that you want executed, and the...
        #...second parameter, and every following parameter, is something...
        #...which can be iterated upon (all the iterable arguments are...
        #...unpacked together, and passed into the given function)
    #Map() is iterable, so we can use like a for loop to look at all of the...
    #...values or items in the map(). 
    #We must convert this "map" object into a list using list(), set, or...
    #...another iterable item to make it readable (i.e. the "map" object...
    #...itself is just a bunch of random mis of letters and number; in...
    #...other words is not readable) <--IMPORTANT.
    
    #"pandas.to_datetime"
    
    #The "pandas.to_datetime": is a function to convert argument to datetime.
        #This function converts a scalar, array-like, Series or...
        #...DataFrame/dict-like to a pandas datetime object.                                   
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observation_dates = map(pd.to_datetime, observation_dates) 
plt.plot(observation_dates, linear_data, '-o',  observation_dates, exponential_data, '-o')

#Instance 5.6.2
#Let's try working with dates! (using Numpy and Pandas)

#We based the main code (an its concetps in "Instance 5.6.1").

#In this case we plot a graph with two lines:
    
    #It is very interesting to see that in just one line of code I wrote...
    #...the code for 2 graps that belong to same axes.
    
    #Step 1.1: taking as a "x axis" the values of range of dates from....
    #...'2017-01-01' to '2017-01-09'.
    
    #Step 1.2: we apply a "map function" over the range of dates using the...
    #...specific function of "pandas.to_datetime".(i.e., the dates values in...
    #...the Numpy array are converterd into a new format of dates thanks to...
    #...the Pandas code).
    
    #Step 2.1: We use as a "y axis" for the curve 1 the values of...
    #..."linear_data".
    
    #Step 2.2: We use as a "y axis" for the curve 2 the values of...
    #..."exponential_data".
    
    #Step 3: Trying to plot a "map" will result in success because we...
    #...converted this "map" object into a "list" to make it readable.
        #To be specific: "map function" returns an "iterator" and Matplotlib...
        #...can't handle the "iterator", so we need to convert the...
        #..."interator" to a "list".

#Some of the code is (from Pandas and Python):   
    #"Map function"
    
    #The "map function" is one of the basis for "functional programming" in..
    #...Python.
        #"Functional programming" is a programming paradigm in which you...
        #...explicitly declare all parameters which could change through...
        #...execution of a given function.
    #It is a way of making lists.
    #You pass inside "map()" a "function and an iterable", then "map()" will...
    #...create an object (i.e., the "interator"). This "object" contains...
    #...the output you would get...
    #...from running each iterable element through the supplied function.
    #The map function signature looks like this "map(function, iterable)":
        #The first parameter, the function that you want executed, and the...
        #...second parameter, and every following parameter, is something...
        #...which can be iterated upon (all the iterable arguments are...
        #...unpacked together, and passed into the given function)
    #Map() is iterable, so we can use like a for loop to look at all of the...
    #...values or items in the map(). 
    #We must convert this "map" object into a list using list(), set, or...
    #...another iterable item to make it readable (i.e. the "map" object...
    #...itself is just a bunch of random mis of letters and number; in...
    #...other words is not readable) <--IMPORTANT.
    
    #"pandas.to_datetime"
    #The "pandas.to_datetime": is a function to convert argument to datetime.
        #This function converts a scalar, array-like, Series or...
        #...DataFrame/dict-like to a pandas datetime object.   
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates)) 
plt.plot(observation_dates, linear_data, '-o',  observation_dates, exponential_data, '-o')

#Instance 5.7

#We based the main code (an its concetps in "Instance 5.6.2").

#We can actually get access to the "axes" using the "GCA function", which...
#...means "Get Current Axes". This code allow us to get the "current...
#...axes" instance on the current "figure" matching the given keyword...
#..."args" or create one. <-IMPORTANT
    #“Current” means that it provides a handle to the last active...
    #..."axes".If there are no "axes" yet, axes will be created. If you...
    #...create two subplots, then the subplot that is created last is..
    #...the "current" one. <-IMPORTANT
    #There are lots of interesting properties of the "axes" object. For...
    #...instance:
        #We can get the grid lines
        #We can get the tick locations for both major and minor ticks.
    #Just like all "artists", an "axes" has a bunch of "children" which are...
    #:..themselves "artists".

    #In this case we are interested in the "x" axis. To be specific we want...
    #...to modify the rotation of the "major tick labels" of the "x" axis...
    #...(with the main purpose to see the dates of "x" axis better we rotate...
    #...those dates 45 degrees).
         #Step 1: First we can get a single axis using the "x" axis or...
         #..."y" axis properties of the "axes" object which we can get,...
         #...with "GCA". <-IMPORTANT
         #Step 2: This rotation was able due to that fact that the code 
         #"x.get_ticklabels()" output a "list of text". Afterwards that...
         #..."list of text" was rotated by the code "set_rotation(s)" that...
         #...allow us rotate text.
             #Each of the "tick labels" are a "text" object which itself...
             #...is an "artist". This means that we can use a number of...
             #...different "artist" functions (one of those functiones...
             #...us "rotation function").
    
#Some of the code is (from Matplotlib):
    #"x.get_ticklabels()"
        
    #"Axis.get_ticklabels": Get this Axis ticklabels (i.e. we get direct...
    #...access through this code to the Axis ticklabels), which could be:
        #"Minor ticklabels":it is the "small line" that come from the "axis...
        #...line" and that is coupled with the number or text or date (this...
        #...number describe a coordinate of a point).
        #"Major ticklabels":it is a number or text or date that is located...
        #...in the the axis to describe a coordinate of a point.
        #Or "both".
     #It returns a "list of Text".
        
    #Syntax:
        #"Axis.get_ticklabels(minor=False, which=None)": 
        #Parameters (some of them):
        #minor: bool
            #Whether to return the minor or the major ticklabels.
        #which: None, ('minor', 'major', 'both')
            #Overrides minor.
            #Selects which ticklabels to return
            
    #"set_rotation()"
    
    #Set the rotation of the text.

    #Syntax:
        #"set_rotation(s)": 
        #Parameters (some of them):
        #s: float or {'vertical', 'horizontal'}
            #The rotation angle in degrees in mathematically positive..
            #...direction (counterclockwise). 'horizontal' equals 0,..
            #...'vertical' equals 90.    
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2

observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates)) 
plt.plot(observation_dates, linear_data, '-o',  observation_dates, exponential_data, '-o')

x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)
    
#Instance 5.8

#We based the main code (an its concetps in "Instance 5.7").

#Adjust the "subplot" so the text doesn't run off the image.

#We are going to compress the vertical axis of the "subplot", taking as a...
#...reference of adjustment of the "bottom of the "subplot" with "0.8"...
#...(considering that the default size is "0.1")

#Some of the code is (from Matplotlib):
    
    #"matplotlib.pyplot.subplots_adjust"
    
    #Adjust or refine the "subplot" structure or design or layout parameters...
    #...(i.e., we can change the shape [stretching or compressing vertically...
    #...or horizontally] of the "subplot" in relation with the "figure" which...
    #...tht "subplot" belongs. As a consequence we are going to...
    #...see the changes in the quantity of "minor ticklabels" that appears...
    #...in the "subplot" after we do the adjustment.

    #Syntax:
        #matplotlib.pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None):
        #Parameters (some of them):
        #left: float (optional).
            #The position of the left edge of the subplots, as a..
            #...fraction of the figure width. Default size is 0.125.
        #right: float (optional).
            #The position of the right edge of the subplots, as a...
            #...fraction of the figure width. Default size is 0.9
        #bottom: float (optional).
            #The position of the bottom edge of the subplots, as a..
            #...fraction of the figure height. Default size is 0.1
        #top: float (optional).
            #The position of the top edge of the subplots, as a...
            #...fraction of the figure height. Default size is 0.9
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates)) 
plt.plot(observation_dates, linear_data, '-o',  observation_dates, exponential_data, '-o')

x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)
    
plt.subplots_adjust(bottom=0.8)

#Instance 5.9.1
#We based the main code (an its concetps in "Instance 5.7").

#Now we are interested in:
    #1.Put a label to the "x" axis and to the "y" axis.
    #2.Put a title to the graph

#We can actually get access to the "axes" using the "GCA function", which...
#...means "Get Current Axes". This code allow us to get the "current...
#...axes" instance on the current "figure" matching the given keyword...
#..."args" or create one. <-IMPORTANT
    #“Current” means that it provides a handle to the last active...
    #..."axes".If there are no "axes" yet, axes will be created. If you...
    #...create two subplots, then the subplot that is created last is..
    #...the "current" one. <-IMPORTANT
    #There are lots of interesting properties of the "axes" object. For...
    #...instance:
        #We can get the grid lines
        #We can get the tick locations for both major and minor ticks.
    #Just like all "artists", an "axes" has a bunch of "children" which are...
    #:..themselves "artists".
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates)) 
plt.plot(observation_dates, linear_data, '-o',  observation_dates, exponential_data, '-o')

x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)

ax = plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title('Exponential vs. Linear performance')

#Instance 5.9.2
#We based the main code (an its concetps in "Instance 5.7").

#Now we are interested in:
    #1.Put a label to the "x" axis and to the "y" axis.
    #2.Put a title to the graph (adding mathematical expressions. It is...
    #...important to say that the mathematical expressions that we want to...
    #...write needs to be between dollar symbols $...$)
        #"Matplotlib" has a fairly strong connection to "LaTeX" (a type...
        #...setting language used by mathematicians and scientists).
        #This means that we can use a subset of "LaTeX" directly in our..
        #...labels then "matplotlib" will render them as equations (we...
        #...do this by escaping to LaTeX" math mode with "dollar signs").
        #"LaTeX" works regardless of whether we have installed it.   
        #"LaTeX" (pronounced «Lah-tech») is a document preparation system...
        #...for high-quality typesetting. It is most often used for...
        #...medium-to-large technical or scientific documents but it can...
        #...be used for almost any form of publishing.
        #LaTeX is not a word processor! Instead, LaTeX encourages authors...
        #...not to worry too much about the appearance of their documents...
        #...but to concentrate on getting the right content

#We can actually get access to the "axes" using the "GCA function", which...
#...means "Get Current Axes". This code allow us to get the "current...
#...axes" instance on the current "figure" matching the given keyword...
#..."args" or create one. <-IMPORTANT
    #“Current” means that it provides a handle to the last active...
    #..."axes".If there are no "axes" yet, axes will be created. If you...
    #...create two subplots, then the subplot that is created last is..
    #...the "current" one. <-IMPORTANT
    #There are lots of interesting properties of the "axes" object. For...
    #...instance:
        #We can get the grid lines
        #We can get the tick locations for both major and minor ticks.
    #Just like all "artists", an "axes" has a bunch of "children" which are...
    #:..themselves "artists".    
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates)) 
plt.plot(observation_dates, linear_data, '-o',  observation_dates, exponential_data, '-o')

x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)

ax = plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title("Exponential ($x^2$) vs. Linear ($x$) performance")

#############################################################################
                                 
#BAR CHARTS (Topic 6)    

#Instance 6.1.1

#We are creating a basic "Bar Chart" taking into account:
    #"x": is a Numpy array of values.
    #"height": a range of values withh the length of the Numpy array of values.
    #width = 0.3

#Some of the code is (from Matplotlib):
    
    #"matplotlib.pyplot.bar"
    
    #Make a bar plot. 
        #The "bars" are positioned at "x" with the given alignment. 
        #The "bars" are given by height and width. 
        #The vertical baseline is bottom (default 0).
        #Many parameters can take either a single value applying to all...
        #...bars or a sequence of values, one for each bar.

    #Syntax:
        #matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
        #Parameters (some of them):
            #x: float or array-like.
                #The "x" coordinates of the bars. See also align for the...
                #...alignment of the bars to the coordinates.
            #height: float or array-like
                #The height(s) of the bars.
            #width: float or array-like, default: 0.8
                #The width(s) of the bars.
            #bottom: float or array-like, default: 0
                #The y coordinate(s) of the bars bases.
            #align: {'center', 'edge'}, default: 'center'
                #Alignment of the bars to the x coordinates (to be specific...
                #...alignment of the bars to the "minor tick label" located...
                #..."x" coordinate. Therefore, the bar could be positioned...
                #...in the center, left edge or right edge of the "minor...
                #...tick label" located "x" coordinate.):
                    #'center': Center the base on the x positions.
                    #'edge': Align the left edges of the bars with the...
                    #..."x" positions.
                    #To align the bars on the right edge pass a negative..
                    #...width and align='edge'.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3)

#Instance 6.1.2

#We based the main code (an its concetps in "Instance 6.1.1.").

#We are creating a basic "Bar Chart" taking into account:
    #"x": is a Numpy array of values.
    #"height": a list of values
    #width = 0.3

#This examples generate the same result as the "Instance 6.1.1."
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
xvals = [1,2,3,4,5,6,7,8]
plt.bar(xvals, linear_data, width = 0.3)

#Instance 6.1.3

#We based the main code (an its concetps in "Instance 6.1.1.").

#We are creating a basic "Bar Chart" taking into account:
    #"x": is a Numpy array of values.
    #"height": a list of values
    #width = 0.2
    #align: edge

#This examples generate the almost the same result as the "Instance 6.1.1."...
#...(except fot the "width = 0.2" and the "align: edge").
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
xvals = [1,2,3,4,5,6,7,8]
plt.bar(xvals, linear_data, width = 0.2, align="edge")

#Instance 6.2

#Plot another set of bars, adjusting the new "xvals".
    #In essence, we plot a "Bar Graph N°1" (just in the center of the...
    #..."minor tick label"). Then we are going to graph another...
    #..."Bar Graph N°2" with a different dataset.
        #We can see that the center of every "bar" of the "Bar Graph N°2"...
        #...is located at the "xvals+0.3" position; therefore we are going...
        #...to see the center of every "bar" of "Bar Graph N°2" not exactly...
        #...located at the center of "minor tick label" (which is already...
        #...occupied for every "bar" of "Bar Graph N°1").
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

    #Bar Graph N°1 (blue color)
linear_data = np.array([1,2,3,4,5,6,7,8])
xvals = [1,2,3,4,5,6,7,8]
plt.bar(xvals, linear_data, width = 0.3)

    #Bar Graph N°2 (red color)
exponential_data = linear_data**2
new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3)
plt.bar(new_xvals, exponential_data, width = 0.3 ,color='red')

#Instance 6.3

#This will plot a new set of "bars" with "errorbars" using the "list"...
#...of random error values. 
    #This kind of "errorbars" allow us to see the errors (in this case...
    #...Symmetric +/- error values for all data points). In some way we...
    #...can apply this when do linear regression to contrast the "y" value...
    #...predicted by our model vs "y" real value

#Some of the code is (from Python):
    
    #"randint()"
    
    #The "randint()" method returns an integer number selected from...
    #...the specified range (both extreme values of the range included).
    
    #Syntax:
        #random.randint(start, stop) 
        #Parameters:
            #start: Required. An integer specifying at which position to...
            #...start (included).
            #stop: Required. An integer specifying at which position to end...
            #...(included).

#Some of the code is (from Matplotlib):
    
    #"matplotlib.pyplot.errorbarr"
    
    #Make a bar plot. 
        #Plot "y" versus "x" as "lines and/or markers" with attached..
        #..."errorbars".
        #"x, y" define the data locations, "xerr, yerr" define the...
        #..."errorbar" sizes. By default, this draws the data...
        #..."markers/lines" as well the "errorbars". 
                    
    #Syntax:
        #matplotlib.pyplot.barh(y, width, height=0.8, left=None, *, align='center', **kwargs)
        #Parameters (some of them):
            #x, y: float or array-like.
                #The data positions.
            #xerr, yerr: float or array-like, shape(N,) or shape(2, N)...
            #...(optional)
                #The errorbar sizes:
                    #scalar: Symmetric +/- values for all data points.
                    #shape(N,): Symmetric +/-values for each data point.
                    #shape(2, N): Separate - and + values for each bar....
                    #...First row contains the lower errors, the second..
                    #...row contains the upper errors.
                    #None: No errorbar.
                
                #Note that all error arrays should have positive values.                    
                    
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from random import randint

linear_data = np.array([1,2,3,4,5,6,7,8])
xvals = [1,2,3,4,5,6,7,8]

linear_err = [randint(0,3) for x in range(len(linear_data))] 
plt.bar(xvals, linear_data, width = 0.5, yerr=linear_err)

#Instance 6.4

#This code will plot first a set of "bars". Then, we are going to plot...
#...a second set of "bars" stacked over the first set of "bars" plotted (i.e.,..
#...the second set of "bars" is above the first a set of "bars". This means,...
#...the "bottom" parameter is not zero in the code of the second set of...
#... "bars" "matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)".
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2

xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3, color='b')
plt.bar(xvals, exponential_data, width = 0.3, bottom=linear_data, color='r')

#Instance 6.5
#In this case we are plotting "horizontal bars" stacked over another set of...
#..."horizontal bars" plotted.

#Some of the code is (from Matplotlib):
    
    #"matplotlib.pyplot.barh"
    
    #Make a horizontal bar plot.
        #The bars are positioned at "y" with the given alignment. Their..
        #...dimensions are given by "width" and "height". The horizontal...
        #...baseline is left (default 0).
        #Many parameters can take either a single value applying to all bars or a sequence of values, one for each bar.

    #Syntax:
        #matplotlib.pyplot.barh(y, width, height=0.8, left=None, *, align='center', **kwargs)
        #Parameters (some of them):
            #y: float or array-like.
                #The "y" coordinates of the bars. See also align for the...
                #...alignment of the bars to the coordinates.
            #width: float or array-like
                #The width(s) of the bars.
            #height ("ancho de barra"): float or array-like, default: 0.8
                #The height(s) of the bars.
            #left: float or array-like, default: 0
                #The "x" coordinate(s) of the left sides of the bars.
            #align: {'center', 'edge'}, default: 'center'
                #Alignment of the bars to the "y" coordinates (to be specific...
                #...alignment of the bars to the "minor tick label" located...
                #..."y" coordinate. Therefore, the bar could be positioned...
                #...in the center, left edge or right edge of the "minor...
                #...tick label" located "y" coordinate.):
                    #'center': Center the base on the "y" positions.
                    #'edge': Align the left edges of the bars with the...
                    #..."y" positions.
                    #To align the bars on the top edge pass a negative..
                    #...width and align='edge'.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2

xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height = 0.3, color='b')
plt.barh(xvals, exponential_data, height = 0.3, left=linear_data, color='r')

##########################################################################

#DEJUNKIFYING A PLOT (Topic 7)   

#Instance 7.1
#Task: Remove all the ticks (both axes), and tick labels on the Y axis
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
plt.bar(pos, popularity, align='center')
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

#Answer 7.1 (by Ramses):
    #First, it is important to clarify some definitions:
        #Ticks: are the markers used to denote the points on the axes or we...
        #...can say that the small geometrical scale lines.
        #Tick labels: are the name given to the "ticks". Or we can say that...
        #..."tick labels" are "ticks" that contain text called "Text Ticks".
        #"Axis labels" are the name given to the axes such as "X-axis" and...
        #..."Y-axis"
        
     #Sometimes we want to hide or remove the "tick marks" and "tick labels". 

     #There are different methods for hiding "tick labels":
         #Option 1: By setting the color of the "tick label" white
         #Option 2: By setting the "tick labels" to be empty
         #Option 3: By setting the label argument to be empty
                  
     #By default when we plot a graph in matplotlib, we get "ticks" in our...
     #...plot on both sides of the "axes" known as "x-axis" and "y-axis"...
     #...But sometimes we don’t want to show the "tick" marks in our plot....
     #...So in that cases, we have to make these "ticks" invisible or we...
     #...can say that we have to remove them.
     
     #By using the "tick_params()" method we can easily remove these "ticks". 
     
     #There are different methods for remove "ticks":
         #Option 1: When we want to remove "ticks" on x-axis
         #Option 2: When we want to remove "ticks" on y-axis
         #Option 3: When we want to remove "ticks" from both the axis
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
plt.bar(pos, popularity, align='center')
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
    
     #Based in what we described previously about several methods to...
     #...remove or hide "tick labels" and "ticks" we are going to choose..
     #...only one method to remove or hide "tick labels" and "ticks"...
     #...in the following lines of code:
         
         #Option #2 of Hiding "tick labels": 
             #Matplotlib remove "tick labels" by setting "tick labels" to...
             #...be empty.
             
             #By using the code "xaxis.set_ticklabels([])" and...
             #..."yaxis.set_ticklabels([])" set the "tick labels" to be empty.
             
             #This method makes the "tick labels" invisible by setting the..
             #..."tick labels" to be empty but leaves "ticks" visible.
ax = plt.gca()
ax.axes.yaxis.set_ticklabels([])

         #Option #3 of removing "ticks": 
             #Matplotlib remove ticks from both the axis.
             
             #Use the "tick_params()" method to remove the "ticks" on...
             #...both axis. In this method pass, the argument "bottom"...
             #...(which represents the "ticks" on "x-axis") and "left"...
             #...(which represents the "ticks" on "y-axis") set its...
             #...value "False".             
plt.tick_params(left=False,bottom=False)

#Answer 7.1 (by PhD):
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
plt.bar(pos, popularity, align='center')
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
    
    #Remove all the ticks (both axis), and "tick labels" on the "Y axis"...
    #...using just one line of code.
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
plt.show()

#Instance 7.2
#Task: Remove the frame of the chart.
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
plt.bar(pos, popularity, align='center')
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
    
    #Answer 7.1
ax = plt.gca()
ax.axes.yaxis.set_ticklabels([])
             
plt.tick_params(left=False,bottom=False)

#Answer 7.2 (by Ramses)
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
plt.bar(pos, popularity, align='center')
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
ax = plt.gca()
ax.axes.yaxis.set_ticklabels([])
plt.tick_params(left=False,bottom=False)

b= 0
ax.set_frame_on(b)

#Answer 7.2 (by PhD):
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
plt.bar(pos, popularity, align='center')
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
ax = plt.gca()
ax.axes.yaxis.set_ticklabels([])             
plt.tick_params(left=False,bottom=False)

    #"matplotlib.spines"
        #An "axis spine" is the line noting the data area boundaries.
        #"Spines" are the lines connecting the "axis tick marks" and...
        #...noting the boundaries of the data area. 
        
        #Other Parameters (**kwargs)
            #visible (bool)
            
        #In essence we iterate over all the spines and set their "visibility"...
        #...to "false".
for spine in plt.gca().spines.values():
    spine.set_visible(False)

#Instance 7.3
#Task: Change the bar colors to be less bright blue, make one bar, the...
#...python bar, a contrasting color, soften all labels by turning grey.
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
plt.bar(pos, popularity, align='center')
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
    
    #Answer 7.1
ax = plt.gca()
ax.axes.yaxis.set_ticklabels([])        
plt.tick_params(left=False,bottom=False)

    #Answer 7.2
b= 0
ax.set_frame_on(b)

#Answer 7.3 (by Ramses)
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

    #I establish a different color for every bar
plt.bar(pos, popularity, align='center',color=['greenyellow', 'skyblue', 'skyblue', 'skyblue', 'skyblue'])

plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
ax = plt.gca()
ax.axes.yaxis.set_ticklabels([])
plt.tick_params(left=False,bottom=False)
b= 0
ax.set_frame_on(b)

    #I establish a different color for the labels in the "y-axis"
ax.yaxis.label.set_color("grey")

#Answer 7.3 (by PhD):
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

    #I establish the same color for every bar, then I modified the color of...
    #...only the bar located in first position (i.e. the bar number "zero").
bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
bars[0].set_color('#1F77B4')

    #Soften all labels by turning grey (using the code "alpha" for...
    #...transparency).
plt.xticks(pos, languages, alpha=0.8)
plt.ylabel('% Popularity', alpha=0.8)
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
ax = plt.gca()
ax.axes.yaxis.set_ticklabels([])
plt.tick_params(left=False,bottom=False)
b= 0
ax.set_frame_on(b)

#Instance 7.4
#Task: Directly label each bar with "y axis" values, and remove the...
#..."y label" since bars are directly labeled.
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

    #Answer 7.3.1
plt.bar(pos, popularity, align='center',color=['greenyellow', 'skyblue', 'skyblue', 'skyblue', 'skyblue'])
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
    
    #Answer 7.1
ax = plt.gca()
ax.axes.yaxis.set_ticklabels([])        
plt.tick_params(left=False,bottom=False)

    #Answer 7.2
b= 0
ax.set_frame_on(b)

    #Answer 7.3.2
ax.yaxis.label.set_color("grey")

#Answer 7.4.(by Ramses)
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
popularity = [56, 39, 34, 34, 29]

    #First Step: I define the variables (x,y) that I am going to use in...
    #...the Second Step.
    #Second Step: I define a function to label each bar with "y axis" values..
    #...using a:
        #1. "for loop" to iterate over every value of the range of "x-axis"...
        #...values.
        #2. matplotlib.pyplot.text" function
    #Third Step: I plot the graph inside the function created previously in...
    #...Second Step. Then I called the function (Including the title of graph).
    #Final Step: I modify other aspects of the graph described in the...
    #...Instances 7.1, 7.2 and 7.3

    #By using "bar charts" we can easily compare the data by observing the...
    #...different heights of the bars. By default bar chart doesn’t display..
    #...value labels on each of the bars. To easy examine the exact value...
    #...of the bar we have to add value labels on them. By using the...
    #..."matplotlib.pyplot.text" method we can:
        #Add the text "s" to the "axes" at location "x, y" in data coordinates.

    #Syntax:
        #matplotlib.pyplot.text(x, y, s, fontdict=None, **kwargs)
        #Parameters (some of them):
            #x, y: float
                #The position to place the text. By default, this is in...
                #...data coordinates. The coordinate system can be...
                #...changed using the transform parameter.
            #s: str
                #The text.
            #Other Parameters: kwargsText properties.
                #color
                #horizontalalignment or ha:'center', 'right', 'left'
                #fontweight or weight: a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'.
            #Returns: Text
def addlabels(languages,popularity):
    for i in range(len(languages)):
        plt.text(i, popularity[i], popularity[i], horizontalalignment = "center",color = 'blue', fontweight = 'bold')
        
    languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
    pos = np.arange(len(languages))
    popularity = [56, 39, 34, 34, 29]
    plt.bar(pos, popularity, align='center',color=['greenyellow', 'skyblue', 'skyblue', 'skyblue', 'skyblue'])
    plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
addlabels(languages,popularity)

ax = plt.gca()
ax.axes.yaxis.set_ticklabels([])        
plt.tick_params(left=False,bottom=False)
b= 0
ax.set_frame_on(b)
ax.yaxis.label.set_color("grey")

#Answer 7.4 (by PhD):
import matplotlib.pyplot as plt
import numpy as np

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
bars[0].set_color('#1F77B4')

plt.xticks(pos, languages, alpha=0.8)
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')

for spine in plt.gca().spines.values():
    spine.set_visible(False)

    #Direct label each bar with Y axis values <--This is the main difference...#
    #...with me because it iterates over the graph and not over the "x-axis"...
    #...values.
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%', 
                 ha='center', color='w', fontsize=11)

############################################################################

#MICROTESTS - PART 1 (FOR THE ASSIGNMENT 2)

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 1 (to solve some doubts)
import numpy as np
import matplotlib.pyplot as plt

    #"Figure size" ("figsize"):
        
        #It determines the size of the "figure" (usually...
        #...in inches. This gives the amount of space the "axes" (and other...
        #...elements) have inside the "figure". The default "figure size"...
        #...is (6.4, 4.8) inch.
        
        #The native "figure size" unit in Matplotlib is inches, deriving...
        #...from print industry standards. However, users may need to...
        #...specify their "figures" in other units like centimeters or pixels.

    #If we change the "figure size" in inches, the points, lines, etc...
    #...inside of it will not change, so a larger "figure" in inches...
    #...still has the same size of the elements (points, lines, etc)....
    #...Changing the "figure" size is thus like taking a piece of paper of a...
    #...different size. For instance: doing so, would of course not change...
    #...the width of the points, lines, etc drawn with the same pen.
    
    #Dots per inches (dpi):
        #It determines how many pixels the figure...
        #...comprises. The default dpi in matplotlib is 100. 

    #Changing the "dpi" scales elements (points, lines, etc). For instance:
        #At 72 "dpi", a line of 1 point size is one pixel strong. 
        #At 144 "dpi", this line is 2 pixels strong. 
    #A larger "dpi" will therefore act like a magnifying glass. All...
    #...elements (points, lines, etc) are scaled by the magnifying power...
    #...of the lens.
    
    #Changing the Defaults using "rcParams"
        #Matplotlib's "runtime configuration" (rc)
        #Each time Matplotlib loads, it defines a "runtime configuration"...
        #...(rc) containing the default styles for every plot element...
        #...we create. This configuration can be adjusted at any time...
        #...using the "plt.rc" convenience routine.
        
# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)
# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
# Plot cosine with a blue continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
# Plot sine with a green continuous line of width 1 (pixels)
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")
# Set x limits
plt.xlim(-4.0, 4.0)
# Set x ticks
plt.xticks(np.linspace(-4, 4, 9))
# Set y limits
plt.ylim(-1.0, 1.0)
# Set y ticks
plt.yticks(np.linspace(-1, 1, 5))
# Show result on screen
plt.show()

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 2 (to solve some doubts)
import numpy as np
import matplotlib.pyplot as plt

#Subplots
    #Option 1: An "axes" (ax) is a single element added or retrieved...
    #...in a "figure" (the entire "figure") by the code "subplot". 
    #Option 2: An "axes" (ax) is a single element added or retrieved...
    #...in a "figure" (just a cell of the "figure") by the code "subplot". 
    #Option 3: Several axes (axs) are two or more elements added or...
    #...retrieved in a "figure" (several cells of the "figure") by the...
    #...code "subplots". 
    
    #In the following syntax we are going to see how to handle the "Option 3"...
    #...therefore the code is "matplotlib.pyplot.subplots".
    
    #Syntax:
    #matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
    
    #Parameters:
        #nrows, ncols: int (default: 1)
            #Number of rows/columns of the subplot grid.
        #sharex, sharey: bool or {'none', 'all', 'row', 'col'}, default: False
            #Controls sharing of properties among x (sharex) or y (sharey)..
            #...axes:
                #True or 'all': x- or y-axis will be shared among all subplots.
                #False or 'none': each subplot x- or y-axis will be...
                #...independent.
                #'row': each subplot row will share an x- or y-axis.
                #'col': each subplot column will share an x- or y-axis.
                
                #When subplots have a shared "x-axis" along a column,...
                #...only the x tick labels of the bottom subplot are created...
                #...Similarly, when subplots have a shared "y-axis" along...
                #...a row, only the y tick labels of the first column...
                #...subplot are created.
        #gridspec_kw: dict (optional)
            #Dict with keywords passed to the "GridSpec" constructor...
            #...used to create the grid the subplots are placed on.

    #The names "ax" and pluralized "axs" are preferred over the term "axes"...
    #...because for the latter it's not clear if it refers to a single "Axes"..
    #...instance or a collection of these.

    #Returns:
        #fig: Figure
        #ax: "axes.Axes" or array of "Axes".
            #"ax" can be either a single "Axes" object or an array of...
            #..."Axes" objects if more than one subplot was created...
            #...The dimensions of the resulting array can be controlled...
            #...with the squeeze keyword, see above.

        #Typical idioms for handling the return value are:
            # using the variable "ax" for single a Axes
fig, ax = plt.subplots()
            # using the variable "axs" for multiple Axes
fig, axs = plt.subplots(2, 2)
            # using tuple unpacking for multiple Axes
fig, (ax1, ax2) = plt.subplots(1, 2)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    #MICRO TEST 2.1
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create just a "figure" and only one "axes"
fig, ax = plt.subplots()
ax.plot(x, y, "red",".")
ax.set_title('Simple plot')

    #MICRO TEST 2.2
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)
    
# Create "two axes" and unpack the output array immediately
    #Number of rows/columns of the subplot grid.
        #nrows = 1 
        #ncols = 2
    #Sharing of properties among y (sharey) axes; ("y-axis" will be...
    #...shared among all subplots.)
    #One axes (ax1) is a "line plot" and the other axes (ax2)...
    #...contain a "scatter plot".
        #I use "f" for "figure".
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

    #MICRO TEST 2.2.1
# First create some toy data:
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
    
# Create "two axes".
    #Number of rows of the subplot grid. When stacking in one direction...
    #...only, the returned "axs" is a "1D numpy array" containing the..
    #...list of created "Axes".
        #nrows = 2
    #One axes "axs[0]" is a "positive line plot" (x, y) and the other...
    #...axes "axs[1]" is a "negative line plot" (x, -y)
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[1].plot(x, -y)

    #MICRO TEST 2.2.2
# First create some toy data:
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

#If we are creating just a few "Axes", it's handy to unpack them...
#...immediately to dedicated variables for each "Axes". That way, we can...
#...use "ax1", "ax2", etc. instead of the more verbose "axs[0]".

# Create "two axes" and unpack the output array immediately
    #Number of rows of the subplot grid. When stacking in one direction...
    #...only, the returned "axs" is a "1D numpy array" containing the..
    #...list of created "Axes".
        #nrows = 2
    #One axes "ax1" is a "positive line plot" (x, y) and the other...
    #...axes "ax2" is a "negative line plot" (x, -y)
fig, (ax1,ax2) = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
ax1.plot(x, y)
ax2.plot(x, -y)

    #MICRO TEST 2.2.3
# First create some toy data:
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# Create "four axes".
    #Number of rows/columns of the subplot grid.
        #nrows = 2 
        #ncols = 2
    #One axes has the coordinates 0,0
    #One axes has the coordinates 0,1
    #One axes has the coordinates 1,0
    #One axes has the coordinates 1,1
    
    #We have to set parameters for each subplot; therefore, was handy to...
    #...iterate over all "subplots" in a 2D grid using for "ax" in "axs.flat"
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Axis [0, 0]')

axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0, 1]')

axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')

axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1, 1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

    #MICRO TEST 2.3
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create four polar axes and access them through the returned array
    #Number of rows/columns of the subplot grid.
        #nrows = 2 
        #ncols = 2
    #Two axes (axs) are a "line plot" and the other two axes (axs) are...
    #...contain a "scatter plot".
        #I use "fig" for "figure".
        #I use "axs" for axes.
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

    #MICRO TEST 2.4
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create "four axes" and unpack the output array immediately
    #Number of rows/columns of the subplot grid.
        #nrows = 1 
        #ncols = 4
    #Sharing of properties among y (sharey) axes; ("y-axis" will be...
    #...shared among all axes.)
    #One axes (ax1) is a "line plot"
    #One axes (ax2) is a "scatter plot"
    #One axes (ax3) is a "line plot"
    #One axes (ax4) is a "scatter plot"
        #I use "fig" for "figure".
        #I use "ax1, ax2, ax3 and ax4" for axes.
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, sharey=True)
ax1.plot(x, y)
ax2.scatter(x, y)
ax3.plot(x, y)
ax4.scatter(x, y)

    #MICRO TEST 2.5
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create "four subplots" and unpack the output array immediately
    #Number of rows/columns of the subplot grid.
        #nrows = 4 
        #ncols = 1
    #Sharing of properties among x (sharex) axes; ("x-axis" will be...
    #...shared among all subplots.)
    #One axes (ax1) is a "line plot"
    #One axes (ax2) is a "scatter plot"
    #One axes (ax3) is a "line plot"
    #One axes (ax4) is a "scatter plot"
        #I use "fig" for "figure".
        #I use "ax1, ax2, ax3 and ax4" for axes.
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True)
ax1.plot(x, y)
ax2.scatter(x, y)
ax3.plot(x, y)
ax4.scatter(x, y)

    #MICRO TEST 2.6
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create "four subplots" and unpack the output array immediately
    #It is important to know that if we are going to use an several...
    #...subplots we can arrange them in the following patterns:
        #Single Line (i.e. several subplots in the same single row or...
        #...several subplots in the same single column).
        #Array (i.e. several subplots per row and per column).
    #Number of rows/columns of the subplot grid.
        #nrows = 2 
        #ncols = 2
    #Sharing of properties among y (sharey: row) axes; (each subplot row...
    #...will share an y-axis.)
    #One axes (ax1) is a "line plot"
    #One axes (ax2) is a "scatter plot"
    #One axes (ax3) is a "line plot"
    #One axes (ax4) is a "scatter plot"
        #I use "fig" for "figure".
        #I use "ax1, ax2, ax3 and ax4" for axes.
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey='row')
ax1.plot(x, y)
ax2.scatter(x, y)
ax3.plot(x, y)
ax4.scatter(x, y)

    #MICRO TEST 2.7
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create "four subplots" and unpack the output array immediately
    #It is important to know that if we are going to use an several...
    #...subplots we can arrange them in the following patterns:
        #Single Line (i.e. several subplots in the same single row or...
        #...several subplots in the same single column).
        #Array (i.e. several subplots per row and per column).
    #Number of rows/columns of the subplot grid.
        #nrows = 2 
        #ncols = 2
    #Sharing of properties among y and x (sharex='all', sharey='all') axes;...
    #...(x and y-axis will be shared among all subplots)
    #One axes (ax1) is a "line plot"
    #One axes (ax2) is a "scatter plot"
    #One axes (ax3) is a "line plot"
    #One axes (ax4) is a "scatter plot"
        #I use "fig" for "figure".
        #I use "ax1, ax2, ax3 and ax4" for axes.    
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='all', sharey='all')
ax1.plot(x, y)
ax2.scatter(x, y)
ax3.plot(x, y)
ax4.scatter(x, y)

    #Also , if we print the "axes" ("ax1, ax2, ax3 and ax4") we can see...
    #...clearly the location of every subplot in the "figure"
      
    #Also , if we print the type of "axes" "ax1, ax2, ax3 and ax4" we can..
    #...see clearly that they are subplot in the "figure" 
A = type(ax3)
print(A)
print(ax1)
print(ax2)
print(ax3)
print(ax4)

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 3 (to solve some doubts)

#Managing multiple "figures" in pyplot. The main ideas are the followings:
    #1. Figures" are identified via a "figure number" that is passed to...
    #..."figure". The "figure" with the given number is set as...
    #..."current figure". Additionally, if no "figure" with the number...
    #...exists, a new one is created.
    
    #2. It discourages working with multiple "figures" in pyplot...
    #...because managing the "current figure" is cumbersome and error-prone... 
    #...Instead, its recommended to use the object-oriented approach and...
    #...call methods on "Figure" and "Axes" instances.

    #MICRO TEST 3.1
#In this instance ww are going to create two figures:
    #First, I create the data.
    #Then I create a "Figure" identified via a "figure number", in this case...
    #...the number "1".
        #In this "figure" number "1" we have a subplot grid of:
            #nrows = 2 
            #ncols = 1
            #index = 1
        #After that, we plot inside this "figure" number "1" the graph.   
        #Then, in this "figure" number "1" we have another "subplot" grid...
        #...(this new "subplot" will overlap the first "subplot" [of the...
        #...same "figure" number "1"], the "subplot" [and its "axes"]...
        #...previously created, will be removed) of:
            #nrows = 2 
            #ncols = 1
            #index = 2
         #After that, we plot inside this "figure" number "1" another graph  
    #Then I create a "Figure" identified via a "figure number", in this case...
    #...the number "2".    
        #After that, we plot inside this "figure" number "2" another graph. 
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)

    #"Figure" number "1" with the first subplot.
        #If we contrast the position of this current "subplot" (211) vs the...
        #...following subplot (212) we are going to see that the only...
        #...obvious difference is the "index" (which is the position that...
        #...a "subplot" take on a grid with "nrows and ncols").
            #We can see that when we print the current axes "print(ax)"
plt.figure(1)
plt.subplot(211)
plt.plot(t, s1,'s')
ax = plt.gca()
ax.set_xticklabels([])
print(ax)

    #"Figure" number "1" with the new subplot.
        #If we contrast the position of this current "subplot" (212) vs the...
        #...previous subplot (211) we are going to see that the only...
        #...obvious difference is the "index" (which is the position that...
        #...a "subplot" take on a grid with "nrows and ncols").
            #We can see that when we print the current axes "print(ax)"
plt.subplot(212)
plt.plot(t,1*s1,'s')
ax = plt.gca()
ax.set_xticklabels([])
print(ax)

    #"Figure" number "2" with the first subplot for this "Figure".
plt.figure(2)
plt.plot(t, s2,"s")
ax = plt.gca()
ax.set_xticklabels([])
print(ax)

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 4 (to solve some doubts)

#Subplot
    #Add an Axes to the current "figure" or retrieve an existing "Axes"...
    #...It is important to say:
    #Option 1: An "axes" (ax) is a single element added or retrieved...
    #...in a "figure" (the entire "figure") by the code "subplot". 
    #Option 2: An "axes" (ax) is a single element added or retrieved...
    #...in a "figure" (just a cell of the "figure") by the code "subplot". 
    #Option 3: Several axes (axs) are two or more elements added or...
    #...retrieved in a "figure" (several cells of the "figure") by the...
    #...code "subplots". 
    
    #In the following syntax we are going to see how to handle the "Option 1"...
    #...and "Option 2"; therefore, the code is "matplotlib.pyplot.subplot".
    
    #Call signatures:
        #subplot(nrows, ncols, index, **kwargs)
        #subplot(pos, **kwargs)
        #subplot(**kwargs)
        #subplot(ax)
        
    #Syntax:
    #matplotlib.pyplot.subplot(*args, **kwargs)
    
    #Parameters:
        #*args: int, (int, int, index), or SubplotSpec, default: (1, 1, 1)
            #The position of the subplot described by one of:
                #1.Three integers (nrows, ncols, index): The "subplot" will...
                #...take the index position on a grid with nrows rows and...
                #...ncols columns (i.e. "nrows" and "ncols" are used to...
                #...notionally split the "figure" into "nrows * ncols"):
                    #1.1.index starts at 1 in the upper left corner and...
                    #...increases to the right. 
                    #1.2.index can also be a two-tuple specifying the...
                    #...(first, last) indices (1-based, and including last)...
                    #...of the subplot, e.g.,...
                    #..."fig.add_subplot(3, 1, (1, 2))" makes a subplot that...
                    #...spans the upper 2/3 of the figure.
                #2.A 3-digit integer: The digits are interpreted as if...
                #...given separately as three single-digit integers, i.e....
                #..."fig.add_subplot(235)" is the same as...
                #..."fig.add_subplot(2, 3, 5)". Note that this can only...
                #...be used if there are no more than 9 subplots.
    #Returns:
        #"axes.SubplotBase", or another subclass of "Axes"
            #The "axes" of the "subplot". The returned "axes" base class...
            #...depends on the projection used. The returned "axes" is then...
            #...a "subplot" subclass of the base class. <--IMPORTANT

    #Creating a new "Axes" will delete any pre-existing "Axes" that...
    #...overlaps with it beyond sharing a boundary.
        #If you do not want this behavior, use the "Figure.add_subplot"...
        #....method or the "pyplot.axes" function instead.
 
    #MICRO TEST 4.1
import matplotlib.pyplot as plt
    #First, I plot a line; implicitly we are creating a "subplot(111)"
plt.plot([1, 2, 3])
    #Now create a "subplot" (in the same "figure") which represents the...
    #...top plot of a grid (grid with 2 rows and 1 column). Since this...
    #..."subplot" will overlap the first plot (of the same "figure"), the...
    #...plot (and its "axes") previously created, will be removed
plt.subplot(211)

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 6 (to solve some doubts)

#The "pyplot" interface allows us to use "setp" and "getp" to set and...
#...get object properties respectively, as well as to do introspection on...
#...the object.

    #MICRO TEST 6.1
# First create some toy data:
line, = plt.plot([1, 2, 3])
plt.setp(line, linestyle='--')

    #If we want to know the valid types of arguments, we can provide...
    #...the name of the property we want to set without a value.
    
    #In this case, we are interested in the valid types of arguments of...
    #...line (to be specific, the 'linestyle').
plt.setp(line, 'linestyle')

    #MICRO TEST 6.2
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

    #Returns the "value" or "all the attribute/value pairs" of a given..
    #...attribute.
    
    # Create just a "figure" and only one "axes". Then we are going to look...
    #...for all the attributes of the "axes" created.
fig, ax = plt.subplots()
ax.plot(x, y, "red",".")
ax.set_title('Simple plot')

plt.getp(ax)

##############################################################################
#ASSIGNMENT 2

#For this assignment, you must:
    
    #Step 1: Read the documentation and familiarize yourself with the...
    #...dataset then write some python code which returns a line graph of the...
    #...record high and record low temperatures by day of the year over...
    #...the period 2005-2014. The area between the record high and record...
    #...low temperatures for each day should be shaded.
    
        #Step 1.1: I am going to create a "line graph" for the year 1788...
        #...This graph will show us only the record high and...
        #...record low temperatures by day of the year over 1788.
        
        #Step 1.2: I am going to fill the area between the "line graphs"...
        #...of the record high and record low temperatures by day of the..
        #...years 1788.
    
    #Step 2: Overlay a scatter of the 2015 data for any points (highs and...
    #... lows) for which the ten year record (2005-2014) record high or...
    #...record low was broken in 2015.
    
        #Step 2.1: I am going to create a "Scatterplot" for the year 1789...
        #...above the "line graphs" created in the Step 1.2 only for the...
        #...points (record high or record low) that were broken in 1789.
    
    #Step 3: Watch out for leap days (i.e. February 29th), it is reasonable...
    #...to remove these points from the dataset for the purpose of this...
    #...visualization.
    
    #Step 4: Make the visual nice! Leverage principles from the first module...
    #...in this course when developing your solution. Consider issues such as...
    #...legends, labels, and chart junk.

    #The data you have been given is near Ann Arbor, Michigan,...
    #...United States, and the stations the data comes from are shown on the...
    #...map below.

#Step 1:
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

    #1.1. I read the CSV file of the year 1788 and 1789.
        #It is important to say that before apply the code "pd.read_csv"...
        #...I add a headrow (titles) manually in the "MS Excel csv dataset"...
        #...because when we read the original "MS Excel csv dataset"...
        #...(without my modification), the headrow of the printed dataframe...
        #...was a piece of the data.
df1788V2 = pd.read_csv('1788-V2.csv')

df1789V2 = pd.read_csv('1789-V2.csv')

    #1.2. I change the name of columns of the dataframe of the year 1788...
    #...and 1789.
df1788V2 = df1788V2.rename(columns={'A':'id'})    
df1788V2 = df1788V2.rename(columns={'B':'date'})    
df1788V2 = df1788V2.rename(columns={'C':'element'})    
df1788V2 = df1788V2.rename(columns={'D':'value'})    

df1789V2 = df1789V2.rename(columns={'A':'id'})    
df1789V2 = df1789V2.rename(columns={'B':'date'})    
df1789V2 = df1789V2.rename(columns={'C':'element'})    
df1789V2 = df1789V2.rename(columns={'D':'value'})   

    #1.3. I drop some columns of the dataframe of the year 1788 and 1789...
    #...because they do not have useful data.
df1788V2.drop(["Unnamed: 4","Unnamed: 5","E","Unnamed: 7"],inplace=True, axis=1)    

df1789V2.drop(["Unnamed: 4","Unnamed: 5","E","Unnamed: 7"],inplace=True, axis=1)     

    #1.4. I drop some rows of the dataframe of the year 1789. To be specific...
    #...I drop rows that have the label "PRCP" of the column "element".
        #1.4.1. Using Regex I replace the "text" of some cells that belong...
        #...to the same column for a "blank spaces".
        #1.4.2. Then, using Regex I transform the "blank spaces" of every ...
        #...cell in the same column into a "NaN value".
        #1.4.3. Then, I dropped the rows that contain "NaN value".
df1789V2['element']= df1789V2['element'].replace('PRCP','',regex=True)
df1789V2 = df1789V2.replace([''],np.nan)
df1789V2 = df1789V2.dropna()    
 
    #1.5. I convert to "Datetime" all the cells of dataframe that belong...
    #...to the column "date" of the dataframes of the year 1788 and 1789.

    #We are converting an argument to "Datetime". This function converts a...
    #... scalar, array-like, Series or DataFrame/dict-like to a pandas..
    #...datetime object.
    
    #The syntax is: 
        #pandas.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=None, format=None, exact=True, unit=None, infer_datetime_format=False, origin='unix', cache=True)[source]
        
        #Some of the Parameters are:
            #arg: int, float, str, datetime, list, tuple, 1-d array, Series,...
            #...DataFrame/dict-like. If a DataFrame is provided, the...
            #...method expects minimally the following columns: "year",...
            #..."month", "day".
            
            #yearfirst: bool (default False). Specify a date parse order if...
            #...arg is str or is list-like. If True, parses dates with the...
            #...year first, e.g. "10/11/12" is parsed as 2012-11-10.
            
                #"True" is not strict, but will prefer to parse with year...
                #...first.
                
            #format: str (default None).
                #The "strftime" to parse time, e.g. "%d/%m/%Y".
df1788V2["date"] = pd.to_datetime(df1788V2["date"],yearfirst=True,format='%Y%m%d')

df1789V2["date"] = pd.to_datetime(df1789V2["date"],yearfirst=True,format='%Y%m%d')


    #1.6. I drop the rows of february/29 of the dataframe of the year 1788.
df1788V2 = df1788V2.drop(labels=[233, 235, 237, 239], axis=0)

print(df1788V2) 
print("\n")   
print(df1789V2)  
print("\n")   

    #1.7. I apply "groupby" by "date". Then I apply "Aggregation" to...
    #...process the data (to be specific, we are going to apply two 
    #..."functions" (Numpy "max" and "min" value) to the grouped...
    #...dataframe and return a single row per dataframe grouped in...
    #...this case "date" is the dataframe/group ("agg()" returns a...
    #...single value per column, so one row per group).
    
        #The step 1.7 apply for the dataframes of the year 1788 and 1789.
dfnew1788 = df1788V2.groupby("date").agg({"value":(np.max,np.min)})
    
dfnew1789 = df1789V2.groupby("date").agg({"value":(np.max,np.min)})

    #1.8. I reset the index of the dataframe to make easy the process of...
    #...choosing the values for the "x-axis" and "y-axis" of the...
    #...line plot.
        #Also I rename the columns to make easy the process of choosing...
        #...the values for the "x-axis" and "y-axis" of the line plot.
dfnew1788 = dfnew1788.reset_index()
dfnew1788.columns = ['date', 'max', 'min']
print (dfnew1788)  
print("\n")         
    
dfnew1789 = dfnew1789.reset_index() 
dfnew1789.columns = ['date', 'max', 'min']   
print (dfnew1789)  
print("\n")       

    #1.9. Do the graph of 1788 and 1789 (Option #1)
        #There are various ways to plot multiple sets of data. The most...
        #...straight forward way is just to call plot multiple times.
            #In this case I am able to see all the graphs that I want...
            #...in the same "axes" because I put at the end of both graphs..
            #...the code "ax=ax" (i.e. to see all the graphs that I want..
            #...in the same "axes").
                #First, I plot either data points of 1788 ("max" and...
                #..."min" temperatures) and as a consequence both lines were...
                #...plotted in the same "axes" (i.e. 2 lines)
                #Second, I plot either data points of 1789 ("max" and...
                #..."min" temperatures) and as a consequence both lines were...
                #...plotted in the same "axes". (i.e. 2 lines)
                #As third option (not mandatory), I also can plot either...
                #...data points of 1788 and 1789 ("max" and "min" temperatures) and as a consequence both lines were...
                #...plotted in the same "axes". (i.e. 4 lines)
            
            #If both x and y are 2D, they must have the same shape. 
            #If only one of them is 2D with shape (N, m) the other must...
            #...have length N and will be used for every data set m.
            
            #Since I am printing with the graphical backend as "automatic"...
            #...which allows me to plot the graph in a different window...
            #...from "Sypder" (ideally for making zoom, move the graph, etc)..
            #...instead of use the graphical backend as "inline" which...
            #...allows me to plot the graph in the "Sypder's window"...
            #...(which does not allow me to apply zoom or move the graph,...
            #..etc); therefore, I need to use at then of each graph the...
            #...code "plt.show()" <--IMPORTANT
plt.figure()
ax = plt.gca()
dfnew1788.plot(kind='line',x='date',y="max",ax=ax)
dfnew1788.plot(kind='line',x='date',y="min",ax=ax)
plt.show()

ax = plt.gca()
dfnew1789.plot(kind='line',x='date',y="max",ax=ax)
dfnew1789.plot(kind='line',x='date',y="min",ax=ax)
plt.show()

            #Printing the datatype poised in the dataframe (just for check)
qqq = dfnew1789.dtypes
print(qqq)

    #1.10. Filling the graph of 1788 (maximun and minimum values).                              
       #First, we change the datatype of the column "date", from...
       #..."datetime64[ns]" to "str"
       #Second: I create the future positions of every tick in x-axis...
       #...through  a "range" code (star, finish, step).
dfnew1788["date"] = dfnew1788["date"].dt.strftime("%m/%d")
xticks = np.arange(0, 365, 31)

       #Third, I establish the "figure", the "axes" (in this case the current...
       #...axes).
       #Fourth: I plot the graphs (upper and lower lines) and after that I...
       #...plot the fill between both graphs.
       #Fifth: I establish the "ticks" previously created (in the Second Step...
       #...), then we set the "tick labels", and after that we modify the...
       #...the rotation of the "tick labels".
ax = plt.gca()
dfnew1788.plot(kind='line',x='date',y="max",ax=ax)
dfnew1788.plot(kind='line',x='date',y="min",ax=ax)
plt.fill_between(dfnew1788["date"],dfnew1788["max"],dfnew1788["min"], facecolor='green', alpha=0.30,linewidth=8,linestyle='-')
plt.show()

ax.set_xticks(xticks)
ax.set_xticklabels(['January','February','March','April','May',"June","July","August","September","October","November","December"])
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(90)

    #1.11. I do for 1789 datapoints what I did for 1788 in the substep 1.10 
dfnew1789["date"] = dfnew1789["date"].dt.strftime("%m/%d")
xticks = np.arange(0, 365, 31)

ax = plt.gca()
dfnew1789.plot(kind='line',x='date',y="max",ax=ax)
dfnew1789.plot(kind='line',x='date',y="min",ax=ax)
plt.fill_between(dfnew1789["date"],dfnew1789["max"],dfnew1789["min"], facecolor='yellow', alpha=0.30,linewidth=8,linestyle='-')
plt.show()

ax.set_xticks(xticks)
ax.set_xticklabels(['January','February','March','April','May',"June","July","August","September","October","November","December"])
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(90)

#Step 2:
    #I plot a mix of:
        #The "two lines plots" (maximum and minimum temperatures for the year...
        #...of 1788)
        #The "fill_between" the two lines plots" of maximum and minimum...
        #...temperatures for the year of 1788)
        #A scatterplot of any points of temperature (highs and lows) for...
        #...the year 1789 for which the 1788 record high or record low..
        #...was broken in 1789.
DfScatterMax = dfnew1789[dfnew1789['max'] > dfnew1788['max']] 
print (DfScatterMax)  

DfScatterMin = dfnew1789[dfnew1789['min'] < dfnew1788['min']]  
print (DfScatterMin)
        #two lines plots" (maximum and minimum temperatures for the year...
        #...of 1788)
xticks = np.arange(0, 365, 31)
ax = plt.gca()
dfnew1788.plot(kind='line',x='date',y="max",ax=ax)
dfnew1788.plot(kind='line',x='date',y="min",ax=ax)
        #The "fill_between" the two lines plots" of maximum and minimum...
        #...temperatures for the year of 1788)
plt.fill_between(dfnew1788["date"],dfnew1788["max"],dfnew1788["min"], facecolor='yellow', alpha=0.30,linewidth=8,linestyle='-')
        #A scatterplot of any points of temperature (highs and lows) for...
        #...the year 1789 for which the 1788 record high or record low..
        #...was broken in 1789.
colors ='green'
plt.scatter(DfScatterMax["date"], DfScatterMax["max"], s=3, c=colors)
plt.scatter(DfScatterMin["date"], DfScatterMin["min"], s=3, c=colors)
plt.show()
        #Setting and labeling ticks of x-axis.
ax.set_xticks(xticks)
ax.set_xticklabels(['January','February','March','April','May',"June","July","August","September","October","November","December"])
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(90)

#To Do (RMDLC):
    #1.11. Put the title, labels X and Y, colors, type of lines, legend,
    #... ticks, color, background, linewidth, linestyle, labels on the...
    #...graph, legend, etc (based in the peer-graded assignment).
    #1.12. Why there is a surpluss after december in 1788 and 1789?
    #1.13. Why does "1789" appears only once in the "x-axis" and 1788 appears...
        #...several times?
    #1.14. See al graphs at the same time (in different squares = the same...
    #...columns but in different rows). Creating a function to plot a final..
    #...graph?

#######################################################################

#MICROTESTS - PART 2 (FOR THE ASSIGNMENT 2)

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 7 (to solve some doubts)

#Comments of data type (datetime64[ns])
    
    #It is important to be aware of the type of data that we are going to...
    #...use when we do the "fill between" curves method. This "Matplotlib"...
    #...code consider mandatory use "array" (i.e. the use of "Numpy") or...
    #..."scalar":
        #x: array (length N)
        #y1: array (length N) or scalar
        #y2: array (length N) or scalar
        
    #In this case the datapoints of my dataframe show the following datatypes:
        #Datatype of column of "Date": "datetime64[ns]"
        #Datatype of column of "max" (temperature): "int64"
        #Datatype of column of "min" (temperature): "int64"
    
    #Due to the fact that the datatype of my "x-axis" "Date" is...
    #..."datetime64[ns]" and also as away to avoid the following message of..
    #..."TypeError" (i.e. problems for the input data type) we need to...
    #...change its datatype:
        #ufunc "isfinite" not supported for the input types, and the...
        #....inputs could not be safely coerced to any supported types...
        #...according to the casting rule "safe"
        
    #We are going to convert the datatype of the column "date" from..
    #..."datetime64[ns]" (which is "datetime" format) to "string" which is a...
    #..."object" datatype.
    
    #The "NumPy" library´s important topics (that revealed that when we talk...
    #...about "array" we are talking about "Numpy" arrays) - Part 1:
        #Contains multidimensional "array" and "matrix" data structures.
        #Gives you an enormous range of fast and efficient ways of...
        #...creating "arrays" and manipulating numerical data inside them. 
        #While a "Python list" can contain different data types within a...
        #...single list, all of the elements in a "NumPy array" should be...
        #...homogeneous (the mathematical operations that are meant to be...
        #...performed on arrays would be extremely inefficient if the...
        #...arrays weren’t homogeneous).
        #NumPy uses much less memory to store data and it provides a...
        #...mechanism of specifying the data types. This allows the code to...
        #...be optimized even further.
        #Array: is a central data structure of the NumPy library. It is a...
        #...grid of values and it contains information about the raw data,..
        #...how to locate an element, and how to interpret an element. 
            #It has a grid of elements that can be indexed in various ways. 
            #The elements are all of the same type, referred to as the...
            #...array dtype.

    #The "NumPy" library´s important topics (that revealed that when we talk...
    #...about "array" we are talking about "Numpy" arrays) - Part 2:
        #An "ndarray" is a (usually fixed-size) multidimensional...
        #...container of items of the same type and size.
        #The number of dimensions and items in an array is defined by its...
        #...shape, which is a tuple of "N" non-negative integers that...
        #...specify the sizes of each dimension. The type of items in the...
        #...array is specified by a separate data-type object (dtype),..
        #...one of which is associated with each "ndarray".

    #The "NumPy" library´s important topics (that revealed that when we talk...
    #...about "array" we are talking about "Numpy" arrays) - Part 3:
        #The data type of dates in Numpy is called "datetime64", so named...
        #...because "datetime" is already taken by the Python standard library.

#In this micro test I change (erroneously in concept) the data type of...
#...the "datetime" to "float".
    #Work for I handle data (base, y1, y2)
    #Does not work correctly for "dtype" (float)    
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np    

df1789V222 = dfnew1789.copy() 
plt.figure()

ax = plt.gca()
base1=df1789V222["date"]
y1=df1789V222["max"]
y2=df1789V222["min"]

df1789V222["date"] = np.array(df1789V222["date"], dtype=float)
base2=df1789V222["date"]

plt.plot(base1, y1,"r-")
plt.plot(base1, y2, "g--")
plt.show()

plt.fill_between(base2,y1,y2, facecolor='blue', alpha=0.25)

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 8 (to solve some doubts)

#In this micro test I change the data type of the "datetime" to "str" and..
#...alsoI change (erroneously in concept) the data type of...
#...the "datetime" to "float" and "int".
    #Work for I handle data (base, y1, y2)
    #Does work correctly for "dtype" (str)
    #Does not work correctly for "dtype" (float / int)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1789V333 = dfnew1789.copy() 
plt.figure()

df1789V333["date"] = np.array(df1789V333["date"], dtype=str)
print(df1789V333["date"])

plt.fill_between(df1789V333["date"],df1789V333["max"],df1789V333["min"], facecolor='blue', alpha=0.25)

df1789V333["date"] = np.array(df1789V333["date"], dtype=int)
print(df1789V333["date"])

plt.fill_between(df1789V333["date"],df1789V333["max"],df1789V333["min"], facecolor='blue', alpha=0.25)

df1789V333["date"] = np.array(df1789V333["date"], dtype=float)
print(df1789V333["date"])

plt.fill_between(df1789V333["date"],df1789V333["max"],df1789V333["min"], facecolor='blue', alpha=0.25)

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 9 (to solve some doubts)

#In this micro test I change the data type of the "datetime" to "str".

    #The datetime default format is: YYYY - MM - DD. 
        #Changing the datetime format changes what order each date field is...
        #...arranged. 
        #"dt.strftime()" changes the data-type of the specified column to...
        #...an object(string)
    #Work for I handle data (base, y1, y2)
    #Does work correctly for "dtype" (str); in this case I change the...
    #...datatype from "datetime64[ns]" to "str"
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1789V444 = dfnew1789.copy() 
df1789V444["date"] = df1789V444["date"].dt.strftime("%m/%d")
print(df1789V444["date"])
plt.figure()

plt.fill_between(df1789V444["date"],df1789V444["max"],df1789V444["min"], facecolor='red', alpha=0.25,linewidth=8,linestyle='--')

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 10 (to solve some doubts)

#Printing the label of the "x-axis". In addition, we set "ticklabels" of the...
#..."x-axis".
    #Only applying rotation of 45° degrees
    #I failed because there are a lot tick labels and as a consequence we...
    #...are not able to see them in a clear way.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1789V555 = dfnew1789.copy() 
df1789V555["date"] = df1789V555["date"].dt.strftime("%m/%d")
plt.figure()

plt.fill_between(df1789V555["date"],df1789V555["max"],df1789V555["min"], facecolor='green', alpha=0.74,linewidth=8,linestyle='-')
plt.xlabel('Date')

x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 11 (to solve some doubts)

#Printing the label of the "x-axis". In addition, we set "ticklabels" of the...
#..."x-axis".
    #Setting the ticklabels of "x-axis" with the numbers of 2,4,6,8,10.
    #THen applying rotation of 45° degrees.
    #I failed because there are a lot tick labels and as a consequence we...
    #...are not able to see them in a clear way.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1789V777 = dfnew1789.copy() 
df1789V777["date"] = df1789V777["date"].dt.strftime("%m/%d")
plt.figure()
ax = plt.subplot()

plt.fill_between(df1789V777["date"],df1789V777["max"],df1789V777["min"], facecolor='yellow', alpha=0.80,linewidth=8,linestyle='-')
plt.xlabel('Date')

ax.set_xticklabels([2, 4, 6, 8, 10])

x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)
    
#//////////////////////////////////////////////////////////////////////
#MICRO TEST 12 (to solve some doubts)

#Setting the ticklabels of "x-axis" with the numbers of 2,4,6,8,10.
    #I failed because the tick labels do not match in a proper way the...
    #..graphs's points.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure()
ax = plt.subplot()
ax.set_xticklabels([2, 4, 6, 8, 10])
x = [1, 2, 3, 4, 5]
y = [2.5, 0.6, 4.9, 3, 6]


plt.plot(x, y,"r-")

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 13 (to solve some doubts)

#Setting the ticklabels of "x-axis" with the labels "G1","G2","G3","G4","G5"
    #I failed because the tick labels do not appear in the graph because...
    #...they were set in a incorrect way.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Defining data
x = [1, 2, 3, 4, 5]
y = [2.5, 0.6, 4.9, 3, 6]
N = 5
ind = np.arange(N) 
labels=["G1", "G2", "G3", "G4", "G5"]

#Plotting
plt.figure()
ax = plt.subplot()
ax.set_xticks(ind, labels)

plt.plot(x, y,"g-")

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 14 (to solve some doubts)  

#Setting the ticks of "x-axis" (i.e., position of ticks)
#Setting the ticklabels of "x-axis" with the labels "G1","G2","G3","G4","G5"...
#...in the position described previously.
    #I accomplish the objective (the ticks were set in the right positions...
    #...and labeled in a correct way).
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2.5, 0.6, 4.9, 3, 6]

plt.figure()
ax = plt.subplot()
ax.set_xticks([1.0,2.0,3.0,4.0,5.0])
ax.set_xticklabels(['G1', 'G2', 'G3', 'G4', 'G5'])

plt.plot(x, y,"r-")

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 15 (to solve some doubts)

#Printing the label of the "x-axis". 
#Setting the ticks of "x-axis" (i.e., position of ticks)
#Setting the ticklabels of "x-axis" with the labels "G1","G2","G3","G4","G5"...
#...in the position described previously.
    #I failed because the tick labels do not appear cleary in the graph ...
    #...because they were set in a incorrect way.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1789V777 = dfnew1789.copy() 
df1789V777["date"] = df1789V777["date"].dt.strftime("%m/%d")
plt.figure()
ax = plt.subplot()
ax.set_xticks([1.0,2.0,3.0,4.0,5.0])
ax.set_xticklabels(['G1', 'G2', 'G3', 'G4', 'G5'])

plt.fill_between(df1789V777["date"],df1789V777["max"],df1789V777["min"], facecolor='yellow', alpha=0.80,linewidth=8,linestyle='-')
plt.xlabel('Date')

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 16 (to solve some doubts)

#Comments of ticks on "x-axis
    
    #It is important to take into account that the best way to handle and...
    #...modify the ticks on "x-axis is the following:
        #Step #1: Set the ticks (i.e. we set or establish the location of...
        #...the ticks). To do that we have the following two options:
            #Option 1:"matplotlib.axes.Axes.set_xticks"
                #Syntax: Axes.set_xticks(ticks, labels=None, *, minor=False, **kwargs)
                    #Set the xaxis' tick locations and optionally labels.
                #Parameters (some of them):
                    #ticks: list of floats
                        #List of tick locations.
                    #labels: list of str, optional
                        #List of tick labels. If not set, the labels show...
                        #...the data value.
            #Option 2:"matplotlib.pyplot.xticks"
                #Syntax: matplotlib.pyplot.xticks(ticks=None, labels=None, **kwargs)
                    #Get or set the current tick locations and labels of...
                    #...the x-axis.
                    #Pass no arguments to return the current values...
                    #...without modifying them.
                #Parameters (some of them):
                    #ticks: array-like (optional)
                        #The list of "xtick" locations. Passing an empty...
                        #...list removes all "xticks".
                    #labels: array-like (optional)
                        #The labels to place at the given ticks locations...
                        #...This argument can only be passed if ticks is...
                        #...passed as well.
                    #kwargs:
                        #Text properties can be used to control the...
                        #...appearance of the labels.
                #Returns
                    #locs
                        #The list of xtick locations.
                    #labels
                        #The list of xlabel Text objects.
            #Calling this function with no arguments (e.g. xticks()) is the..
            #...pyplot equivalent of calling "get_xticks" and...
            #..."get_xticklabels" on the current axes. Calling this...
            #...function with arguments is the pyplot equivalent of...
            #...calling "set_xticks" and "set_xticklabels" on the current...
            #...axes <--IMPORTANT.
        #Step #2: Set the ticks labels (i.e. we set or establish the labels...
        #...of the ticks). To do that we have the following two options:
            #Option 1: "matplotlib.axes.Axes.set_xticklabels"
                #Syntax: Axes.set_xticklabels(labels, *, fontdict=None, minor=False, **kwargs)
                    #Set the x-axis' labels with list of string labels.
                    #This method should only be used after fixing the...
                    #...tick positions using "Axes.set_xticks". Otherwise,...
                    #...the labels may end up in unexpected positions.
                #Parameters (some of them):
                    #labels: list of str
                        #The label texts.
                    #fontdict: dict (optional)
                        #A dictionary controlling the appearance of the...
                        #...ticklabels.
                #Returns:
                    #list of Text
                        #The labels.
            #Option 2: It is Option 2 discused in Step #1.
                          
#Printing the label of the "x-axis". 
#Setting the ticks of "x-axis" (i.e., position of ticks)
#Setting the ticklabels of "x-axis" with the labels "G1","G2","G3","G4","G5"...
#...in the position described previously.
    #I accomplish the objective (the ticks were set in the right positions...
    #...and labeled in a correct way).
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Define the data
df1789V888 = dfnew1789.copy() 
df1789V888["date"] = df1789V888["date"].dt.strftime("%m/%d")
xticks = np.arange(0, 365, 31)

#Plotting
plt.figure()
ax = plt.subplot()
ax.set_xticks(xticks)
ax.set_xticklabels(['January','February','March','April','May',"June","July","August","September","October","November","December"])
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(90)

plt.fill_between(df1789V888["date"],df1789V888["max"],df1789V888["min"], facecolor='pink', alpha=0.20,linewidth=8,linestyle='-')
plt.xlabel('Date 1788')

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 17 (to solve some doubts)
    #The plot was good (i.e., mix "two lines plots", "fill_between" and...
    #...a scatterplot.)
    #We only need to put only the highest and lowest...
    #...points of temperature for 1789 (scatterplot) in contrast with....
    #...the lines of temperature of 1788 (lines).
import matplotlib.pyplot as plt
import numpy as np

dfnew1900 = dfnew1789.copy()
dfnew1800 = dfnew1788.copy()

xticks = np.arange(0, 365, 31)

ax = plt.gca()
dfnew1800.plot(kind='line',x='date',y="max",ax=ax)
dfnew1800.plot(kind='line',x='date',y="min",ax=ax)
plt.fill_between(dfnew1800["date"],dfnew1800["max"],dfnew1800["min"], facecolor='yellow', alpha=0.30,linewidth=8,linestyle='-')

ax.set_xticks(xticks)
ax.set_xticklabels(['January','February','March','April','May',"June","July","August","September","October","November","December"])
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(90)

colors ='green'
plt.scatter(dfnew1900["date"], dfnew1900["max"], s=3, c=colors)
plt.scatter(dfnew1900["date"], dfnew1900["min"], s=3, c=colors)

#//////////////////////////////////////////////////////////////////////
#MICRO TEST 18 (to solve some doubts)
    #The plot was good (i.e., mix "two lines plots", "fill_between" and...
    #...a scatterplot.)
    #I plot only the highest and lowest points of temperature for...
    #...1789 (scatterplot) in contrast with the lines of temperature of...
    #...1788 (lines).
import matplotlib.pyplot as plt
import numpy as np

dfnew1900 = dfnew1789.copy()
dfnew1800 = dfnew1788.copy()

DfScatterMax = dfnew1900[dfnew1900['max'] > dfnew1800['max']]
DfScatterMax.drop(["min"],inplace=True, axis=1)    
print (DfScatterMax)  

DfScatterMin = dfnew1900[dfnew1900['min'] < dfnew1800['min']]
DfScatterMin.drop(["max"],inplace=True, axis=1)    
print (DfScatterMin)  

xticks = np.arange(0, 365, 31)

ax = plt.gca()
dfnew1800.plot(kind='line',x='date',y="max",ax=ax)
dfnew1800.plot(kind='line',x='date',y="min",ax=ax)
plt.fill_between(dfnew1800["date"],dfnew1800["max"],dfnew1800["min"], facecolor='yellow', alpha=0.30,linewidth=8,linestyle='-')

ax.set_xticks(xticks)
ax.set_xticklabels(['January','February','March','April','May',"June","July","August","September","October","November","December"])
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(90)

colors ='green'
plt.scatter(DfScatterMax["date"], DfScatterMax["max"], s=3, c=colors)
plt.scatter(DfScatterMin["date"], DfScatterMin["min"], s=3, c=colors)

############################################################################
    
    
    
    
    



























