
from traits.api import HasTraits, Event, Int, Callable, provides

from .i_tile_manager import ITileManager


@provides(ITileManager)
class TileManager(HasTraits):
    """
    Base class for tile managers
    """

    min_level = Int(0)
    max_level = Int(17)

    tile_ready = Event

    process_raw = Callable

    def get_tile_size(self):
        """ Return size of tile
        """
        return 256

    def get_tile(self, zoom, row, col):
        """ Request a tile at row and col for a particular zoom level
        """
        raise Exception()

    def convert_to_tilenum(self, x, y, zoom):
        """ Convert screen space to a particular tile reference
        """
        raise Exception()
