import requests


def fetchRandomUser():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    res = requests.get(url)
    print(res)
    data = res.json()
    # print(data)
    if(data["success"] and "data" in data):
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    
    else:
        raise Exception("Failed to fetch userdata")


def fetchRandomJokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    res = requests.get(url)
    data = res.json()
    result = data["data"]["data"]
    return result

def fetchKitchenSink(obj):
    # print(obj["Food"])
    # print(obj.items())
    # for key, val in obj.items():
    #     print(f"Key = {key} and Value = {val}")
    url = "https://api.freeapi.app/api/v1/kitchen-sink/cookies/set"
    res = requests.post(url, obj)
    data = res.json()
    return (data["data"]["cookies"])
    


def main():
    # try:
    #     username, country = fetchRandomUser()
    #     print(f"\nUsername = {username} and country = {country}\n")
    # except Exception as e:
    #     print(str(e))

    # try:
    #     data = fetchRandomJokes()
    #     print(data)
    #     for item in data:
    #         for singleItem in item["categories"]:
    #             print(f"\n\nCategory : {singleItem}, ")
    #         print(f"\n id : {item["id"]},\n Content : {item["content"]}")
    # except Exception as e:
    #     print(e)
    try:
        result = fetchKitchenSink({"Food": "Bread", "Food2" : "Roti"})
        for key, val in result.items():
            print(f"Key is : {key} and Value is : {val}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()