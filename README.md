# EastVantage-Task
Task:

Create an address book application where API users can create, update and delete
addresses.
The address should:
-contain the coordinates of the address.
-be saved to an SQLite database.
-be validated
API Users should also be able to retrieve the addresses that are within a given distance
and location coordinates.


I have deployed it on heroku but you can interact with it on your localhost as well

The admin panel of this app can be accessed by:

https://eastvantage-address-book.herokuapp.com/admin/
username: 123456
password: 123456

1. TO GET THE LIST OF ALL AVAILABLE ADDRESSES
		 		 
		Api Path :- https://eastvantage-address-book.herokuapp.com/
		its a simple get request so you get all the available address in order of their city name

2. TO GET,POST,PATCH THE ADDRESS OF ONE PRIMARY KEY ID IS AS FOLLOWS
		
			
		Api Path :- https://eastvantage-address-book.herokuapp.com/address/1
    
    here it is of the type url <int:pk> where you pass the primary key an get patch post address via this url
    
		
		eg: in json
        {
          "add": "Old Trafford \r\nstretford end",
          "city": "Stretford",
          "state": "Manchester",
          "country": "England United Kingdom",
          "zipcode": "11001",
          "latitude": "53.463600",
          "longitude": "-2.290524"
        }
        
     same for patch request 
			

			
3. GET NEARBY ADDRESS OF THE GIVEN KEY VIA PARAMTER IN THE API KEY
		
		Api path:- https://eastvantage-address-book.herokuapp.com/nearby-address/?aid=1
		
		it takes a parameter at the end as an address id as aid to generate list of nearby addresses to that address
		
