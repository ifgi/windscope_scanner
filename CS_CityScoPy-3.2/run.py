#!/usr/bin/python


from cityscopy import Cityscopy
import copyright


if __name__ == '__main__':
    copyright.print_copyright()
    CITYSCOPY_SETTINGS_PATH = "settings/cityscopy.json"
    # init cityscopy class
    cityscopy = Cityscopy(CITYSCOPY_SETTINGS_PATH)
    # run CityScopy main methods
    # keystone the scanned area
    # cityscopy.keystone()
    # scan the grid and send to cityIO
    cityscopy.scan()
    # start local UDP comms
    # cityscopy.udp_listener()
