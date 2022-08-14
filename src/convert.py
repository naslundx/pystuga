import sys

src_file = sys.argv[1]
dst_file = sys.argv[2]

with open(src_file) as f:
    with open(dst_file, 'w') as f2:
        f2.write(f.read())
