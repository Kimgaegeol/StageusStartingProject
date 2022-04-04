import pafy 
import vlc
import youtube_dl
import time
import validators

# try:
#     instance = vlc.Instance()
#     mp = instance.media_player_new()
#     url = "https://www.youtube.com/watch?v=_8FXzLYAvxE"
#     video = pafy.new(url)
#     streams = video.streams
#     best = video.getbest()
#     mf = "videos/" + str(video.title) + ".mp4"
#     media = instance.media_new(mf)
#     media.get_mrl()
#     mp.set_media(media)
#     mp.play()
# except:
#     print(123)




# k = []
# k.append(3)
# print(k)

# table = "member"

# colum = ["k", "d","c"]
# value = ["j","a","b"]

# sql = "SELECT * FROM " + table + " WHERE "
# for index in range(0, len(colum)):
#     sql += colum[index] + "=" + "?"
#     if index >= 0 and index + 1 != len(colum):
#         sql += " and "
#     if index + 1 == len(colum):
#         sql += ";"
# print(sql)



# try:
#     url = "https://www.youtube.com/watch?v=_8FXzLYAvxE"

# playurl = best.url
# instance = vlc.Instance()
# player = play_song.play_song()
# media = instance.media_new(playurl)
# media.get_mrl()
# player.set_media(media)
# player.play()


# ur1l = "https://www.youtube.com/watch?v=Yg9VqAjE9VI"
# url1 = "aswefsdafds"

# if validators.url(url1):
#     print(1)
# else:
#     print(0)
# # # video = pafy.new(url)

# # if validators.url(url):
# #     print(1)
# # else: 
# #     print(0)

# # # if pafy.new(url):
# # #     print("1")
# # # else:
# # #     print("0")



# # # while True:
# # #     pass

colum = ["id" , "pw"]
value = ["id" , "pw"]

value[0] = "stageus1234@"
value[1] = "stageus1234@"

sql = "SELECT * FROM member WHERE "
for index in range(0, len(colum)):
    sql += colum[index] + "=" + value[index]
    if index >= 0 and index + 1 != len(colum):
        sql += " and "
    if index + 1 == len(colum):
        sql += ";"

print(sql)




