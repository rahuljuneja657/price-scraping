
import urllib.request
import re
import schedule
import time
from datetime import datetime

def job():
    
    print ("Cetaphil Gentle Skin Cleanser prices on Walmart.com")
    htmlfile = urllib.request.urlopen("https://www.walmart.com/ip/Cetaphil-Gentle-Skin-Cleanser-Face-Wash-For-Sensitive-and-All-Skin-Types-8-Oz/10317217")
    htmltext = htmlfile.read()
    regex1 = re.findall(r'<span class="price display-inline-block arrange-fit price price--stylized"><span class="visuallyhidden">(.*?)</span>',str(htmltext))
    currenttime = str(datetime.now())
    print ("Cetaphil Gentle Skin Cleanser price:",regex1[1], " at: ",currenttime[0:19])
    regex2 = re.findall(r'<span class="ReviewsHeader-ratingPrefix font-bold">(.*?)</span>',str(htmltext))
    print ("Cetaphil Gentle Skin Cleanser review rate:",regex2)
    
    print ("\n Cetaphil Gentle Skin Cleanser prices on Walgreens.com")
    htmlfile = urllib.request.urlopen("https://www.walgreens.com/store/c/cetaphil-gentle-skin-cleanser/ID=prod5001-product")
    htmltext = htmlfile.read()
    regex3 = re.findall(r'<span id="regular-price-info" class="sr-only" data-reactid="51">(.*?)</span>',str(htmltext))
    currenttime = str(datetime.now())
    print ("Cetaphil Gentle Skin Cleanser price:",regex3, " at: ",currenttime[0:19])
    regex4 = re.findall(r'"overallRating":"(.*?)"',str(htmltext))
    print ("Cetaphil Gentle Skin Cleanser review rate:",regex4)

    print ("\n Cetaphil Gentle Skin Cleanser prices on CVS.com")
    htmlfile = urllib.request.urlopen("https://www.cvs.com/shop/cetaphil-daily-facial-cleanser-prodid-1016716")
    htmltext = htmlfile.read()
    regex5 = re.findall(r'<div dir="auto" aria-label="Price (.*?)" class=',str(htmltext))
    currenttime = str(datetime.now())
    print ("Cetaphil Gentle Skin Cleanser price:",regex5, " at: ",currenttime[0:19])
    regex6 = re.findall(r'<section aria-label="Rated (.*?) out of 5',str(htmltext))
    print ("Cetaphil Gentle Skin Cleanser review rate:",regex6)
    
    print ("\n Cetaphil Gentle Skin Cleanser prices on ebay.com")
    htmlfile = urllib.request.urlopen("https://www.ebay.com/itm/Cetaphil-Daily-Facial-Cleanser-For-Normal-To-Oily-Skin-8-OZ/283668245506?epid=10029956188&_trkparms=ispr%3D1&hash=item420bf1ec02:g:0bYAAOSw-mtdWnT3&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qWQWBLZkoQG6AFs9aR978y4C%2FmZ71vaI2j7kVHY0u59S5IPuSSxbRZRvcPPDeRoEgx600PmZCVE2mEJQTz253LqtNlJ1guArF%2F9032ATHqgMF0%2F%2BRuoBw72%2BYm7GpyB88TlrbrFf7jwEfme5tb3I%2B4%2BLIfQT%2FoChC4TYTA1aK9vOMI%2FLOPcMXs9NQAC8QRpetlbwnw4DHBblv6VRyPfVbplGzn5b%2BV6YSE5wyY5mDNBJb%2FQL5B0vvVyXQWfV9G0XZwFxcZ1omPCGCQU7zmVxEoVe9R4KAbrImTaE%2F4WBMRHQ9UPbbCcltInQjlPCNhhJ9sfMdJr4SHdFgos77CtBlbNjsxxAQeCt%2FxO5sWCSs%2FaysJMKPISqZxLW6%2BnYozHZ3yt6hYkYsf9Kcc1DQLP0l0mGzMwIXMsWA4gG1Ukjfir37ktSIM74TlStr8twB%2Bc1rlfph11c03tM%2F59PAVGi2qlILIr5rQ2JxR2Z5Sd9m%2FU%2FoYQNCecVyWlhtE0XxDGm8m%2BBHooPzLWDwxQC1HV%2FbfNaQKL1Ex48PEgzAomFKiAp7PtmjQ%2FyP7iiWFqHP81X5pBGxI7HyIy7iKoO6%2B28GwxUELD6c537bnf%2F%2BtU5XCHpH8kg8a8SslLOeUuPwpEs9kbLVHe%2FsEaqLX97KstDK9%2BgPbXunLxIf%2FAQmtTG6Dmx1e906ubwUKT%2BNIiDHXIwlp6aJZS91wPtOiWbInxRaYuLqduc0%2Fv8HkpLtcYdd4f4g%3D%3D&checksum=28366824550670f1cbe7272d44938240738719dab430&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qWQWBLZkoQG6AFs9aR978y4C%2FmZ71vaI2j7kVHY0u59S5IPuSSxbRZRvcPPDeRoEgx600PmZCVE2mEJQTz253LqtNlJ1guArF%2F9032ATHqgMF0%2F%2BRuoBw72%2BYm7GpyB88TlrbrFf7jwEfme5tb3I%2B4%2BLIfQT%2FoChC4TYTA1aK9vOMI%2FLOPcMXs9NQAC8QRpetlbwnw4DHBblv6VRyPfVbplGzn5b%2BV6YSE5wyY5mDNBJb%2FQL5B0vvVyXQWfV9G0XZwFxcZ1omPCGCQU7zmVxEoVe9R4KAbrImTaE%2F4WBMRHQ9UPbbCcltInQjlPCNhhJ9sfMdJr4SHdFgos77CtBlbNjsxxAQeCt%2FxO5sWCSs%2FaysJMKPISqZxLW6%2BnYozHZ3yt6hYkYsf9Kcc1DQLP0l0mGzMwIXMsWA4gG1Ukjfir37ktSIM74TlStr8twB%2Bc1rlfph11c03tM%2F59PAVGi2qlILIr5rQ2JxR2Z5Sd9m%2FU%2FoYQNCecVyWlhtE0XxDGm8m%2BBHooPzLWDwxQC1HV%2FbfNaQKL1Ex48PEgzAomFKiAp7PtmjQ%2FyP7iiWFqHP81X5pBGxI7HyIy7iKoO6%2B28GwxUELD6c537bnf%2F%2BtU5XCHpH8kg8a8SslLOeUuPwpEs9kbLVHe%2FsEaqLX97KstDK9%2BgPbXunLxIf%2FAQmtTG6Dmx1e906ubwUKT%2BNIiDHXIwlp6aJZS91wPtOiWbInxRaYuLqduc0%2Fv8HkpLtcYdd4f4g%3D%3D&checksum=28366824550670f1cbe7272d44938240738719dab430")
    htmltext = htmlfile.read()
    regex7 = re.findall(r'<button class="vi-vpqp-pills vi-vpqp-sel" id="vi-vpqp-pills-0" data-index="0"  aria-label="Buy 1 for (.*?), selected">',str(htmltext))
    currenttime = str(datetime.now())
    print ("Cetaphil Gentle Skin Cleanser price:",regex7, " at: ",currenttime[0:19])
    regex8 = re.findall(r' <div role="img" class="ebay-star-rating" aria-label="(.*?) out of 5 stars">',str(htmltext))
    print ("Cetaphil Gentle Skin Cleanser review rate:",regex8)
    
    print ("\n Cetaphil Gentle Skin Cleanser prices on H-E-B.com")
    htmlfile = urllib.request.urlopen("https://www.heb.com/product-detail/cetaphil-gentle-skin-cleanser-for-all-skin-types/231577")
    htmltext = htmlfile.read()
    regex9 = re.findall(r'<meta itemprop="price" content="(.*?)" />',str(htmltext))
    currenttime = str(datetime.now())
    print ("Cetaphil Gentle Skin Cleanser price:",regex9, " at: ",currenttime[0:19])
    print ("Cetaphil Gentle Skin Cleanser review rate not available")
    
    
    #2 Star Wars Jedi: Fallen Order
    
    print ("\n Star Wars Jedi: Fallen Order PC game price on Walmart.com")
    htmlfile = urllib.request.urlopen("https://www.walmart.com/ip/Star-Wars-Jedi-Fallen-Order-Electronic-Arts-PC-014633373073/338776673")
    htmltext = htmlfile.read()
    regex1 = re.findall(r'<div class="prod-PriceHero"><span class="hide-content display-inline-block-m"><span class="price display-inline-block arrange-fit price price--stylized"><span class="visuallyhidden">(.*?)</span>',str(htmltext))
    currenttime = str(datetime.now())
    print ("Star Wars Jedi: Fallen Order price:",regex1, " at: ",currenttime[0:19])
    regex2 = re.findall(r'<div itemprop="aggregateRating" itemscope="" itemtype="//schema.org/AggregateRating" class="stars stars-small"><span class="stars-container" tabindex="0" aria-label="(.*?) Stars',str(htmltext))
    print ("Star Wars Jedi: Fallen Order user review ratings:",regex2)

    print ("\n Star Wars Jedi: Fallen Order PC game price on ebay.com")
    htmlfile = urllib.request.urlopen("https://www.ebay.com/i/123977865439?chn=ps&norover=1&mkevt=1&mkrid=711-117182-37290-0&mkcid=2&itemid=123977865439&targetid=541453972732&device=c&mktype=pla&googleloc=9016722&poi=&campaignid=6470549460&mkgroupid=81274343007&rlsatarget=pla-541453972732&abcId=1139336&merchantid=6296724&gclid=Cj0KCQiAoIPvBRDgARIsAHsCw0-wvWLlTIHK3YxZWFtP_VoLUmxBNrU4IgnAWHagzM9-bbfhFmXrqQcaAoKnEALw_wcB")
    htmltext = htmlfile.read()
    regex3 = re.findall(r'<div class="item-price-logistics-wrapper"><span class="item-price "><h2 class="display-price">(.*?)</h2>',str(htmltext))
    currenttime = str(datetime.now())
    print ("Star Wars Jedi: Fallen Order price:",regex3, " at: ",currenttime[0:19])
    print ("Star Wars Jedi: Fallen Order user review rating not available")
    
    print ("\n Star Wars Jedi: Fallen Order PC game price on kastoff.com")
    htmlfile = urllib.request.urlopen("https://www.kastoff.store/products/star-wars-jedi-fallen-order-deluxe-edition-pc-download-windows-computer-game?variant=31133522493542&currency=USD")
    htmltext = htmlfile.read()
    regex4 = re.findall(r'<span id="ProductPrice" class="product-single__price" itemprop="price" content="(.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("Star Wars Jedi: Fallen Order price:",regex4, " at: ",currenttime[0:19])
    regex5 = re.findall('<meta itemprop="ratingValue" content="(.*?)">',str(htmltext))
    print ("Star Wars Jedi: Fallen Order user review ratings:",regex5)
    
    print ("\n Star Wars Jedi: Fallen Order PC game price on MallDirect.com")
    htmlfile = urllib.request.urlopen("https://mall.direct/star-wars-jedi-fallen-order-deluxe-edition-electronic-arts-xbox-one-014633741377-p240417?language=en&currency=USD&gclid=CjwKCAiA8qLvBRAbEiwAE_ZzPWv3LuW1qN8a65aQhkw3sk6QU7uGn8mSTilXYA2aP435Cs8iPn7pSxoCx2wQAvD_BwE")
    htmltext = htmlfile.read()
    regex6 = re.findall(r'<h2>(.*?)</h2>',str(htmltext))
    currenttime = str(datetime.now())
    print ("Star Wars Jedi: Fallen Order price:",regex6, " at: ",currenttime[0:19])
    print ("Star Wars Jedi: Fallen Order user review rating not available")
    
    print ("\n Star Wars Jedi: Fallen Order PC game price on SamsClub.com")
    htmlfile = urllib.request.urlopen("https://www.samsclub.com/p/star-wars-jedi-fallen-order-ps4/prod23250157")
    htmltext = htmlfile.read()
    regex7 = re.findall(r'<div><div class="sc-channel-price"><div class="sc-channel-price-price"><span class="sc-price "><span class="Price-group" title="current price: (.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("Star Wars Jedi: Fallen Order price:",regex7, " at: ",currenttime[0:19])
    regex8 = re.findall('<meta itemProp="ratingValue" content="5"/><meta itemProp="worstRating" content="0"/><meta itemProp="bestRating" content="(.*?)"/>',str(htmltext))
    print ("Star Wars Jedi: Fallen Order user review ratings:",regex8)
    
    
    #3 God Of War 4 PC
    
    
    print ("\n God of War 4 PS4 game price on Walmart.com")
    htmlfile = urllib.request.urlopen("https://www.walmart.com/ip/Star-Wars-Jedi-Fallen-Order-Electronic-Arts-PC-014633373073/338776673")
    htmltext = htmlfile.read()
    regex1 = re.findall(r'<meta itemprop="priceValidUntil" content=""/><div><span class="display-inline-block-xs prod-PaddingRight--xs valign-top" id="price"><div class="prod-PriceHero"><span class="hide-content display-inline-block-m"><span class="price display-inline-block arrange-fit price price--stylized"><span class="visuallyhidden">(.*?)</span>',str(htmltext))
    currenttime = str(datetime.now())
    print ("God of War 4 price:",regex1, " at: ",currenttime[0:19])
    regex2 = re.findall(r'<div class="ReviewsHeader-wrapper"><div class="ReviewsHeader-ratingContainer" aria-hidden="true"><span class="ReviewsHeader-rating"><span class="ReviewsHeader-ratingPrefix font-bold">(.*?)</span>',str(htmltext))
    print ("God of War 4 user review ratings:",regex2)
    
    print ("\n God of War 4 PS4 game price on ebay.com")
    htmlfile = urllib.request.urlopen("https://www.ebay.com/itm/God-of-War-PlayStation-Hits-PS4-Brand-New/264545147559?_trkparms=ispr%3D1&hash=item3d981e9aa7:g:lqgAAOSwAGxd2-g8&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qV8m%2FWuuOHbrRbR3x2YaQdgtTUoo4ObpVGWS2ruaewj445RMWrKfgDuhnHPxHQ4AeXspGu37Ducu%2Bu4WdUw3kH%2FCnfUPASaaPw26TMZaawvVZRwip2Is1wf4shraUHl4o8pUSfz1lfstkEqE4w0I9pQGUngCg8t48xHp875uqMGfTduWMMuEumhW8QQdwNnJyj11uSmyg3WXqVuogln4LD1E4zgS3QpW3kJyHkWrVxjZcaOzSU5bTuSCguLUlZNbYyWDZZ706I7SXnINMFW4uNOQ52KTZyuezXTuvkVP0L%2FXWx9ZfLqPn%2FdKrTphdenUp5cMW3pu5wBJhZkOnWAjingh5NftB8aGqQMhFt0Pf1MYhETRPP0TEz1Mn9nqBPHhRoqU0is%2BnHpRlSWeRqUs6PYY29S3gU4PXuHV5bIEUh8%2FKqWGurVBh9GyCbn%2BheeHo3p%2B%2BsJN2juqVCfu9dDeKdcl%2FfzBdVR8TT%2BQ92NEao68nltZPanvCkhWrKZIHz3BL%2B2aIupAE9UMgq2hNOXJCZEL82UZNj8Hfg1%2Bynqt8Cz42a%2F%2BoHXrnA1YwrIBV6AYe72YdKpS%2B7NsjjkMYqVpNlDsj6ILjY0wJcYp%2FC060qSBxswCP8nGJbDdKbZGcEDTa9xzCX3ar9WprAl5W%2FMODLfyPwXKwdSY5w7QyEiq3xjsQbHTaqYZQH0oAO%2FOIeflSPG7WGjeD2ZQhZU0J23zoiWs9kXUnmU7mHrCw6VBvijOQ%3D%3D&checksum=26454514755978d425a6598f471daa9ff66bec3033e4&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qV8m%2FWuuOHbrRbR3x2YaQdgtTUoo4ObpVGWS2ruaewj445RMWrKfgDuhnHPxHQ4AeXspGu37Ducu%2Bu4WdUw3kH%2FCnfUPASaaPw26TMZaawvVZRwip2Is1wf4shraUHl4o8pUSfz1lfstkEqE4w0I9pQGUngCg8t48xHp875uqMGfTduWMMuEumhW8QQdwNnJyj11uSmyg3WXqVuogln4LD1E4zgS3QpW3kJyHkWrVxjZcaOzSU5bTuSCguLUlZNbYyWDZZ706I7SXnINMFW4uNOQ52KTZyuezXTuvkVP0L%2FXWx9ZfLqPn%2FdKrTphdenUp5cMW3pu5wBJhZkOnWAjingh5NftB8aGqQMhFt0Pf1MYhETRPP0TEz1Mn9nqBPHhRoqU0is%2BnHpRlSWeRqUs6PYY29S3gU4PXuHV5bIEUh8%2FKqWGurVBh9GyCbn%2BheeHo3p%2B%2BsJN2juqVCfu9dDeKdcl%2FfzBdVR8TT%2BQ92NEao68nltZPanvCkhWrKZIHz3BL%2B2aIupAE9UMgq2hNOXJCZEL82UZNj8Hfg1%2Bynqt8Cz42a%2F%2BoHXrnA1YwrIBV6AYe72YdKpS%2B7NsjjkMYqVpNlDsj6ILjY0wJcYp%2FC060qSBxswCP8nGJbDdKbZGcEDTa9xzCX3ar9WprAl5W%2FMODLfyPwXKwdSY5w7QyEiq3xjsQbHTaqYZQH0oAO%2FOIeflSPG7WGjeD2ZQhZU0J23zoiWs9kXUnmU7mHrCw6VBvijOQ%3D%3D&checksum=26454514755978d425a6598f471daa9ff66bec3033e4")
    htmltext = htmlfile.read()
    regex3 = re.findall(r'<span class="notranslate" id="prcIsum" itemprop="price"  style="" content="(.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("God of War 4 price:",regex3, " at: ",currenttime[0:19])
    regex3 = re.findall(r'<div role="img" class="ebay-star-rating" aria-label="(.*?) out of 5 stars">',str(htmltext))
    print ("God of War 4 user review ratings:",regex3)

    print ("\n God of War 4 PS4 game price on kastoff.com")
    htmlfile = urllib.request.urlopen("https://www.kastoff.store/products/star-wars-jedi-fallen-order-deluxe-edition-pc-download-windows-computer-game?variant=31133522493542&currency=USD")
    htmltext = htmlfile.read()
    regex4 = re.findall(r'<span id="ProductPrice" class="product-single__price" itemprop="price" content="(.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("God of War 4 price:",regex4, " at: ",currenttime[0:19])
    regex5 = re.findall('<meta itemprop="ratingValue" content="(.*?)">',str(htmltext))
    print ("God of War 4 user review ratings:",regex5)
    
    print ("\n God of War 4 PS4 game price on MallDirect.com")
    htmlfile = urllib.request.urlopen("https://mall.direct/god-of-war-sony-playstation-4-711719506133-p241346?search=god%20of%20war&description=true")
    htmltext = htmlfile.read()
    regex6 = re.findall(r'<h2>(.*?)</h2>',str(htmltext))
    currenttime = str(datetime.now())
    print ("God of War 4 price:",regex6, " at: ",currenttime[0:19])
    print ("God of War 4 user review rating not available")
    
    print ("\n God of War 4 PS4 game price on SamsClub.com")
    htmlfile = urllib.request.urlopen("https://www.samsclub.com/p/god-of-war-ps4/prod22922143?xid=plp_product_1_13")
    htmltext = htmlfile.read()
    regex7 = re.findall(r'<div class="sc-channel sc-channel-online"><div><div class="sc-channel-price"><div class="sc-channel-price-price"><span class="sc-price "><span class="Price-group" title="current price: (.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("God of War 4 price:",regex7, " at: ",currenttime[0:19])
    regex8 = re.findall('<meta itemProp="mpn" content="3001886"/><span itemProp="aggregateRating" itemscope="" itemType="http://schema.org/AggregateRating"><meta itemProp="ratingValue" content="(.*?)"/>',str(htmltext))
    print ("God of War 4 user review ratings:",regex8)
    
    
    #4 FIFA 20 PS$
    
    
    print ("\n FIFA 20 PS4 game price on Walmart.com")
    htmlfile = urllib.request.urlopen("https://www.walmart.com/ip/FIFA-20-Electronic-Arts-PlayStation-4-014633738636/807355352")
    htmltext = htmlfile.read()
    regex1 = re.findall(r'<meta itemprop="priceValidUntil" content=""/><div><span class="display-inline-block-xs prod-PaddingRight--xs valign-top" id="price"><div class="prod-PriceHero"><span class="hide-content display-inline-block-m"><span class="price display-inline-block arrange-fit price price--stylized"><span class="visuallyhidden">(.*?)</span>',str(htmltext))
    currenttime = str(datetime.now())
    print ("FIFA 20 price:",regex1, " at: ",currenttime[0:19])
    regex2 = re.findall(r'<div class="ReviewsHeader-wrapper"><div class="ReviewsHeader-ratingContainer" aria-hidden="true"><span class="ReviewsHeader-rating"><span class="ReviewsHeader-ratingPrefix font-bold">(.*?)</span>',str(htmltext))
    print ("FIFA 20 user review ratings:",regex2)
    
    print ("\n FIFA 20 PS4 game price on ebay.com")
    htmlfile = urllib.request.urlopen("https://www.ebay.com/itm/FIFA-20-Standard-Edition-PlayStation-4/283697663055?epid=7032785009&hash=item420db2cc4f:g:WbEAAOSwihtd5ixu")
    htmltext = htmlfile.read()
    regex3 = re.findall(r'<span class="notranslate" id="prcIsum" itemprop="price"  style="" content="(.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("FIFA 20 price:",regex3, " at: ",currenttime[0:19])
    regex3 = re.findall(r'<div role="img" class="ebay-star-rating" aria-label="(.*?) out of 5 stars">',str(htmltext))
    print ("FIFA 20 user review ratings:",regex3[1])
    
    print ("\n FIFA 20 PS4 game price on Kastoff.com")
    htmlfile = urllib.request.urlopen("https://www.kastoff.store/products/fifa-19-pc-soccer-download-windows-computer-game?_pos=1&_sid=ecfdd380a&_ss=r")
    htmltext = htmlfile.read()
    regex4 = re.findall(r'<span id="ProductPrice" class="product-single__price" itemprop="price" content="(.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("FIFA 20 price:",regex4, " at: ",currenttime[0:19])
    regex5 = re.findall('<meta itemprop="ratingValue" content="(.*?)">',str(htmltext))
    print ("FIFA 20 user review ratings:",regex5)
    
    print ("\n FIFA 20 PS4 game price on MallDirect.com")
    htmlfile = urllib.request.urlopen("https://mall.direct/fifa-20-electronic-arts-xbox-one-014633738650-p240382?search=fifa&description=true")
    htmltext = htmlfile.read()
    regex6 = re.findall(r'<h2>(.*?)</h2>',str(htmltext))
    currenttime = str(datetime.now())
    print ("FIFA 20 price:",regex6, " at: ",currenttime[0:19])
    print ("FIFA 20 user review rating not available")

    print ("\n FIFA 20 PS4 game price on SamsClub.com")
    htmlfile = urllib.request.urlopen("https://www.samsclub.com/p/fifa-20-playstation-ps4/prod23603791?xid=plp_product_1_23")
    htmltext = htmlfile.read()
    regex7 = re.findall(r'<div class="sc-channel sc-channel-online"><div><div class="sc-channel-price"><div class="sc-channel-price-price"><span class="sc-price "><span class="Price-group" title="current price: (.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("FIFA 20 price:",regex7, " at: ",currenttime[0:19])
    print ("FIFA 20 user review rating not available")
    
    
    #5 GTA V
    
    
    print ("\n GTA V game price on Walmart.com")
    htmlfile = urllib.request.urlopen("https://www.walmart.com/ip/Grand-Theft-Auto-V-Premium-Edition-Rockstar-Games-PlayStation-4-710425570322/280167762")
    htmltext = htmlfile.read()
    regex1 = re.findall(r'<meta itemprop="priceValidUntil" content=""/><div><span class="display-inline-block-xs prod-PaddingRight--xs valign-top" id="price"><div class="prod-PriceHero"><span class="hide-content display-inline-block-m"><span class="price display-inline-block arrange-fit price price--stylized"><span class="visuallyhidden">(.*?)</span>',str(htmltext))
    currenttime = str(datetime.now())
    print ("GTA V price:",regex1, " at: ",currenttime[0:19])
    regex2 = re.findall(r'<div class="ReviewsHeader-wrapper"><div class="ReviewsHeader-ratingContainer" aria-hidden="true"><span class="ReviewsHeader-rating"><span class="ReviewsHeader-ratingPrefix font-bold">(.*?)</span>',str(htmltext))
    print ("GTA V user review ratings:",regex2)
    
    print ("\n GTA V game price on ebay.com")
    htmlfile = urllib.request.urlopen("https://www.ebay.com/itm/Grand-Theft-Auto-V-Premium-Edition-PS4-Brand-New-Factory-Sealed-GTA-5/312732952285?epid=13030519243&_trkparms=ispr%3D1&hash=item48d05626dd:g:ttIAAOSwRQxdVYfD:sc:USPSFirstClass!47906!US!-1&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qWmrLmD0L47etLKihYX2SSBOBieVPHGle5OZIe4njS0bTrrKGIsB1RbifW5Y8tNxPVxJl8kT9FQsXEHojigZwLNinyf1BLqduZxE7HULaiHnBEEfoTjwU2SmTL0gQkswaMBKqYEE8bj4n7gDeb%2Ba4ja3Xy%2F8%2BUUUdsgwTkRkfIrzXeGQKDzy9e13bzvRSTU9a1hKE%2BixicQONitl0e%2Bgx9D4nFbdIlpFraMwFiR9iGHuZFopGxl8I6jQ%2B8qP4%2FiPISC4ZtjpPFpABEfhqYgQ%2BA%2B%2BZw6xusI36sSk%2BBvMbrpFpr2fJh91QxXGcoTlgzDzQWx0Gh4XqWVZpV%2FY7HHxt8O37JUG0kgU5s0wYWralBbbxKKbJHcKbj3RYrzHkRKvLMDAYl56En%2BWEfbWIaEvSo7j%2B3Z6MMjFjUsIlfe71zdv9s8aPRbABg2uItytv55xotqu1RY44Zz3t6Jdl%2B81DLGIdnEeI9Iuz5TLbua1uPB6F5eGrXYgOlfJfFXRp54FBA9EYFkq0fd3Wmo%2B5NuSrBK5KqsSbiRpcs6LlEKFd7NWSkTkTD2jC9tO%2BGP3ADMNSjm0QLZGoksebpvuIvmBchHZlgP6XgavO7zQW%2Bp7MuunPMDoxNYIEcu7v3HBy%2BIenUsTquoRTbo%2Fuov0VbxK1gB%2FIVCC%2FWD0AqCCkid647BqY6eMpgYdW%2FyzAE3oX9z941P7Q55cDI2Z0qORcMw7%2B1X0s3rtRKim%2Fi6UHWKxZ6BcA%3D%3D&checksum=312732952285946538603f7c486ebc93238857c25e10&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qWmrLmD0L47etLKihYX2SSBOBieVPHGle5OZIe4njS0bTrrKGIsB1RbifW5Y8tNxPVxJl8kT9FQsXEHojigZwLNinyf1BLqduZxE7HULaiHnBEEfoTjwU2SmTL0gQkswaMBKqYEE8bj4n7gDeb%2Ba4ja3Xy%2F8%2BUUUdsgwTkRkfIrzXeGQKDzy9e13bzvRSTU9a1hKE%2BixicQONitl0e%2Bgx9D4nFbdIlpFraMwFiR9iGHuZFopGxl8I6jQ%2B8qP4%2FiPISC4ZtjpPFpABEfhqYgQ%2BA%2B%2BZw6xusI36sSk%2BBvMbrpFpr2fJh91QxXGcoTlgzDzQWx0Gh4XqWVZpV%2FY7HHxt8O37JUG0kgU5s0wYWralBbbxKKbJHcKbj3RYrzHkRKvLMDAYl56En%2BWEfbWIaEvSo7j%2B3Z6MMjFjUsIlfe71zdv9s8aPRbABg2uItytv55xotqu1RY44Zz3t6Jdl%2B81DLGIdnEeI9Iuz5TLbua1uPB6F5eGrXYgOlfJfFXRp54FBA9EYFkq0fd3Wmo%2B5NuSrBK5KqsSbiRpcs6LlEKFd7NWSkTkTD2jC9tO%2BGP3ADMNSjm0QLZGoksebpvuIvmBchHZlgP6XgavO7zQW%2Bp7MuunPMDoxNYIEcu7v3HBy%2BIenUsTquoRTbo%2Fuov0VbxK1gB%2FIVCC%2FWD0AqCCkid647BqY6eMpgYdW%2FyzAE3oX9z941P7Q55cDI2Z0qORcMw7%2B1X0s3rtRKim%2Fi6UHWKxZ6BcA%3D%3D&checksum=312732952285946538603f7c486ebc93238857c25e10")
    htmltext = htmlfile.read()
    regex3 = re.findall(r'<span class="notranslate" id="prcIsum" itemprop="price"  style="" content="(.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("GTA V price:",regex3, " at: ",currenttime[0:19])
    regex3 = re.findall(r'<div role="img" class="ebay-star-rating" aria-label="(.*?) out of 5 stars">',str(htmltext))
    print ("GTA V user review ratings:",regex3[1])
    
    print ("\n GTA V game price on Kastoff.com")
    htmlfile = urllib.request.urlopen("https://www.kastoff.store/products/grand-theft-auto-v-5-gta-5-rockstar-social-club-key-code-pc-download-windows-computer-game")
    htmltext = htmlfile.read()
    regex4 = re.findall(r'<span id="ProductPrice" class="product-single__price" itemprop="price" content="(.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("GTA V price:",regex4, " at: ",currenttime[0:19])
    print ("GTA V user review rating not available")
    
    print ("\n GTA V game price on MallDirect.com")
    htmlfile = urllib.request.urlopen("https://mall.direct/toys-games/ps4s/ps4-games/grand-theft-auto-v-rockstar-games-playstation-4-710425475252-p197246")
    htmltext = htmlfile.read()
    regex6 = re.findall(r'<h2>(.*?)</h2>',str(htmltext))
    currenttime = str(datetime.now())
    print ("GTA V price:",regex6, " at: ",currenttime[0:19])
    print ("GTA V user review rating not available")
    
    print ("\n GTA V game price on SamsClub.com")
    htmlfile = urllib.request.urlopen("https://www.samsclub.com/p/no-mans-sky-beyond-playstation-ps4/prod23990038?xid=plp_product_1_28")
    htmltext = htmlfile.read()
    regex7 = re.findall(r'<div class="sc-channel sc-channel-online"><div><div class="sc-channel-price"><div class="sc-channel-price-price"><span class="sc-price "><span class="Price-group" title="current price: (.*?)">',str(htmltext))
    currenttime = str(datetime.now())
    print ("GTA V price:",regex7, " at: ",currenttime[0:19])
    print ("GTA V user review rating not available")
    
    
        
 # schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every(1).day.at("21:57").do(job)
# schedule.every(8).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)