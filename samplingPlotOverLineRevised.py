outputpersec=2
try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

q = 4
U = 1
xx = q/U*4*6
yy = q/U*4

my_foam = FindSource("U75H_q5withdisext.OpenFOAM")
SetActiveSource(my_foam)

tsteps = my_foam.TimestepValues
PlotOverLine1 = PlotOverLine( Source="High Resolution Line Source" )
DataRepresentation7 = Show()

PlotOverLine1.Source.Point1 = [xx/2, 0.0, 0.1]
PlotOverLine1.Source.Point2 = [xx/2, yy, 0.1]
#select fields
passArrays1 =PassArrays(Input=PlotOverLine1)
passArrays1.PointDataArrays = ['U','alpha.water']
source = PlotOverLine1

#for TimeStepNum in range(0,len(tsteps)):
for TimeStepNum in range(0,101*outputpersec,1*outputpersec):
    view = GetActiveView()
    view.ViewTime = tsteps[TimeStepNum]
    Render()
    writer = CreateWriter("%dvel.csv" %(TimeStepNum/outputpersec), source)
    writer.FieldAssociation = "Points"
    writer.UpdatePipeline()
    Render()
    del writer
