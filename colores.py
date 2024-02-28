class SetColors:
    def __init__(self , color_mode):
        # Definir colores
        self.WHITE            = (255, 255, 255)
        self.BLACK            = (  0,   0,   0)
        self.RED              = (255,   0,   0)
        self.GREEN            = (  0, 255,   0)
        self.BLUE             = (  0,   0, 255)
        self.MAGENTA          = (255,   0, 255)
        self.GRAY             = (130, 130, 130)
        self.LIGHT_BLUE       = (  0, 191, 235)
        self.LIGHT_GRAY       = (169, 169, 169)

        self.GRAY_E           = ()

        self.color_moode = color_mode

    def set_colors(self):
        if self.color_moode == 'NORMAL':
            
            title_color      = self.BLACK      # Título
            color_backgruond = self.GRAY       # Fondo
            default_color    = self.LIGHT_GRAY # Default de rg e input del usuario
            color_subtitle   = self.WHITE      # Subtítulo
            color_results    = self.BLACK      # Resultados
            color_error      = self.RED        # Mensaje de error
            color_hover      = self.LIGHT_BLUE # Hover
            color_active     = self.BLUE       # Active
            color_bin        = self.GREEN      # Binario
            classless_color  = self.RED        # Classless
            classfull_color  = self.GREEN      # Classfull

        elif self.color_moode == 'EARTHTHONE':

            title_color      = self.BLACK      # Título
            color_backgruond = self.GRAY       # Fondo
            default_color    = self.LIGHT_GRAY # Default de rg e input del usuario
            color_subtitle   = self.WHITE      # Subtítulo
            color_results    = self.BLACK      # Resultados
            color_error      = self.RED        # Mensaje de error
            color_hover      = self.LIGHT_BLUE # Hover
            color_active     = self.BLUE       # Active
            color_bin        = self.GREEN      # Binario
            classless_color  = self.RED        # Classless
            classfull_color  = self.GREEN      # Classfull

        return title_color, color_backgruond, default_color, color_subtitle, color_results, color_error, color_hover, color_active, color_bin, classless_color, classfull_color
            
