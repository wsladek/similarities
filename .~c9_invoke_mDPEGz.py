from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    #Split the lines
    splita = a.splitlines()
    splitb = b.splitlines()
    #Compare
    linematches = list(set(splita) & set(splitb))
    return linematches 


def sentences(a, b):
    """Return sentences in both a and b"""
    #Sentence tokenize the strings
    senta = sent_tokenize(a)
    sentb = sent_tokenize(b)
    #Compare
    sentmatches = list(set(senta) & set(sentb))
    return(sentmatches)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    substrsa = []
    substrsb = []

    for i in range(len(a)):
        substr = a[i:i+n]
        if len(substr) == n:
            substrsa.append(substr)

    for j in range(len(b)):
        substr = b[j:j+n]
        if len(substr) == n:
            substrsb.append(substr)

    substrmatches = list(set(substrsa) & set(substrsb))
    return (substrmatches)
