#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class SierpinskiCarpet(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Sierpinski Carpet"
        self.color = "255:255:118:150"
        self.group = "Artistic"
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
                "label":"Recursivity",
                "conn_type":"Input",
                "name":"recursivity"}
            ]
        self.properties = [{"name": "x1",
                            "label": "x1",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": -1.0,
                            },
                            {"name": "y1",
                            "label": "y1",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": -1.0,
                            },
                            {"name": "x2",
                            "label": "x2",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 1.0,
                            },
                            {"name": "y2",
                            "label": "y2",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 1.0,
                            },
                            {"name": "recursivity",
                            "label": "recursivity",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.0,
                            "upper": 100.0,
                            "step": 1.00,
                            "page_inc": 1.00,
                            "page_size": 1.00,
                            "value": 5.0,
                            }
                           ]
        
        self.codes["global"] = """
            float float_$id$ = $prop[recursivity]$;
            float * $port[color]$;
            void $port[recursivity]$(float value){
                float_$id$ = value;
            }
"""
        self.codes["call"] = """
        glColor3f($port[color]$[0],$port[color]$[1],$port[color]$[2]);
        sierpinskicarpet(float_$id$,$prop[x1]$,$prop[y1]$,$prop[x2]$,$prop[y2]$);
        """

        self.codes["function"] = """
        void sierpinskicarpet(int number, float x1, float y1, float x2,float y2){
            float lenX,lenY;
            lenX = x1-x2;
            lenY = y1-y2;
            glBegin(GL_QUADS);
            glVertex2d(x1-lenX/3.0,y1-lenY/3.0);
            glVertex2d(x1-lenX/3.0,y2+lenY/3.0);
            glVertex2d(x2+lenX/3.0,y2+lenY/3.0);
            glVertex2d(x2+lenX/3.0,y1-lenY/3.0);
            glEnd();
            if(number > 1){
                //float x12,y12,x23,y23,x13,y13;
                sierpinskicarpet(number-1,x1,y1,x1-lenX/3.0,y1-lenY/3.0);
                sierpinskicarpet(number-1,x1-lenX/3.0,y1,x2+lenX/3.0,y1-lenY/3.0);
                sierpinskicarpet(number-1,x2+lenX/3.0,y1,x2,y1-lenY/3.0);
                sierpinskicarpet(number-1,x2+lenX/3.0,y1-lenY/3.0,x2,y2+lenY/3.0);
                sierpinskicarpet(number-1,x2+lenX/3.0,y2+lenY/3.0,x2,y2);
                sierpinskicarpet(number-1,x1-lenX/3.0,y2+lenY/3.0,x2+lenX/3.0,y2);
                sierpinskicarpet(number-1,x1,y2+lenY/3.0,x1-lenX/3.0,y2);
                sierpinskicarpet(number-1,x1,y1-lenY/3.0,x1-lenX/3.0,y2+lenY/3.0);
                return;
            }else{
                return;
            }
        }
"""
        self.codes["declaration"] = """
        $port[color]$ = (float*)malloc (3 * sizeof (float));
        $port[color]$[0] = 1.0;
        $port[color]$[1] = 0.5;
        $port[color]$[2] = 1.0;
"""
