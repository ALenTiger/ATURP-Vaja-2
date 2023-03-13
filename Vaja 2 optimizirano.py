ladje = []
def napolniLadje(n):
    for i in range(n):
        ladje.append([i, 0])

def union(M, S):
    ladje[M][0] = S
    ladje[M][1] = abs(M - S) % 1000

def razdaljaG(X):
    razdalja = 0
    while(X != ladje[X]):
        razdalja += ladje[X][1]
        X = ladje[X][0]
    return razdalja

def testFile(path, output_to_console=True, output_to_file=False, debug_progress=False):
    test_examples = []
    with open(path, 'r') as file:
        for line in file:
            test_examples.append(line)
    with open('moji rezultati.txt', 'w') as file:
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

testFile("estudij_pdf_primer_test.txt", True, False, False)
#testFile("testni_primer2.txt", False, True, True)