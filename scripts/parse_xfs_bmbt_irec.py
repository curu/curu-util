import sys
import bitstring

version_offset = 4*8
bmbt_offset_v4 = 100*8
bmbt_offset_v5 = 176*8

if len(sys.argv) < 2:
    print("Usage:%s inode.dat" % sys.argv[0])
    sys.exit(1)

content = open(sys.argv[1], "rb").read()
b = bitstring.BitArray(bytes=content)
#b.pp('h8', width=53)

if b[0:16].uint != 0x494e:
    print("input not an inode data")
    sys.exit(1)

inode_version = b[version_offset:version_offset+8].uint8
if inode_version < 3:
    b = b[bmbt_offset_v4:]
else:
    b = b[bmbt_offset_v5:]


def print_bmbt(b):
    b = b[0:128]
    old_lsb = bitstring.lsb0
    bitstring.lsb0 = True
    blockcount = b[0:21].uint
    startblock = b[21:73].uint
    startoff = b[73:127].uint
    extentflag = b[127:].uint
    bitstring.lsb0 = old_lsb
    print("startoff:%d startblock:%d blockcount:%d extentflag:%d" % (startoff, startblock, blockcount, extentflag))


while len(b) > 128:
    print_bmbt(b)
    b = b[128:]
