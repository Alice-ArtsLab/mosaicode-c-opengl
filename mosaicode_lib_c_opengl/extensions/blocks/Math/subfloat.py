#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class SubFloat(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Sub Float"
        self.color = "60:60:255:150"
        self.group = "Math"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Float",
                    "conn_type":"Input",
                    "name":"input1"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Float",
                    "conn_type":"Input",
                    "name":"input2"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Result",
                    "conn_type":"Output",
                    "name":"result"}
            ]

        self.properties = []
        self.codes["global"] = """
std::vector<void (*)(float)> $port[result]$;
float value1_$id$ = 0;
float value2_$id$ = 0;

void $port[input1]$(float value){
     value1_$id$ = value;
     float result = value1_$id$ - value2_$id$;
     for(auto n : $port[result]$){
        n(result);
   }
}

void $port[input2]$(float value){
     value2_$id$ = value;
     float result = value1_$id$ - value2_$id$;
     for(auto n : $port[result]$){
        n(result);
   }
}
"""
