string="abcdeasdashasdasdas"
z="ZenDesk"

f=' '.join(list(z))
print(f.replace(' ', '.'))

print ('-'.join( [string[i:i+4] for i in range(0, len(string), 4)] ))
