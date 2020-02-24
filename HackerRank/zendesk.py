string="abcdeasdashasdasdas"
z="ZenDesk"

print('.'.join(list(z)))

print ('-'.join( [string[i:i+4] for i in range(0, len(string), 4)] ))
