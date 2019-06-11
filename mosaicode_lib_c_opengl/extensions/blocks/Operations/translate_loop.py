#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class TranslateLoop(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Translate Loop"
        self.color = "120:0:208:150"
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
                            "value": 0.01,
			    "page_inc": 0.1,
                            "page_size": 0.1,
                            },
                            {"name": "y",
                            "label": "y",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "value": 0.01,
			    "page_inc": 0.1,
                            "page_size": 0.1,
                            },
                            {"name": "z",
                            "label": "z",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "value": 0.01,
			    "page_inc": 0.1,
                            "page_size": 0.1,
                            }
                           ]
        self.codes["global"] = """
GLfloat xTranslate$id$,yTranslate$id$,zTranslate$id$;
"""
        self.codes["call"] = """
    glTranslatef(xTranslate$id$,yTranslate$id$,zTranslate$id$);
"""

        self.codes["idle"] = """
    xTranslate$id$ += $prop[x]$;
    yTranslate$id$ += $prop[y]$;
    zTranslate$id$ += $prop[z]$;
"""
