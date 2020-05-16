
import urllib.request
import re
import schedule
import time
import smtplib
from datetime import datetime

def jobemail():
    
    print ("\n God of War 4 PS4 game price on Walmart.com")
    htmlfile = urllib.request.urlopen("https://www.walmart.com/ip/Star-Wars-Jedi-Fallen-Order-Electronic-Arts-PC-014633373073/338776673")
    htmltext = htmlfile.read()
    regex1 = re.findall(r'<meta itemprop="priceValidUntil" content=""/><div><span class="display-inline-block-xs prod-PaddingRight--xs valign-top" id="price"><div class="prod-PriceHero"><span class="hide-content display-inline-block-m"><span class="price display-inline-block arrange-fit price price--stylized"><span class="visuallyhidden">(.*?)</span>',str(htmltext))
    currenttime = str(datetime.now())
    print ("God of War 4 price:",regex1, " at: ",currenttime[0:19])
    regex2 = re.findall(r'<div class="ReviewsHeader-wrapper"><div class="ReviewsHeader-ratingContainer" aria-hidden="true"><span class="ReviewsHeader-rating"><span class="ReviewsHeader-ratingPrefix font-bold">(.*?)</span>',str(htmltext))
    print ("God of War 4 user review ratings:",regex2)
    
    server = smtplib.SMTP('smtp.live.com', 587)
    server.starttls()
    server.login("rjuneja@purdue.edu", "RAli2357")
 
    # type subject
    SUBJECT = "Price Update " + str(datetime.now())[0:19]

    # type message
    msg1 = "Price & Rating updates of God of War 4 PS4\n"
    msg2 = "Current time " + str(datetime.now())[0:19] +"\n"
   

    msg5 = "Price:" + str(regex1) + "\n"
    msg6 = "Rating:" + str(regex2) + "\n"

    TEXT = msg1 + msg2 + msg5 + msg6
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    # send email (sender, receiver, message with subject)
    server.sendmail("rjuneja@purdue.edu", "rahuljuneja657@gmail.com", msg)
    server.quit()

schedule.every().day.at("22:32").do(jobemail)

while 1:
    schedule.run_pending()
    time.sleep(1)

# To clear all functions, in console type
# schedule.clear()
