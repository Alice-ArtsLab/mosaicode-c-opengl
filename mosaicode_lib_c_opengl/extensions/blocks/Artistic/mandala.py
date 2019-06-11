#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Mandala(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Mandala"
        self.color = "255:255:59:150"
        self.group = "Artistic"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Input",
                "name":"color"},
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
                            {"name": "slice",
                            "label": "slice",
                            "type": MOSAICODE_FLOAT,
                            "lower": 4.0,
                            "upper": 100.0,
                            "step": 1.00,
                            "page_inc": 1.00,
                            "page_size": 1.00,
                            "value": 6.0,
                            }]

      
        self.codes["global"] = """
            float * $port[color]$;
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
            render$id$();
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
                pixel.x = (((float)xMouse$id$-(float)width$id$/2.0)/(float)width$id$*2.0);
                pixel.y = (((float)yMouse$id$-(float)width$id$/2.0)/(float)width$id$*2.0);
                pincel$id$.push_back(pixel);
            }

            void render$id$(){
                float angule,r;
                glColor3f($port[color]$[0],$port[color]$[1],$port[color]$[2]);
                for(auto j = objetos$id$.begin(); j!= objetos$id$.end();++j){
                    for(int k=0;k<$prop[slice]$;k++){
                        glBegin(GL_LINE_STRIP);
                        for (auto i = (*j).begin(); i!= (*j).end();++i){
                            r = sqrt(pow(i->x,2)+pow(i->y,2));        
                            angule = atan2(i->x,i->y);
                            angule = angule *180.0/3.1415;
                            angule = (float)k*360.0/$prop[slice]$+angule;
                            angule = angule/180.0*3.1415;
                            glVertex2d(r*cos(angule),r*sin(angule));
                        }
                        glEnd();
                    }
                }
                glBegin(GL_LINE_STRIP);
                for (auto i = pincel$id$.begin(); i!= pincel$id$.end();++i){
                    glVertex2d(i->x,-i->y);
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
"""