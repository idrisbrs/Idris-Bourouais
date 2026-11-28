from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile


class GameModel:

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car1: Car | None = None
        self.car2: Car | None = None

    def load_circuit(self) -> None:
        grid = [[RoadTile(col=col_idx, row=row_idx)
                for row_idx in range(GRID_COLS)] for col_idx in range(GRID_ROWS)]
        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        self.car1 = Car(7, 1, color=(255, 0, 0))    # Voiture 1 (Rouge)
        self.car2 = Car(8, 1, color=(0, 120, 255))  # Voiture 2 (Bleue

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car1.update_position()
        self.car2.update_position()
