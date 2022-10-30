def profile_data(player,test,odi,t20):
    data = {
            "Player": player,
            "Test": test,
            "Odi": odi,
            "T20": t20
            }
    return data
def profile_retrieve(player):
    data = {
             "Player" : player
           }
    return data