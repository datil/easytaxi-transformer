import csv
import StringIO

def csv2string(data):
    si = StringIO.StringIO()
    writer = csv.writer(si, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in data:
        writer.writerow(row)
    return si.getvalue()

def datilize(ifile, properties):
    rownum = 0
    newlist = []
    invoice_seq = properties["init_sequence"]
    reader = csv.reader(StringIO.StringIO(ifile))
    print reader

    for row in reader:
        if rownum == 0:
            headers = row[3:7]
            rownum += 1
        else:
            newrow = [properties["branch_code"],
                      properties["pos_code"],
                      invoice_seq,
                      row[0],
                      row[1],
                      properties["id_type"],
                      row[2],
                      properties["fixed_address"],
                      properties["fixed_phone"],
                      properties["product_code"],
                      properties["product_aux_code"]]
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

    return csv2string(newlist)
