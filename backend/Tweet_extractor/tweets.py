from pyparsing import FollowedBy
from sqlalchemy import true
import tweepy
from . import scrape_data as sd
# import pandas as 

consumer_key = "ELB5ShB1IY78UaqpIPdj0YamN"
consumer_secret = "vKC2Pizeh7fc1Y6iG5CDWncvCq8HJwcHwR3kvl1dLMIKDuSI9r"
access_token = "1551970360496496641-QKzmkFWK3v6FyXEgEQZXxQ8y27kYp2"
access_token_secret = "DAQ1JuIalr9eMkvivjsemKhRAlUEeKIRde2gt3PO0aFQS"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


Electronics_Keywords = [
    "HP Pavilion X360 Core i3 11th Gen",
    "APPLE ipad mini 6",
    "DELL Vostro",
    "alienware",
    "dell xps 13 ",
    "Apple MacBook Pro ",
    " Acer Swift 3",
    "MacBook Air M2",
    "lenovo thinkpad i5",
    " Microsoft Surface laptop",
    "Asus ZenBook",
    "Asus ROG Zephyrus",
    " Lenovo IdeaPad ",
    "HP Spectre",
    "MICROSOFT surDELLface pro 8 with keyboard",
    "Voice Assistant and 1.69 HD Display",
    "Amazfit GTS 4 Mini Smartwatch",
    "Realme Buds Air 3 Neo",
    "RealmeWatch3",
    "DELL G15 gaming laptop with RTX",
    "HP Pavilion 15 with 12th Gen Intel",
]
Shoes_Keywords = [
    "Zixer Men's PRO ",
    "Comfort shoes Leather ",
    "RedTape Women White Sneakers",
    "Jack & Jones Men Charcoal Grey Solid Leather Brogues ",
    "FILA Men Grey Printed PU Sneakers",
    "MAX Women Green Walking Non-Marking Shoes",
    "bata Boys Black Velcro School Sneakers",
    "Puma Softride Enzo NXT Men Red Textile Shoes",
    " Shoetopia Women White Sneakers",
    "bacca bucci Men Black Leather High-Top Chelsea Boots",
    "Denill Peach-Coloured Block Pumps",
    "liberty Women Green Mesh Walking Non-Marking Shoes",
    "FAUSTO Men Tan Textured PU Loafers",
    "Tucson Men ",
    "NIKE Women White Downshifter 11",
    "ADIDAS Men Teal Blue",
    "Roadster Men Grey Cargos",
    "Sparx Men Black Mesh Running",
    "Skechers Women Black Go Walk Joy ",
    "Sparx Men Black",
    "PROVOGUE Men Brown Textured Loafers",
    "FENTACIA Men Brown Loafers ",
    "MACTREE Men ",
    "Nike Air Zoom Vomero ",
    "kerzl Women ",
    "SEGA Original ",
    "Paragon EV0740G ",
    "Paragon K1003G M For Men",
    "asics GEL-Trabuco ",
    "SAUCONY Triumph ",
    "Tuff Slip On Sneakers For Men",
    "HimQuen Girls Stylish High ",
    "KRAFTER New Stylish ",
    "REEBOK IDENTITY ",
    "Nike Air Zoom Pegasus 38",
    "REEBOK Plus Lite ",
    "Da Veneto Running Shoes For Men",
    "Paragon shoe",
    "Joker Italy Men's ",
    "Bata shoes",
    "HimQuen Girls Stylish High Heel ",
    "HOTSTYLE Loafers For Men",
    "NIKE shoes",
    "PUMA Tango Running Shoes For Men",
    "FILA Running Shoes For Men",
    "METRO shoes",
    "METRO Awesome Casuals For Men",
    "Jordan shoes",
    "AIRBELL Sneakers For Men",
    "RED TAPE shoes",
]
Fashion_Keywords = [
    "Ira Collections",
    "Roadster Men Grey Cargos",
    "LIBAS Women Pink Flora",
    "KOTTY Women Blue",
    "Indo Era Women Kurta and Palazzo Set Cotton Blend ",
    "Varanga Women Printed Cotton Blend Straight Kurta ",
    "FeelBlue Color Block Women Pink Regular Shorts ",
    "Alaya By Stage3 Green Ethnic Motifs Midi Dress",
    "Roadster Washed Women Blue Denim Shorts ",
    "WROGN Solid Men White Track Pants",
    "Fabindia Women Striped Crepe Straight Kurta",
    "Nayo Women Printed Pure Cotton Straight Kurta",
    "Aspora Embellished Bollywood Georgette Saree ",
    "soch Women Churidar and Dupatta Set Georgette",
    "NAUTICA ",
    "Indo Era Women Kurta and Palazzo Set Cotton Silk",
    "DUCATI Full Sleeve Color Block Men Sweatshirt ",
    "Urban creation Sleeveless Printed Women White, Blue Top  ",
    "SASSAFRAS Regular Women Blue Jeans ",
    " DILLINGER Typography Women Round Neck Black T-Shirt",
    "GLAM ROOTS Women Printed Cotton Blend Anarkali Kurta ",
    "Varanga Women Printed Pure Cotton Anarkali Kurta",
    "Messenger Bag",
    "Urban Creation",
    "FILA Color Block Women Pink Tights",
    "FILA CLOTHING",
    "Classic Polo Slim Fit Men Blue Cotton Blend Trousers",
    "labh traders Sports Shorts",
    "Urbano Fashion Slim Men White Jeans",
    "Lzard Regular Men Light Blue Jeans",
    "GulshanCollection Small ",
    "EVA White Women Clutch - Mini",
    "Alan Jones Full Sleeve Solid Men Sweatshirt",
    "FastColors Full Sleeve Solid Men Sweatshirt",
    "Rich Club Polarized Aviator, Wayfarer Sunglasses",
    "METRONAUT Polarized, Gradient Sunglass",
    "Blackberrys Skinny Men Grey Jeans",
    "WILLIAM PAUL Black Men Sling Bag",
    "Poloport UV Protection Wayfarer, Retro Square, Rectangular Sunglasses ",
    "OLD JERSEY Regular Men Black Jeans",
    "Aarzu Style Slim Men Black Jeans",
    "VDangi Women Solid Low Cut, Peds/Footie/No-Show",
    "House Of Kkarma Women Solid Green Night Suit Set",
    "House Of Kkarma Women Printed Black Top & Pyjama Set",
    "ACCESSORIZE LONDON Women Tan Shoulder Bag",
    "Snappy Women Black Shoulder Bag - Mini",
    "Zuperia UV Protection Retro Square Sunglasses",
    "ABNER Mirrored, UV Protection Sports Sunglasses",
    "Benling BL-GC-007-BLK-MGRN Analog-Digital Watch",
    "MF Limited Edition Analog Watch",
    "Rangmanch by Pantaloons Women Printed Pure Cotton Straight Kurta",
    "Jade Blue Men Regular Fit Checkered Spread Collar Formal Shirt",
    "Aturabi Casual Flared Sleeves Solid Women Blue Top",
    "LACOSTE 2010972 LACOSTE.12.12 Analog Watch",
    "LACOSTE L.12.12 Pour Lui Natural Eau de Toilette",
    "Urban Creation Pack of 2 Party Sleeveless Printed Women Dark Blue Top",
    "U.S. POLO ASSN",
    "MODA ELEMENTI Round Neck Solid Women Pullover",
    "D'CART Women Fit and Flare Black Dress",
    "EDGETOUCH ",
    "ALDO Women Black Tote",
    "ALDO Women Beige Tote",
    "usi Solid Men V Neck Red T-Shirt",
    "quadronic Pumice Stone Foot Feet Body Cleaning for Man and Women Combo",
    "Clirva Party One Shoulder Sleeves Striped Women Black Top",
    "OURDREAM Casual One Shoulder Sleeves Solid Women Red Top",
]
Phones_keywords = [
    "OnePlus Nord",
    "Infinix HOT 12 Play",
    "vivo T1 Pro 5G",
    "Infinix Note 12 TURBO",
    "vivo X80 ",
    "OnePlus 10R",
    "MOTOROLA Edge 30",
    "MOTOROLA g82",
    "REDMI Note 10 Pro",
    "Realme Narzo",
    "Tecno Phantom X",
    "Tecno Camon",
    "Tecno Spark 9",
    "MOTOROLA e32s",
    "boAt Wave ",
    "APPLE iPhone 6",
    "Realme Pad X",
    "MOTOROLA g31",
    "OnePlus 10 Pro 5G",
    "realme Pad X ",
    "realme Pad Mini ",
    "realme Buds Air 3 Neo ",
    "Sansui 5 L ",
    "realme Watch 3 ",
    " Xiaomi Redmi K50i",
    " Apple iPhone 12 Mini 2020",
    "WONDERWORLD ™ DZ09 Gear Fitness Smartwatch  ",
    "Apple AirPods ",
    "APPLE iPhone XR ",
    "SAMSUNG Galaxy Z ",
    "GORILLA Extra Strong ",
    "ASUS ZenFone Max M2 ",
    "SAMSUNG Galaxy S21 ",
    "Google Pixel 6a ",
    "MOTOROLA g31 ",
    "APPLE iPhone 13 Pro Max ",
    "OnePlus 9 Pro 5G",
    "ASUS ZenFone Max Pro M2",
    "realme 9 Pro+ 5G ",
    "vivo X60 Pro",
    "APPLE iPhone 6 ",
    "OPPO F19 Pro ",
    "Google Pixel 2 ",
    "IQOO Neo 6 5G",
]

# number of tweets to fetch
number_of_tweets_to_extract = 100


def electronics(name="Electronics"):
    Electronics_List = [
        "#computers",
        "#tech",
        "#innovation",
        "laptops",
        " #Technology",
        "gbs_systems",
        "#laptops",
        "Delllaptop",
        "Laptop Mag",
        "hplaptop",
        "avitalaptop",
        "iball laptop",
    ]
    Electronics_tweet = []
    count = 0
    for electronic in Electronics_List:
        tweets_electronics = tweepy.Cursor(
            api.search_tweets,
            electronic,
            tweet_mode="extended",
            lang="en",
            include_entities=True,
        ).items(number_of_tweets_to_extract)
        tweet_count = 0
        for tweet in tweets_electronics:
            try:
                # information of tweet
                txt = tweet.full_text
                id = tweet.id
                screen_id_name = tweet.author._json["screen_name"]
                user = api.get_user(screen_name=screen_id_name)
                follower_count = user.followers_count
                url = "https://twitter.com/twitter/statuses/" + str(id)
                likes = tweet.favorite_count
                retweet_count = tweet.retweet_count
                Trend_score = likes + retweet_count + follower_count * 0.4
                hash_list = []
                # Inserting hashtags in hash_list
                if "hashtags" in tweet.entities:
                    hashtag = tweet.entities["hashtags"]
                    for hsht in hashtag:
                        hash_list.append(hsht["text"])
                if "media" in tweet.entities:
                    for image in tweet.entities["media"][0]:
                        line = {
                            "Category": f"{name}",
                            "url": url,
                            "Tweet_Text": txt,
                            "Trend_score": Trend_score,
                            "IMAGE_URL": tweet.entities["media"][0]["media_url"],
                            "hashtags_Tweet_Text": hash_list,
                        }

                    print("Image found!")
                else:
                    line = {
                        "Category": f"{name}",
                        "url": url,
                        "Tweet_Text": txt,
                        "Trend_score": Trend_score,
                        "IMAGE_URL": "null",
                        "hashtags_Tweet_Text": hash_list,
                    }

                try:
                    if "media" in tweet.entities:
                        for media in tweet.extended_entities["media"]:
                            line["video_img_url"] = media["media_url"]
                except:
                    pass
                line["id"] = id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break
            # searching for the product name in the tweet
            flag = False
            line["Brand"] = "null"
            try:
                for i in Electronics_Keywords:
                    if i in line["Tweet_Text"]:
                        flag = True
                        # Full_name = i.split(" ")
                        # line["main_category"] = name
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        print(i)
                        line = sd.get_flipkart_data(line)
                        break
                    elif i in hash_list:
                        # for j in line["hashtags_Tweet_Text"]:
                        flag = True
                        Full_name = i.split(" ")
                        # line["main_category"] = name
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        line = sd.get_flipkart_data(line)
                        print(i)
                        break
            except Exception as e:
                print(str(e))
            # checking if our tweet is valid or not
            try:
                if Trend_score >= 10 and flag == True:
                    Electronics_tweet.append(line)
                    # print("Tweet Accepted according to requirements")
                else:
                    print("Tweet rejected not according to requirements")
            except:
                Electronics_tweet.append(line)
            tweet_count += 1
        count = count + tweet_count
        print(count)
    print(f"Total Tweets Scraped:=> {count}")
    print(Electronics_tweet)
    if len(Electronics_tweet) == 0:
        return
    Electronics_tweet = sd.remove_duplicates(Electronics_tweet)
    new_Electronics_tweet = sd.sort_list(Electronics_tweet, "Trend_score")
    sd.write_json_file(new_Electronics_tweet, f"{name}")


def shoes(name="Shoes"):
    Shoes_List = [
        "paragonfootwear",
        "FluoShoes",
        "Batakenya",
        "RedTapeindia",
        "LakhaniFootwear",
        "metroshoes",
        "dvsshoes",
        "#shoes",
        "J23app",
    ]
    Shoes_tweet = []
    count = 0
    for shoes in Shoes_List:
        tweets_Shoes = tweepy.Cursor(
            api.search_tweets,
            shoes,
            tweet_mode="extended",
            lang="en",
            include_entities=True,
        ).items(number_of_tweets_to_extract)
        tweet_count = 0
        for tweet in tweets_Shoes:
            try:
                # information of tweet
                txt = tweet.full_text
                id = tweet.id
                screen_id_name = tweet.author._json["screen_name"]
                user = api.get_user(screen_name=screen_id_name)
                follower_count = user.followers_count
                url = "https://twitter.com/twitter/statuses/" + str(id)
                likes = tweet.favorite_count
                retweet_count = tweet.retweet_count
                Trend_score = likes + retweet_count + follower_count * 0.4
                hash_list = []
                if "hashtags" in tweet.entities:
                    hashtag = tweet.entities["hashtags"]
                    for hsht in hashtag:
                        hash_list.append(hsht["text"])
                if "media" in tweet.entities:
                    for image in tweet.entities["media"][0]:
                        line = {
                            "Category": f"{name}",
                            "url": url,
                            "Tweet_Text": txt,
                            "Trend_score": Trend_score,
                            "IMAGE_URL": tweet.entities["media"][0]["media_url"],
                            "hashtags_Tweet_Text": hash_list,
                        }

                    print("Image found!")
                else:
                    line = {
                        "Category": f"{name}",
                        "url": url,
                        "Tweet_Text": txt,
                        "Trend_score": Trend_score,
                        "IMAGE_URL": "null",
                        "hashtags_Tweet_Text": hash_list,
                    }

                # Access video info
                try:
                    if "media" in tweet.entities:
                        for media in tweet.extended_entities["media"]:
                            line["video_img_url"] = media["media_url"]
                except:
                    pass
                line["id"] = id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break
            flag = False
            line["Brand"] = "null"
            try:
                for i in Shoes_Keywords:
                    if i in line["Tweet_Text"]:
                        flag = True
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        print(i)
                        line = sd.get_flipkart_data(line)
                        break
                    elif i in hash_list:
                        flag = True
                        Full_name = i.split(" ")
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        line = sd.get_flipkart_data(line)
                        print(i)
                        break
            except Exception as e:
                print(str(e))
            # checking if our tweet is valid or not
            try:
                if Trend_score >= 10 and flag:
                    Shoes_tweet.append(line)
                else:
                    print("Tweet rejected not according to requirements")
            except:
                Shoes_tweet.append(line)
            tweet_count += 1
        count = count + tweet_count
        print(count)
    print(f"Total Tweets Scraped:=> {count}")
    print(Shoes_tweet)
    if len(Shoes_tweet) == 0:
        return
    Shoes_tweet = sd.remove_duplicates(Shoes_tweet)
    new_Shoes_tweet = sd.sort_list(Shoes_tweet, "Trend_score")
    sd.write_json_file(new_Shoes_tweet, f"{name}")


def fashion(name="Fashion"):
    Fashion_List = [
        "#fashion",
        "#handbags",
        "@refinery29",
        "#Sunglasses",
        "asimjofa",
        "Ezpopsy",
        "StingClothing",
        "casualclassics",
        "#jeans",
    ]
    Fashion_tweet = []
    count = 0
    for fashion in Fashion_List:
        tweets_fashion = tweepy.Cursor(
            api.search_tweets,
            fashion,
            tweet_mode="extended",
            lang="en",
            include_entities=True,
        ).items(number_of_tweets_to_extract)
        tweet_count = 0
        for tweet in tweets_fashion:
            try:
                # information of tweet
                txt = tweet.full_text
                id = tweet.id
                screen_id_name = tweet.author._json["screen_name"]
                user = api.get_user(screen_name=screen_id_name)
                follower_count = user.followers_count
                url = "https://twitter.com/twitter/statuses/" + str(id)
                likes = tweet.favorite_count
                retweet_count = tweet.retweet_count
                Trend_score = likes + retweet_count + follower_count * 0.4
                hash_list = []
                if "hashtags" in tweet.entities:
                    hashtag = tweet.entities["hashtags"]
                    for hsht in hashtag:
                        hash_list.append(hsht["text"])
                if "media" in tweet.entities:
                    for image in tweet.entities["media"][0]:
                        line = {
                            "Category": f"{name}",
                            "url": url,
                            "Tweet_Text": txt,
                            "Trend_score": Trend_score,
                            "IMAGE_URL": tweet.entities["media"][0]["media_url"],
                            "hashtags_Tweet_Text": hash_list,
                        }

                    print("Image found!")
                else:
                    line = {
                        "Category": f"{name}",
                        "url": url,
                        "Tweet_Text": txt,
                        "Trend_score": Trend_score,
                        "IMAGE_URL": "null",
                        "hashtags_Tweet_Text": hash_list,
                    }

                # Access video info
                try:
                    if "media" in tweet.entities:
                        for media in tweet.extended_entities["media"]:
                            line["video_img_url"] = media["media_url"]
                except:
                    pass
                line["id"] = id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break
            flag = False
            line["Brand"] = "null"
            try:
                for i in Fashion_Keywords:
                    if i in line["Tweet_Text"]:
                        flag = True
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        print(i)
                        line = sd.get_flipkart_data(line)
                        break
                    elif i in hash_list:
                        flag = True
                        Full_name = i.split(" ")
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        line = sd.get_flipkart_data(line)
                        print(i)
                        break
            except Exception as e:
                print(str(e))
            # checking if our tweet is valid or not
            try:
                if Trend_score >= 10 and flag == True:
                    Fashion_tweet.append(line)
                else:
                    print("Tweet rejected not according to requirements")
            except:
                Fashion_tweet.append(line)
            tweet_count += 1
        count = count + tweet_count
        print(count)
    print(f"Total Tweets Scraped:=> {count}")
    print(Fashion_tweet)
    if len(Fashion_tweet) == 0:
        return
    Fashion_tweet = sd.remove_duplicates(Fashion_tweet)
    new_Fashion_tweet = sd.sort_list(Fashion_tweet, "Trend_score")
    sd.write_json_file(new_Fashion_tweet, f"{name}")


def phones(name="Phones"):
    Phone_List = [
        "91mobiles",
        "techdroider",
        "techylogy",
        "#iphone",
        "#newphone",
        "#watchestobuy",
    ]
    Phone_tweet = []
    count = 0
    for phone in Phone_List:
        tweets_phones = tweepy.Cursor(
            api.search_tweets,
            phone,
            tweet_mode="extended",
            lang="en",
            include_entities=True,
        ).items(number_of_tweets_to_extract)
        tweet_count = 0
        for tweet in tweets_phones:
            try:
                # information of tweet
                txt = tweet.full_text
                id = tweet.id
                screen_id_name = tweet.author._json["screen_name"]
                user = api.get_user(screen_name=screen_id_name)
                follower_count = user.followers_count
                url = "https://twitter.com/twitter/statuses/" + str(id)
                likes = tweet.favorite_count
                retweet_count = tweet.retweet_count
                Trend_score = likes + retweet_count + follower_count * 0.4
                hash_list = []
                if "hashtags" in tweet.entities:
                    hashtag = tweet.entities["hashtags"]
                    for hsht in hashtag:
                        hash_list.append(hsht["text"])
                if "media" in tweet.entities:
                    for image in tweet.entities["media"][0]:
                        line = {
                            "Category": f"{name}",
                            "url": url,
                            "Tweet_Text": txt,
                            "Trend_score": Trend_score,
                            "IMAGE_URL": tweet.entities["media"][0]["media_url"],
                            "hashtags_Tweet_Text": hash_list,
                        }

                    print("Image found!")
                else:
                    line = {
                        "Category": f"{name}",
                        "url": url,
                        "Tweet_Text": txt,
                        "Trend_score": Trend_score,
                        "IMAGE_URL": "null",
                        "hashtags_Tweet_Text": hash_list,
                    }

                # Access video info
                try:
                    if "media" in tweet.entities:
                        for media in tweet.extended_entities["media"]:
                            line["video_img_url"] = media["media_url"]
                except:
                    pass
                line["id"] = id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break
            flag = False
            line["Brand"] = "null"
            try:
                for i in Phones_keywords:
                    if i in line["Tweet_Text"]:
                        flag = True
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        print(i)
                        line = sd.get_flipkart_data(line)
                        break
                    elif i in hash_list:
                        flag = True
                        Full_name = i.split(" ")
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        line = sd.get_flipkart_data(line)
                        print(i)
                        break
            except Exception as e:
                print(str(e))
            # checking if our tweet is valid or not
            try:
                if Trend_score >= 10 and flag:
                    Phone_tweet.append(line)
                else:
                    print("Tweet rejected not according to requirements")
            except:
                Phone_tweet.append(line)
            tweet_count += 1
        count = count + tweet_count
        print(count)
    print(f"Total Tweets Scraped:=> {count}")
    print(Phone_tweet)
    if len(Phone_tweet) == 0:
        return
    Phone_tweet = sd.remove_duplicates(Phone_tweet)
    updated_Phone_tweet = sd.sort_list(Phone_tweet, "Trend_score")
    sd.write_json_file(updated_Phone_tweet, f"{name}")


# electronics()
# shoes()
# fashion()
# phones()
