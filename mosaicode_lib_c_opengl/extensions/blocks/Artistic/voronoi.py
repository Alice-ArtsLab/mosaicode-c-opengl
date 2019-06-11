#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Voronoi(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Voronoi Diagram"
        self.color = "255:255:157:150"
        self.group = "Artistic"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Input",
                "name":"flow"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Output",
                "name":"flow"}
            ]
        self.properties = [{"name": "x1",
                            "label": "x1",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": -0.5,
                            },
                            {"name": "y1",
                            "label": "y1",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.5,
                            },
                            {"name": "x2",
                            "label": "x2",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": -0.5,
                            },
                            {"name": "y2",
                            "label": "y2",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": -0.5,
                            },
                            {"name": "x3",
                            "label": "x3",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.5,
                            },
                            {"name": "y3",
                            "label": "y3",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": -0.5,
                            },
                            {"name": "x4",
                            "label": "x4",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.5,
                            },
                            {"name": "y4",
                            "label": "y4",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.5,
                            },
                            {"name": "x5",
                            "label": "x5",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.0,
                            },
                            {"name": "y5",
                            "label": "y5",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.0,
                            },
                            {"name": "x6",
                            "label": "x6",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.0,
                            },
                            {"name": "y6",
                            "label": "y6",
                            "type": MOSAICODE_FLOAT,
                            "lower": -1.0,
                            "upper": 1.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 1.0,
                            }
                           ]
        
        self.codes["global"] = """
            vector<pnt> pontos$id$;
"""
        self.codes["call"] = """
            voronoi();
            for(auto i = pontos$id$.begin(); i!= pontos$id$.end();++i){
                mosaicgraph_draw_pnt((*i));
            }
        """

        self.codes["function"] = """
            void mosaicgraph_draw_pnt(pnt p){
                glColor3f(1.0,1.0,1.0);
                glBegin(GL_POLYGON);
                    glVertex2f(p.x-0.01,p.y-0.01);
                    glVertex2f(p.x+0.01,p.y-0.01);
                    glVertex2f(p.x+0.01,p.y+0.01);
                    glVertex2f(p.x-0.01,p.y+0.01);
                glEnd();
            }

            void auto_color(int value,int total){
                float passo=1;
                int r,g,b;
                passo = 1000/(float)total;
                passo = passo*value;
                r = passo/100;
                passo = passo -r*100;
                g = passo/10;
                b = passo - g*10;
                glColor3f((float)r/10.0,(float)g/10.0,(float)b/10.0);
            }
            void voronoi(){
                float x0,y0;
                vector<float> distancia;
                float aux,value=88888.9;
                int indice=0, atual;
                for(int i =0;i<500;i++){
                    for(int j=0;j<500;j++){
                        indice=0;
                        value=88888.9;
                        x0 = (float)i/250.0-1.0;
                        y0 = (float)j/250.0-1.0;
                        for(auto i = pontos$id$.begin(); i!= pontos$id$.end();++i){
                            aux = sqrt(pow(((*i).x-x0),2)+pow(((*i).y-y0),2));
                            if(aux < value){
                                value = aux;
                                atual = indice;
                            }
                            indice++; 
                        }
                        auto_color(atual,pontos$id$.size());
                        glBegin(GL_POINTS);
                        glVertex2f(x0,y0);
                        glEnd();

                    }
                        
                }
                distancia.clear();

            }
"""
        self.codes["declaration"] = """
            pnt value;
            value.x = $prop[x1]$;
            value.y = $prop[y1]$;
            pontos$id$.push_back(value);
            value.x = $prop[x2]$;
            value.y = $prop[y2]$;
            pontos$id$.push_back(value);
            value.x = $prop[x3]$;
            value.y = $prop[y3]$;
            pontos$id$.push_back(value);
            value.x = $prop[x4]$;
            value.y = $prop[y4]$;
            pontos$id$.push_back(value);
            value.x = $prop[x5]$;
            value.y = $prop[y5]$;
            pontos$id$.push_back(value);
            value.x = $prop[x6]$;
            value.y = $prop[y6]$;
            pontos$id$.push_back(value);
"""
