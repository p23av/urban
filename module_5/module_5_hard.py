from time import sleep

class UrTube:
    '''
    Класс видео хостинга
    '''
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return None
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if isinstance(video, Video):
                self.videos.append(video)

    def get_videos(self, search_word):
        list_ = []
        for video in self.videos:
            if search_word in video:
                list_.append(video.title)
        return list_

    def watch_video(self, video_name):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return None
        elif self.current_user < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return None
        for video in self.videos:
            if video_name in video:
                # print(video.time_now)
                for i in range(video.time_now, video.duration):
                    i += 1
                    print(i)
                    sleep(1)
                print('Конец видео')
                video.time_now = 0

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __contains__(self, item):
        return item.lower() in self.title.lower()

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __lt__(self, other):
        return self.age < other

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')