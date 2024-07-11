#!/usr/bin/env python
import sys
Version = "Version: 0.3"
print(" _     _       ____  ____   ____")
print("| |__ (_)_ __ |___ \/ ___| / ___|")
print("| '_ \| | '_ \  __) \___ \| |")
print("| |_) | | | | |/ __/ ___) | |___")
print("|_.__/|_|_| |_|_____|____/ \____|")
print(version)
print("\n\n")
if __name__ == "__main__":
 if len(sys.argv) < 3:
  print("usage: %s file.bin c|casm|cs\n" % (sys.argv[0],))
  sys.exit(0)

 if sys.argv[2] == "c":
  # for c shellcode
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
 
 if sys.argv[2] == "casm":
  # for inline c asm
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
 
 if sys.argv[2] == "cs":
 #else:
  # for cs shellcode
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
 else:
  exit()
