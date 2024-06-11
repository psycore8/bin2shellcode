# Convert binary to different outputs

A little helper to convert raw shellcode into different outputs

## Usage

```
python3 bin2sc.py <file>.bin c|casm|cs
```
c - C style format

`"\x00"`

casm - C Inline ASM

`".byte 0x00\n\t"`

cs - C# format

`0x00`

## Credits

Forked from [fanbyprinciple](https://github.com/fanbyprinciple/bin2shellcode)

![](./havoc.png)


