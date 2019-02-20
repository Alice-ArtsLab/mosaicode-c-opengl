#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class PrintFloat(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Print Float"
        self.color = "50:50:50:150"
        self.group = "Math"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Float",
                    "conn_type":"Input",
                    "name":"float"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                    "label":"Color",
                    "conn_type":"Input",
                    "name":"color"}
            ]

        self.properties = []
        self.codes["global"] = """
void $port[float]$(float value){
    std::cout << value << std::endl ;
}
void $port[color]$(char * value){
    std::cout << value << std::endl ;
}"""
