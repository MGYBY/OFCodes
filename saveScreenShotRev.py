# generated using paraview version 5.8.1-RC1-970-g93200f474d
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

my_foam = FindSource("100hnOnePeriod.foam")
SetActiveSource(my_foam)

tsteps = my_foam.TimestepValues
# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1499, 753]

# get layout
layout1 = GetLayout()

# current camera placement for renderView1
# renderView1.CameraPosition = [18.875949409046036, 0.5577951471398768, 37.91210719285424]
# renderView1.CameraFocalPoint = [18.875949409046036, 0.5577951471398768, 0.05000000074505806]
# renderView1.CameraParallelScale = 25.41720916354348

# save screenshot
# SaveScreenshot('/home/boyuan/OpenFOAM/boyuan-7/run/78S005_q8_U1575/100hnOnePeriod/sc1.png', renderView1, ImageResolution=[2998, 1506])


for TimeStepNum in range(0,20,1):
    view = GetActiveView()
    view.ViewTime = tsteps[TimeStepNum]
    Render()
    renderView1 = GetActiveViewOrCreate('RenderView')
    writer = SaveScreenshot("/home/boyuan/OpenFOAM/boyuan-7/run/78S005_q8_U1575/100hnOnePeriod/%dss.png"%(TimeStepNum), renderView1, ImageResolution=[2998, 1506])
    # writer.UpdatePipeline()
    # writer = CreateWriter("%dws1.csv" %(TimeStepNum), source)
    # writer.FieldAssociation = "Point Data"
    # writer.UpdatePipeline()
    Render()
    del writer

