outputpersec=1
try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

#q = 4
#U = 1
#xx = q/U*4*6
#yy = q/U*4

my_foam = FindSource("U75H_q5withdisext.foam")
SetActiveSource(my_foam)

tsteps = my_foam.TimestepValues
# create a new 'Contour'
contour1 = Contour()
contour1.ContourBy = ['POINTS', 'alpha.water']
contour1.Isosurfaces = [0.55]


DataRepresentation7 = Show()


source = contour1

#for TimeStepNum in range(0,len(tsteps)):
for TimeStepNum in range(399,401,1):
    view = GetActiveView()
    view.ViewTime = tsteps[TimeStepNum]
    Render()
    #contour1 = Contour(Input=my_foam)
    #contour1.ContourBy = ['POINTS', 'alpha.water']
    #contour1.Isosurfaces = [0.5]
    #contour1.PointMergeMethod = 'Uniform Binning'
    writer = CreateWriter("./%dsur.csv" %((TimeStepNum)), source)
    writer.FieldAssociation = "Point Data"
    writer.UpdatePipeline()
    Render()
    del writer
