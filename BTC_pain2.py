#This program plays the song "You suffer" every time the price of BTC dips below a certain price
# https://open.spotify.com/intl-fr/track/5oD2Z1OOx1Tmcu2mc9sLY2?si=4f0a9fe2c91e42ba
"""
TO do:
Clean up:
Write into functions

The State list solution is not ideal, a sort of "State" boolean would be better
Error handling: 
- What if no internet connection to fetch the BTC price
- BTC price provider times out
- mp3 not found

"""

import requests
import vlc
import threading
import numpy

threshold = int(input("What is you threshold today?"))
#function to retreieve the BTC price, store it as variable 

alert = vlc.MediaPlayer(r"C:\Users\numap\Documents\Labo secu\Dev\BTC_suffer\You Suffer (Napalm Death).mp3")
State = []

def Get_BTC_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    eur_value = data["bpi"]["EUR"]["rate_float"]
    timestamp = data["time"]["updatedISO"]
    print (timestamp, eur_value)
    #This following loop should be replaced by a while loop so that nothing happens whi eur_value remains below the threshold, and triggers only when threshold is broken upwards or downward
# should have a state variable TRUE/FALSE above or below threshold and compare it to previous state, if state changes, then triggers
#While state remains the same, do nothing, simply print, if state changes, trigger alarm

    mining_state = "FALSE" if eur_value < threshold else "TRUE"
    State.append(mining_state)

def Check_BTC_Price():

    if len(State) > 2:
        if State[-1] != State[-2]:
            print(timestamp, "Threshold has been crossed! You suffer!")
            alert.play()
            del State[0]
        else:
            None
            print(timestamp, "BTC is still under or over threshold of ", threshold)
            del State[0]
    else:
        None
    print(State)


'''    
    if eur_value < threshold:
        print("BTC is under you threshold of", threshold, ", it is too cheap to mine, YOU SUFFER!")
        #print (mining_state)
     else: 
        print ("the price of BTC is over your threshold of ", threshold, ",MINE IT!")
        #print (mining_state)
'''        

def main():
    threading.Timer(10.0, BTC_price).start()
    BTC_price()
    Check_BTC_Price()

if __name__ == '__main__':
    main()






#Part 1: Fetch the price of BTC in EUR online, using an API like CoinGecko or Binance








#Part 2: Create a while loop that checks the price of BTC against the threshold, if the condition is met, play the song you suffer on VLC
#while eur_value < threshold:



#How to go back in the while loop after meeting condition?

#invoke the VLC player and play the song
#importing the VLC library
#find the mp3 file in local relative path

#close VLC player


#To do features: 
# maintain the script runing in the background using CRONJOBS. 
# Upon start, ask the user for the threshold price
# Print the BTC at set time interval
# When price dips below threshold, pop up a window with the message "YOU SUFFER"
