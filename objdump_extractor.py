#!/usr/bin/python
import subprocess
# parse objdump
# by pasteBin - Jordan

def objdump_extract(binname):
	"""
	Returns an array of elements with dicts
	like this:
		[
			{
				"addr"  : 0x400efb,
				"bytes" : array [49, 208],
				"opcode": "xor",
				"args"  : ['eax', 'edx']
			}
		]
	"""
	extracted = []
	response = ""
	try:
		response = subprocess.check_output(["objdump", "-d", "-M", "intel", binname])
	except:
		# maybe mac
		response = subprocess.check_output(["gobjdump", "-d", "-M", "intel", binname])
	# print response.replace('\x09', 'A')
	for line in response.split('\n'):
		if line.count('\x09') != 2:
			continue
		entry = {}
		sections = line.split('\x09')
		address = int(sections[0].replace(":",''), 16)
		entry["address"] = address
		bytes = filter(None, sections[1].split(' '))
		entry["bytes"] = [int(x,16) for x in bytes]
		cmd = sections[2]
		first_space = cmd.index(' ')
		# get the first bit i.e opcode
		entry["opcode"] = cmd[:first_space]
		# get the second bit, split the args on commas and filter out empties
		entry["args"] = filter(None, cmd[first_space:].lstrip().split(','))
		extracted.append(entry)
	return extracted


objdump_extract("path/to/binary")


