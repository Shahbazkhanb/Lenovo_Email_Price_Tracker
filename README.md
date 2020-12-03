# Lenovo_Email_Price_Tracker
The .py file contained webscrapes details off of the Lenovo link i provided it. It extracts the current price of the model that I want to buy (but is currently too expensive). If the price dips below $1,200 then it will send me an email alert to check the price. I learned to use the SMTP library and how to connect to my email via connection codes. This also reaffirmed my knowledge of webscraping via the BeautifulSoup and Requests library.
  
I've created a .bat file and run this daily via Windows Task Scheduler to check for daily price changes
  
To send the email, it requires my user agent details, email password and email username, which I have removed for privacy reasons
