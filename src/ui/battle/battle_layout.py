from src.constants import *
from src.ui.button import Button

panel_w = SCALE * 600

battle_field = {
    'panel_w': panel_w,
    'panel_h': SCALE * 600,
    'coord': ((SCREENW - panel_w) / 2, SCALE*25)
}

bf_coord = battle_field['coord'][0], battle_field['coord'][1] + SCALE * 100
disp_w = Button.BUTTON_W + SCALE * 10
disposition_panel = {
    'panel_w': disp_w,
    'coord': (bf_coord[0]-disp_w, bf_coord[1]),
    'right': battle_field['panel_w']+disp_w
}


maneuver_panel = {
    'panel_w': disp_w,
    'coord': (bf_coord[0]-disp_w, bf_coord[1]),
    'right': battle_field['panel_w']+disp_w
}