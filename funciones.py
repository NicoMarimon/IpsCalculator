import colores as c

def ip_valida (ip):
    # Esta función devuelve False si la IP es inválida y True si es válida
    ip_list = ip.split('.')
    if len(ip_list) == 4:
        for i in ip_list:
            if i == '':
                return False
            elif int(i) <= 255:
                continue
            else:
                return False
        return True
    else:
        return False
    
def bucle_validacion (num, bool, stri):
    # Esta función vuelve a pedir el input de la IP o de la máscara, si estas son inválidas.
    while not bool:
        num = input(c.reset_style('Por favor introduzca ')+ stri + ': ' + c.verde(''))
        c.reset_color('')
        bool = ip_valida(num)
        if bool == False:
            print(c.rojo((stri + ' inválida por favor introduzca una '+ stri + ' válida.')))
            c.reset_color('')
    return num
         
def reverse_list (list):
    # Esta función devuelve una lista dada la vuelta
    return list[::-1]

def pasar_bin (num):
    # Esta función pasa las IPs o las Máscaras a binario
    num_list = num.split('.')
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
        

    return bin_list

def calcular_CIDR (mask):
    # Esta función calcula la máscara en notación CIDR
    reversed_mask = reverse_list(mask)
    mask_CIDR = 32
    for eight_bits in reversed_mask:
        for bit in reverse_list(eight_bits):
            if bit == 0:
                mask_CIDR -= 1
            else:
                return mask_CIDR
            
def calcular_ip_red_o_broadcast (ip, mask, num):
    # Esta función calcula la IP de red y la de Broadcast, si quieres calcular la IP de red, has de igualar el argumento num a 0, si quieres calcular la IP de Broadcast a 1.
    reversed_ip = []

    for list in reverse_list(ip):
        reversed_ip.append(reverse_list(list))

    num_bit = 32

    for x in range(len(ip)):
        for y in range(len(reversed_ip[x])):
            if num_bit == mask:
                break
            else:
                reversed_ip[x][y] = num
                num_bit -= 1

    ip = []
    for list in reverse_list(reversed_ip):
        ip.append(reverse_list(list))

    return ip

def calcular_num_hosts(mask):
    # Esta función calcula el número de IPs de Host
    num_ips = (2**(32 - mask))-2
    return num_ips

def calcular_host(ip,mask, num):
    # Esta función calcula la primera o la última IP de Host, si quieres calcular la primera, has de igualar el argumento num a 1, si quieres calcular la última, lo has de igualar a 1.
    if num == 0:
        last_num = 1
    else:
        last_num = 0
    
    reversed_ip = []

    for list in reverse_list(ip):
        reversed_ip.append(reverse_list(list))

    num_bit = 32

    for x in range(len(ip)):
        for y in range(len(reversed_ip[x])):
            if num_bit == mask:
                break
            else:
                if num_bit == 32:
                    reversed_ip[x][y] = last_num
                else:
                    reversed_ip[x][y] = num
                num_bit -= 1

    ip = []
    for list in reverse_list(reversed_ip):
        ip.append(reverse_list(list))

    return ip

def pasar_bin_a_normal (list):
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

    return normal_str

def clase_ip (ip):
    # Esta función devuelce una letra, según la clase de IP
    ip_list = ip.split('.')

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

def que_IP_es(ip,ip_red,ip_broadcast):
    # Esta función devuelve el tipo de la IP
    if ip == ip_red:
        return 'Red'
    elif ip == ip_broadcast:
        return 'Broadcast'
    else:
        return 'Host'

def classfull_classless (ip_class, mask_CIDR):
    # Esta función devuelve si es Classfull o no
    if ip_class == 'A' and mask_CIDR == 8:
        return c.verde('Classfull')
    elif ip_class == 'B' and mask_CIDR == 16:
        return c.verde('Classfull')
    elif ip_class == 'C' and mask_CIDR == 24:
        return c.verde('Classfull')
    else:
        return c.rojo('Classless')

def mostrar_todo (ip, que_ip, ip_red, mask, mask_CIDR, num_ips_host, primer_host, ultimo_host, ip_class, clas):
    # Esta función muestra toda la info de la IP
    print(c.blanco('La IP que desea inspaccionar es : ') + c.azul(ip))
    print(c.blanco('Es una IP de ') + c.azul(que_ip) + '.')
    print()

    print(c.blanco('IP de red:          ')  + c.cyan(ip_red))
    if clas == 'Classfull':
        print(c.blanco('La IP es de clase:  ')  + c.verde(ip_class) + ' ' + clas)
    else:
        print(c.blanco('La IP es de clase:  ')  + c.rojo(ip_class) + ' ' + clas)
    print()
    print(c.blanco('Máscara de red:     ')  + c.verde(mask))
    print(c.blanco('Máscara CIDR:       /') + c.verde(str(mask_CIDR)))
    print()
    print(c.blanco('Número IPs de Host: ')  + c.amarillo(str(num_ips_host)))
    print(c.blanco('Primer IP de Host:  ')  + c.amarillo(primer_host))
    print(c.blanco('Último IP de Host:  ')  + c.amarillo(ultimo_host))
    print()
    print(c.blanco('IP de Broadcast:    ')  + c.rojo(ip_red))
