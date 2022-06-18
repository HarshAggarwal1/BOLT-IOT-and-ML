# Description of Project ( Check Code in the file for reference)

We are taking live price of Bitcoin in dollars from the server https://min-api.cryptocompare.com. We are using Bolt Library

Step 1: Taking current bitcoin rate from the server

Step 2: Adding the value in a global variable bitcoin_rate.

Step 3: If a new session is started then set boolean to true to keep it stored that from now on we have to check new BTC value with previous BTC value send the message "The new session is started" and bicoin price and continue to another iteration.

Step 4: Now in next iterations get the new BTC value and check it with already stored "bitcoin_rate" with this new value.
        
        If new value is greater or equal then send message and current BTC rate and update "bitcoin_rate" with new value.
        If new value is smaller then send message and current BTC rate and update "bitcoin_rate" with new value.

Step 5: Now as current value is smaller than previous one, set "0" pin value to "HIGH" for 5 seconds to notify, then set it to "LOW".

Step 6: Repeat Step 1 to 5 after every 30 seconds.

PFA the code in the file.
