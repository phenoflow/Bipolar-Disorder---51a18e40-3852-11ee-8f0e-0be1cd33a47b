# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Jonathan Green, Carolyn A Chew-Graham, Nav Kapur, Darren M Aschcroft, 2023.

import sys, csv, re

codes = [{"code":"E111.00","system":"readv2"},{"code":"E111000","system":"readv2"},{"code":"E111100","system":"readv2"},{"code":"E111200","system":"readv2"},{"code":"E111300","system":"readv2"},{"code":"E111400","system":"readv2"},{"code":"E111500","system":"readv2"},{"code":"E111600","system":"readv2"},{"code":"E111z00","system":"readv2"},{"code":"Eu31000","system":"readv2"},{"code":"Eu31100","system":"readv2"},{"code":"Eu31200","system":"readv2"},{"code":"Eu31300","system":"readv2"},{"code":"Eu31400","system":"readv2"},{"code":"Eu31500","system":"readv2"},{"code":"Eu31600","system":"readv2"},{"code":"Eu31y12","system":"readv2"},{"code":"Eu3y100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bipolar-disorder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["current-bipolar-disorder---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["current-bipolar-disorder---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["current-bipolar-disorder---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
