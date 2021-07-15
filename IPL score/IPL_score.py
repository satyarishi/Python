import sports

from pynotifier import Notification

Matchinfo = sports.get_sport("cricket")

Notification(title = "Ipl score",description = str(Matchinfo),duration = 5).send()