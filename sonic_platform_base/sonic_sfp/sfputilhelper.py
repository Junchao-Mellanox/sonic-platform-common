# sfputilbase.py
#
# Base class for creating platform-specific SFP transceiver interfaces for SONiC
#

from __future__ import print_function

try:
    import abc
    import binascii
    import os
    import re
except ImportError as e:
    raise ImportError("%s - required module not found" % str(e))

class SfpUtilHelper(object):
    # List to specify filter for sfp_ports
    # Needed by platforms like dni-6448 which
    # have only a subset of ports that support sfp
    sfp_ports = []

    # List of logical port names available on a system
    """ ["swp1", "swp5", "swp6", "swp7", "swp8" ...] """
    logical = []

    # dicts for easier conversions between logical, physical and bcm ports
    logical_to_physical = {}

    physical_to_logical = {}
    physical_to_phyaddrs = {}

    def __init__(self):
        pass

    def read_porttab_mappings(self, porttabfile):
        from .sfputilbase import read_porttab_mappings
        self.logical, _, self.logical_to_physical, self.physical_to_logical = read_porttab_mappings(porttabfile)
        
    def get_physical_to_logical(self, port_num):
        """Returns list of logical ports for the given physical port"""

        return self.physical_to_logical[port_num]

    def get_logical_to_physical(self, logical_port):
        """Returns list of physical ports for the given logical port"""

        return self.logical_to_physical[logical_port]

    def is_logical_port(self, port):
        if port in self.logical:
            return 1
        else:
            return 0
