#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Scale(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Scale"
        self.color = "86:0:150:150"
        self.group = "Operations"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                    "label":"Flow",
                    "conn_type":"Input",
                    "name":"flow"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                    "label":"Flow",
                    "conn_type":"Output",
                    "name":"flow"}
            ]

        self.properties = [{"name": "x",
                            "label": "x",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.0,
                            "upper": 5.0,
                            "step": 0.001,
			    "page_inc": 0.1,
                            "page_size": 0.1,
                            "value": 0.50,
                            },
                            {"name": "y",
                            "label": "y",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.0,
                            "upper": 1.0,
                            "page_inc": 0.1,
                            "page_size": 0.1,
			    "step": 0.001,
                            "value": 0.50,
                            },
                            {"name": "z",
                            "label": "z",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.0,
                            "upper": 5.0,
			    "page_inc": 0.1,
                            "page_size": 0.1,
                            "step": 0.001,
                            "value": 0.50,
                            }
                           ]
        self.codes["call"] = """
    glScalef($prop[x]$,$prop[y]$,$prop[z]$);
"""
