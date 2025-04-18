'''不同分辨率、缩放率适配，贴图坐标、圣遗物坐标、截图坐标定位'''
import win32gui

from PySide6.QtGui import QGuiApplication

app = QGuiApplication.instance()
SCALE = app.devicePixelRatio()

# 游戏窗口信息获取
window_sc = win32gui.FindWindow('UnityWndClass', '崩坏：星穹铁道')
window_start = win32gui.FindWindow('START Cloud Game', 'START云游戏-Game')
window = window_sc or window_start
left, top, right, bottom = win32gui.GetWindowRect(window)
# print('游戏窗口坐标：', left, top, right, bottom)

w_left = left
w_top = top
w_width = right - left - 3 * SCALE
w_hight = bottom - top - 26 * SCALE
print(f'窗口x,y,w,h{w_left, w_top, w_width, w_hight}')

if w_hight != 0:
    ratio = w_width / w_hight
else:
    ratio = 1

# 分辨率适配，A代表背包面板，B代表角色面板
# 16:10窗口模式
if ratio > 1.55 and ratio < 1.65:
    x_initial_A, y_initial_A, x_offset_A, y_offset_A = (
        300 / 2560 * w_width + w_left, (386 - 48) / 1600 * w_hight + SCALE * 24 + w_top, 195 / 2560 * w_width,
        234 / 1600 * w_hight)  # 第一个贴图坐标，y需要根据SCALE的标题栏高度做偏移
    x_left_A, x_right_A, y_top_A, y_bottom_A = (
        161 / 2560 * w_width + w_left, 326 / 2560 * w_width + w_left, (208 - 48) / 1600 * w_hight + SCALE * 24 + w_top,
        (412 - 48) / 1600 * w_hight + SCALE * 24 + w_top)  # 第一个圣遗物坐标
    # x_grab_A, y_grab_A, w_grab_A, h_grab_A = (1808 / 2560 * w_width + w_left, (677 - 48) / 1600 * w_hight + SCALE * 24 + w_top, 377 / 2560 * w_width, 214 / 1600 * w_hight) # 截图x, y, w, h，y需要根据SCALE的标题栏高度做适配
    x_grab_A, y_grab_A, w_grab_A, h_grab_A = (
        1776 / 2560 * w_width + w_left, (214 - 48) / 1600 * w_hight + SCALE * 24 + w_top, (602 - 50) / 2560 * w_width,
        677 / 1600 * w_hight)  # 截图x, y, w, h，y需要根据SCALE的标题栏高度做适配
    row_A, col_A = (6, 8)  # 圣遗物行列数

    x_initial_B, y_initial_B, x_offset_B, y_offset_B = (
        198 / 2560 * w_width + w_left, (397 - 48) / 1600 * w_hight + SCALE * 24 + w_top, 189 / 2560 * w_width,
        225 / 1600 * w_hight)
    x_left_B, x_right_B, y_top_B, y_bottom_B = (
        52 / 2560 * w_width + w_left, 220 / 2560 * w_width + w_left, (215 - 48) / 1600 * w_hight + SCALE * 24 + w_top,
        (419 - 48) / 1600 * w_hight + SCALE * 24 + w_top)
    x_grab_B, y_grab_B, w_grab_B, h_grab_B = (
        1951 / 2560 * w_width + w_left, (196 - 48) / 1600 * w_hight + SCALE * 24 + w_top, 551 / 2560 * w_width,
        504 / 1600 * w_hight)
    row_B, col_B = (6, 4)

# 16:9窗口模式
elif ratio > 1.7 and ratio < 1.8:
    x_initial_A, y_initial_A, x_offset_A, y_offset_A = (
        230 / 1920 * w_width + w_left,
        (360 - 43) / 1080 * w_hight + SCALE * 24 + w_top,
        124 / 1920 * w_width,
        147 / 1080 * w_hight)

    x_left_A, x_right_A, y_top_A, y_bottom_A = (
        131 / 1920 * w_width + w_left,
        252 / 1920 * w_width + w_left,
        (243 - 43) / 1080 * w_hight + SCALE * 24 + w_top,
        (386 - 43) / 1080 * w_hight + SCALE * 24 + w_top)

    x_grab_A, y_grab_A, w_grab_A, h_grab_A = (
        [1384 / 1920 * w_width + w_left, 1384 / 1920 * w_width + w_left],
        [(158 - 43) / 1080 * w_hight + SCALE * 24 + w_top, (422 - 43) / 1080 * w_hight + SCALE * 24 + w_top],
        [416 / 1920 * w_width, 481 / 1920 * w_width],
        [264 / 1080 * w_hight, 229 / 1080 * w_hight])
    row_A, col_A = (5, 9)

    x_initial_B, y_initial_B, x_offset_B, y_offset_B = (
        144 / 1920 * w_width + w_left,
        (360 - 43) / 1080 * w_hight + SCALE * 24 + w_top,
        124 / 1920 * w_width,
        147 / 1080 * w_hight)

    x_left_B, x_right_B, y_top_B, y_bottom_B = (
        47 / 1920 * w_width + w_left,
        166 / 1920 * w_width + w_left,
        (238 - 43) / 1080 * w_hight + SCALE * 24 + w_top,
        (385 - 43) / 1080 * w_hight + SCALE * 24 + w_top)

    x_grab_B, y_grab_B, w_grab_B, h_grab_B = (
        [1478 / 1920 * w_width + w_left, 1478 / 1920 * w_width + w_left],
        [(205 - 43) / 1080 * w_hight + SCALE * 24 + w_top, (333 - 43) / 1080 * w_hight + SCALE * 24 + w_top],
        [360 / 1920 * w_width, 424 / 1920 * w_width],
        [128 / 1080 * w_hight, 203 / 1080 * w_hight])
    row_B, col_B = (5, 4)

# 3:2窗口模式
elif ratio > 1.45 and ratio < 1.55:
    x_initial_A, y_initial_A, x_offset_A, y_offset_A = (
        254 / 2160 * w_width + w_left, (318 - 43) / 1440 * w_hight + SCALE * 24 + w_top, 165 / 2160 * w_width,
        197 / 1440 * w_hight)
    x_left_A, x_right_A, y_top_A, y_bottom_A = (
        136 / 2160 * w_width + w_left, 276 / 2160 * w_width + w_left, (173 - 43) / 1440 * w_hight + SCALE * 24 + w_top,
        (344 - 43) / 1440 * w_hight + SCALE * 24 + w_top)
    x_grab_A, y_grab_A, w_grab_A, h_grab_A = (
        1500 / 1920 * w_width + w_left, (175 - 43) / 1080 * w_hight + SCALE * 24 + w_top, (508 - 50) / 1920 * w_width,
        571 / 1080 * w_hight)
    row_A, col_A = (6, 8)

    x_initial_B, y_initial_B, x_offset_B, y_offset_B = (
        160 / 2160 * w_width + w_left, (326 - 43) / 1440 * w_hight + SCALE * 24 + w_top, 160 / 2160 * w_width,
        189 / 1440 * w_hight)
    x_left_B, x_right_B, y_top_B, y_bottom_B = (
        43 / 2160 * w_width + w_left, 186 / 2160 * w_width + w_left, (178 - 43) / 1440 * w_hight + SCALE * 24 + w_top,
        (350 - 43) / 1440 * w_hight + SCALE * 24 + w_top)
    x_grab_B, y_grab_B, w_grab_B, h_grab_B = (
        1649 / 1920 * w_width + w_left, (165 - 43) / 1080 * w_hight + SCALE * 24 + w_top, 461 / 1920 * w_width,
        421 / 1080 * w_hight)
    row_B, col_B = (6, 4)

else:
    print('请将游戏显示模式调至1920*1080窗口，然后重启软件')
    x_initial_A, y_initial_A, x_offset_A, y_offset_A = (
        300 / 2560 * w_width + w_left, (386 - 48) / 1600 * w_hight + SCALE * 24 + w_top, 195 / 2560 * w_width,
        234 / 1600 * w_hight)  # 第一个贴图坐标，y需要根据SCALE的标题栏高度做偏移
    x_left_A, x_right_A, y_top_A, y_bottom_A = (
        161 / 2560 * w_width + w_left, 326 / 2560 * w_width + w_left, (208 - 48) / 1600 * w_hight + SCALE * 24 + w_top,
        (412 - 48) / 1600 * w_hight + SCALE * 24 + w_top)  # 第一个圣遗物坐标
    x_grab_A, y_grab_A, w_grab_A, h_grab_A = (
        1808 / 2560 * w_width + w_left, (677 - 48) / 1600 * w_hight + SCALE * 24 + w_top, 377 / 2560 * w_width,
        214 / 1600 * w_hight)  # 截图x, y, w, h，y需要根据SCALE的标题栏高度做适配
    row_A, col_A = (6, 8)  # 圣遗物行列数

    x_initial_B, y_initial_B, x_offset_B, y_offset_B = (
        198 / 2560 * w_width + w_left, (397 - 48) / 1600 * w_hight + SCALE * 24 + w_top, 189 / 2560 * w_width,
        225 / 1600 * w_hight)
    x_left_B, x_right_B, y_top_B, y_bottom_B = (
        52 / 2560 * w_width + w_left, 220 / 2560 * w_width + w_left, (215 - 48) / 1600 * w_hight + SCALE * 24 + w_top,
        (419 - 48) / 1600 * w_hight + SCALE * 24 + w_top)
    x_grab_B, y_grab_B, w_grab_B, h_grab_B = (
        1983 / 2560 * w_width + w_left, (510 - 48) / 1600 * w_hight + SCALE * 24 + w_top, 334 / 2560 * w_width,
        190 / 1600 * w_hight)
    row_B, col_B = (6, 4)

# 贴图坐标组
position_A = []
for i in range(row_A):
    for j in range(col_A):
        position = x_initial_A + j * x_offset_A, y_initial_A + i * y_offset_A
        position_A.append(position)

position_B = []
for i in range(row_B):
    for j in range(col_B):
        position = x_initial_B + j * x_offset_B, y_initial_B + i * y_offset_B
        position_B.append(position)

# 鼠标事件有效坐标区间
xarray_A = []
for i in range(col_A):
    position = x_left_A + i * x_offset_A, x_right_A + i * x_offset_A
    xarray_A.append(position)

yarray_A = []
for i in range(row_A):
    position = y_top_A + i * y_offset_A, y_bottom_A + i * y_offset_A
    yarray_A.append(position)

xarray_B = []
for i in range(col_B):
    position = x_left_B + i * x_offset_B, x_right_B + i * x_offset_B
    xarray_B.append(position)

yarray_B = []
for i in range(row_B):
    position = y_top_B + i * y_offset_B, y_bottom_B + i * y_offset_B
    yarray_B.append(position)
