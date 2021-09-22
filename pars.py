import xlsxwriter
import io
import re

f = io.open("reqs1.txt", mode="r", encoding="utf-8")
print(type(f))
workbook = xlsxwriter.Workbook('rex.xlsx')
worksheet = workbook.add_worksheet()
regex_str = "\** \d+. row \*+"
id_regex = "    id: "
de_regex = " descr: "
tm_add = "tm_add: "
row=-1
status="id"
de_count=0
de = ""
for line in f:
    if(status == "id"):
        if(re.match(id_regex, line)):
            match = re.match(id_regex, line).group(0)
            line = line.replace(' id:', '')
            worksheet.write(row, 0, line.strip())
            status="de"
            continue
    if(re.match(regex_str, line)):
        row+=1
        status="id"
    if(status=="de"):
        if(de_count==0):
            line = line.replace(' descr: ', '')
            de = line
            de_count=1
        elif(re.match(tm_add, line)):
            worksheet.write(row, 1, de.strip())
            de = ""
            de_count = 0
            status = "id"
            write = line.replace('tm_add: ', '')
            worksheet.write(row, 2, write)
        else:
            de += line
workbook.close()