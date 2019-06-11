#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class ScaleLoop(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Keyboard"
        self.color = "0:148:0:150"
        self.group = "I/O"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Value",
                    "conn_type":"Output",
                    "name":"value"}
            ]

        self.properties = [{"name": "caractere",
                            "label": "caractere",
                            "type": MOSAICODE_STRING,
                            "value": "a"
                            }]
       
        self.codes["global"] = """
        std::vector<void (*)(float)> $port[value]$; //keyboard output
        float bool$id$ = 0;
"""
        self.codes["keyboard"] = """
    if (key == (int)'$prop[caractere]$'){
      if(bool$id$ == 0.0){
        bool$id$ = 1.0;
        for(auto n : $port[value]$){
            n(bool$id$);
        }
      }else{
        bool$id$ = 0.0;
        for(auto n : $port[value]$){
            n(bool$id$);
        }
      }
      
    }
"""
