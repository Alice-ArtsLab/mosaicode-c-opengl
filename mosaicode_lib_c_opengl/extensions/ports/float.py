from mosaicode.model.port import Port

class Float(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "FLOAT"
        self.color = "#fc2300"
        self.multiple = False
        self.code = "$output$.push_back($input$);\n"
        self.var_name = "$block[label]$_$port[name]$_$block[id]$"
