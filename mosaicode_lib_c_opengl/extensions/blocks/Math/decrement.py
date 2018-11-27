#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Decrement(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Decrement"
        self.color = "50:50:50:150"
        self.group = "Math"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Float",
                    "conn_type":"Input",
                    "name":"input"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Trigger",
                    "conn_type":"Input",
                    "name":"trigger"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Result",
                    "conn_type":"Output",
                    "name":"result"}
            ]

        self.properties = []
        self.codes["global"] = """
std::vector<void (*)(float)> $port[result]$;
float trigger_$id$ = 0;
float input_$id$ = 0;
float value_$id$ = 0;

void $port[trigger]$(float value){
     trigger_$id$ = value;
     float result;
     if(value_$id$ == 0){
         value_$id$ = input_$id$;
     }
     if(trigger_$id$ =! 0){
        value_$id$ = value_$id$ - 0.001;
        result = value_$id$;
    }else{
        result = input_$id$;
    }
     for(auto n : $port[result]$){
        n(result);
   }
}

void $port[input]$(float value){
     input_$id$ = value;
}
"""
