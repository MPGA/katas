def movie(card, ticket, perc):
	n = 1
	total = 0
	aux = ticket
	while True:
		ticket_price = ticket*n
		aux *= perc
		total += aux
		if(ticket_price>round(total+card)):
			break;
		n+=1
	return n
