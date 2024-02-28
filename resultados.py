class Resultados:
    def __init__(self, cidr, que_ip, class_ip, cless_cfull, ip_red, cantidad_host, ip_broadcast, subtitle_color, results_color, classless_color, classfull_color, font, title_font, title_color, text_list):
        self.font = font
        self.title_font = title_font
        self.text_list = text_list

        self.title_color = title_color
        self.result_color    = results_color
        self.subtitle_color  = subtitle_color
        self.classless_color = classless_color
        self.classfull_color = classfull_color

        self.que_ip       = que_ip
        self.class_ip     = class_ip
        self.cless_cfull  = cless_cfull
        self.cidr         = cidr
        self.ip_red       = ip_red
        self.hosts        = cantidad_host
        self.ip_broadcast = ip_broadcast


    def draw(self, screen):
        title_surface = self.title_font.render(self.text_list[0], True, self.title_color)
        screen.blit(title_surface, (20,20))


        que_ip_sub_surface = self.font.render(self.text_list[1], True, self.subtitle_color)
        screen.blit(que_ip_sub_surface, (20,220))
        que_ip_surface = self.font.render(str(self.que_ip), True, self.result_color)
        screen.blit(que_ip_surface, (300,220))

        class_ip_sub_surface = self.font.render(self.text_list[2], True, self.subtitle_color)
        screen.blit(class_ip_sub_surface, (20,270))
        class_ip_surface = self.font.render(str(self.class_ip), True, self.result_color)
        screen.blit(class_ip_surface, (300,270))

        color = self.classfull_color
        if self.cless_cfull == 'Classless':
            color = self.classless_color
        cless_cfull_surface = self.font.render(self.cless_cfull, True, color)
        screen.blit(cless_cfull_surface, (340,270))
        
        cidr_sub_surface = self.font.render(self.text_list[3], True, self.subtitle_color)
        screen.blit(cidr_sub_surface, (20,320))
        cidr_surface = self.font.render(str(self.cidr), True, self.result_color)
        screen.blit(cidr_surface, (300,320))

        ip_red_sub_surface = self.font.render(self.text_list[4], True, self.subtitle_color)
        screen.blit(ip_red_sub_surface, (20,370))
        ip_red_surface = self.font.render(str(self.ip_red), True, self.result_color)
        screen.blit(ip_red_surface, (300,370))

        hosts_sub_surface = self.font.render(self.text_list[5], True, self.subtitle_color)
        screen.blit(hosts_sub_surface, (20,420))
        hosts_surface = self.font.render(str(self.hosts), True, self.result_color)
        screen.blit(hosts_surface, (300,420))

        ip_broadcast_sub_surface = self.font.render(self.text_list[6], True, self.subtitle_color)
        screen.blit(ip_broadcast_sub_surface, (20,470))
        ip_broadcast_surface = self.font.render(str(self.ip_broadcast), True, self.result_color)
        screen.blit(ip_broadcast_surface, (300,470))

