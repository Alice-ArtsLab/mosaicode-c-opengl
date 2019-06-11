#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class RotateLoop(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Rotate Loop"
        self.color = "75:0:130:150"
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
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "page_inc": 0.1,
                            "page_size": 0.1,
                            "value": 0.1,
                            },
                            {"name": "y",
                            "label": "y",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "page_inc": 0.1,
                            "page_size": 0.1,
                            "value": 0.1,
                            },
                            {"name": "z",
                            "label": "z",
                            "type": MOSAICODE_FLOAT,
                           "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "page_inc": 0.1,
                            "page_size": 0.1,
                            "value": 0.1,
                            },
                            {"name": "angle",
                            "label": "angle",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 360,
                            "step": 1,
                            "value": 0,
                            }
                           ]
        self.codes["global"] = """
GLfloat xRotated$id$, yRotated$id$, zRotated$id$;
"""
        self.codes["call"] = """
    glRotatef(xRotated$id$,1.0,0.0,0.0);
    glRotatef(yRotated$id$,0.0,1.0,0.0);
    glRotatef(zRotated$id$,0.0,0.0,1.0);
"""
        self.codes["idle"] = """
    xRotated$id$ += $prop[x]$;
    yRotated$id$ += $prop[y]$;
    zRotated$id$ += $prop[z]$;
"""

        self.codes["execution"] = """
    xRotated$id$ = yRotated$id$ = zRotated$id$ = $prop[angle]$;
"""
