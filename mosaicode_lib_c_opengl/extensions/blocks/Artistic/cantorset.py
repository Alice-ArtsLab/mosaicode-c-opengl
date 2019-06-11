#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class CantorSet(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Cantor Set"
        self.color = "255:255:20:150"
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
                            "value": 0.9,
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
                            "value": -1.0,
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
            cantorset(float_$id$,$prop[x1]$,$prop[x2]$,$prop[y1]$,$prop[y2]$);
        """

        self.codes["function"] = """
            void cantorset(int number, float x1, float x2,float y1,float y2){
                float xm1,xm2,ynew;
                xm1 = x1+(x2-x1)/3.0;
                xm2 = x1+2.0*(x2-x1)/3.0;
                ynew = y1-(y1-y2)/(float)number;
                glBegin(GL_LINES);
                glVertex2d(x1,y1);
                glVertex2d(x2,y1);
                glEnd();
                if(number > 1){
                    cantorset(number-1,x1,xm1,ynew,y2);
                    cantorset(number-1,xm2,x2,ynew,y2);
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
