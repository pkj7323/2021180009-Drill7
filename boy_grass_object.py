from pico2d import *

# Game object class here

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
    running = True


def update_world():
    pass


def render_world():
    clear_canvas()
    update_world()

open_canvas()
running = True
# initialization code
reset_world() # 초기화


# game main loop code

while running:
    handle_events()
    update_world() #상호작용을 시뮬레이션
    render_world() # 그결과를 보여줌
    delay(0.05)


# finalization code
close_canvas()



