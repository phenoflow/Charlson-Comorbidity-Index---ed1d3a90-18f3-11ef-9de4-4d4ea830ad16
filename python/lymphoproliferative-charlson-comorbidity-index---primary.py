# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"BBrA111","system":"readv2"},{"code":"BBr6800","system":"readv2"},{"code":"B69..00","system":"readv2"},{"code":"BBr2300","system":"readv2"},{"code":"BBr6300","system":"readv2"},{"code":"BBgP.00","system":"readv2"},{"code":"B602300","system":"readv2"},{"code":"BBr6.00","system":"readv2"},{"code":"BBr6z00","system":"readv2"},{"code":"BBk2.00","system":"readv2"},{"code":"BBr6100","system":"readv2"},{"code":"BBr0400","system":"readv2"},{"code":"BBk7.00","system":"readv2"},{"code":"B627W00","system":"readv2"},{"code":"BBr9000","system":"readv2"},{"code":"BBr2.00","system":"readv2"},{"code":"B62y100","system":"readv2"},{"code":"BBkz.00","system":"readv2"},{"code":"ByuD800","system":"readv2"},{"code":"ByuD200","system":"readv2"},{"code":"B620.00","system":"readv2"},{"code":"B660.00","system":"readv2"},{"code":"B64yz00","system":"readv2"},{"code":"A789700","system":"readv2"},{"code":"B672.11","system":"readv2"},{"code":"AyuC600","system":"readv2"},{"code":"B627600","system":"readv2"},{"code":"BBgC.11","system":"readv2"},{"code":"BBr2011","system":"readv2"},{"code":"B66z.00","system":"readv2"},{"code":"BBr0000","system":"readv2"},{"code":"BBr0111","system":"readv2"},{"code":"BBr..00","system":"readv2"},{"code":"B652.00","system":"readv2"},{"code":"B68..00","system":"readv2"},{"code":"BBr2600","system":"readv2"},{"code":"B661.00","system":"readv2"},{"code":"B620000","system":"readv2"},{"code":"BBr3.00","system":"readv2"},{"code":"B62x.00","system":"readv2"},{"code":"A789600","system":"readv2"},{"code":"BBr6600","system":"readv2"},{"code":"B62x000","system":"readv2"},{"code":"B62y800","system":"readv2"},{"code":"B67..00","system":"readv2"},{"code":"B631.00","system":"readv2"},{"code":"ByuD700","system":"readv2"},{"code":"B651000","system":"readv2"},{"code":"BBgT.00","system":"readv2"},{"code":"ZV10600","system":"readv2"},{"code":"B66y.00","system":"readv2"},{"code":"B602200","system":"readv2"},{"code":"ByuD900","system":"readv2"},{"code":"4M22.00","system":"readv2"},{"code":"B624.12","system":"readv2"},{"code":"B627700","system":"readv2"},{"code":"ByuD500","system":"readv2"},{"code":"B66..00","system":"readv2"},{"code":"B620800","system":"readv2"},{"code":"BBrA400","system":"readv2"},{"code":"ByuDE00","system":"readv2"},{"code":"4M21.00","system":"readv2"},{"code":"BBr0300","system":"readv2"},{"code":"BBm4.00","system":"readv2"},{"code":"BBgz.00","system":"readv2"},{"code":"B64..00","system":"readv2"},{"code":"B64y.00","system":"readv2"},{"code":"B627B00","system":"readv2"},{"code":"B651.00","system":"readv2"},{"code":"4M20.00","system":"readv2"},{"code":"BBr6311","system":"readv2"},{"code":"BBg2.11","system":"readv2"},{"code":"BBg3.00","system":"readv2"},{"code":"B67yz00","system":"readv2"},{"code":"BBg1.00","system":"readv2"},{"code":"BBr0z00","system":"readv2"},{"code":"BBgJ.00","system":"readv2"},{"code":"BBk0.13","system":"readv2"},{"code":"BBg1.11","system":"readv2"},{"code":"BBg7.00","system":"readv2"},{"code":"B64y100","system":"readv2"},{"code":"BBm9.00","system":"readv2"},{"code":"ByuDF11","system":"readv2"},{"code":"BBv0.00","system":"readv2"},{"code":"B672.00","system":"readv2"},{"code":"B620z00","system":"readv2"},{"code":"BBgG.00","system":"readv2"},{"code":"B64z.00","system":"readv2"},{"code":"BBgL.00","system":"readv2"},{"code":"B62y600","system":"readv2"},{"code":"B627.00","system":"readv2"},{"code":"4M2..00","system":"readv2"},{"code":"BBrA100","system":"readv2"},{"code":"ByuD100","system":"readv2"},{"code":"BBgR.00","system":"readv2"},{"code":"B62x600","system":"readv2"},{"code":"ByuDC00","system":"readv2"},{"code":"B62y200","system":"readv2"},{"code":"B620100","system":"readv2"},{"code":"B627900","system":"readv2"},{"code":"B67y000","system":"readv2"},{"code":"BBk..00","system":"readv2"},{"code":"B627800","system":"readv2"},{"code":"B62x100","system":"readv2"},{"code":"B620300","system":"readv2"},{"code":"B641.11","system":"readv2"},{"code":"B640.00","system":"readv2"},{"code":"BBgE.00","system":"readv2"},{"code":"BBr8.00","system":"readv2"},{"code":"BBg8.00","system":"readv2"},{"code":"BBrA500","system":"readv2"},{"code":"BBr2500","system":"readv2"},{"code":"B627C00","system":"readv2"},{"code":"B62y700","system":"readv2"},{"code":"B65..00","system":"readv2"},{"code":"ByuDF00","system":"readv2"},{"code":"B65yz00","system":"readv2"},{"code":"B62y400","system":"readv2"},{"code":"BBmH.00","system":"readv2"},{"code":"BBrA.00","system":"readv2"},{"code":"BBgV.00","system":"readv2"},{"code":"BBgC.00","system":"readv2"},{"code":"BBr6011","system":"readv2"},{"code":"BBr0112","system":"readv2"},{"code":"B651.11","system":"readv2"},{"code":"BBr0200","system":"readv2"},{"code":"B620500","system":"readv2"},{"code":"BBg4.00","system":"readv2"},{"code":"B690.00","system":"readv2"},{"code":"BBr0100","system":"readv2"},{"code":"B62x200","system":"readv2"},{"code":"B62xX00","system":"readv2"},{"code":"B627D00","system":"readv2"},{"code":"BBm5.00","system":"readv2"},{"code":"ByuD600","system":"readv2"},{"code":"B627500","system":"readv2"},{"code":"B68z.00","system":"readv2"},{"code":"B691.00","system":"readv2"},{"code":"B67y.00","system":"readv2"},{"code":"B651z00","system":"readv2"},{"code":"B68y.00","system":"readv2"},{"code":"BBgS.00","system":"readv2"},{"code":"BBr6700","system":"readv2"},{"code":"BBgK.00","system":"readv2"},{"code":"B62yz00","system":"readv2"},{"code":"BBg1000","system":"readv2"},{"code":"B64y200","system":"readv2"},{"code":"B602500","system":"readv2"},{"code":"ZV67811","system":"readv2"},{"code":"B673.00","system":"readv2"},{"code":"BBB1.00","system":"readv2"},{"code":"B602.00","system":"readv2"},{"code":"B65z.00","system":"readv2"},{"code":"BBgG.12","system":"readv2"},{"code":"B67z.00","system":"readv2"},{"code":"B670.00","system":"readv2"},{"code":"B62y.00","system":"readv2"},{"code":"B681.00","system":"readv2"},{"code":"B680.00","system":"readv2"},{"code":"B62y500","system":"readv2"},{"code":"BBgA.00","system":"readv2"},{"code":"ZV10611","system":"readv2"},{"code":"B66..12","system":"readv2"},{"code":"BBr2100","system":"readv2"},{"code":"BBr4.00","system":"readv2"},{"code":"B65y100","system":"readv2"},{"code":"B627000","system":"readv2"},{"code":"B627200","system":"readv2"},{"code":"BBgN.00","system":"readv2"},{"code":"BBgM.00","system":"readv2"},{"code":"B627C11","system":"readv2"},{"code":"B602100","system":"readv2"},{"code":"BBgQ.00","system":"readv2"},{"code":"BBgB.00","system":"readv2"},{"code":"BBr6000","system":"readv2"},{"code":"1429.00","system":"readv2"},{"code":"BBr2700","system":"readv2"},{"code":"BBk0.00","system":"readv2"},{"code":"B62y300","system":"readv2"},{"code":"B642.00","system":"readv2"},{"code":"BBg2.00","system":"readv2"},{"code":"B602z00","system":"readv2"},{"code":"BBr8000","system":"readv2"},{"code":"BBgD.00","system":"readv2"},{"code":"B641.00","system":"readv2"},{"code":"B627X00","system":"readv2"},{"code":"BBrz.00","system":"readv2"},{"code":"BBr0.00","system":"readv2"},{"code":"B627100","system":"readv2"},{"code":"BBg5.00","system":"readv2"},{"code":"B64..11","system":"readv2"},{"code":"B682.00","system":"readv2"},{"code":"BBg..00","system":"readv2"},{"code":"B62y000","system":"readv2"},{"code":"B650.00","system":"readv2"},{"code":"BBr4z00","system":"readv2"},{"code":"BBv2.00","system":"readv2"},{"code":"B627300","system":"readv2"},{"code":"BBr2000","system":"readv2"},{"code":"BBr4000","system":"readv2"},{"code":"ByuD300","system":"readv2"},{"code":"BBr0113","system":"readv2"},{"code":"BBmD.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('charlson-comorbidity-index-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lymphoproliferative-charlson-comorbidity-index---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lymphoproliferative-charlson-comorbidity-index---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lymphoproliferative-charlson-comorbidity-index---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
