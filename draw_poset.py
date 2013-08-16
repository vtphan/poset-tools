
import os, sys, math

def usage():
    print "Output: _draw_poset.png"
    print "Input: %s pattern" % sys.argv[0]
    print "pattern is a k(k-1)/2-string of 0,1,2"
    sys.exit(0)
################################
## p is a string of 0,1,2.
################################
def parse_pattern( p ):
    if False in [ i in ('0','1','2') for i in p ]: usage()
    n = int((1.0+math.sqrt(1+8*len(p)))*0.5)

    ################################
    file = open("_draw_poset.gv", "w")
    file.write("digraph G {\n\trankdir=TB\n\tnode [shape=circle];\n")
    ################################

    digits = [ int(i) for i in p ]
    width = count = 1
    for k,digit in enumerate(digits):
        i, j = (k+count)/n, (k+count)%n
        if j==n-1:
            width = width+1
            count = count+width
        if digit == 0: file.write("\t%d -> %d [dir=none];\n" % (i,j))
        elif digit == 2: file.write("\t%d -> %d [dir=none];\n" % (j,i))

    ################################
    file.write("}\n")
    file.close()
    print "output to _draw_poset.gv"
    os.system("dot -Tpng _draw_poset.gv -o _draw_poset.png")
    print "output to _draw_poset.png"
    # os.system("/Applications/Preview.app/Contents/MacOS/Preview _draw_poset.png")
    ################################


if __name__ == "__main__":
    if len(sys.argv) != 2: usage()
    parse_pattern(sys.argv[1])
