# objdump_wrapper
Python script (just a function really) that gets the address/bytes/opcode/args from objdump -d

Returns this
	"""
	  [
			{
				"addr"  : 0x400efb,
				"bytes" : array [49, 208],
				"opcode": "xor",
				"args"  : ['eax', 'edx']
			}
		]
	"""

