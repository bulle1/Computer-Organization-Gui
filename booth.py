def BitAdd(m, n, length):
    """Return m+n in string.
    
    Arguments:
    m -- Binary number in string
    n -- Same as above
    length -- The length of returned number (overflowed bit will be ignored)
    Returns: string
    """

    lmax = max(len(m), len(n))
    c = 0
    ml = [0] * (lmax - len(m)) + [int(x) for x in list(m)]
    nl = [0] * (lmax - len(n)) + [int(x) for x in list(n)]
    rl = []
    for i in range(1, lmax+1):
        if ml[-i] + nl[-i] + c == 0:
            rl.insert(0, 0)
            c = 0
        elif ml[-i] + nl[-i] + c == 1:
            rl.insert(0, 1)
            c = 0
        elif ml[-i] + nl[-i] + c == 2:
            rl.insert(0, 0)
            c = 1
        elif ml[-i] + nl[-i] + c == 3:
            rl.insert(0, 1)
            c = 1
    if c == 1:
        rl.insert(0, 1)
    if length > len(rl):
        rl = [0] * (length - len(rl)) + rl
    else:
        rl = rl[-length:]
    rl = "".join([str(x) for x in rl])
    return rl


def TwoComp(n):
    """Return the two's complement of given number.
    Arguments:
    n -- Binary number in string
    Returns: string
    """

    l = list(n)
    for i in range(len(l)):
        l[i] = "0" if l[i] == "1" else "1"
    return BitAdd("".join(l), "1", len(l))


def BitShift(n, shift):
    """Shift the bits rightward in arithmetical method.
    If shift is negative, it shifts the bits leftward.
    Arguments:
    n -- Binary number in string
    shift -- Number of times to shift
    Returns: string
    """

    if shift > 0:       #Right shift
        if n[0] == "0":
            n_ = "".join(["0"] * shift) + n
        else:
            n_ = "".join(["1"] * shift) + n
        return n_[:len(n)]
    else:
        n_ = n + "".join(["0"] * (-shift))
        return n_[-len(n):]


def CalcBoothRecoding(n):
    """Calculate the Booth recoding number of given n.
    Arguments:
    n -- Binary number to calculate in string
    Returns: string
    Attention:
    "2" in returned string represents "1-hat".
    """

    n_ = [int(x) for x in list(n + "0")]
    r = []
    for i in range(len(n)):
        x = n_[i+1] - n_[i]
        if x == -1: r.append(2)
        else:       r.append(x)
    return "".join([str(x) for x in r])


def GenZeroStr(n):
    """Generate a bunch of zeroes.
    Arguments:
    n -- Number of zeroes
    Returns: string
    """

    return "".join(["0"] * n)

def BoothRecToString(s, indent=0):
    """Convert a Booth recoding number to human-readable string.
    Arguments:
    s -- String of Booth recoding
    indent -- Number of spaces in the head of lines (optional)
    Returns: string
    """

    sp = " " * indent
    h = []
    n = []
    for i in list(s):
        if   i == "0":
            h.append(" ")
            n.append("0")
        elif i == "1":
            h.append(" ")
            n.append("1")
        elif i == "2":
            h.append("^")
            n.append("1")
    return sp + "".join(h) + "\n" + sp + "".join(n)


def boot():
    print("This program excecutes Booth's multiplication algorithm.\n")
    print("The formula it's going to calculate is:  M * R = ?")
    print("Input the bit length of first variable M: ", end="")
    mlen = int(input())
    print("Input the bit length of second variable Q: ", end="")
    rlen = int(input())

    print("Input the number of first variable M: ", end="")
    m = int(input())
    if m < 0:
        m = TwoComp( ("{0:0%db}" % mlen).format(m) )    #Calculate the two's complement number of m
    else:
        m = ("{0:0%db}" % mlen).format(m)   #Convert to bits and assign directly

    print("Input the number of second variable Q: ", end="")
    r = int(input())
    if r < 0:
        r = TwoComp( ("{0:0%db}" % rlen).format(r) )
    else:
        r = ("{0:0%db}" % rlen).format(r)

    ilen = mlen + rlen + 1                  #The common length of internal variables
    a = m + GenZeroStr(rlen + 1)            #A: place M in leftmost position. Fill the left bits with 0.
    s = TwoComp(m) + GenZeroStr(rlen + 1)   #S: place negative M in leftmost position.
    p = GenZeroStr(mlen) + r + "0"          #P: place R by rightmost 0.

    print("Internal variables:")
    print("M = %s" % m)
    print("Q = %s" % r)
    print("Mbar + 1 (2's Complement of M)= %s" % s[:mlen])
    print('Step 0')
    print('P = A + Q + Q1 bit')
    print("P = %s\n" % p)
    print('NOTE: P given after doing required step')

    for i in range(rlen):   #Do operation rlen times
        print("Step %d:" % (i+1))

        op = p[-2:]
        print("    " + "The last 2 bits of p are: %s" % "".join(op))
        if   op == "10":
            print("    " + "A+Mbar+1 and ARshift")
            p = BitAdd(p, s, len(p))
        elif op == "01":
            print("    " + "A+M and ARshift")
            p = BitAdd(p, a, len(p))
        elif op == "00":
            print("    " + "ARshift")
        elif op == "11":
            print("    " + "ARshift")

        p = BitShift(p, 1)
        print("    " + "P = %s\n" % p
              )

    p = p[:-1]
    print("The answer is: %s" % p)


if __name__ == "__main__":
    boot()
