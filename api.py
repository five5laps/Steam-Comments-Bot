import requests
import random
import time

# Your comments array
messages = [
    "disgusting nurse", "slugging bot", "op nurse", "tunneler", "slugging",
    "toxic", "good looping", "nice movement", "bunnyhop script",
    "scripting", "cheater",
    "hvh god", "skeet user", "smurfing", "trash player", "garbage noob",
    "-rep try hard toxic have not touched grass in a decade lol", "-rep, urod",
    "i almost feel bad", 
    "- i almost feel bad", "それぞれの都合と自由のため", "君と防空壕で呼吸する",
    "息が詰まる息が詰まる息が詰まる息が詰まる", "プロミス", "humiliated hollow",
    "心障り", "aimware", "dead inside", "pandora",
    "ぼくらは コンプレックス コンプレックス コンプレックス",
    "お互い相手の本心を知らずに空回りしちゃってるの悲しい…",
    "dead inside 力伝toxic伝力 everlasting hate", "スタイリッシュなスーツ",
    "数の暴力に白旗をあげて 悪感情を殺してハイチーズ",
    "息が詰まる息が詰まる息が詰まる息が詰まる", "toggled", "hacker",
    "millionware", "fatality.win invite code 9502a1b6d6c8d6bf19ee26ac48c9968a0183a047",
    ".cc", "skeet", "gamesense.pub", "hns pro",
    "86800f9dcaf7624a023123879d2eb8a2ed4f37da",
    "生きたいが死ねと言われ 死にたいが生きろと言われ",
    "I love you それぞれの好きを守るため",
    "「この世には息もできない人が沢山いるんですよ」",
    "86e32f2610d501930890527486462a4955527142", "Lund",
    "リーダー", "throw down your tears 灯 ༒crying༒", "bad",
    "fatality.win (since 2018)", "movement", "727", "help",
    "gamesense.pub (since 2023)", "5429", "世界中のすべての人間に好かれるなんて気持ち悪いよ",
    "系をfearfulを系 igrushka otchima", "マϒdrainϒマ дед инсайд если че",
    "autostrafer", "bunnyhop", "sl1mer.5429", "x3n", "xentyui",
    "15k", "15k gamesense", "quit", "dead", "die", "fxck",
    "r4ve.cc invite code a5e93ce6b4b810f788735f2f9cdce26ff720a70d",
    "love was never an option", "skeet invite", "ev0lve (since 2019)",
    "ev0lve.xyz", "15447", "fxck bluepaste", "feeling the sense",
    "gamesense", "e5869ebf2bfe06536dd23b49583ce21364bd4569"
]

# Your steam profile id 
steam_profile_id = 76561198470738686

def select_random_message(messages):
    return random.choice(messages)

def send_api_request(profile_id, message,  session_id, steam_login_sequre):
    url = f"https://steamcommunity.com/comment/Profile/post/{profile_id}/-1/"
    data = {
        "comment": message, 
        "sessionid": session_id,
    }
    # This is ONLY necessary cookies
    cookies = {
        "sessionid": session_id,
        "steamLoginSecure": steam_login_sequre
    }
    # Request itself
    response = requests.post(url, data=data, cookies=cookies)
    json_data = response.json()
    # Checking response 
    if response.status_code == 200:
        if "name" in json_data:
            print(f"Comment successfully sent! -> {message} ")
        else:
            print("Error")
            print(json_data)
    else:
        print(f"Error: {response.status_code}")
        print(json_data)


main_account = {
    # Example :
    # "profile" : "76561198261286661",
    "profile" : "Your profile ID",
    # Example :
    # "session_id" : "35bf242cac659b5f6af6116b",
    "session_id" : "Your session ID",
    # Example : 
    # "steam_login_sequre" : "eyAidHlwIjogIkpXVCIsICJhbGciAiAiRWWEU1EiIH0.eyAiaXNzIjogInI6MDAwRl8yNUE3NUI5Ql81NUVCMyIsICJzdWIiOiAiNzY1NjExOTgyNjEyODY2NjEiLCAiYXVkIjogWyAid2ViOmNvbW11bml0eSIgXSwgImV4cCI6IDE3MzY5Nzg3NDYsICJuYmYiOiAxNzI4MjUxNzg3LCAiaWF0IjogMTczNjg5MTc4NywgImp0aSI6ICIwMDA5XzI1QTc1Qjk5XzU5MzAxIiwgIm9hdCI6IDE3MzY4OTE3ODYsICJydF9leHAiOiAxNzU1MDc4MTY4LCAicGVyIjogMCwgImlwX3N1YmplY3QiOiAiMTYzLjE3Mi4xMzcuMTIiLCAbaXBfY29uZmlybWVyIjogIjE2My4xNzIuMTM3LjEyIiB9.aSg1fkAKzfr0ytI1l86OEyP---LHWdNCpbQC2wovcN4aYq3PbgQGXdj4cQXbOpO_-RKZJQ4UC7mvfU_UrVuhDg"
    "steam_login_sequre" : "Your login sequre"
}

alt_account_1 = {
    "profile" : "Alt account profile ID",
    "session_id" : "Alt account session ID",
    "steam_login_sequre" : "Alt account login sequre" 
}

# Add up to infinite accounts
accounts = [
    main_account, alt_account_1, alt_account_2, alt_account_3
]
    


if __name__ == "__main__":
    while True:
        account = random.choice(accounts)
        print("Account chosen -> " + account["profile"])
        sequre = account["profile"] + "||" + account["steam_login_sequre"]
        send_api_request(steam_profile_id, select_random_message(messages), account["session_id"], sequre)
        time.sleep(2)
