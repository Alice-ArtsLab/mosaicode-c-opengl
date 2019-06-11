#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class KochCurve(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Koch Curve"
        self.color = "255:255:39:150"
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
            kochcurve(float_$id$,$prop[x1]$,$prop[y1]$,$prop[x2]$,$prop[y2]$);
        """

        self.codes["function"] = """
            void kochcurve(int number,float x1, float y1, float x2, float y2){
                float distx = x2-x1,disty = y2-y1;
                float xm1 = x1+distx/3.0;
                float xm2 = x1+2.0*distx/3.0;
                float xm = x1+distx/2.0;
                float ym1 = y1+disty/3.0;
                float ym2 = y1+2.0*disty/3.0;
                float ym = y1+disty/2.0;
                float pontoAltox,pontoAltoy;
                float modulo = sqrt(pow(distx,2)+pow(disty,2));
                float xvec = distx/modulo;
                float yvec = disty/modulo;
                pontoAltoy = (modulo*xvec*sqrt(3.0))/(6.0);
                pontoAltox = -(pontoAltoy*yvec)/xvec;
                modulo = sqrt(pow(pontoAltox,2)+pow(pontoAltoy,2));
                pontoAltoy = ym+pontoAltoy;
                pontoAltox = xm+pontoAltox;
                if(number > 1){
                    kochcurve(number-1,x1,y1,xm1,ym1);
                    kochcurve(number-1,xm1,ym1,pontoAltox,pontoAltoy);
                    kochcurve(number-1,pontoAltox,pontoAltoy,xm2,ym2);
                    kochcurve(number-1,xm2,ym2,x2,y2);
                    return;
                }else{
                    glBegin(GL_LINE_STRIP);
                    glVertex2d(x1,y1);
                    glVertex2d(xm1,ym1);
                    glVertex2d(pontoAltox,pontoAltoy);//mudar
                    glVertex2d(xm2,ym2);
                    glVertex2d(x2,y2);
                    glEnd();
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
