#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Octahedron(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Octahedron"
        self.color = "255:159:64:150"
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
        self.properties = [{"name": "size",
                            "label": "size",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.01,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.1,
                            }
                           ]
        self.codes["global"] = """
        float float_$id$ = $prop[size]$;
        float * $port[color]$;
        void $port[float]$(float value){
            float_$id$ = value;
        }
"""

        self.codes["declaration"] = """
        $port[color]$ = (float*)malloc (3 * sizeof (float));
        $port[color]$[0] = 1.0;
        $port[color]$[1] = 0.5;
        $port[color]$[2] = 0.0;
"""

        self.codes["function"] = """
        void mosaicgraph_draw_octahedron(float * rgb){
            glColor3f(rgb[0],rgb[1],rgb[2]);
            glutSolidOctahedron();
        }

"""
        self.codes["call"] = """
        glPushMatrix();
        glScalef(float_$id$,float_$id$,float_$id$);
        mosaicgraph_draw_octahedron($port[color]$);
        glPopMatrix();
"""
