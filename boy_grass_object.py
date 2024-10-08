import random

from pico2d import *

# Game object class here
class Grass:
    # 생성자 만들기
    def __init__(self):
        # self는 모양 없는 납작한 붕어빵
        # 이제 이걸 모양을 잡아줌
        self.image = load_image("grass.png")
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image("run_animation.png")
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0 , 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global world
    world = []
    running = True
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(11)]
    world += team


def update_world():
    for obj in world:
        obj.update()

def render_world():
    clear_canvas()
    for obj in world:
        obj.draw()
    update_canvas()




open_canvas()
running = True

# initialization code
reset_world() # 초기화


# game main loop code

while running:
    handle_events()
    update_world() # 상호작용을 시뮬레이션
    render_world() # 그결과를 보여줌
    delay(0.05)


# finalization code
close_canvas()



