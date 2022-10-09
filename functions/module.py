hai=[23,67,343,89,87,35,677,45]

def selection():
    for hold in range(len(hai)):
        for comp in range(hold+1,len(hai)):
            if hai[hold]<hai[comp]:
                hai[hold]^=hai[comp]
                hai[comp]^=hai[hold]
                hai[hold]^=hai[comp]