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
    newlist = [["Codigo establecimiento", "Punto de emision", "Secuencia", "Fecha Emision", \
                "Razon Social Comprador", "Identificacion Comprador", "Tipo Identificacion", \
                "Email Comprador", "Direccion Comprador", "Telefono Comprador", "Codigo", \
                "Codigo Auxiliar", "Descripcion", "Precio Unitario", "Descuento Unitario", \
                "Cantidad", "Tipo IVA", "Informacion Adicional"]]
    invoice_seq = properties["init_sequence"]
    reader = csv.reader(StringIO.StringIO(ifile))

    for row in reader:
        if rownum == 0:
            headers = row[3:7]
            rownum += 1
        else:
            newrow = [properties["branch_code"],
                      properties["pos_code"],
                      invoice_seq,
                      properties["issue_date"],
                      row[0],
                      row[1],
                      properties["id_type"],
                      row[2],
                      properties["fixed_address"],
                      properties["fixed_phone"]]
            items = row[3:7]
            for index, item in enumerate(items):
                if item:
                    newlist.append(newrow + \
                                   [properties["product_codes"][index]] + \
                                   [properties["product_aux_code"]] + \
                                   [headers[index]] + \
                                   [item] + \
                                   [0.00] + \
                                   [1] + \
                                   ["14%"] + \
                                   [""])
            rownum += 1
            invoice_seq += 1

    return csv2string(newlist)
