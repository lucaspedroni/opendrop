from typing import Optional

from gi.repository import Gtk

from opendrop import observer

from opendrop.widgets.integer_entry import IntegerEntry

from ..base_config.view import ObserverConfigView


# TODO: if user tries to submit with a blank camera index input, show some kind of error/warning.
class USBCameraConfigView(ObserverConfigView):
    OBSERVER_TYPE = observer.types.USB_CAMERA

    def setup(self) -> None:
        grid = Gtk.Grid(column_spacing=10, row_spacing=10)
        self.container.pack_start(grid, expand=True, fill=True, padding=0)

        lbl = Gtk.Label('Camera Index:')
        grid.attach(lbl, 0, 0, 1, 1)

        index_input = IntegerEntry()
        grid.attach(index_input, 1, 0, 1, 1)

        index_input.connect('changed', self._on_camera_index_changed)

        self.index_input = index_input  # type: IntegerEntry

        grid.show_all()

    def _on_camera_index_changed(self, widget: IntegerEntry) -> None:
        new_value = int(widget.props.text) if widget.props.text else None  # type: Optional[int]
        self.events.on_camera_index_changed.fire(new_value)

    def set_camera_index(self, text: int) -> None:
        self.index_input.props.text = str(text)
