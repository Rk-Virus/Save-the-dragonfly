class GameStats:
    def __init__(self):
        """Initialize statistics."""
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False
        self.score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.game_active = False