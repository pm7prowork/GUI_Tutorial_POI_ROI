horizontalSlider_zoom_value = 1
POI = []
feat_dct = [1, 0]
ROIFinal = []

def gethorizontalSlider_zoom_value():
    # print "horizontalSlider_zoom_value  at : " + str(horizontalSlider_zoom_value)
    return horizontalSlider_zoom_value

def sethorizontalSlider_zoom_value(horizontalSlider_zoomvalue):
    global horizontalSlider_zoom_value
    horizontalSlider_zoom_value = horizontalSlider_zoomvalue

def getPOI():
    # print "POI : " + str(POI)
    return POI

def setPOI(Poi):
    global POI
    POI = Poi

def getfeat_dct():
    # print "feat_dct : " + str(feat_dct)
    return feat_dct

def setfeat_dct(featdct):
    global feat_dct
    feat_dct = [0, 0]
    feat_dct[featdct] = 1

def getROI():
    return ROIFinal

def setROI(ROI):
    global ROIFinal
    ROIFinal = ROI
    print ROIFinal