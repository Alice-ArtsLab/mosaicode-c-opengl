#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Rotate(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Rotate"
        self.color = "135:206:250:150"
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
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 360,
                            "step": 1,
                            "value": 30,
                            },
                            {"name": "y",
                            "label": "y",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 360,
                            "step": 1,
                            "value": 00,
                            },
                            {"name": "z",
                            "label": "z",
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
    glRotatef($prop[x]$,1.0,0.0,0.0);
    glRotatef($prop[y]$,0.0,1.0,0.0);
    glRotatef($prop[z]$,0.0,0.0,1.0);
"""
