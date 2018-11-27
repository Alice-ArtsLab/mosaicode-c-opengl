#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Torus(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Torus"
        self.color = "250:250:50:150"
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
                "label":"InnerRadius",
                "conn_type":"Input",
                "name":"innerradius"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                "label":"OuterRadius",
                "conn_type":"Input",
                "name":"outerradius"}
            ]

        self.properties = [{"name": "innerradius",
                            "label": "innerRadius",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.01,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.1,
                            },
                            {"name": "outerradius",
                            "label": "outerRadius",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.2,
                            },
                            {"name": "nsides",
                            "label": "nsides",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 1000,
                            "step": 1,
                            "value": 10,
                            },
                            {"name": "rings",
                            "label": "rings",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 1000,
                            "step": 1,
                            "value": 10,
                            }
                           ]

        self.codes["global"] = """
        float innerradius_$id$ = $prop[innerradius]$;;
        float outerradius_$id$ = $prop[outerradius]$;
        void $port[innerradius]$(float value){
            innerradius_$id$ = value;
        }
        void $port[outerradius]$(float value){
            outerradius_$id$ = value;
        }
"""
        self.codes["function"] = """
        void mosaicgraph_draw_torus(float innerRadius,float outerRadius, int nsides, int rings){
            glColor3f(0.8f,0.2f,0.0);
            glutSolidTorus(innerRadius, outerRadius, nsides, rings);
        }

"""
        self.codes["call"] = """
        mosaicgraph_draw_torus(innerradius_$id$,outerradius_$id$,$prop[nsides]$,$prop[rings]$);
"""

