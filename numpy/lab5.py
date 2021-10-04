#==============================================================================================
#function 1: main function
def main():
    import os
    hint = input('Enter h for hint, p for proceeding without hint.\n')
    if hint=='h' or hint=='H':
        hintf()
    flines = fread()
    N=[]
    M=[]
    for i, each in zip(range(0, len(flines)),flines):
        X = each.split(',')

        if i==0:
            continue
        elif shouldKeep(X):
            N.append('\t'.join(X))
            M.append(X)
#=============================================================================================
    #Writing to a tab seperated file in the same folder as input csv file
    #outfname = fname.replace('.csv', '_new.tsv')
    outval(N)
    '''while True:
        try:
            outfolder0 = input('Please enter the name of folder to store output .tsv file (e.g C:\Workspace): \n')
            outfolder = outfolder0.replace('\\\\','\\').replace('"','').replace("'","")
            print(outfolder0)
            if os.path.exists(outfolder0):
                break
        except:
            print(outfolder0)
            print('Some issue with output folder name.')
        else:
            break
            
    case = True
    while case:
        try:
            outfname0 = input('Please enter the name of output .tsv file (e.g output.tsv): \n')
            outfname1 = outfname0.replace('\\\\','\\').replace('"','').replace("'","")
            outfname = os.path.join(outfolder, outfname1)
            if os.path.exists(outfname):
                print('File with specified name already exists.')
                overwrite = input('Enter y to override\t or n to save as another file\t')
                if overwrite=='y' or overwrite=='Y':
                    fwrite(outfname,N)
                    case = False
                    break
            else:
                fwrite(outfname,N)
                case = False
                break
            
        except:
            case = True
            print("Some error occured\n")'''
    

    printAverage(M)


#=============================================================================================
#function 2: fread, to read input file
def fread():
    while True:
        try:
            fname0 = input('Please enter the input file name. (e.g C:\Workspace\RiverFlux_months.csv): \n')
            #print(fname0)
            fname = fname0.replace('\\\\','\\').replace('"','').replace("'","")
            #print(fname)
            return open(str(fname),'r').readlines()
        except:
            import sys
            print("\nPlease, check your inputs and try again.Be wary of quotation marks.\n")
            #sys.exit(1)
        else:
            break
#=============================================================================================
#function 3: shouldkeep, to check if a row from input csv file should be kept or discarded
def shouldKeep(Line):
    l = len(Line)
    keep = True
    for i in range(1,l):
        if float(Line[i].strip())==0:
            keep=False
    return keep
#=============================================================================================
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

    print('These are the average values of columns:\n')
    print('Average Q  : {a:12.5f}\n-------------------------\nAverage Qs : {b:12.5f}\n-------------------------\nAverage Qc : {c:12.5f}'.format(a=Qav, b=Qsav, c=Qcav))

#=============================================================================================
#function 5: hintf, to show hint on how to copy as path the full location of a file
def hintf():
    print('\nHint:\n-1-To get the full path of a file, navigate to the file\n-2-While holding the shift key, right click\n-3-choose Copy as path.\nThis should give the full path to paste in input file names.\n')
    print('---------Now provide input and output file names----------\n')

#=============================================================================================
#function 6: fwrite, to write output file
def fwrite(outfname,N):
    with open(outfname,'w') as of:
        of.writelines(N)

    print('\n\nPlease, check the following file:\n{}\n'.format(outfname))


#=============================================================================================
#function 7: outval, to validate output folder name and output file name
def outval(N):
    import os
    outfolder0 = input('Please enter the name of folder to store output .tsv file (e.g C:\Workspace): \n')
    outfolder = outfolder0.replace('\\\\','\\').replace('"','').replace("'","")
    print(outfolder0)
    if not os.path.exists(outfolder):
        os.mkdir(outfolder)
        print('New folder {} created.'.format(outfolder))
    
    while True:
        try:
            outfname0 = input('Please enter the name of output .tsv file (e.g output.tsv): \n')
            outfname1 = outfname0.replace('\\\\','\\').replace('"','').replace("'","")
            outfname = os.path.join(outfolder, outfname1)
            if os.path.exists(outfname):
                print('File with specified name already exists.')
                overwrite = input('Enter y to override\t or n to save as another file\t')
                if overwrite=='y' or overwrite=='Y':
                    fwrite(outfname,N)
                    break
            else:
                fwrite(outfname,N)
                break
            
        except:
            print("Some error occured\n")

main()
