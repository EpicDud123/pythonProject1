def insertverycoolandfunnynamethatalsorelatestofindingdifferencesintextshere(A, B):
    inconsinsticies=0
    for i in range(len(A)):
        if A[i] != B[i]:
            inconsinsticies += 1
    return inconsinsticies




if __name__ == "__main__":
    A = "19dollarfortnitecard"
    B = "welivewelovewelieeee"
    C = "20yenminecraftcarddd"
    result = insertverycoolandfunnynamethatalsorelatestofindingdifferencesintextshere(A, C)
    print(result)