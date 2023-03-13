import time

ladje = []
def napolniLadje(n):
    for i in range(n):
        ladje.append([i, 0, 0, 0])#0: index staraša, 1: razdalja do starša, 2: index do trenutno glavnega, razdalja do trenutno glavnega

def union(M, S):
    ladje[M][0] = S
    ladje[M][1] = abs(M - S) % 1000
    razdalaja=0
    X = S
    while(X != ladje[X][0]):
        razdalja += ladje[X][1]
        X = ladje[X][0]
    ladje[M][2] = X
    ladje[M][3] = razdalaja

def razdaljaG(X):
    razdalja = 0
    while(X != ladje[X][0]): 
        razdalja += ladje[X][3]
        X = ladje[X][2]
    return razdalja

def testFile(path, output_to_console=True, output_to_file=False, debug_progress=False):
    test_examples = []
    with open(path, 'r') as file:
        for line in file:
            test_examples.append(line)
    with open('moji rezultati.txt', 'w') as file:
        start_time = time.time()
        for i, example in enumerate(test_examples):
            args = example.split()
            if(i==0):
                napolniLadje(int(example))
            if(args[0]=='C'):
                M = int(args[1]) - 1
                S = int(args[2]) - 1
                union(M, S)
            if(args[0]=='G'):
                X = int(args[1]) - 1
                razdalja = razdaljaG(X)
                if(output_to_file): 
                    file.write(str(razdalja)+"\n")
                if(output_to_console):
                    print(razdalja)
            if (i % 100 == 0):
                if (debug_progress):
                    print(str(i/len(test_examples)*100)+"%")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")

#testFile("estudij_pdf_primer_test.txt", True, False, False)
testFile("testni_primer2.txt", False, True, True)