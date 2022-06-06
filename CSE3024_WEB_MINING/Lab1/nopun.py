
test_str = "Anmol! ? anmol* ()"

out = ""
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for ele in test_str:
	if ele not in punc:
		out = out + ele

print(out)