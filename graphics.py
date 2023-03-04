from abc import ABC, abstractmethod


class Graphics(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def _get_artist(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def get_artist(self):
        """returns not initialized artists. Run .update() before use and after adding to axis"""
        self.artist = self._get_artist()
        return self.artist
