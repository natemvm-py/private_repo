coin_name = ""
coin_value = 0.0
amount_invested = 0.0
exchange_rate = 0.0
recieved_coin = 0.0
held_coin_value = 0.0
user_coin_value = 0.0
gain = 0.0
loss = 0.0

print(
    """
   _____                  _          _____            __ _ _      _____      _            _       _             
  / ____|                | |        |  __ \          / _(_| |    / ____|    | |          | |     | |            
 | |     _ __ _   _ _ __ | |_ ___   | |__) _ __ ___ | |_ _| |_  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    | '__| | | | '_ \| __/ _ \  |  ___| '__/ _ \|  _| | __| | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |____| |  | |_| | |_) | || (_) | | |   | | | (_) | | | | |_  | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \_____|_|   \__, | .__/ \__\___/  |_|   |_|  \___/|_| |_|\__|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
               __/ | |                                                                                          
              |___/|_|                                                                                          
    
    A calculator for finding what profit can be made from a certain coin once it reaches a certain value.
"""
)

coin_name = input("Please enter coin code (e.g. BTC for 'bitcoin'): ")

coin_value = float(input("Enter how much it costs to buy 1 " + coin_name + ": "))
#print(type(coin_value))

amount_invested = float(input("How much NZD did you invest in said coin?: "))

recieved_coin = amount_invested / coin_value

print("You will recieved", recieved_coin, coin_name)
print("Reminder! Fees are not included in this calculation, therefore the amount that ends up in your wallet may slightly vary from this result.")

coin_value_nzd = coin_value * recieved_coin

print("1 ", coin_name, "is worth: ", coin_value_nzd)

user_coin_value = float(input("Enter desired coin value: "))

if(user_coin_value > coin_value):
    gain = recieved_coin * user_coin_value
    print("You gained:", gain)
elif(user_coin_value < coin_value):
    loss = recieved_coin * user_coin_value
    print("You lost:", loss)
elif(user_coin_value == coin_value):
    print("You're coin value at time of purchase is the same as current coin value. No gain or loss.")
else:
    print("You done fucked up somewhere bro. Tell Nate.")
