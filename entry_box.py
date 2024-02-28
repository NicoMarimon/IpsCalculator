import pygame as pg

WHITE = (255,255,255)

class EntryBox:
    def __init__(self, x_sub, y_sub, x_big, y_big, font, error_font, active_color, hover_color, default_color, error_color, bin_color, subtitle_text):

        # Definimos rectángulo grande y pqueño
        self.width_big = 220
        self.height_big = 36
        self.big_rectangle = pg.rect.Rect(x_big,y_big,self.width_big,self.height_big)
        self.small_rectangle = pg.rect.Rect(x_big + 3,y_big + 3,self.width_big - 6,self.height_big - 6)

        # Text x y
        self.x_sub = x_sub
        self.y_sub = y_sub
        
        # Definimos fuente
        self.font = font
        self.error_font = error_font

        # Definimos colores
        self.default_color = default_color
        self.active_color = active_color
        self.hover_color = hover_color
        self.error_color = error_color
        self.bin_color = bin_color

        # Definimos booleanos necesarios
        self.is_hovered = False
        self.is_active = False
        self.permiso = False

        # Definimos textos
        self.subtitle_text = subtitle_text
        self.text = ''
        self.error_text = ''


    # Función para validar input
    def es_valida(self, text):
        text_list = text.split('.')
        if len(text_list) == 4:
            for i in text_list:
                if i == '':
                    return False
                elif int(i) <= 255:
                    continue
                else:
                    return False
            return True
        else:
            return False

    # Función para manejar eventos
    def handle_events(self, event, otro_bool):
        # Evento si el ratón está sobre la caja
        if event.type == pg.MOUSEMOTION:
            self.is_hovered = self.big_rectangle.collidepoint(event.pos)

        # Evento el ratón hace click sobre la caja
        elif event.type == pg.MOUSEBUTTONDOWN:
            if self.big_rectangle.collidepoint(event.pos) and not otro_bool:
                self.is_active = True
                self.permiso = False

        # Evento pulsa tecla
        elif event.type == pg.KEYDOWN and self.is_active:

            # Si pulsa la tecla de borrar
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]

            # Pulsa numero o "."
            elif len(self.text) < 15 and event.key in [pg.K_0,pg.K_1,pg.K_2,pg.K_3,pg.K_4,pg.K_5,pg.K_6,pg.K_7,pg.K_8,pg.K_9,pg.K_PERIOD]:
                self.text += event.unicode

            # Pulsa Eeter
            elif event.key == pg.K_RETURN:
                if self.es_valida(self.text):
                    self.is_active = False
                    self.error_text = ''
                    self.permiso = True
                else:
                    self.error_text = 'Invalid input'

    # Función para dibujar por pantalla
    def draw(self, screen, bin_str):
        color = self.default_color

        # Definimos el color según el booleano activo
        if self.is_active:
            color = self.active_color
        elif self.is_hovered:
            color = self.hover_color

        # Pintamos rectángulos
        pg.draw.rect(screen, color, self.big_rectangle)
        pg.draw.rect(screen, WHITE, self.small_rectangle)

        # Iprimimos texto escrito por pantalla
        text_surface = self.font.render(self.text, True, color)
        screen.blit(text_surface, (self.big_rectangle.x + 4, self.big_rectangle.y + 4))

        # Imprimimos Subtítulo por pantalla
        subtitle_surface = self.font.render(self.subtitle_text + ':', True, color)
        screen.blit(subtitle_surface, (self.x_sub, self.y_sub))

        # Imprimimos mensaje de error por pantalla
        error_surface = self.error_font.render(self.error_text, True, self.error_color)
        screen.blit(error_surface, (380, self.y_sub))

        # Imprimimos mensaje de error por pantalla
        if self.error_text == '':
            bin_surface = self.error_font.render(bin_str, True, self.bin_color)
            screen.blit(bin_surface, (380, self.y_sub))

    # Exporta un string con la máscara o la ip si es que es correcta.
    def export_num(self):
        if self.permiso:
            return self.text
        else:
            return ''



        
                    




