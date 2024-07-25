#!/usr/bin/env python
import sys
Version = "V0.3"
print(" _     _       ____  ____   ____")
print("| |__ (_)_ __ |___ \\/ ___| / ___|")
print("| '_ \\| | '_ \\  __) \\___ \\| |")
print("| |_) | | | | |/ __/ ___) | |___")
print("|_.__/|_|_| |_|_____|____/ \\____|")
print("https://www.nosociety.de")
print(Version)
print("\n\n")
if __name__ == "__main__":
 if len(sys.argv) < 3:
  print("usage: %s <binary_file> <argument>" % (sys.argv[0],))
  print("possible arguments:")
  print("c | casm | cs | hex | ps1 | py")
  print("visit https://github.com/psycore8/bin2shellcode for documentation")

  sys.exit(0)

# C++
 if sys.argv[2] == "c":
  shellcode = "\""
  ctr = 1
  maxlen = 15

  for b in open(sys.argv[1], "rb").read():
   shellcode += "\\x" + b.to_bytes(1, "big").hex()
   if ctr == maxlen:
    shellcode += "\" \n\""
    ctr = 0
   ctr += 1
  shellcode += "\""
  print(shellcode)
 
# C Inline Assembler
 if sys.argv[2] == "casm":
  shellcode = "\".byte "
  ctr = 1
  maxlen = 15

  for b in open(sys.argv[1], "rb").read():
   shellcode += "0x" + b.to_bytes(1, "big").hex()
   if ctr != maxlen:
    shellcode += ","
   if ctr == maxlen:
    shellcode += "\\n\\t\"\n\".byte "
    ctr = 0
   ctr += 1
  shellcode = shellcode[:-1] + "\""
  shellcode += "\n\"ret\\n\\t\""
  print(shellcode)
 
# C-Sharp
 if sys.argv[2] == "cs":
  shellcode = ""
  ctr = 1
  maxlen = 15
  
  for b in open(sys.argv[1], "rb").read():
   shellcode += "0x" + b.to_bytes(1, "big").hex()
   if ctr != maxlen:
    shellcode += ","
   if ctr == maxlen:
    shellcode += "\n"
    ctr = 0
   ctr += 1
  shellcode = shellcode[:-1]
  print(shellcode)

# PowerShell
 if sys.argv[2] == "ps1":
  shellcode = "[Byte[]] $buf = "
  ctr = 1
  maxlen = 15
  
  for b in open(sys.argv[1], "rb").read():
   shellcode += "0x" + b.to_bytes(1, "big").hex()
   if ctr != maxlen:
    shellcode += ","
   if ctr == maxlen:
    shellcode += ""
    ctr = 0
   ctr += 1
  shellcode = shellcode[:-1]
  print(shellcode)

# Python
 if sys.argv[2] == "py":
  shellcode = "buf =  b\'\'\nbuf += b\'\\"
  ctr = 1
  maxlen = 12
  
  for b in open(sys.argv[1], "rb").read():
   shellcode += "x" + b.to_bytes(1, "big").hex()
   if ctr != maxlen:
    shellcode += "\\"
   if ctr == maxlen:
    shellcode += "\'\nbuf += b\'\\"
    ctr = 0
   ctr += 1
  shellcode = shellcode[:-1] + "\'"
  print(shellcode)
 
# Hex
 if sys.argv[2] == "hex":
  shellcode = ""
  for b in open(sys.argv[1], "rb").read():
   shellcode += b.to_bytes(1, "big").hex()
  print(shellcode)

 else:
  exit()
