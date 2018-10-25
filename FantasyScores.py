import requests, bs4, os, openpyxl
#TODO Need a better way to stop a loop once one of the teams scoring is done
#TODO Need to insert a blank if a team just didn't start someone
#TODO Need to create Functions to print to the excel file and simplify loops
j = 1 #This is the team number
wb = openpyxl.Workbook()

while j < 11:
    site = 'http://games.espn.com/ffl/boxscorequick?leagueId=775790&teamId=' + str(j) + '&scoringPeriodId=1&seasonId=2018&view=scoringperiod&version=quick'
    res = requests.get(site)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    playerPositions = soup.select('.pncPlayerRow > .playerSlot')
    playerNames = soup.select('.playertablePlayerName > a')
    playerScore = soup.select('.appliedPointsProGameFinal')

    ws = wb.create_sheet(title="Team " + str(j))

    i = 1 
    for position in playerPositions:
        if i == 50:
            break
        if len(position.getText()) == 0:
            break
        else:
            ws['A'+str(i)] = position.getText()
        i += 1

    i = 1
    for playerName in playerNames:
        if i == 50:
            break
        if len(playerName.getText()) > 0:
            ws['B'+str(i)] = playerName.getText()
            i += 1

    i = 1
    for score in playerScore:
        if i == 50:
            break
        if len(score.getText()) == 0:
            ws['C'+str(i)] == '0'
        else:
            ws['C'+str(i)] = score.getText()
        i += 1
    
    j += 1

wb.save('week1.xlsx')
