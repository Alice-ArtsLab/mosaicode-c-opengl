#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Elipse(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Elipse"
        self.color = "250:250:50:150"
        self.group = "2D Shapes"
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
                "label":"Radius",
                "conn_type":"Input",
                "name":"radius"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                "label":"FocusX",
                "conn_type":"Input",
                "name":"focusX"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                "label":"FocusY",
                "conn_type":"Input",
                "name":"focusY"}
            ]

        self.properties = [{"name": "radius",
                            "label": "Radius",
                            "type": MOSAICODE_FLOAT,
                            "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
			    "value": 0.5
                            },
                            {"name": "focusX",
                            "label": "Focus X",
                            "type": MOSAICODE_FLOAT,
                            "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.0,
                            },
                            {"name": "focusY",
                            "label": "Focus Y",
                            "type": MOSAICODE_FLOAT,
                            "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.5,
                            }
                           ]

        self.codes["global"] = """
        float focusX_$id$ = $prop[focusX]$;
        float focusY_$id$ = $prop[focusY]$;
        float radius_$id$ = $prop[radius]$;
        void $port[radius]$(float value){
            radius_$id$ = value;
        }
        void $port[focusX]$(float value){
            focusX_$id$ = value;
        }
        void $port[focusY]$(float value){
            focusY_$id$ = value;
        }
"""
        self.codes["function"] = """
        void mosaicgraph_draw_elipse(float radius,float elipse_x,float elipse_y){
            glColor3f(0.8f,0.6f,0.0);
            glBegin(GL_POLYGON);
            for (int i=0; i < 360; i++){
                    float degInRad = i*3.14159/180;
                    glVertex2f(cos(degInRad)*(radius+elipse_x),sin(degInRad)*(radius+elipse_y));
                }
            glEnd();
        }

"""
        self.codes["call"] = """
        mosaicgraph_draw_elipse(radius_$id$,focusX_$id$,focusY_$id$);
"""
