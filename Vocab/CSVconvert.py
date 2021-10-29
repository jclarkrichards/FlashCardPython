import argparse

parser = argparse.ArgumentParser(description="Convert text file to a CSV file")
parser.add_argument('--filename', '-f', help="Name of a text file to convert")
args = parser.parse_args()
filename = args.filename
print(filename)

f = open(filename, "r")
justname = filename.split(".")[0]
print(justname)
f2 = open(justname+".csv", "w")
f2.write("id, english, polish")


for linenum, line in enumerate(f):
    print(line)
    parsed = line.split("::")
    fixedline = str(linenum)+","
    for i, item in enumerate(parsed):
        fixedline += item
        if i < len(parsed)-1:
            fixedline += ","
    print(fixedline)
    f2.write(fixedline)

f.close()
f2.close()
    
