def main():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %I:%M %p")

	passer = ''
	for i in range(len(roomName)):
		passer = passer + "<p class='roomtitle'>%s</p>" % (roomName[i])
		for j in range(len(accName[i])):
			buttonHtmlName = accName[i][j].replace(" ", "<br>")
			passer = passer + "<span id='button%d%d'><button class='%s' onclick='toggle(%d,%d)'>%s</button></span>" % (i, j, accState(i,j), i, j, buttonHtmlName)

	buttonGrid = Markup(passer)
	templateData = {
		'title' : 'WebGPIO',
		'time': timeString,
		'buttons' : buttonGrid
	}
	return render_template('main.html', **templateData) 