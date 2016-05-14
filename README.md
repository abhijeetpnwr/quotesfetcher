# quotesfetcher

Motive:
------

Motive of project is to scrappe quotes on based on  based of categories and to show timely desktop notification of the same using linux's notification API.

For scheduling Script to send tiemly notification:
-------------------------------------------------

# To get desktop nitification every 15 minute , do his entry in your cron file

*/15 * * * * export DISPLAY=:0.0 && /usr/bin/python /home/abhijeet/projects/quotesfetcher/scrapper.py
