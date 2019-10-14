# order skills alphabetically for CV glossary
# put your skills list here seperated by , 
items = "skill1, skill2, skill3, skill4"
skills = items.split(',')
sort_items = str(sorted(skills))
format_list = sort_items.replace("'",'')
print (format_list.replace("  "," "))