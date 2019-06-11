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
        self.color = "255:172:20:150"
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
                "label":"Base",
                "conn_type":"Input",
                "name":"base"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                "label":"Height",
                "conn_type":"Input",
                "name":"height"}
            ]

        self.properties = [{"name": "base",
                            "label": "base",
                            "type": MOSAICODE_FLOAT,
                           "lower": 0.01,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.6,
                            },
                            {"name": "height",
                            "label": "height",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.01,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
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
        self.codes["global"] = """
        float base_$id$ = $prop[base]$;
        float * $port[color]$;
        float height_$id$ = $prop[height]$;
        void $port[base]$(float value){
            base_$id$ = value;
        }
        void $port[height]$(float value){
            height_$id$ = value;
        }
"""
        self.codes["declaration"] = """
        $port[color]$ = (float*)malloc (3 * sizeof (float));
        $port[color]$[0] = 1.0;
        $port[color]$[1] = 0.5;
        $port[color]$[2] = 0.0;
"""
        self.codes["function"] = """
        void mosaicgraph_draw_cone(float base,float height, int slices, int stacks, float *rgb){
            glColor3f(rgb[0],rgb[1],rgb[2]);
            glutSolidCone(base,height,slices,stacks);
        }

"""
        self.codes["call"] = """
        mosaicgraph_draw_cone(base_$id$,height_$id$,$prop[slices]$,$prop[stacks]$,$port[color]$);
"""
