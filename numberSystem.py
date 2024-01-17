Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bin(18)
'0b10010'
>>> here 0b represent binary te ache
SyntaxError: invalid binary literal
>>> oct(18)
'0o22'
>>> 
>>> 0o represent Octal
SyntaxError: invalid octal literal
>>> hex(18)
'0x12'
>>> 0x represent hexadecimal
SyntaxError: invalid hexadecimal literal
>>> bin(0o35)
'0b11101'
>>> here we converted octal to binary
SyntaxError: invalid syntax
>>> 0o35
29
>>> converted to decimal which is default
SyntaxError: invalid syntax
>>> oct(0xDAD)
'0o6655'
>>> bin(0xBAD)
'0b101110101101'
>>> 76+0o36+0b10111
129
>>> 0b1101+0xC2E+62+0o74
3253
