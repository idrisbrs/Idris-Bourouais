import pygame


MAPPING_P1 = {
    pygame.K_UP:     "accelerate", pygame.K_DOWN:     "reverse", pygame.K_b: "brake", pygame.K_LEFT: "turn_left",
    pygame.K_RIGHT:"turn_right",}
MAPPING_P2 = {
    pygame.K_z: "accelerate",pygame.K_s: "reverse",pygame.K_r: "brake",pygame.K_q: "turn_left", pygame.K_d: "turn_right",
}


class InputHandler:

    def __init__(self):
        self.mapping_p1 = MAPPING_P1
        self.mapping_p2 = MAPPING_P2

    def get_inputs(self,mapping: dict) -> dict:
        keys = pygame.key.get_pressed()
        p = {action: False for action in mapping.values()}

        for key, action in mapping.items():
            if keys[key]:
                p[action] = True

        return p
