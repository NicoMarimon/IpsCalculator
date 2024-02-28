import funciones as f

class Calculator:
    def __init__(self, ip, mask):
        self.str_ip   = ip
        self.str_mask = mask

        self.bin_list_ip         = self.pasar_bin(self.str_ip)
        self.bin_list_mask       = self.pasar_bin(self.str_mask)

        self.cidr_num = self.cidr()

        self.bin_list_red        = self.calcular_redObroadcast(0)
        self.bin_list_broadcast  = self.calcular_redObroadcast(1)

        self.bin_str_ip   = self.binAstr(self.bin_list_ip)
        self.bin_str_mask = self.binAstr(self.bin_list_mask)
        self.cidr_str = str(self.cidr_num)
        self.ip_red_bin_str = self.binAstr(self.bin_list_red)
        self.ip_broadcast_bin_str = self.binAstr(self.bin_list_broadcast)
        self.ip_red_str = self.pasar_bin_a_normal(self.bin_list_red)
        self.ip_broadcast_str = self.pasar_bin_a_normal(self.bin_list_broadcast)
        self.que_ip = self.tipo_ip()
        self.cant_host = self.num_host()
        self.class_ip = self.clase_ip()
        self.cless_cfull = self.classfull_classless()

    # Esta función pasa las IPs o las Máscaras a binario
    def pasar_bin(self, str):   
        num_list = str.split('.')
        bin_list = []

        for i in num_list:
            numero = int(i)
            bin_num = []
            resul = 'x'
            resto = 'x'
            while resul != 0:
                resul = numero // 2
                resto = numero % 2
                numero = resul
                bin_num.append(resto)
            while len(bin_num) != 8:
                bin_num.append(0)
            bin_num = bin_num[::-1]
            bin_list.append(bin_num)

        return bin_list # [[x,x,x,x,x,x,x,x],[x,x,x,x,x,x,x,x],[x,x,x,x,x,x,x,x],[x,x,x,x,x,x,x,x]]
    
    # Esta función devuelve un string para imprimir el binario en pantalla
    def binAstr(self, bin_list):
        bin_str = ''
        iteracion = 0
        for i in bin_list:
            for j in i:
                bin_str +=str(j)
            iteracion += 1
            if iteracion <= 3:
                bin_str += '    '
        
        return bin_str # "xxxxxxxx    xxxxxxxx    xxxxxxxx    xxxxxxxx"
    
    def pasar_bin_a_normal (self, list):
        # Esta función pasa una IP o una Máscara de binario a normal.
        normal = []

        for i in list:
            num = 0
            if i[0] == 1:
                num += 128
            if i[1] == 1:
                num += 64
            if i[2] == 1:
                num += 32
            if i[3] == 1:
                num += 16
            if i[4] == 1:
                num += 8
            if i[5] == 1:
                num += 4
            if i[6] == 1:
                num += 2
            if i[7] == 1:
                num += 1
            normal.append(num)
        
        normal_str = str(normal[0]) + '.' + str(normal[1]) + '.' + str(normal[2]) + '.' + str(normal[3])

        return normal_str # "xxx.xxx.xxx.xxx"
    
    # Esta función calcula la máscara en notación CIDR
    def cidr(self):
        reversed_mask = f.reverse_list(self.bin_list_mask)
        mask_CIDR = 32
        for eight_bits in reversed_mask:
            for bit in f.reverse_list(eight_bits):
                if bit == 0:
                    mask_CIDR -= 1
                else:
                    return mask_CIDR # x
                
    # Esta función calcula la IP de red y la de Broadcast, si quieres calcular la IP de red, has de igualar el argumento num a 0, si quieres calcular la IP de Broadcast a 1.
    def calcular_redObroadcast(self, num):
        reversed_ip = []

        for list in f.reverse_list(self.bin_list_ip):
            reversed_ip.append(f.reverse_list(list))

        num_bit = 32

        for x in range(len(self.bin_list_ip)):
            for y in range(len(reversed_ip[x])):
                if num_bit == self.cidr_num:
                    break
                else:
                    reversed_ip[x][y] = num
                    num_bit -= 1

        ip = []
        for list in f.reverse_list(reversed_ip):
            ip.append(f.reverse_list(list))

        return ip # [[x,x,x,x,x,x,x,x],[x,x,x,x,x,x,x,x],[x,x,x,x,x,x,x,x],[x,x,x,x,x,x,x,x]]
                
    # Esta función devuelve el tipo de la IP
    def tipo_ip(self):
        if self.str_ip == self.ip_red_str:
            return 'Red'
        elif self.str_ip == self.ip_broadcast_str:
            return 'Broadcast'
        else:
            return 'Host'
        
    # Esta función calcula el número de IPs de Host
    def num_host(self):
        num_ips = (2**(32 - self.cidr_num))-2
        return str(num_ips) # "x"
    
    # Esta función devuelce una letra, según la clase de IP
    def clase_ip (self):
        ip_list = self.ip_red_str.split('.')

        if int(ip_list[0]) <= 127:
            return 'A'
        elif int(ip_list[0]) >= 128 and int(ip_list[0]) <= 191:
            return 'B'
        elif int(ip_list[0]) >= 192 and int(ip_list[0]) <= 223:
            return 'C'
        elif int(ip_list[0]) >= 224 and int(ip_list[0]) <= 239:
            return 'E'
        elif int(ip_list[0]) >= 240:
            return 'D'
        
    # Esta función devuelve si es Classfull o no
    def classfull_classless (self):
        if self.class_ip == 'A' and self.cidr_num == 8:
            return 'Classfull'
        elif self.class_ip == 'B' and self.cidr_num == 16:
            return 'Classfull'
        elif self.class_ip == 'C' and self.cidr_num == 24:
            return 'Classfull'
        else:
            return 'Classless'
