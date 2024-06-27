import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def show_video_list(videos):
    print("\n"*3)
    print("*" * 70)
    if(len(videos) <= 0):
        print("There is no video in list")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["name"]} {video["time"]}" )
    print("*" * 70)
    print("\n"*3)

def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter video time : ")
    videos.append({"name" : name, "time" : time})
    save_data_helper(videos)
    print("Video Added Successfully")
    

def update_video(videos):
    show_video_list(videos)
    index = int(input("Enter a number which video you want to update : "))
    name = input("Enter video name : ")
    time = input("Enter video time : ")
    videos[index-1] = {"name" : name, "time": time}
    save_data_helper(videos)
    print("Video Updated Successfully")

def delete_video(videos):
    show_video_list(videos)
    index = int(input("Enter a video number which you want to delete : "))
    del videos[index-1]
    save_data_helper(videos)
    print("Video Deleted Successfully")

while True:
    videos = load_data()

    print("1. Show videos list ")
    print("2. Add video")
    print("3. Update Video")
    print("4. Delete Video")
    print("5. Exit ")

    choise = input("Choose an option to perform task : ")

    match choise:
        case '1':
            show_video_list(videos)
        case '2':
            add_video(videos)
        case '3':
            update_video(videos)
        case '4':
            delete_video(videos)
        case '5':
            break
        case _:
            print("You choose an invalid number")


        