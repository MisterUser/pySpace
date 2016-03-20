import sys

SRC_FILE = sys.argv[1]
OUT_FILE = sys.argv[2]
THEME = sys.argv[3]

beg_ = "\\begin{" + THEME + "}"
end_ = "\\end{" + THEME + "}"


with open(SRC_FILE) as infile, open(OUT_FILE, 'a') as outfile:
    copy = False
    for line in infile:
        if line.strip() == beg_:
            copy = True
        elif line.strip() == end_:
            outfile.write(line)
            copy = False

        if copy:
            outfile.write(line)
