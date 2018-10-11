#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Window class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class WindowProperties(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Window Properties"
        self.color = "250:150:150:150"
        self.group = "Window"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Background",
                "conn_type":"Input",
                "name":"background"}
            ]

        self.properties = [{"name": "x",
                            "label": "x",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 2000,
                            "step": 1,
                            "value": 0,
                            },
                            {"name": "y",
                            "label": "y",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 2000,
                            "step": 1,
                            "value": 0,
                            },
                            {"name": "width",
                            "label": "width",
                            "type": MOSAICODE_INT,
                            "lower": 100,
                            "upper": 2000,
                            "step": 1,
                            "value": 500,
                            },
                            {"name": "height",
                            "label": "height",
                            "type": MOSAICODE_INT,
                            "lower": 100,
                            "upper": 2000,
                            "step": 1,
                            "value": 500,
                            },
                            {"name": "title",
                            "label": "title",
                            "type": MOSAICODE_STRING,
                            "value": "New Window",
                            },
                            {"name": "polygon",
                            "label": "polygon",
                            "type": MOSAICODE_COMBO,
                            "values": ["GL_FILL",
                                        "GL_LINE",
                                        "GL_POINT"],
                            "value": "GL_LINE",
                            },
                            {"name": "background",
                            "label": "background",
                            "type": MOSAICODE_COLOR,
                            "value": "#A83333"
                            }

                           ]
        self.codes["declaration"] = """
        window->x = $prop[x]$;
        window->y = $prop[y]$;
        window->width = $prop[width]$;
        window->height = $prop[height]$;
        strcpy(window->title, "$prop[title]$");
        float background[3] = rgbToFloat("$prop[background]$");
        window->red = background[0];
        window->green = background[1]; 
        window->blue = background[2] ;
"""
        self.codes["call"] = """
        glPolygonMode(GL_FRONT_AND_BACK, $prop[polygon]$);
"""
