import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com', 'github.com/cavidparker','youtube.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(1, 20)
    time.sleep(seconds)