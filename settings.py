import pygame as pg

class Settings:
    def __init__(self, language, color_mode, hover_color, active_color, background_color):
        self.hover_c = hover_color
        self.active_c = active_color
        self.background_c = background_color

        self.language = language
        self.color_mode = color_mode
        self.text_list = self.language_settings()

        self.x_sb   = 1410
        self.y      = 20
        self.width  = 30
        self.height = 30

        self.spanish_button = pg.rect.Rect(self.x_sb,self.y,self.width,self.height)
        # self.spanish_flag1 = pg.rect.Rect(self.x_sb,self.y,self.width,self.height/4)
        # self.spanish_flag2 = pg.rect.Rect(self.x_sb,self.y + 3*(self.height/4)+1,self.width,self.height/4)

        self.english_button = pg.rect.Rect(self.x_sb+self.width+10,self.y,self.width,self.height)
        # self.english_hb = pg.rect.Rect(self.x_sb+self.width+10,self.y+(self.height/3),self.width,(self.height/3))
        # self.english_vb = pg.rect.Rect(self.x_sb+self.width+10+(self.height/3),self.y,(self.width/3),self.height)
        # self.english_hr = pg.rect.Rect(self.x_sb+self.width+10,self.y+(self.height/3)+3,self.width,(self.height/3)-6)
        # self.english_vr = pg.rect.Rect(self.x_sb+self.width+10+(self.height/3)+3,self.y,(self.width/3)-6,self.height)

        self.es_br = pg.rect.Rect(self.x_sb-3,self.y-3,self.width+6,self.height+6)
        self.en_br = pg.rect.Rect(self.x_sb+self.width+10-3,self.y-3,self.width+6,self.height+6)

        self.es_is_hovered = False
        self.en_is_hovered = False
        self.es_is_active  = False
        self.en_is_active  = False

    def language_settings(self):
        if self.language == 'ES':
            title = "Calculadora de IPs"
            ip_type = "Tu Ip es de tipo:"
            clase = "Clase:"
            cidr = "CIDR:"
            ip_red = "Ip de red:"
            num_host = "Cantidad de host:"
            ip_broadcast = "Ip de broadcast:"
            error_message = "Input inválido"

        elif self.language == 'EN':
            title = "IPs calculator"
            ip_type = "Your Ip is type:"
            clase = "Class:"
            cidr = "CIDR:"
            ip_red = "Network Ip:"
            num_host = "Host cuantity:"
            ip_broadcast = "Broadcast Ip:"
            error_message = "Invalid input"

        return [title,ip_type,clase,cidr,ip_red,num_host,ip_broadcast,error_message]
    
    def handle_event(self,event):
        if event.type == pg.MOUSEMOTION:
            self.es_is_hovered = self.es_br.collidepoint(event.pos)

        elif event.type == pg.MOUSEMOTION:
            self.en_is_hovered = self.en_br.collidepoint(event.pos)

        elif event.type == pg.MOUSEBUTTONDOWN:
            self.es_is_active = self.es_br.collidepoint(event.pos)
            self.en_is_active = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            self.en_is_active = self.en_br.collidepoint(event.pos)
            self.es_is_active = False


    
    def draw_language_buttons(self, screen):
        color_extra_en = self.background_c
        color_extra_es = self.background_c
        if self.es_is_hovered:
            color_extra_es = self.hover_c
        elif self.en_is_hovered:
            color_extra_en = self.hover_c

        if self.es_is_active:
            color_extra_es = self.active_c
        elif self.en_is_active:
            color_extra_en = self.active_c

        pg.draw.rect(screen, color_extra_es, self.es_br)
        pg.draw.rect(screen, color_extra_en, self.en_br)

        pg.draw.rect(screen, 'yellow', self.spanish_button)
        # pg.draw.rect(screen, 'red', self.spanish_flag1)
        # pg.draw.rect(screen, 'red', self.spanish_flag2)

        pg.draw.rect(screen, 'blue', self.english_button)
        # pg.draw.rect(screen, 'white', self.english_hb)
        # pg.draw.rect(screen, 'white', self.english_vb)
        # pg.draw.rect(screen, 'red', self.english_hr)
        # pg.draw.rect(screen, 'red', self.english_vr)
