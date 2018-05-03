#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Cone(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Cone"
        self.color = "50:50:50:150"
        self.group = "3D Shapes"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Input",
                "name":"color"}
            ]

        self.properties = [{"name": "base",
                            "label": "base",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "value": 0.6,
                            },
                            {"name": "height",
                            "label": "height",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "value": 0.9,
                            },
                            {"name": "slices",
                            "label": "slices",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 1000,
                            "step": 1,
                            "value": 100,
                            },
                            {"name": "stacks",
                            "label": "stacks",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 1000,
                            "step": 1,
                            "value": 100,
                            }
                           ]
        self.codes["function"] = """
        void mosaicgraph_draw_cone(float base,float height, int slices, int stacks){
            glColor3f(0.8f,0.2f,0.0);
            glutSolidCone(base,height,slices,stacks);
        }

"""
        self.codes["call"] = """
        mosaicgraph_draw_cone($prop[base]$,$prop[height]$,$prop[slices]$,$prop[stacks]$);
"""