#function 1: main function
def main():
    fname = input('Please enter the file name. (e.g C:\\Workspace\\RiverFlux_months.csv): \n')
    flines = fread(fname.replace('\\\\','\\'))
    N=[]
    M=[]
    for i, each in zip(range(0, len(flines)),flines):
        X = each.split(',')

        if i==0:
            continue
        elif shouldKeep(X):
            N.append('\t'.join(X))
            M.append(X)

    #Writing to a tab seperated file in the same folder as input csv file
    outfname = fname.replace('.csv', '_new.tsv')
    of = open(outfname, 'w')
    of.writelines(N)
    of.close()

    printAverage(M)

#function 2: fread, to read input file
def fread(fname):
    return open(str(fname),'r').readlines()

#function 3: shouldkeep, to check if a row from input csv file should be kept or discarded
def shouldKeep(Line):
    l = len(Line)
    keep = True
    for i in range(1,l):
        if float(Line[i].strip())==0:
            keep=False
    return keep

#function 4: printAverage, to print the averages of columns directly to the console
def printAverage(M):
    Q, Qs, Qc = 0,0,0
    ln=len(M)
    for row in M:
        Q+=float(row[1])
        Qs+=float(row[2])
        Qc+=float(row[3])
    Qav=Q/ln
    Qsav = Qs/ln
    Qcav = Qc/ln

    print('Average Q : {a:20.5f}\nAverage Qs : {b:20.5f}\nAverage Qc : {c:20.5f}'.format(a=Qav, b=Qsav, c=Qcav))

main()
