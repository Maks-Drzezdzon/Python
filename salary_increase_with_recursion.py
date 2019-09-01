def rec(time_years, salary, percent_per_year):
	if time_years < 1:
		return salary
	else:
		tmp = ((((salary/100) * percent_per_year) * 2) + salary)
		return rec(time_years - 1, tmp, percent_per_year)

	    
print(rec(2,29000,3))