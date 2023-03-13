import time

ladje = []
def napolniLadje(n):
    ladje.clear()
    for i in range(n):
        ladje.append([i, i, i, 0])#0: index staraša, 1: index sina, 2: index glavnega, razdalja do glavnega

def printLadje():
    output = "ladje: "
    index = 0
    while(ladje[index][1] != index):
        index = ladje[index][1]
    
    while(ladje[index][0] != index):
        output += "-> " + str(index)
        index = ladje[index][0]
    print(output)


def union(M, S):
    ladje[M][0] = S # S dobi očeta S
    ladje[S][1] = M # S dobi sina M
    ladje[M][2] = ladje[S][2] # M dobi očeta, ki je oče od S
    ladje[M][3] = ladje[S][3] + abs(M - S) % 1000

    prelomna_razdalja = ladje[M][3] - ladje[S][3]

    index = M
    index_sina = ladje[index][1]
    while( index_sina != index):
        ladje[index_sina][3] += prelomna_razdalja
        index = index_sina
        index_sina = ladje[index][1]

def razdaljaG(X):
    return ladje[X][3]

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

testFile("estudij_pdf_primer_test.txt", True, False, False)
printLadje()
#testFile("testni_primer2.txt", False, True, True)