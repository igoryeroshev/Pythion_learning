#!/usr/bin/env python
# -*- coding: utf-8 -*-


ip_address = ''
mask = ''
mask_full = ''
bin_mask = ''

net_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:>08b} {1:>08b} {2:>08b} {3:>08b}
'''

mask_template = '''
{0:<8} {1:<8} {2:<8} {3:<08}
{0:<8} {1:<8} {2:<8} {3:<08}
'''

network = input('\nВведите IP-адрес в формате XXX.XXX.XXX.XXX/NN:   ')
ip_address, mask = network.split('/')
ip_address = ip_address.split('.')
mask_full = '1'*int(mask)
bin_mask = [int(mask_full[:8]),int(mask_full[8:16]),int(mask_full[16:24]),int(mask_full[24:32])]
 
print(net_template.format(int(ip_address[0]),int(ip_address[1]),int(ip_address[2]),int(ip_address[3])))
print('Mask:'+'\n' + '/'+mask)
print(mask_template.format(bin_mask[0],bin_mask[1],bin_mask[2],bin_mask[3]))
