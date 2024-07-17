import matplotlib.pyplot as plt
import matplotlib.text
import matplotlib.ticker 
import matplotlib.lines
import numpy as np


#creating a simple plot

fig,axes=plt.subplots()
#fig,ax=plt.subplots(2,2) creates a 2x2 matrix of grids

axes.set_xlabel("X") #setting the name of X-axis.Axes object usually contains 2 or 3 axis objects
axes.set_ylabel("Y") #setting the name of Y-axis
axes.set_title("Graph") #setting the name of Graph
#axes.plot([1,2,3,3.5,5,10,12],[2,4,6,5,7,1,12])

#-----------------------------------------------


axes.xaxis.set_major_locator(matplotlib.ticker.AutoLocator()) #put ticks with the distances automatically determined.Default for most
                                                                    #plotting
axes.yaxis.set_major_locator(matplotlib.ticker.AutoLocator())
axes.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(n=2)) #divides each section into 3 subsections and determines
                                                                #the length of each subsection automatically
axes.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda val,pos:int(val))) #using funcformatter and customer formatter
                                                                    #to label the major ticks
axes.xaxis.set_minor_formatter(matplotlib.ticker.FuncFormatter(lambda val,pos:float(val))) #giving labels to minor ticks
axes.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(2))
axes.yaxis.set_minor_formatter(matplotlib.ticker.FuncFormatter(lambda val,pos:float(val))) #similar labeling for y-axis

#plt.show()

#-----------------------------------------------


axes.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(numticks=7)) #Puts 7 marks between min and max and divides the interval
                                                                            #into equal parts
axes.xaxis.set_minor_locator(matplotlib.ticker.LinearLocator(numticks=10)) #puts 10 minor ticks(positions are irrelevant to major ticks)
                                                        #this just divide the whole xaxis into 10 for minor ticks
#plt.show()

#-----------------------------------------------

axes.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=2)) #puts tickers at multiples of base
axes.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(base=0.75)) #puts minor tickers at multiples of 0.75

#plt.show()

#-----------------------------------------------

axes.xaxis.set_major_locator(matplotlib.ticker.FixedLocator([2,4,6,8,10])) #puts tickers at the specified locations
axes.xaxis.set_minor_locator(matplotlib.ticker.FixedLocator([1,3,5,7,9])) 
axes.yaxis.set_major_locator(matplotlib.ticker.FixedLocator([1,2,3,4,5]))
axes.yaxis.set_minor_locator(matplotlib.ticker.FixedLocator([0.5,1.5,2.5,3.5,4.5]))
axes.yaxis.set_major_formatter(matplotlib.ticker.FixedFormatter([1.0,2.0,3.0,4.0,5.0])) #give labels by using FixedFormatter in the
                                                                                #same way was FixedLocator

#plt.show()

#-----------------------------------------------

axes.xaxis.set_major_locator(matplotlib.ticker.IndexLocator(base=2,offset=0)) #starts from offset and put ticks with the distance between
                                                                                #them set to 2
axes.yaxis.set_major_locator(matplotlib.ticker.IndexLocator(base=0.5,offset=1))

#plt.show()

#-----------------------------------------------

axes.xaxis.set_minor_locator(matplotlib.ticker.NullLocator()) #default minor tick locator  
#plt.show()

#-----------------------------------------------


#creating a customlocator and using it in set_major_locator
class CustomLocator(matplotlib.ticker.Locator):
    def __init__(self,parts):
        self.parts=parts 

    def __call__(self):
        vmin,vmax=1,10#self.axis.get_view_interval() #axis object is attached to CustomLocator upon creation
        ticks=np.linspace(vmin,vmax,self.parts)
        return ticks
    
axes.xaxis.set_major_locator(CustomLocator(5))
#similar things can be said for matplotlib.ticker.Formatter

#------------------------------------------------

axes.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=2,offset=1))
axes.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda val,pos:float(val)))
axes.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=2,offset=0))
axes.yaxis.set_minor_locator(matplotlib.ticker.NullLocator())
axes.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda val,pos:float(val)))
#axes.set_xlim(left=1,right=5) we can get only a portion of the graph by specifying limits in set_xlim or set_ylim

#plt.show()

#-------------------------------------------------

#an example plot 
A=np.linspace(0,100,200)
B=np.random.uniform(0,10,200)
axes.plot(A,B)
axes.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=5,offset=0))
axes.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(base=1,offset=0))
axes.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
axes.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(base=1))
axes.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
axes.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda val,pos:float(val)))
axes.set_xlim(left=0)
axes.set_ylim(bottom=0)
axes.text(x=20,y=10,s="Peak",color="blue",fontsize=8,ha="right",va="center") #adding some text on the figure
                                        #ha="right" aligns the right part of the text at the specified x coordinate
                                        #it can also be left or center
                                        #va is similar,top and bottom align the top or bottom of the text at the 
                                        #specified y-location,respectively.
axes.text(x=50,y=10,s="Peak2",color="blue",ha="right",va="center",
          fontsize=8,fontstyle="italic",fontweight="bold",fontfamily="serif")


#plt.show()

#-------------------------------------------------

line=matplotlib.lines.Line2D(xdata=[5,100],ydata=[4,5],color="red",linewidth=1,linestyle="solid") #adding a custom line to the graph
            #linestyle can be dotted,dashdot,dashed,solid
axes.add_line(line)

#we can also add a curve
xvals=np.arange(0,100)
yvals=np.sqrt(xvals)
curve=matplotlib.lines.Line2D(xdata=xvals,ydata=yvals,linewidth=1,color="green",linestyle="solid")
#axes.add_line(curve) #adding sqrt(x) curve
plt.show()

#--------------------------------------------------




