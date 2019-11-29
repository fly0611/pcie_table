# -*- coding=utf-8 -*-
########################################
#      将lscpu输出结果转为字典           #
#         2019-11-20 11:14             #
#                                   v1 #
########################################
import os
from  pprint import pprint

def PCIE():
    # 执行的cmd命令
    cmd = 'dmidecode -t slot'
    # 将执行结果保存到cm变量里
    command = os.popen(cmd).readlines()
    #
    pcie_slot = {}
    list = []
    list1 = []
    slot_id = 0
    pcie_slot1 = {}
    pcie_list = []
    for i in command[4:]:
        d =i.replace('\t','').replace('\n','')
        if d.startswith('De')or d.startswith('Cu') or d.startswith("Ty") \
                or d.startswith('Bus')or d.startswith('Ha') or d.startswith('Le'):
            if d.startswith('Ha'):
                d = '--'
            list.append(d)
    list.append('--')
    for i in  list[1:]:
        if i.startswith('Bus Address'):
            w = i.replace(': ','_')
            w = w.split('_')
        else:
            c =i.split(':')
            #print c
            if len(c) == 2:
                #print c
                pcie_slot[c[0]] = c[1]
            else:
                pcie_slot[w[0]] = w[1]
                list1 = []
                list1.append(pcie_slot)
                slot_id+=1
                slot_name = 'Slot_' + str(slot_id)
                pcie_slot1[slot_name] = list1
                pcie_slot = {}

    return  pcie_slot1

def LSPCI():
    lspci_list =[]
    lspci_dict = {}
    lspci_dict1 = {}

    # 执行的cmd命令
    cmd = 'lspci -vmm'
    # 将执行结果保存到cm变量里
    command = os.popen(cmd).readlines()

    for i in command:
        c = i.replace('\n','').replace('\t','')
        if c.startswith('Slot'):
            w = c.split('t:')
            #print w
        else:
            c = c.split(':')
            if len(c) ==2:
                lspci_dict[c[0]] = c[1]
                lspci_list.append(lspci_dict)

            else:
                lspci_dict1[w[1]] = lspci_list
                lspci_list = []
                lspci_dict = {}
    #去掉重复的字典
    lspci_dict_new = {}
    for i,x in lspci_dict1.items():
        seen = set()
        new_l = []
        for d in x:
            t = tuple(d.items())
            if t not in seen:
                seen.add(t)
                new_l.append(d)

        lspci_dict_new[i] = new_l
    return lspci_dict_new

#将lspci的信息添加到pcie字典里
def ALL_Pcie():
    pcie = PCIE()
    lspci = LSPCI()
    for i in pcie.items():
         if i[1][0]['Current Usage'] == ' In Use':
            mac = i[1][0]['Bus Address'][5:12]
            device =  lspci[mac][0]['Device']
            SVendor = lspci[mac][0]['SVendor']
            i[1][0]['device'] = device
            i[1][0]['SVendor'] = SVendor
         else:
             i[1][0]['device'] = 'N/A'
             i[1][0]['SVendor'] = 'N/A'
    return pcie

pcie = ALL_Pcie()
#pprint(pcie)
#title = ['Bus Address','Current Usage','Designation','Length','SVendor','Type','device']
kys = pcie['Slot_1'][0].keys()

max_len_list =[]
for zz in kys:
    len_nu = 0
    for i,x in pcie.items():
        max_len = len(x[0][zz])

        len_nu=max(len_nu,max_len,len(zz))
    max_len_list.append(len_nu+2)
pc = ''
fm = ''
for i in max_len_list:
    pt = '+'
    pw = '-'* i
    pc = pc+pt+pw
    fw = "|{:^"+str(i)+"}"
    fm = fm + fw
pc = pc + '+'

#生成字符表格
print pc
print fm.format('SVendor','Designation','Current Usage','Length','device','Type','Bus Address') + '|'
print pc

for i in pcie.values():
    print fm.format(i[0]['SVendor'], i[0]['Designation'], i[0]['Current Usage'],
                    i[0]['Length'], i[0]['device'], i[0]['Type'], i[0]['Bus Address']) + '|'
print pc
