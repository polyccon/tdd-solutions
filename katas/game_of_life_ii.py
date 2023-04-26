from enum import Enum
from dataclasses import dataclass


class CellState(Enum):
    DEAD = 0
    ALIVE = 1


class Position:
    POSITION_DELTA = [-1, 1]

    def __init__(self, coordinates) -> None:
        (x, y) = coordinates
        self.x = x
        self.y = y

    def get_neighbour_positions(self):
        return (
            [Position((self.x + delta, self.y)) for delta in self.POSITION_DELTA]
            + [Position((self.x, self.y + delta)) for delta in self.POSITION_DELTA]
            + [
                Position((self.x + delta, self.y + delta))
                for delta in self.POSITION_DELTA
            ]
        )

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Cell:
    def __init__(self, cell_state, coordinates) -> None:
        self.cell_state = cell_state
        self.position = Position(coordinates)

    def get_neighbour_positions(self):
        return self.position.get_neighbour_positions()

    def __eq__(self, other):
        return self.cell_state == other.cell_state and self.position == other.position

    def evolve(self, number_of_neighbours):
        self.cell_state = (
            CellState.DEAD if number_of_neighbours < 2 else CellState.ALIVE
        )


class Board:
    def __init__(self, cells) -> None:
        self.cells = cells

    def get_cells(self):
        return self.cells

    def calculate_number_of_neighbours(self, current_cell):
        count = 0
        for cell in self.cells:
            if cell.position in current_cell.get_neighbour_positions():
                count += 1
        return count


class Game:
    def __init__(self, cells) -> None:
        self.board = Board(cells)

    def play(self):
        for cell in self.board.get_cells():
            number_of_neighbours = self.board.calculate_number_of_neighbours(cell)
            cell.evolve(number_of_neighbours)
