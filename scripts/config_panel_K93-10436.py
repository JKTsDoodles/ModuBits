App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Sketch').AttachmentSupport = (App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('BaseFeature'),['Face9',])
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

import PartDesignGui
# ActiveSketch = App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Sketch')
# if ActiveSketch.ViewObject.RestoreCamera:
#   ActiveSketch.ViewObject.TempoVis.saveCamera()
#   if ActiveSketch.ViewObject.ForceOrtho:
#     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
# 

from dataclasses import dataclass

@dataclass
class Cutout:
    coord_x: float
    coord_y: float
    diameter: float

# constants
DIAMETER_BNC = 13.0
DIAMETER_IFXXXX = 6.3
DIAMETER_Banana = 11.5
DIAMETER_PJ = 7.0
DIAMETER_PTS645V = 3.6
DIAMETER_SJ3 = 5.2

# defines frontpanel type, slot no. in chassis and orientation
frontpanel_type = {
    "K93-10436-H7-L120_L1up":1,
    "K97-10473-H7-L120_L1up":2,
    "K97-10473-H7-L120_L4down":3,
    "K96-10463-H7-L120_L1up":4,
    "K96-10463-H7-L120_L4down":5,
    "K127-13031-H7-L120_L1up":6
}

module_type = {
    "BNC": 1,
    "IFXXXX": 2,
    "Banana": 3,
    "PJ": 4,
    "PTS645V": 5,
    "SJ3": 6
}

 

def get_coords_K93_10436_H7_L120_L1up(module, index):
    if (module==module_type["BNC"]):
        x = 15.18+index*1.27
        y = 20.72
        diameter = DIAMETER_BNC
    elif (module==module_type["IFXXXX"]):
        x = 11.36+index*1.27
        y = 20.6
        diameter = DIAMETER_IFXXXX
        #do something
    elif (module==module_type["Banana"]):
        x = 12.63+index*1.27
        y = 19.92
        diameter = DIAMETER_Banana
        #do something
    elif (module==module_type["PJ"]):
        x = 12.63+index*1.27
        y = 18.62
        diameter = DIAMETER_PJ
        #do something
    elif (module==module_type["PTS645V"]):
        x = 11.38+index*1.27
        y = 17.12
        diameter = DIAMETER_PTS645V
        #do something
    elif (module==module_type["SJ3"]):
        x = 10.09+index*1.27
        y = 16.15
        diameter = DIAMETER_SJ3
        #do something
    else:
        print("mdule-type unknown")
    return x-52.0,y-18.0,diameter

def add_hole(x,y,diameter):
    ActiveSketch = App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Sketch')
    #lastGeoId = len(ActiveSketch.Geometry)
    geoList = []
    geoList.append(Part.Circle(App.Vector(x, y, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.5*diameter))
    App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Sketch').addGeometry(geoList,False)
    del geoList
    App.getDocument('K93_10436_H7_L120_frontpanel_blank').recompute()
    return 0

def add_cutout(frontpanel_config, module, index):
    if (frontpanel_config == frontpanel_type["K93-10436-H7-L120_L1up"]):
        x,y,diameter = get_coords_K93_10436_H7_L120_L1up(module, index)
        add_hole(x,y,diameter)
        pass
    elif (frontpanel_config == frontpanel_type["K97-10473-H7-L120_L1up"]):
        pass
    elif (frontpanel_config == frontpanel_type["K97-10473-H7-L120_L4down"]):
        pass
    elif (frontpanel_config == frontpanel_type["K96-10463-H7-L120_L1up"]):
        pass
    elif (frontpanel_config == frontpanel_type["K96-10463-H7-L120_L4down"]):
        pass
    elif (frontpanel_config == frontpanel_type["K127-13031-H7-L120_L1up"]):
        pass
    else:
        print("undefined frontpanel config")

# begin user area--------------------------------------------------------------
# make changes below to config your panel
# available types:
# "BNC"
# "IFXXXX" Fiber emitter / receiver of the IF-series
# "Banana" 4mm Banana Jack
# "PJ" Barrel Jack of the type PJ-063AH
# "PTS645V" tactile switch
# "SJ3" 3.5mm stereo audio jack with switches (SJ3-35083D-TR)
#
# the example below generates the frontpanel cutouts for the modules
# depicted in the title image.
# From left to right:
# IF-D91B, BNC, Banana, PTS645V, PJ-063AH, IF-IF-E96E, SJ3-35083D-TR
add_cutout(frontpanel_type["K93-10436-H7-L120_L1up"], module_type["IFXXXX"], 0)
add_cutout(frontpanel_type["K93-10436-H7-L120_L1up"], module_type["BNC"], 8)
add_cutout(frontpanel_type["K93-10436-H7-L120_L1up"], module_type["Banana"], 22)
add_cutout(frontpanel_type["K93-10436-H7-L120_L1up"], module_type["PTS645V"], 33)
add_cutout(frontpanel_type["K93-10436-H7-L120_L1up"], module_type["PJ"], 42)
add_cutout(frontpanel_type["K93-10436-H7-L120_L1up"], module_type["IFXXXX"], 53)
add_cutout(frontpanel_type["K93-10436-H7-L120_L1up"], module_type["SJ3"], 61)
#
# end user area----------------------------------------------------------------

# generate cutouts
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Body').newObject('PartDesign::Pocket','Pocket')
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').Profile = (App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Sketch'), ['',])
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').Length = 5
App.ActiveDocument.recompute()
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').ReferenceAxis = (App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Sketch'),['N_Axis'])
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Sketch').Visibility = False
App.ActiveDocument.recompute()

App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').UseCustomVector = 0
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').Direction = (0, 0, -1)
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').ReferenceAxis = (App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Sketch'), ['N_Axis'])
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').AlongSketchNormal = 1
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').Type = 1
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').UpToFace = None
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').Reversed = 0
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').Midplane = 0
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Pocket').Offset = 0
App.getDocument('K93_10436_H7_L120_frontpanel_blank').recompute()
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('BaseFeature').Visibility = False
App.getDocument('K93_10436_H7_L120_frontpanel_blank').getObject('Sketch').Visibility = False





