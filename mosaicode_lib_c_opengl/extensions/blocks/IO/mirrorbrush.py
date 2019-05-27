#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MirrorBrush(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Mirror Brush"
        self.color = "200:200:50:100"
        self.group = "I/O"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Input",
                "name":"color"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"ColorMirror",
                "conn_type":"Input",
                "name":"colormirror"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Input",
                "name":"flow"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Output",
                "name":"flow"},
                    ]
        self.properties = [{"name": "clear",
                            "label": "clear",
                            "type": MOSAICODE_STRING,
                            "value": "x"
                            },
                            {"name": "last",
                            "label": "last",
                            "type": MOSAICODE_STRING,
                            "value": "z"
                            },
                            {"name": "type",
                            "label": "type",
                            "type": MOSAICODE_COMBO,
                            "values": ["vertical",
                                        "horizontal",
                                        "diagonal"],
                            "value": "vertical",
                            }]

      
        self.codes["global"] = """
string type$id$ ("$prop[type]$");
float * $port[color]$;
float * $port[colormirror]$;
float bool$id$ = 0;
int xMouse$id$,yMouse$id$,width$id$;
vector<vector<pnt>> objetos$id$;
vector<pnt> pincel$id$;
bool press$id$ = false;
void draw$id$();

"""
        self.codes["call"] = """
        if(press$id$){
            draw$id$();
        }
        mirror$id$();
        glOrtho(-1.0,1.0,-1.0,1.0,0.0,0.0);
"""

        self.codes["execution"] = """
        width$id$ = window->width;
        glutMotionFunc(movementMouse$id$);
        glutMouseFunc(onMouseBrush$id$);

"""
        self.codes["function"] = """
        void movementMouse$id$(int x, int y){
    if (press$id$ == true && (xMouse$id$ != x || yMouse$id$ != y)){
        xMouse$id$ = x;
        yMouse$id$ = y;
        draw$id$();
    }
}
void onMouseBrush$id$(int button, int state, int x, int y){
    if ((button == GLUT_LEFT_BUTTON) && (state == GLUT_DOWN)) {
        xMouse$id$ = x;
        yMouse$id$ = y;
        press$id$ = true;
        draw$id$();
    }if (button == GLUT_LEFT_BUTTON && state == GLUT_UP) {
        press$id$ = false;
        objetos$id$.push_back(pincel$id$);
        pincel$id$.clear();
    }
}
void draw$id$(){
    pnt pixel;
    pixel.x = xMouse$id$;
    pixel.y = yMouse$id$;
    pincel$id$.push_back(pixel);
}

void mirror$id$(){
    for(auto j = objetos$id$.begin(); j!= objetos$id$.end();++j){
        glColor3f($port[color]$[0],$port[color]$[1],$port[color]$[2]);
        glBegin(GL_LINE_STRIP);
        for (auto i = (*j).begin(); i!= (*j).end();++i){
            glVertex2d(((float)i->x-(float)width$id$/2.0)/(float)width$id$*2.0,-((float)i->y-(float)width$id$/2.0)/(float)width$id$*2.0);
        }
        glEnd();
        if(type$id$.compare("vertical")==0){    
            glBegin(GL_LINE_STRIP);
            glColor3f($port[colormirror]$[0],$port[colormirror]$[1],$port[colormirror]$[2]);
            for (auto i = (*j).begin(); i!= (*j).end();++i){
                glVertex2d(-((float)i->x-(float)width$id$/2.0)/(float)width$id$*2.0,-((float)i->y-(float)width$id$/2.0)/(float)width$id$*2.0);
            }
            glEnd();
        }else if(type$id$.compare("horizontal")==0){    
            glBegin(GL_LINE_STRIP);
            glColor3f($port[colormirror]$[0],$port[colormirror]$[1],$port[colormirror]$[2]);
            for (auto i = (*j).begin(); i!= (*j).end();++i){
                glVertex2d(((float)i->x-(float)width$id$/2.0)/(float)width$id$*2.0,((float)i->y-(float)width$id$/2.0)/(float)width$id$*2.0);
            }
            glEnd();
        }else if(type$id$.compare("diagonal")==0){    
            glBegin(GL_LINE_STRIP);
            glColor3f($port[colormirror]$[0],$port[colormirror]$[1],$port[colormirror]$[2]);
            for (auto i = (*j).begin(); i!= (*j).end();++i){
                glVertex2d(-((float)i->x-(float)width$id$/2.0)/(float)width$id$*2.0,((float)i->y-(float)width$id$/2.0)/(float)width$id$*2.0);
            }
            glEnd();
        }
        
    }
    glBegin(GL_LINE_STRIP);
    glColor3f(1.0,1.0,1.0);
    for (auto i = pincel$id$.begin(); i!= pincel$id$.end();++i){
        glVertex2d(((float)i->x-(float)width$id$/2.0)/(float)width$id$*2.0,-((float)i->y-(float)width$id$/2.0)/(float)width$id$*2.0);
    }
    glEnd();
}


"""

        self.codes["keyboard"] = """
    if (key == (int)'$prop[clear]$'){
        objetos$id$.clear();
    }if (key == (int)'$prop[last]$'){
        objetos$id$.pop_back();
    }
"""

        self.codes["declaration"] = """
        $port[color]$ = (float*)malloc (3 * sizeof (float));
        $port[color]$[0] = 1.0;
        $port[color]$[1] = 0.5;
        $port[color]$[2] = 0.0;
        $port[colormirror]$ = (float*)malloc (3 * sizeof (float));
        $port[colormirror]$[0] = 0.0;
        $port[colormirror]$[1] = 0.5;
        $port[colormirror]$[2] = 1.0;
"""