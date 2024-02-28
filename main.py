import pygame as pg
import sys
from pantalla import Pantalla
from entry_box import EntryBox
from colores import SetColors
from calculator import Calculator
from resultados import Resultados
from settings import Settings


# COLORES
title_c, background_c, default_c, subtitle_c, results_c, error_c, hover_c, active_c, bin_c, cless_c, cfull_c = SetColors('NORMAL').set_colors()


# PANTALLA
WIDTH = 1500
HEIGHT = 700
scrn = Pantalla(WIDTH,HEIGHT)


# FUENTES (Montserrat)
montserrat_bold = 'fuente/static/Montserrat-Bold.ttf'
montserrat_italic = 'fuente/static/Montserrat-BoldItalic.ttf'

fuente_titulo   = pg.font.Font(montserrat_bold, 32)
fuente          = pg.font.Font(montserrat_bold, 25)
fuente_error    = pg.font.Font(montserrat_italic, 25)
fuente_bin      = pg.font.Font(montserrat_italic, 15)


# ENTRY BOX
entry_box_ip = EntryBox(x_sub=20, y_sub=80, x_big=147, y_big=77, font=fuente, error_font=fuente_error, active_color=active_c, hover_color=hover_c, default_color=default_c, error_color=error_c, bin_color=bin_c, subtitle_text='IP')# Class idioma
entry_box_mask = EntryBox(x_sub=20, y_sub=140, x_big=147, y_big=137, font=fuente, error_font=fuente_error, active_color=active_c, hover_color=hover_c, default_color=default_c, bin_color=bin_c, error_color=error_c, subtitle_text='MASK')# Class idioma

while True:
    # Inicializamos SETTINGS
    conf = Settings(language='EN',color_mode='', hover_color=default_c, active_color=hover_c, background_color=background_c)
    text_list = conf.text_list

    # Entry box activas
    ip_active = entry_box_ip.is_active
    mask_active = entry_box_mask.is_active

    # Exportamos IP y MASK a main.py
    ip = entry_box_ip.export_num()
    mask = entry_box_mask.export_num()

    # Declarando variables vacías
    ip_bin  = '' # MOSTRAR BINARIO O NO
    mask_bin = ''

    mask_cidr    = ''
    que_ip       = ''
    ip_red       = ''
    ip_broadcast = ''
    num_host     = ''
    class_ip     = ''
    cless_cfull  = ''

    # Inicializamos calculadora
    if ip != '' and mask != '':
        calculadora = Calculator(ip, mask)

        ip_bin = calculadora.bin_str_ip
        mask_bin = calculadora.bin_str_mask

        mask_cidr    = '/'+calculadora.cidr_str
        que_ip       = calculadora.que_ip
        ip_red       = calculadora.ip_red_str
        ip_broadcast = calculadora.ip_broadcast_str
        num_host     = calculadora.cant_host
        class_ip     = calculadora.class_ip
        cless_cfull  = calculadora.cless_cfull

    # Inicializamos resultados
    results = Resultados(cidr=mask_cidr, que_ip=que_ip, class_ip=class_ip, cless_cfull=cless_cfull, cantidad_host=num_host, ip_red=ip_red, ip_broadcast=ip_broadcast, subtitle_color=subtitle_c, results_color=results_c, classless_color=cless_c, classfull_color=cfull_c, font=fuente, title_font=fuente_titulo, title_color=title_c, text_list=text_list)



    for event in pg.event.get():
        # Cierre del prgram
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        # Control de eventos para el input de la IP
        entry_box_ip.handle_events(event, mask_active)
        

        # Control de eventos para el input de la MASK
        entry_box_mask.handle_events(event, ip_active)

        conf.handle_event(event)

    # Dibujando botones idioma
    conf.draw_language_buttons(scrn.screen)

    # Color de fondo
    scrn.screen.fill(background_c)

    # Dibujar botones idioma
    conf.draw_language_buttons(scrn.screen)

    # Dibujamos todo IP
    entry_box_ip.draw(scrn.screen, ip_bin)

    # Dibujamos todo MASK
    entry_box_mask.draw(scrn.screen, mask_bin)

    # Dibujamos Resultados
    results.draw(scrn.screen)

    scrn.update_screen()