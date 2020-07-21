outputpersec=2
try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

q = 5.0
U = 7.5
xx = q/U*100.0
yy = q/U

my_foam = FindSource("U75H_q5withdisext.foam")
SetActiveSource(my_foam)

tsteps = my_foam.TimestepValues
PlotOverLine1 = PlotOverLine( Source="Line" )
DataRepresentation7 = Show()

PlotOverLine1.Source.Point1 = [0, 0.0, 0.1]
PlotOverLine1.Source.Point2 = [xx, 0.0, 0.1]
#select fields
passArrays1 =PassArrays(Input=PlotOverLine1)
#passArrays1.PointDataArrays = ['U','alpha.water']
passArrays1.PointDataArrays = ['wallShearStress']
source = PlotOverLine1

#for TimeStepNum in range(0,len(tsteps)):
for TimeStepNum in range(0,403,1):
    view = GetActiveView()
    view.ViewTime = tsteps[TimeStepNum]
    Render()
    writer = CreateWriter("%dws1.csv" %(TimeStepNum), source)
    writer.FieldAssociation = "Point Data"
    writer.UpdatePipeline()
    Render()
    del writer
