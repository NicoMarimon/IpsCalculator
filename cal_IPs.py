import funciones as f

print('INSPECCIÓN DE DIRECCIÓN IP')
print()

# Asignación de variables iniciales
ip = ''
mask = ''
ip_es_valida = False
mask_is_valid = False
str_ip = 'IP'
str_mask = 'Máscara de red'

# Input del usuario de la IP y su Máscara
ip = f.bucle_validacion(ip, ip_es_valida, str_ip)
mask = f.bucle_validacion(mask, mask_is_valid, str_mask)
print()

# Convertimos la IP y la Mácara en binario para poder manipularlos
ip_bin = f.pasar_bin(ip) 
mask_bin = f.pasar_bin(mask)

# Calculamos Máscara en notación CIDR
mask_CIDR = f.calcular_CIDR(mask_bin)

# Calculamos las IPs de Red y de Broadcast
ip_red = f.pasar_bin_a_normal(f.calcular_ip_red_o_broadcast(ip_bin,mask_CIDR, 0))
ip_broadcast = f.pasar_bin_a_normal(f.calcular_ip_red_o_broadcast(ip_bin,mask_CIDR, 1))

# Cálculamos las IPs de Host
num_ips_host = f.calcular_num_hosts(mask_CIDR)
primer_host = f.pasar_bin_a_normal(f.calcular_host(ip_bin, mask_CIDR, 0))
ultimo_host = f.pasar_bin_a_normal(f.calcular_host(ip_bin, mask_CIDR, 1))

# Clásificamos el tipo de IP y la clase
ip_class = f.clase_ip(ip)
que_ip = f.que_IP_es(ip, ip_red, ip_broadcast)
clas = f.classfull_classless(ip_class, mask_CIDR)

# Función mostrar_todo
f.mostrar_todo (ip, que_ip, ip_red, mask, mask_CIDR, num_ips_host, primer_host, ultimo_host, ip_class, clas)
