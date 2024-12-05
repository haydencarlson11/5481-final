
#BEAST requires that we partition our FASTA file into precovid,
#during, and post covid. However they must be aligned. So we make one big FASTA, align it, then run this to partition it.

from datetime import datetime, date
import sys

def partition_fasta(input_file):
    preCOVID = open("pre-COVID.fasta", "w")
    duringCOVID = open("during-COVID.fasta", "w")
    postCOVID = open("post-COVID.fasta", "w")
    fout = None
    covidStart = date(2020, 3, 1)
    covidEnd = date(2022, 6, 1)

    with open(input_file, 'r') as fin:
        for line in fin:
            line = line.strip()
            if line.startswith(">"):
                dateStr = line.split()[2]
                dateObj = datetime.strptime(dateStr, "%Y/%m/%d").date()
                if dateObj < covidStart:
                    fout = preCOVID
                elif dateObj > covidEnd:
                    fout = postCOVID
                else:
                    fout = duringCOVID
                fout.write(">"+dateStr.replace("/", "-")+"\n") #we only care about date
            else:
                fout.write(line + "\n")

    preCOVID.close()
    duringCOVID.close()
    postCOVID.close()
    return


partition_fasta(sys.argv[1])
