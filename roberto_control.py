from PIL import Image, ImageDraw

file_location = open('./location', 'r')
location = list(file_location.readlines()[0])
for i in range(len(location)):
    location[i] = int(location[i])
file_location.close()

base = Image.open('./assets/base.png')
base_draw = ImageDraw.Draw(base)


def draw_circle(image_draw: ImageDraw, center: tuple[int], radius: int = 25, fill: tuple[int] = (0, 0, 0)):
    '''draw_circle(image_draw=image_draw, center=[50, 50], radius=25, fill=(0, 0, 0)'''
    image_draw.ellipse(
        [
            center[0]-radius, center[1]-radius,  # X1, Y1
            center[0]+radius, center[1]+radius  # X2, Y2
        ],
        fill=fill
    )


def transport(image_draw: ImageDraw, offset: tuple[int]):
    '''transport(image_draw=image_draw, offset=[x, y])'''
    global location
    location[0] = 6 if location[0] == 7 and offset[0] > 0 else location[0]
    location[1] = 6 if location[1] == 7 and offset[1] > 0 else location[1]
    location[0] = 2 if location[0] == 1 and offset[0] < 0 else location[0]
    location[1] = 2 if location[1] == 1 and offset[1] < 0 else location[1]
    draw_circle(
        image_draw=image_draw,
        center=(100*location[0] - 50, 100*location[1] - 50),
        radius=26,
        fill=(255, 255, 255)
    )
    draw_circle(
        image_draw=image_draw,
        center=(
            100*location[0]-50+offset[0]*100,
            100*location[1]-50+offset[1]*100
        ),
        radius=25,
        fill=(0, 0, 0)
    )
    location = [location[0]+offset[0], location[1]+offset[1]]


def move_circle(direction: str):
    '''move_circle(direction='left')'''
    global base, base_draw
    if direction == 'down':
        transport(image_draw=base_draw, offset=[0, 1])

    elif direction == 'up':
        transport(image_draw=base_draw, offset=[0, -1])

    elif direction == 'right':
        transport(image_draw=base_draw, offset=[1, 0])

    elif direction == 'left':
        transport(image_draw=base_draw, offset=[-1, 0])

    base.save('table.png')
    file_location = open('./location', 'w')
    file_location.write(str(location[0])+str(location[1]))
    file_location.close()


draw_circle(
    image_draw=base_draw,
    center=(100*location[0]-50, 100*location[1]-50)
)

base.save('table.png')
