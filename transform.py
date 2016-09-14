import csv

BRANCH_CODE = ""
POS_CODE = ""
INIT_SEQUENCE = 0
ISSUE_DATE = ""
ID_TYPE = ""
PRODUCT_CODE = ""
PRODUCT_AUX_CODE = ""
FIXED_ADDRESS = ""
FIXED_PHONE = ""
INPUT_FILE = ""
OUTPUT_FILE = ""

ifile = open(INPUT_FILE, "rb")
reader = csv.reader(ifile)
rownum = 0
newlist = []
invoice_seq = INIT_SEQUENCE

for row in reader:
    if rownum == 0:
        headers = row[3:7]
        rownum += 1
    else:
        newrow = [BRANCH_CODE,
                  POS_CODE,
                  invoice_seq,
                  row[0],
                  row[1],
                  ID_TYPE,
                  row[2],
                  FIXED_ADDRESS,
                  FIXED_PHONE,
                  PRODUCT_CODE,
                  PRODUCT_AUX_CODE]
        items = row[3:7]
        for index, item in enumerate(items):
            if item:
                newlist.append(newrow + \
                               [headers[index]] + \
                               [item] + \
                               [0.00] + \
                               [1] + \
                               ["14%"] + \
                               [""])
        rownum += 1
        invoice_seq += 1

ofile = open(OUTPUT_FILE, "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for row in newlist:
    writer.writerow(row)

ifile.close()
ofile.close()
