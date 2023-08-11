# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Jonathan Green, Carolyn A Chew-Graham, Nav Kapur, Darren M Aschcroft, 2023.

import sys, csv, re

codes = [{"code":"1S42.00","system":"readv2"},{"code":"E11..13","system":"readv2"},{"code":"E110.00","system":"readv2"},{"code":"E110000","system":"readv2"},{"code":"E110100","system":"readv2"},{"code":"E110200","system":"readv2"},{"code":"E110300","system":"readv2"},{"code":"E110400","system":"readv2"},{"code":"E110600","system":"readv2"},{"code":"E110z00","system":"readv2"},{"code":"E114.00","system":"readv2"},{"code":"E114.11","system":"readv2"},{"code":"E114000","system":"readv2"},{"code":"E114100","system":"readv2"},{"code":"E114200","system":"readv2"},{"code":"E114300","system":"readv2"},{"code":"E114500","system":"readv2"},{"code":"E114600","system":"readv2"},{"code":"E114z00","system":"readv2"},{"code":"E11y100","system":"readv2"},{"code":"Eu30.00","system":"readv2"},{"code":"Eu30.11","system":"readv2"},{"code":"Eu30100","system":"readv2"},{"code":"Eu30200","system":"readv2"},{"code":"Eu30211","system":"readv2"},{"code":"Eu30212","system":"readv2"},{"code":"Eu30z00","system":"readv2"},{"code":"Eu30z11","system":"readv2"},{"code":"Eu31.11","system":"readv2"},{"code":"Eu31.12","system":"readv2"},{"code":"Eu31.13","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bipolar-disorder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["xmanic-bipolar-disorder---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["xmanic-bipolar-disorder---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["xmanic-bipolar-disorder---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
