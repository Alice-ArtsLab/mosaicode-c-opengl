from mosaicode.model.port import Port

class Float(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "COLOR"
        self.color = "#2c6300"
        self.multiple = False
        self.code = "$input$ = $output$;"
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"	
