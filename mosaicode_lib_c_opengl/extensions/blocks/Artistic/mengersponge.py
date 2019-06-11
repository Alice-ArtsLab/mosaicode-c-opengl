#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MengerSponge(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Menger Sponge"
        self.color = "255:255:78:150"
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
                "name":"recursivity"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                "label":"Size",
                "conn_type":"Input",
                "name":"size"}
            ]
        self.properties = [{"name": "x",
                            "label": "x",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.0,
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
                            {"name": "z",
                            "label": "z",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.0,
                            },
                            {"name": "size",
                            "label": "size",
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
            float size_$id$ = $prop[size]$;
            float * $port[color]$;
            void $port[recursivity]$(float value){
                float_$id$ = value;
            }
            void $port[size]$(float value){
                size_$id$ = value;
            }
"""
        self.codes["call"] = """
            glColor3f($port[color]$[0],$port[color]$[1],$port[color]$[2]);
            mengersponge(float_$id$,$prop[x]$,$prop[y]$,$prop[z]$,$prop[size]$);
        """

        self.codes["function"] = """
            void mengersponge(int number, float size,float initx,float inity,float initz){
                float move;
                move = size/3.0;
                if(number > 1){
                    mengersponge(number-1,size/3.0,initx+move,inity+move,initz);
                    mengersponge(number-1,size/3.0,initx+move,inity,initz+move);
                    mengersponge(number-1,size/3.0,initx+move,inity+move,initz+move);
                    mengersponge(number-1,size/3.0,initx+move,inity-move,initz);
                    mengersponge(number-1,size/3.0,initx+move,inity,initz-move);
                    mengersponge(number-1,size/3.0,initx+move,inity-move,initz-move);
                    mengersponge(number-1,size/3.0,initx+move,inity-move,initz+move);
                    mengersponge(number-1,size/3.0,initx+move,inity+move,initz-move);

                    mengersponge(number-1,size/3.0,initx-move,inity+move,initz);
                    mengersponge(number-1,size/3.0,initx-move,inity,initz+move);
                    mengersponge(number-1,size/3.0,initx-move,inity+move,initz+move);
                    mengersponge(number-1,size/3.0,initx-move,inity-move,initz);
                    mengersponge(number-1,size/3.0,initx-move,inity,initz-move);
                    mengersponge(number-1,size/3.0,initx-move,inity-move,initz-move);
                    mengersponge(number-1,size/3.0,initx-move,inity-move,initz+move);
                    mengersponge(number-1,size/3.0,initx-move,inity+move,initz-move);

                    mengersponge(number-1,size/3.0,initx,inity+move,initz+move);
                    mengersponge(number-1,size/3.0,initx,inity-move,initz-move);
                    mengersponge(number-1,size/3.0,initx,inity+move,initz-move);
                    mengersponge(number-1,size/3.0,initx,inity-move,initz+move);
                    return;
                }else{
                    glPushMatrix();
                    glTranslatef(initx,inity,initz);
                    glutSolidCube(size);
                    glPopMatrix();
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
