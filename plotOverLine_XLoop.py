import numpy as np
try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

q = 4.0
U = 10.0
# hn=q/U
hn=0.222
xx = q/U*4*6
# yy = q/U*2.0
yy=0.222
xCenter = 20 #position of the wave front

my_foam =GetActiveSource()
PlotOverLine1 = PlotOverLine(Input=my_foam, Source="High Resolution Line Source" )
DataRepresentation7 = Show()


passArrays1 =PassArrays(Input=PlotOverLine1)
passArrays1.PointDataArrays = ['U','alpha.water']
source = PlotOverLine1
xlist = np.arange(-5,6,1)

#for TimeStepNum in range(0,len(tsteps)):

for i in range(len(xlist)):
    PlotOverLine1.Source.Point1 = [xCenter+hn*xlist[i], 0, 0.1]
    PlotOverLine1.Source.Point2 = [xCenter+hn*xlist[i], yy, 0.1]
    writer = CreateWriter("data_plot_x{0}.csv" .format(xlist[i]))
    # writer.FieldAssociation = "Point Data"
    writer.UpdatePipeline()
   #  del writer

