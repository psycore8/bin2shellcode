#Organisation/Aktuell 
# Convert binary to different outputs

A little helper to convert raw shellcode into different outputs

## Usage

```
python3 bin2sc.py <binary_file> <argument> 
```

| Argument | Description       | Output                      |
| -------- | ----------------- | --------------------------- |
| `c`      | C / C++           | `"\x00\xff"`                |
| `casm`   | C inline assembly | `".byte 0x00,0xff\n\t"`     |
| `cs`     | C-Sharp           | `0x00,0xff`                 |
| hex      | hex dunp          | `00ff`                      |
| ps1      | ps1 buffer        | `[Byte[]] $buf = 0x00,0xff` |
| py       | Python buffer     | `buf =+ b'\x00\xff'`        |



![](./bin2sc.png)


