outputpersec=2
try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

#q = 4
#U = 1
#xx = q/U*4*6
#yy = q/U*4

my_foam = FindSource("U56H_q5wd_test.OpenFOAM")
SetActiveSource(my_foam)

tsteps = my_foam.TimestepValues
# create a new 'Contour'
contour1 = Contour()
contour1.ContourBy = ['POINTS', 'alpha.water']
contour1.Isosurfaces = [0.5]


DataRepresentation7 = Show()


source = contour1

#for TimeStepNum in range(0,len(tsteps)):
for TimeStepNum in range(0,101*outputpersec,1):
    view = GetActiveView()
    view.ViewTime = tsteps[TimeStepNum]
    Render()
    #contour1 = Contour(Input=my_foam)
    #contour1.ContourBy = ['POINTS', 'alpha.water']
    #contour1.Isosurfaces = [0.5]
    #contour1.PointMergeMethod = 'Uniform Binning'
    writer = CreateWriter("./%dsur.csv" %(TimeStepNum*2), source)
    writer.FieldAssociation = "Points"
    writer.UpdatePipeline()
    Render()
    del writer
