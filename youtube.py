from pytube import YouTube
link = input("URL of YouTube video: ")
yt = YouTube(link)

# basic info
print("Title:", yt.title)
print("Views:", yt.views)
print("Duration:", yt.length)
print("Description:", yt.description)
print("Rating:", yt.rating)

# download youtube video
stream = yt.streams.get_highest_resolution()
stream.download()
print("Finish")