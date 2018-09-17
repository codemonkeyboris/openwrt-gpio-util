
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
    PIN_DIR_SET_SUCCESS         = 5
    PIN_SET_VAL_SUCCESS         = 6
    PIN_INIT_ERROR              = -1
    PIN_DIR_SET_ERROR           = -2
    PIN_SET_VAL_ERROR           = -3
    PIN_GET_VAL_ERROR           = -4

    ########################################

    def __init__(self, name, score):
        self.name = name
        self.score = score

    # echo "29" > /sys/class/gpio/export
    def initPin(self, type):
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
    def setPinDir(self, direction):
        try:
            with open("/sys/class/gpio/gpio" + PinNum + "/direction", "w") as fd:
                if direction == PIN_IN:
                    fd.write("in")
                elif direction == PIN_OUT:
                    fd.write("out")
                fd.close()
            return PIN_INIT_SUCCESS
        except Exception as e:
            print "error set pin direction"
            return PIN_DIR_SET_ERROR

    # echo "1" > /sys/class/gpio/gpio29/value
    def setPinValue(self, value):   
        try:
            with open("/sys/class/gpio/gpio" + PinNum + "/value", "w") as fd:
                if value == PIN_LOW:
                    fd.write("0")
                elif value == PIN_HIGH:
                    fd.write("1")
                fd.close()
            return PIN_SET_VAL_SUCCESS
        except Exception as e:
            print "error set pin value"
            return PIN_SET_VAL_ERROR

    def getPinValue(self):   
        get_value = 0
        try:
            with open("/sys/class/gpio/gpio" + PinNum + "/value", "r") as fd:+
                get_value = read()
                fd.close()
            return get_value
        except Exception as e:
            print "error get pin value"
            return PIN_GET_VAL_ERROR
