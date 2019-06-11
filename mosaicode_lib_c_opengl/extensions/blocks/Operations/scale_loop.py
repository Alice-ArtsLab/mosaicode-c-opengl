#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class ScaleLoop(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Scale Loop"
        self.color = "98:0:169:150"
        self.group = "Operations"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                    "label":"Flow",
                    "conn_type":"Input",
                    "name":"flow"},
                    {"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                    "label":"Flow",
                    "conn_type":"Output",
                    "name":"flow"}
            ]

        self.properties = [{"name": "x",
                            "label": "x",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "value": 0.01,
			    "page_inc": 0.1,
                            "page_size": 0.1,
                            },
                            {"name": "y",
                            "label": "y",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "value": 0.01,
			                 "page_inc": 0.1,
                            "page_size": 0.1,
                            },
                            {"name": "z",
                            "label": "z",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "value": 0.01,
			                 "page_inc": 0.1,
                            "page_size": 0.1,
                            },
                            {"name": "tamMax",
                            "label": "tamMax",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 10000.0,
                            "step": 0.001,
                            "value": 2.0,
			                 "page_inc": 0.1,
                            "page_size": 0.1,
                            },
                            {"name": "tamMin",
                            "label": "tamMin",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.001,
                            "value": 0.1,
			                 "page_inc": 0.1,
                            "page_size": 0.1,
                            }
                           ]
        self.codes["global"] = """
GLfloat xScale$id$,yScale$id$,zScale$id$;
GLint signal$id$;
"""
        self.codes["call"] = """
    glScalef(xScale$id$,yScale$id$,zScale$id$);
"""
        self.codes["idle"] = """
        if(signal$id$ == 0){
		    xScale$id$ += $prop[x]$;
		    yScale$id$ += $prop[y]$;
		    zScale$id$ += $prop[z]$;
		    if((xScale$id$ > $prop[tamMax]$) || (yScale$id$ > $prop[tamMax]$) || (zScale$id$ > $prop[tamMax]$)){
		    	signal$id$ = 1;
		    }
		}else{
			xScale$id$ -= $prop[x]$;
		    yScale$id$ -= $prop[y]$;
		    zScale$id$ -= $prop[z]$;
		    if((xScale$id$ < $prop[tamMin]$) || (yScale$id$ < $prop[tamMin]$) || (zScale$id$ < $prop[tamMin]$)){
		    	signal$id$ = 0;
		    }
		}
"""

        self.codes["execution"] = """
    xScale$id$ = yScale$id$ = zScale$id$ = 1.0;

"""
