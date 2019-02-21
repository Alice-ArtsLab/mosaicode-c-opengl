#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Window class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class WindowProperties(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Window Properties"
        self.color = "250:150:150:150"
        self.group = "Window"

        self.properties = [{"name": "x",
                            "label": "x",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 2000,
                            "step": 1,
                            "value": 0,
                            },
                            {"name": "y",
                            "label": "y",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 2000,
                            "step": 1,
                            "value": 0,
                            },
                            {"name": "width",
                            "label": "width",
                            "type": MOSAICODE_INT,
                            "lower": 100,
                            "upper": 2000,
                            "step": 1,
                            "value": 500,
                            },
                            {"name": "height",
                            "label": "height",
                            "type": MOSAICODE_INT,
                            "lower": 100,
                            "upper": 2000,
                            "step": 1,
                            "value": 500,
                            },
                            {"name": "title",
                            "label": "title",
                            "type": MOSAICODE_STRING,
                            "value": "New Window",
                            },
                            {"name": "polygon",
                            "label": "polygon",
                            "type": MOSAICODE_COMBO,
                            "values": ["GL_FILL",
                                        "GL_LINE",
                                        "GL_POINT"],
                            "value": "GL_LINE",
                            },
                            {"name": "background",
                            "label": "background",
                            "type": MOSAICODE_COLOR,
                            "value": "#A83333"
                            }

                           ]
        self.codes["declaration"] = """
        float background$id$[3];
        convert_text_to_color_background("$prop[background]$", background$id$);
        window->x = $prop[x]$;
        window->y = $prop[y]$;
        window->red = background$id$[0];
        window->green = background$id$[1];
        window->blue = background$id$[2];
        window->alpha = 1.0;
        window->width = $prop[width]$;
        window->height = $prop[height]$;
        strcpy(window->title, "$prop[title]$");
"""
        self.codes["call"] = """
        glPolygonMode(GL_FRONT_AND_BACK, $prop[polygon]$);
"""

        self.codes["function"] = """
        void convert_text_to_color_background(const char * rgbColor, float * output){
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