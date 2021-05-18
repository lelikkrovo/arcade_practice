import arcade
import pathlib


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = " Arcade Platformer"

ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parert

class Platformer(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.coins = None
        self.background = None
        self.walls = None
        self.ladders = None
        self.goals = None
        self.enemies = None

        self.player = None

        self.physics_engine = None
        
        self.score = 0

        self.level = 1

        self.coin_sound = arcade.load_sound(
                str(ASSETS_PATH /"sounds" / "coin.wav")
        )
        self.jump_sound = arcade.load_sound(
                str(ASSETTS_PATH / "sounds" / "jump.wav")
        )
        self.victory_sound = arcade.load_sound(
                str(ASSETS_PATH / "sounds" / "victory.wav")
        )
