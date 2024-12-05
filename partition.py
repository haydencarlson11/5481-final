
#BEAST requires that we partition our FASTA file into precovid,
#during, and post covid. However they must be aligned. So we make one big FASTA, align it, then run this to partition it.

from datetime import datetime, date
import sys

def partition_fasta(input_file):
    preCOVID = open("pre-COVID.fasta", "w")
    preCovidDates = []
    duringCOVID = open("during-COVID.fasta", "w")
    duringCovidDates = []
    postCOVID = open("post-COVID.fasta", "w")
    fout = None
    postCovidDates = []
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
                    preCovidDates.append(dateStr.replace("/", "-"))
                elif dateObj > covidEnd:
                    fout = postCOVID
                    postCovidDates.append(dateStr.replace("/", "-"))
                else:
                    fout = duringCOVID
                    duringCovidDates.append(dateStr.replace("/", "-"))
                
                fout.write(">"+dateStr.replace("/", "-")+"\n") #we only care about date
            else:
                fout.write(line + "\n")

    preCOVID.close()
    duringCOVID.close()
    postCOVID.close()

    #now write to dates file
    dates = open('dates.txt', 'w')
    for dateStr in preCovidDates:
        dates.write(dateStr + "\n")
    for dateStr in duringCovidDates:
        dates.write(dateStr + "\n")
    for dateStr in postCovidDates:
        dates.write(dateStr + "\n")
    dates.close()
    return


partition_fasta(sys.argv[1])
