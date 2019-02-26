#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Color(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Color"
        self.color = "77:00:146:150"
        self.group = "Types"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Output",
                "name":"color"}
            ]

        self.properties = [{"name": "color",
                            "label": "Color",
                            "value":"#FF0000",
                            "format":"FF0000",
                            "type": MOSAICODE_COLOR
			                }]

        self.codes["function"] = """
void convert_text_to_color(const char * rgbColor, float * output){
    if (strlen(rgbColor) < 7 || rgbColor[0] != '#'){
        output[0] = 0.0;
        output[1] = 0.0;
        output[2] = 0.0;
        }

    char * r = (char*)malloc(2*sizeof(char)), * g= (char*)malloc(2*sizeof(char)), *b= (char*)malloc(2*sizeof(char));
    r[0] = rgbColor[1];
    r[1] = rgbColor[2];
    g[0] = rgbColor[3];
    g[1] = rgbColor[4];
    b[0] = rgbColor[5];
    b[1] = rgbColor[6];

    float ri=0.0, gi =0.0, bi =0.0;
    ri = (float) strtol(r, NULL, 16);
    gi = (float) strtol(g, NULL, 16);
    bi = (float) strtol(b, NULL, 16);

    output[0] = ri / 255.0;
    output[1] = gi / 255.0;
    output[2] = bi / 255.0;
}
"""

        self.codes["declaration"] = """
        // Color Baby!
		float $port[color]$[3];
        convert_text_to_color("$prop[color]$", $port[color]$);
"""