from src.nation.powers import power_archive


class PowerManager(object):

    power_keys = power_archive.powers.keys()

    def __init__(self, state):

        self.state = state

        self.selection_table = {key: False for key in PowerManager.power_keys}
        self.power_buttons = None

        self.selected_power = None

    def set_power_buttons(self, pb):
        self.power_buttons = pb

    def select_power_button(self, power_key):

        if self.selection_table[power_key]:
            self.deselect_power(power_key)
        else:
            for key in PowerManager.power_keys:
                if self.selection_table[key]:
                    self.deselect_power(key)
            self.select_power(power_key)

    def deselect_power(self, key):
        self.selection_table[key] = False
        self.power_buttons[key].normal()
        if self.selected_power is not None:
            self.selected_power.free()
            self.state.cursor.unbind_power()
            self.selected_power = None

    def select_power(self, key):
        self.selection_table[key] = True
        self.selected_power = power_archive.powers[key]
        self.state.cursor.bind_power(self.selected_power)
        self.selected_power.bind(self.state)
        self.power_buttons[key].highlight()
