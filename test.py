#coding:utf8
import re

with open(r'C:\Users\cc\Desktop\jingnei.txt') as f:
    region = ''
    regionarr = {}
    majorarr = []
    while True:
        linetext = f.readline()
        if not linetext:
            break
        linetext = linetext.strip()
        if linetext.find('\t') < 0:
            region = linetext
            regionarr[region] = {}
        else:
            temp = linetext.split('\t')
            if temp[1] not in majorarr:
                majorarr.append(temp[1])
            regionarr[region][temp[1]] = temp[2]


with open(r'C:\Users\cc\Desktop\jingnei.csv','ab') as f:
    csvarr = ['']
    for major in majorarr:
        csvarr.append('"' + major + '"')
    csvstr = ','.join(csvarr) + '\n'
    csvstr = csvstr.encode('GBK')
    f.write(csvstr)
    for region in regionarr:
        regmajor = regionarr[region]
        csvarr = []
        csvarr.append('"' + region + '"')
        for major in majorarr:
            if major in regmajor:
                csvarr.append('"' + regmajor[major] + '"')
            else:
                csvarr.append('')
        csvstr = ','.join(csvarr) + '\n'
        csvstr = csvstr.encode('GBK')
        f.write(csvstr)
    print(csvstr)
