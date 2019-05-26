#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class PeanoCurve(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Peano Curve"
        self.color = "75:75:75:100"
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
                            {"name": "y",
                            "label": "y",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.0,
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
        peanox(float_$id$,$prop[x1]$,$prop[x2]$,$prop[y]$);
        """

        self.codes["function"] = """
            void peanox(int number, float x1, float x2,float y);
            void peanoy(int number, float y1, float y2,float x){
                float xm1,xm2,ym1,ym2;
                ym1 = y1+(y2-y1)/3.0;
                ym2 = y1+2.0*(y2-y1)/3.0;
                xm1 = x+(y2-y1)/3.0;
                xm2 = x-(y2-y1)/3.0;
                glPushMatrix();
                glBegin(GL_LINES);
                glVertex2d(x,y1);
                glVertex2d(x,y2);
                glEnd();
                glBegin(GL_LINE_STRIP);
                glVertex2d(xm1,ym1);
                glVertex2d(xm1,ym2);
                glVertex2d(xm2,ym2);
                glVertex2d(xm2,ym1);
                glVertex2d(xm1,ym1);
                glEnd();
                glPopMatrix();
                if(number > 1){
                    peanoy(number-1,y1,ym1,x);
                    peanoy(number-1,ym1,ym2,x);
                    peanoy(number-1,ym2,y2,x);
                    peanoy(number-1,ym1,ym2,xm1);
                    peanoy(number-1,ym1,ym2,xm2);
                    peanox(number-1,xm1,x,ym1);
                    peanox(number-1,x,xm2,ym1);
                    peanox(number-1,xm1,x,ym2);
                    peanox(number-1,x,xm2,ym2);
                    return;
                }else{
                    return;
                }
            }
            void peanox(int number, float x1, float x2,float y){
                float xm1,xm2,ym1,ym2;
                xm1 = x1+(x2-x1)/3.0;
                xm2 = x1+2.0*(x2-x1)/3.0;
                ym1 = y+(x2-x1)/3.0;
                ym2 = y-(x2-x1)/3.0;
                glPushMatrix();
                glBegin(GL_LINES);
                glVertex2d(x1,y);
                glVertex2d(x2,y);
                glEnd();
                glBegin(GL_LINE_STRIP);
                glVertex2d(xm1,ym1);
                glVertex2d(xm1,ym2);
                glVertex2d(xm2,ym2);
                glVertex2d(xm2,ym1);
                glVertex2d(xm1,ym1);
                glEnd();
                glPopMatrix();
                if(number > 1){
                    peanox(number-1,x1,xm1,y);
                    peanox(number-1,xm1,xm2,y);
                    peanox(number-1,xm2,x2,y);
                    peanox(number-1,xm1,xm2,ym1);
                    peanox(number-1,xm1,xm2,ym2);
                    peanoy(number-1,ym1,y,xm1);
                    peanoy(number-1,y,ym2,xm1);
                    peanoy(number-1,ym1,y,xm2);
                    peanoy(number-1,y,ym2,xm2);
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
