from random import randrange
import webbrowser
import json

#Open json file
with open('episodes.json') as f:
    data = json.load(f);

#Chooses an episode of "The Simpsons" randomly and opens the url
def play_episode():
    #Generate a random number from 1 - x. Total numbero f simpsons episodes is 722 :O
    episode_num = randrange(1, 14)

    for episode in data['episodes']:
        if (episode_num == episode['id']):
            print(episode['season'])
            print(episode['episode'])
            #open episode in browser
            webbrowser.open(episode['url'])

play_episode()
