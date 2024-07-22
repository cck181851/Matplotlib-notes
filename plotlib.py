import matplotlib.pyplot as plt
import matplotlib.dates
import matplotlib.text
import matplotlib.ticker as ticker
import matplotlib.lines
import numpy


#creating a plot with sizes 5x3.7


""" fig,axes=plt.subplots(ncols=1,nrows=1,figsize=(5,3.7))
numpy.random.seed(100000) #random.seed ensures that every time random number generator is called,the same number sequence is produced
x=numpy.arange(100)
y=numpy.cumsum(numpy.random.uniform(-2,2,100))
axes.plot(x,y,color="red",linewidth=2,linestyle="solid",alpha=0.95) 
plt.show()  """

#-----------------------------------------

#apart from plot,we have bar,hist,scatter and color maps


""" fig,axes=plt.subplots(ncols=1,nrows=1,figsize=(5,3.7))
numpy.random.seed(10000)
x=numpy.arange(100)
y=numpy.cumsum(numpy.random.uniform(-2,2,100))
pc=axes.scatter(x,y,c=numpy.random.uniform(0,50,100),marker="o",edgecolor="black") #we can use c to determine color
                #c can also be a 2D array with rows representing colors in RGBA
axes.xaxis.set_major_locator(ticker.MultipleLocator(20)) #setting major tick positions
axes.xaxis.set_minor_locator(ticker.MultipleLocator(10)) #setting minor tick positions
axes.xaxis.set_major_formatter(ticker.FuncFormatter(lambda val,pos:int(val))) #setting names for major ticks
axes.xaxis.set_minor_formatter(ticker.FuncFormatter(lambda val,pos:str(int(val))+'.')) #setting names for minor ticks

axes.grid(True,linestyle="dotted") #adding grid configuration to the figure
fig.colorbar(pc,ax=axes)
plt.show()  """

#---------------------------------------------

#We can use bars to represent data

""" 
X=["Germany","UK","US","France","Norway","China","India"]
Y=[82,66,396,56,4,1300,1350]

fig,ax=plt.subplots()
ax.bar(X,Y,color=["red","red","yellow","red","red","blue","green"],edgecolor="black",
       linestyle="solid",width=0.75,align="center")
ax.grid(True,linestyle="dotted")
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
plt.show()

 """

#---------------------------------------------
#If we need another dimension to represent data,we can use colormaps


""" 
fig,axes=plt.subplots()
X,Y=numpy.meshgrid(numpy.linspace(-3,3,128),numpy.linspace(-3,3,128))
Z=(1 - X/2 + X**5 + Y**3) * numpy.exp(-X**2 - Y**2)
pc=axes.pcolormesh(X,Y,Z,cmap="magma",vmin=numpy.nanmin(Z),vmax=numpy.nanmax(Z))
    #cmap possiblr values:viridis,plasma,BuPy,RdBu_r,inferno...

fig.colorbar(pc,ax=axes)
axes.set_title("pcolormesh")
plt.show()
"""

#-----------------------------------------------
#Another colormap in contourf

""" 
fig,axes=plt.subplots()
X,Y=numpy.meshgrid(numpy.linspace(-3,3,128),numpy.linspace(-3,3,128))
Z=(1 - X/2 + X**5 + Y**3) * numpy.exp(-X**2 - Y**2)
pc=axes.contourf(X,Y,Z,levels=numpy.linspace(numpy.nanmin(Z),numpy.nanmax(Z),18)) #numpy.nanmin and numpy.nanmax can be used to
                                                                    #set limits without missing any possible f(X,Y) values
fig.colorbar(pc,ax=axes)
plt.show()
 """

#----------------------------------------------
#We can plot coordinate-color pairs to graphs by using ax.imshow.

""" 
Z=numpy.random.randint(-3,3,(32,32,3)).astype("float")
fig,ax=plt.subplots()
pc=ax.imshow(Z,vmin=-3,vmax=3)
fig.colorbar(pc,ax=ax)
plt.show()
"""


""" 
fig,ax=plt.subplots()
X,Y=numpy.meshgrid(numpy.linspace(-3,3,128),numpy.linspace(-3,3,128))
Z=(1 - X/2 + X**5 + Y**3) * numpy.exp(-X**2 - Y**2)
pc=ax.imshow(Z,cmap="magma",vmin=numpy.nanmin(Z),vmax=numpy.nanmax(Z))
fig.colorbar(pc,ax=ax)
plt.show()

"""

#----------------------------------------
#creating QR code using matplotlib

""" 
Z=numpy.random.randint(0,2,(64,64))
fig,ax=plt.subplots()
pc=ax.imshow(Z,cmap="binary",vmin=0,vmax=1)
fig.colorbar(pc,ax=ax)
plt.show()
 """

#-----------------------------------------
#We can create legend and annotations for curves.We can also set tick parameters by using tick_params

""" 
X=numpy.linspace(0,100,100)
Y=[numpy.random.uniform(max(0,i-10),i+15) for i in X]
Z=[numpy.random.uniform(max(0,i-20),i+25) for i in X]
fig,ax=plt.subplots()
ax.scatter(X,Z,label="IQ")
ax.scatter(X,Y,label="EQ")
ax.set_xlabel("Age")
ax.set_ylabel("Level")
ax.set_title("Age-IQ&EQ Relation")
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.tick_params(axis="x",which="minor",top=True,labeltop=True,labelcolor="green",color="red",length=5)
ax.tick_params(axis="y",right=True,labelright=True,color="blue",labelcolor="green",length=3,which="both")
ax.annotate(text="turning point",xytext=(60,20),xy=(55,35),arrowprops=dict(arrowstyle="->",color="black"))
plt.legend()
plt.show()
"""

#----------------------------------------------

""" 
fig,ax=plt.subplots(2,2,sharex=True,sharey=False)

for row in range(2):
    for col in range(2):
        ax[row,col].annotate(text=f'axs[{row}-{col}]',ha="center",va="center",xy=(0.5,0.5),
                             transform=ax[row,col].transAxes,color="darkgrey",fontsize=18)
                            #setting annotate for each subplot
fig.suptitle("Subplots()",color="Blue",fontsize=12,fontfamily="sanserif") #setting a title for all subplots
plt.show()
"""

#---------------------------------------------
#There are different ways of adding axes on the figure

""" 
fig,[ax1,ax2]=plt.subplots(1,2) #using matplotlib.pyplot.subplots
ax1.set_position([0.1,0.1,0.3,0.3]) #setting position and sizes of some axes
fig.add_axes([0.1,0.58,0.3,0.3]) #using matplotlib.Figure.add_axes

[ax3,ax4]=fig.subplots(1,2) #using matplotlib.pyplot.Figure.subplots
ax3.set_position([0.2,0.2,0.1,0.1]) #using set_position the adjust the position and sizes of axes on the figure
ax4.set_position([0.6,0.6,0.1,0.1])
plt.show()
"""

#---------------------------------------------
#The above methods create and place all axes onto the figure at once but we can also add them one by one
#and this was how matplotlib used to work when first released

""" 
fig,ax=plt.subplots(1,2)
fig.add_axes([0.3,0.3,0.1,0.2]) #using matplotlib.pyplot.Figure.add_axes to add a single axis at a time
fig.add_axes([0.7,0.3,0.1,0.2])
plt.show()
"""

#--------------------------------------------

"""  
fig=plt.figure(facecolor="lightblue") 
ax1=fig.add_subplot(111) #using matplotlib.Figure.add_subplot to add a subplot
ax2=fig.add_subplot(121) #111 can be interpreted as row-col-index
ax3=plt.subplot(211) #same effect can be achieved by using this
ax4=fig.add_subplot(211)
ax1.set_position([0.1,0.1,0.2,0.2])
ax2.set_position([0.1,0.5,0.2,0.2])
ax3.set_position([0.7,0.1,0.2,0.2])
ax4.set_position([0.7,0.5,0.2,0.2])
plt.show()
"""

#-------------------------------------------

#we can also create subplots by using matplotlib.pyplot.subplot_mosaic.In this case,a dictionary is returned instead of list of lists



""" 
fig,ax=plt.subplot_mosaic([["upper left","upper right"],["lower left","lower right"]])
for i,j in ax.items():
    j.annotate(f'subplot[{i}]',xy=(0.35,0.5),fontsize=14,color="darkgrey")
fig.suptitle("subplot_mosaic",color="green")
#plt.show()

fig,ax=plt.subplot_mosaic([["upper left","right"],["lower left","right"]])
for i,j in ax.items():
    x,y=j.get_xlim(),j.get_ylim()
    j.annotate(f'subplot[{i}]',color="darkgrey",fontsize=14,ha="center",va="center",xy=((x[0]+x[1])/2,(y[0]+y[1])/2))
plt.show()
"""
#-------------------------------------------
#We can also have subfigures in a figure,similar to subplots

""" 
fig=plt.figure()
fig1,fig2=fig.subfigures(1,2,width_ratios=[2,1])
ax1,ax2=fig1.subplots(1,2)
fig1.suptitle("first fig")
fig1.set_facecolor("lightblue")
fig1.supxlabel("x label of fig1")
fig1.supylabel("y label of fig2")
fig2.set_facecolor("lightgreen")
fig2.suptitle("second fig")
fig2.supxlabel("x label of fig2")
fig2.supylabel("y label of fig2")
ax3=fig2.subplots(1,1)
ax3.set_aspect(1)
ax1.set_aspect(1)
ax2.set_aspect(1)
plt.show()
"""

#--------------------------------------------
#subplot_mosaic is very convenient for creating subplots 

""" 
fig,ax=plt.subplot_mosaic([["upper left",[["inner top"],["inner bottom"]]],["lower left","lower right"]],layout="constrained")
for i,j in ax.items():
    j.annotate(f'subplot[{i}]',xy=(0.5,0.5),ha="center",va="center",transform=j.transAxes,color="darkgrey",fontsize=14)
    j.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
plt.show()
"""

#-------------------------------------------
#gridspec can be used to access grid locations

""" 
fig=plt.figure(facecolor="lightblue")
spec=fig.add_gridspec(2,2,left=0.05,right=0.9,top=0.8)
ax0=fig.add_subplot(spec[0,0])
ax0.annotate("ax0",xy=(0.5,0.5),va="center",ha="center",color="lightgrey",fontsize=14)
ax1=fig.add_subplot(spec[0,1])
ax2=fig.add_subplot(spec[1,0])
ax3=fig.add_subplot(spec[1,1])
#ax4=fig.add_subplot(spec[0,:])  more than one slot can be allocated to a subplot by using slicing
#the same effect can be achieved by using subplot_mosaic as well
fig.suptitle("Manuelly added subplots using Figure.add_gridspec")
plt.show()
 """

#--------------------------------------------
#gridspec can also be used to create subfigures 

""" 
fig=plt.figure(facecolor="lightblue")
outer=fig.add_gridspec(1,2)
inner0=outer[0].subgridspec(2,2)
inner1=outer[1].subgridspec(3,1)

for row in range(2):
    for col in range(2):
        ax=fig.add_subplot(inner0[row,col])
        ax.annotate(f'subplot[1][{row},{col}]',xy=(0.5,0.5),ha="center",va="center")
for row in range(3):
    for col in range(1):
        ax=fig.add_subplot(inner1[row,col])
        ax.annotate(f'subplot[0][{row},{col}]',xy=(0.5,0.5),ha="center",va="center")

plt.show()
"""

#--------------------------------------------
#a more sophisticated example

""" 
fig=plt.figure()
outer=fig.add_gridspec(3,3)
for row in range(3):
    for col in range(3):
        inner=outer[row,col].subgridspec(3,3)
        for row2 in range(3):
            for col2 in range(3):
                ax=fig.add_subplot(inner[row2,col2])
                ax.annotate(f'subplot[{row},{col}][{row2},{col2}]',color="black",fontsize=3,xy=(0.5,0.5),ha="center",va="center")
plt.show() 
"""

#--------------------------------------------

""" 
numpy.random.seed(1)
fig,axs=plt.subplots(2,2)
cmaps=["magma","RdBu_r"]
for col in range(2):
    for row in range(2):
        ax=axs[row,col]
        pc=ax.pcolormesh(numpy.random.random((40,40))*(col+1),cmap=cmaps[col])
    fig.colorbar(pc,ax=axs[:,col],shrink=0.6) #we can use just one colorbar for two subplots that use the same colormap
                                        #we also can determine its size by using shrink parameter
plt.show()
"""

#--------------------------------------------
#another example to this concept


""" 
fig,axs=plt.subplots(3,3,layout="constrained")
for ax in axs.flat:
    pc=ax.pcolormesh(numpy.random.random((20,20)),cmap="RdBu_r")
fig.colorbar(pc,ax=axs[0,:2],location="bottom",shrink=0.7)
fig.colorbar(pc,ax=axs[0,2],location="bottom",shrink=0.6)
fig.colorbar(pc,ax=axs[1:,:],location="right",shrink=0.6)
fig.colorbar(pc,ax=axs[2,0],location="right",shrink=0.7) #we can specift te location of colorbar

plt.show()
"""

#--------------------------------------------
#we can set pad distances around colorbar.But if we use it in non-constrained layout,it causes the parent axis to shrink

""" 
fig,ax=plt.subplots(3,1,figsize=(5,5))
pads=[0.1,0.15,0.25]

for ax,pad in zip(ax,pads):
    pc=ax.pcolormesh(numpy.random.random((20,20)),cmap="RdBu_r")
    fig.colorbar(pc,ax=ax,pad=pad,location="right") #causes x-axis to shrink since we are not using constraint layout

plt.show()
"""

#-------------------------------------------

#By default,the plots extends 5% beyond the graphs.We can change this by using ax.margins() method

""" 
fig=plt.figure(figsize=(5,3.7),layout="constrained")
ax=fig.subplots()
data=numpy.linspace(-3,3,100)
ax.plot(data,numpy.sin(data))
ax.margins(0.5,0.1) #setting x and y axes at once
ax.set_xmargin(0.1) #setting the margin of only x axis
ax.set_ymargin(-0.1) #setting the margin of only y axis.In case of negative numbers,the graph is clipped off
plt.show() 
"""

#-------------------------------------------

#By default,the margins are adjusted automatically every time a new plot is added but we can switch off this
#functionality by using set_xlim and set_ylim and setting the limits manually.

""" 
data1=numpy.linspace(-3,3,100)
fig=plt.figure(figsize=(5,3.7))
ax=fig.subplots(1,1)
ax.plot(data1,numpy.sin(data1))
ax.set_xlim(-3,3)
ax.set_ylim(-1,1)
ax.plot(data1*2,data1) #now,the margins are not adjusted automatically and the second plot is clipped off 
plt.show() 
"""


#-------------------------------------------
#If we want to change this feature after setting x and y margins,we can use ax.autoscale

""" 
data1=numpy.linspace(-3,3,100)
fig=plt.figure(figsize=(5,3.7))
ax=fig.subplots(1,1)
ax.plot(data1,numpy.sin(data1))
ax.set_xlim(-3,3)
ax.set_ylim(-1,1)
ax.plot(data1*2,data1) 
ax.autoscale(tight=True) #After this command,the margins are set automatically
plt.show()  
"""

#------------------------------------------

#By default,matplotlib displays data on linear scale but we can set it to other scales by using ax.set_xscale or ax.set_yscale
#depending on our needs

""" 
data=numpy.linspace(-1000,1000,100000)
fig=plt.figure(figsize=(5,3.7))
ax=fig.subplots()
ax.plot(data,numpy.log(data))
ax.set_xscale("log") #apart from log,there are other scales like loglog and semilog
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.grid(True)
plt.show()
"""

#------------------------------------------

#We can use matplotlib.ticker package to set formatter and locaters but ax.set_xtick and x.set_ytick are also
#methods that can be used for the same purpose


""" 
fig,ax=plt.subplots(2,1,figsize=(3,5))
data=numpy.linspace(0,100,11)
for idx,a in enumerate(ax):
    if idx==0:
        a.set_title("Automatic")
        a.plot(data,data,color="green")
        a.set_ylabel("(Cost)",fontsize=9,color="blue")
        a.set_xlabel("(Age)",fontsize=9,color="blue")
        a.yaxis.set_label_coords(-0.015,1.1,transform=None) #we can set the coordinates of x and y labels by using this command
        a.xaxis.set_label_coords(1,-0.04,transform=None) #same for x axis label
    else:
        a.set_title("Manual")
        a.plot(data,data,color="green")
        a.set_ylabel("(Cost)",fontsize=9,color="blue")
        a.set_xlabel("(Year)",fontsize=9,color="blue")
        a.set_xticks(numpy.linspace(0,100,6),labels=[f'{i}' for i in numpy.linspace(0,100,6)])
        a.set_yticks(numpy.linspace(0,100,6),labels=[f'{i}' for i in numpy.linspace(0,100,6)])
        a.set_yticks(numpy.linspace(0,100,11),labels=['' for i in numpy.linspace(0,100,11)],minor=True)
        a.yaxis.set_label_coords(-0.015,1.1,transform=None) #we can set the coordinates of x and y labels by using this command
        a.xaxis.set_label_coords(1,-0.04,transform=None) #same for x axis label
    
plt.show()
"""

#---------------------------------------

#a demonstration of ticker locators

""" 
def setup(ax,title):
    ax.spines[["left","top","right"]].set_visible(False) #makes the left,top and right spines unvisible and focuses on the bottom
    ax.yaxis.set_major_locator(ticker.NullLocator())

    ax.set_xlim(0,5)
    ax.set_ylim(0.1)
    ax.tick_params(which="major",width=1,length=5,color="blue") #adjusting the properties of ticks
    ax.tick_params(which="minor",width=0.75,length=2.5,color="green")
    ax.xaxis.set_ticks_position("bottom")
    ax.text(0.0,0.2,title,transform=ax.transAxes,color="tab:blue")

fig,axs=plt.subplots(7,1,layout="constrained")

setup(axs[0],"NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())

setup(axs[1],"MultipleLocator(0.5)")
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(0.5))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(0.1))

setup(axs[2],"IndexLocator()")
axs[2].xaxis.set_major_locator(ticker.FixedLocator([0,1,5]))
axs[2].xaxis.set_minor_locator(ticker.FixedLocator([0.1,0.2,0.8]))


setup(axs[3],"LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))

setup(axs[4],"AutoLocator()")
axs[4].xaxis.set_major_locator(ticker.AutoLocator())
axs[4].xaxis.set_minor_locator(ticker.AutoLocator()) 

setup(axs[5],"IndexLocator(base=0.25,offset=0.5)")
axs[5].plot(range(0, 5), [0]*5, color='white')
axs[5].xaxis.set_major_locator(ticker.IndexLocator(base=0.5,offset=0))

setup(axs[6],"MaxNLocator(4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(4))

plt.show()
"""

#------------------------------------
#a similar demonstration for labels

""" 
def setup(ax, title):
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[["left","right","top"]].set_visible(False)

    ax.set_xlim(0,5)
    ax.set_ylim(0,1)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
    ax.tick_params(which="major",length=5,width=1)
    ax.tick_params(which="minor",length=2.5,width=0.75)

    ax.text(0.5,0.2,title,transform=ax.transAxes,color="tab:blue",fontsize=14,ha="center")


fig = plt.figure(layout="constrained")
fig0, fig1, fig2 = fig.subfigures(3, height_ratios=[1.5, 1.5, 7.5])

fig0.suptitle("String Formatting",ha="center",fontsize=16)
ax0=fig0.subplots()
setup(ax0,"{x}")
ax0.xaxis.set_major_formatter("{x} units")

fig1.suptitle("Function Formatting",ha="center",fontsize=16)
ax1=fig1.subplots()
setup(ax1,"def f(val,pos) -> str(val-5)")
ax1.xaxis.set_major_formatter(lambda val,pos:str(val-5))

fig2.suptitle("Formatter Object Formatting",fontsize=16,ha="center")
axs=fig2.subplots(4)

setup(axs[0],"NullFormatter()")
axs[0].xaxis.set_major_formatter(ticker.NullFormatter())

setup(axs[1],"StrMethodFormatter('{x:.3f}')")
axs[1].xaxis.set_major_formatter(ticker.StrMethodFormatter("[{x:.3f}] units"))

setup(axs[2],"FixedFormatter()")
axs[2].xaxis.set_major_formatter(ticker.FixedFormatter(["A","B","C","D","E"]))

setup(axs[3],"FuncFormatter(f'[{x:.2f}]')")
axs[3].xaxis.set_major_formatter(ticker.FuncFormatter(lambda x,y:f'[{x:.2f}]'))


plt.show() 
"""




