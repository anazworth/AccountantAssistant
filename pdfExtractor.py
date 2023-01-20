from pypdf import PdfReader
import csv
import os

with open('letter.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'address1', 'address2', 'amount']
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(fieldnames)

    for file in os.listdir():
        if file.endswith(".pdf"):
            print(file)
    
            # PDF file to read
            reader = PdfReader(file)

            fields = reader.get_form_text_fields()

            # The fields are going to be in the format of p1-t1[0] for the first page, first text field
            # This is set up specifically to pull an individual's information from an IRS Form 8300
            name = fields['p1-t2[0]'] + ' ' + fields['p1-t1[0]']
            address1 = fields['p1-t5[0]']
            address2 = fields['p1-t7[0]'] + ', ' + fields['p1-t8[0]'] + ' ' + fields['p1-t9[0]']
            amount = fields['p1-t29[0]']
            
            writer.writerow([name, address1, address2, amount]) 
            
    csvfile.close()