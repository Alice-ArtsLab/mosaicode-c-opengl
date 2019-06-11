#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Triangle(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Triangle"
        self.color = "255:98:98:150"
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
                "label":"Scale",
                "conn_type":"Input",
                "name":"scale"}
            ]

        self.properties = [{"name": "base",
                            "label": "base",
                            "type": MOSAICODE_FLOAT,
                            "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.5,
                            },
                            {"name": "altura",
                            "label": "altura",
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
        float scale_$id$ = 1.0;
        float * $port[color]$;
        void $port[scale]$(float value){
            scale_$id$ = value;
        }
"""
        self.codes["function"] = """

        void mosaicgraph_draw_triangle(float base,float altura, float * rgb){
            glColor3f(rgb[0],rgb[1],rgb[2]);
            float x0 = 0.0 - base/2.0;
            float y0 = 0.0 - altura/2.0;
            glBegin(GL_POLYGON);
                glVertex2f(x0,y0);
                x0 = 0.0;
                y0 = y0 + altura;
                glVertex2f(x0,y0);
                x0 = 0.0 + base/2.0;
                y0 = y0 - altura;
                glVertex2f(x0,y0);
            glEnd();
        }

"""
        self.codes["declaration"] = """
        $port[color]$ = (float*)malloc (3 * sizeof (float));
        $port[color]$[0] = 1.0;
        $port[color]$[1] = 0.5;
        $port[color]$[2] = 0.0;
"""
        self.codes["call"] = """
        glPushMatrix();
        glScalef(scale_$id$,scale_$id$,0.0);
        mosaicgraph_draw_triangle($prop[base]$,$prop[altura]$,$port[color]$);
        glPopMatrix();
"""
