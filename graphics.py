from abc import ABC, abstractmethod


class Graphics(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def _get_artist(self):
        pass

    def plot(self, ax):
        self.artist = self._get_artist()
        try:
            ax.add_artist(self.artist)
        except Exception as ex:
            print(ex)

    def clear_artist(self):
        try:
            self.artist.remove()
        except Exception as ex:
            print("could not clear because of ", ex)


# class Graphics(ABC):

#     def __init__(self):
#         pass

#     @abstractmethod
#     def getArtistGraphics(self):
#         pass

#     def plot(self, ax):
#         self._g = self.getArtistGraphics()
#         try:
#             ax.add_artist(self._g)
#         except Exception as ex:
#             print("you still have to work... ", ex)

#     def clear(self):
#         print("clearing now")
#         try:
#             self._g.remove()
#         except Exception as ex:
#             print("could not clear because of ", ex)
