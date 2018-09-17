
import os

class WRTGpioUtil(object):
    #attributes
    # basic
    PIN_LOW = 0
    PIN_HIGH = 1
    PIN_IN = 2
    PIN_OUT = 3

    #SetPinInit
    PIN_INIT_SUCCESS            = 4
    PIN_INIT_FILE_OPEN_ERROR    = -1
    PIN_INIT_FILE_WRITE_ERROR   = -2
    PIN_INIT_FILE_CLOSE_ERROR   = -3
    
    ########################################

    def __init__(self, name, score):
        self.name = name
        self.score = score
    '''
    def p_score(self):
        print('%s: %s' % (self.name, self.score))
    def g_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    '''

    '''
    Init Export/UnExport
    This is used in SetPinExport() and SetPinUnExport() to initiate pins
    '''








    def InitPin(string type):
        try:
            with open("/sys/class/gpio/" + type, "w") as fd:
                fd.write(PinNum)
                fd.close()
            return PIN_INIT_SUCCESS
        except Exception as e:
            print "error initialte pin"
            return PIN_INIT_FILE_OPEN_ERROR

    def exportPin():
        return InitPin("export");

    def unExportPin():   
        return InitPin("unexport");

    # echo $in/out$ > /sys/class/gpio/gpio$PinNum$/direction
    def SetPinDir(Pin_Direction get_Direction):
        

    # echo $0/1$ > /sys/class/gpio/gpio$PinNum$/value
    def SetPinValue(Pin_Value get_Value);   

    # Export + SetPinDir + SetPinValue
    def SetPin(string get_PinNum, Pin_Direction get_Direction, Pin_Value get_Value);    

    # unexport
    def DelPin();   



PIN_LOW = 0
    PIN_HIGH = 1
    PIN_IN = 2
    PIN_OUT = 3