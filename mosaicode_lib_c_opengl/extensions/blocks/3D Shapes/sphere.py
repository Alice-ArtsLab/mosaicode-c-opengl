#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Sphere(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Sphere"
        self.color = "50:150:250:150"
        self.group = "3D Shapes"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Input",
                "name":"flow"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Output",
                "name":"flow"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Input",
                "name":"color"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                "label":"Float",
                "conn_type":"Input",
                "name":"float"}
            ]

        self.properties = [{"name": "radius",
                            "label": "radius",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.01,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.1,
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
        self.codes["global"] = """
        float float_$id$ = $prop[radius]$;
        void $port[float]$(float value){
            float_$id$ = value;
        }
"""
        self.codes["function"] = """
        void mosaicgraph_draw_sphere(float radius, int slices, int stacks){
            glColor3f(0.8f,0.2f,0.0);
            glutSolidSphere(radius,slices,stacks);
        }

"""
        self.codes["call"] = """
        mosaicgraph_draw_sphere(float_$id$,$prop[slices]$,$prop[stacks]$);
"""

