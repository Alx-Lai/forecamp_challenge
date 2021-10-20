class TeamAI():
    def __init__(self, api):
        self.api = api

    def decide(self):
        #methods
        #api.get_snake_pos() -> (int, int)
        #api.get_snake_len() -> int
        #api.get_snake_dir() -> str in ['left', 'right', 'up', 'down']
        #api.get_apple_pos() -> (int, int)

        #return:
        #str in ['left', 'right', 'up', 'down']

        boundary_x = (0,1000)
        boundary_y = (0,800)
        cell_size = 40
        a_pos = self.api.get_apple_pos()
        s_pos = self.api.get_snake_pos()
        direction = self.api.get_snake_dir()
        if s_pos[0] == 40 and direction == 'left':
            if s_pos[1] < a_pos[1]:
                return 'down'
            else:
                return 'up'
        if s_pos[0] == boundary_x[1] - cell_size and direction == 'right':
            if s_pos[1] < a_pos[1]:
                return 'down'
            else:
                return 'up'
        if s_pos[1] == 40 and direction == 'up':
            if s_pos[0] < a_pos[0]:
                return 'right'
            else:
                return 'left'
        if s_pos[1] == boundary_y[1] - cell_size and direction == 'down':
            if s_pos[0] < a_pos[0]:
                return 'right'
            else:
                return 'left'

        if s_pos[0] == a_pos[0] and (direction == 'left' or direction == 'right'):
            if s_pos[1] < a_pos[1]:
                return 'down'
            else:
                return 'up'
        if s_pos[1] == a_pos[1] and (direction == 'up' or direction == 'down'):
            if s_pos[0] < a_pos[0]:
                return 'right'
            else:
                return 'left'
        return direction
