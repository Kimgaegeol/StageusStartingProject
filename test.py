# import vlc
# import pafy
# import time

# url = "https://www.youtube.com/watch?v=COBqmxYaXks"
# video = pafy.new(url)
# best = video.getbest()
# media = vlc.MediaPlayer(best.url)
# media.play()
# time.sleep(10)


# class GlobalWealth(object):
#     def __init__(self):
#         self._global_wealth = 10.0
#         self._observers = []

#     def global_wealth(self):
#         return self._global_wealth

#     def global_wealth(self,value):
#         self._global_wealth = value
#         for callback in self._observers:
#             print('announcing change')
#             callback(self._global_wealth) #callback의 값을 self._global_wealth로 바꿈 

#     def bind_to(self, callback):
#         print('bound')
#         self._observers.append(callback)

# class Person(object):
#     def __init__(self, data):
#         self.wealth = 1.0
#         self.data = data
#         self.data.bind_to(self.update_now_happy)
#         self.happiness = self.data.global_wealth

#     def update_now_happy(self, global_wealth):
#         self.happiness = self.wealth / global_wealth
    
# if __name__ == '__main__':
#     data = GlobalWealth()
#     p = Person(data)
#     print(p.happiness)
#     data.global_wealth = 1.0
#     print(p.happiness)