
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
    PIN_DIR_SET_SUCCESS            = 5
    PIN_INIT_ERROR              = -1
    PIN_DIR_SET_ERROR              = -1
    
    ########################################

    def __init__(self, name, score):
        self.name = name
        self.score = score

    # echo "29" > /sys/class/gpio/export
    def InitPin(self, type):
        try:
            with open("/sys/class/gpio/" + type, "w") as fd:
                fd.write(PinNum)
                fd.close()
            return PIN_INIT_SUCCESS
        except Exception as e:
            print "error initialte pin"
            return PIN_INIT_ERROR

    def exportPin(self):
        return InitPin("export");

    def unExportPin(self):   
        return InitPin("unexport");

    # echo "out" > /sys/class/gpio/gpio29/direction
    def SetPinDir(self, get_Direction):
        try:
            with open("/sys/class/gpio/gpio" + PinNum + "/direction") as fd:
                if get_Direction == PIN_IN:
                    fd.write("in")
                elif get_Direction == PIN_OUT:
                    fd.write("out")
                fd.close()
            return PIN_INIT_SUCCESS
        except Exception as e:
            print "error set pin direction"
            return PIN_DIR_SET_ERROR

    # echo $0/1$ > /sys/class/gpio/gpio$PinNum$/value
    def SetPinValue(Pin_Value get_Value);   

    # Export + SetPinDir + SetPinValue
    def SetPin(string get_PinNum, Pin_Direction get_Direction, Pin_Value get_Value);    

    # unexport
    def DelPin();   
