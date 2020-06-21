class set():
    def __init__(self):
        self.width=1920
        self.height=1080
        self.size=40
        self.FPS = 60
        self.Fall_speed=4                       #고드름이 떨어지는 속도
        self.wall=None
        self.time_adjustment=60/self.FPS        #프레임 차이로 인한 속도를 조정하기위한 변수
        self.MAX_SPEED = 3*self.time_adjustment  # 공의 최대 속도

    def set_FPS(self,FPS):
        self.FPS=FPS
        self.time_adjustment=60/self.FPS
        self.MAX_SPEED=3*self.time_adjustment

setting=set()