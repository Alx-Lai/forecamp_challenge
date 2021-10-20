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

        #print now score
        print(f'now score:{api.get_snake_len()}')

        if s_pos[0] == 40:
            return 'down'
        return direction
