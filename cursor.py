import ctypes
import Tkinter


class VC_RECT_T(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
        ('width', ctypes.c_int32),
        ('height', ctypes.c_int32),
        ]

class Cursor:
    lib_bcm = ctypes.CDLL('libbcm_host.so')

    def __init__(self, x, y, width, height):
        ret = self.lib_bcm.bcm_host_init()
        assert( not ret )
        self.display = self.lib_bcm.vc_dispmanx_display_open(0)
        assert( self.display )
        self.win_x = x
        self.win_y = y
        self.win_width = width
        self.win_height = height
        self.box_size = 20
        self.layer = 10

        dst_rect = VC_RECT_T(self.win_x, self.win_y, self.win_width+self.box_size, self.win_height+self.box_size)
        src_rect = VC_RECT_T(self.win_x, self.win_y, self.win_width<<16, self.win_height<<16)
        update_handle = self.lib_bcm.vc_dispmanx_update_start(0)
        assert( update_handle )
        assert( not self.lib_bcm.vc_dispmanx_update_submit_sync(update_handle) )
        self.element = self.lib_bcm.vc_dispmanx_element_add(update_handle, self.display, self.layer,
            ctypes.byref(dst_rect), 0, ctypes.byref(src_rect), ctypes.c_uint32(0), 0, 0, 0, 0)
        assert( self.element )

    def MoveWindow(self, x, y):
        self.win_x = x
        self.win_y = y
        self._update_element()

    def ResizeWindow(self, width, height):
        self.win_width = width
        self.win_height = height
        self._update_element()

    def _update_element(self):
        assert( self.element )
        dst_rect = VC_RECT_T(self.win_x, self.win_y, self.win_width+self.box_size, self.win_height+self.box_size)
        src_rect = VC_RECT_T(self.win_x, self.win_y, self.win_width<<16, self.win_height<<16)
        dispman_update = self.lib_bcm.vc_dispmanx_update_start(0)
        assert( dispman_update )
        change_flag = 1<<2 | 1<<3
        assert( not self.lib_bcm.vc_dispmanx_element_change_attributes(dispman_update, self.display, change_flag, 0, 0,
                                                                 ctypes.byref(dst_rect), ctypes.byref(src_rect), 0, 0) )
        assert( not self.lib_bcm.vc_dispmanx_update_submit_sync(dispman_update) )


    def __del__(self):
        update_handle = self.lib_bcm.vc_dispmanx_update_start(0)
        assert( update_handle )
        assert( not self.lib_bcm.vc_dispmanx_element_remove(update_handle, self.element) )
        assert( not self.lib_bcm.vc_dispmanx_update_submit_sync(update_handle) )
        assert( not self.lib_bcm.vc_dispmanx_display_close(self.display) )

class Top:

    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.bind("<Motion>", self.onMotion)
        self.root.update()
        x = self.root.winfo_x()
        y = self.root.winfo_y()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        print '%(width)dx%(height)d+%(x)d+%(y)d' % locals()
        self.bcm = Cursor(x, y, width, height)

    def onMotion(self, evt):
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        cx = evt.x
        cy = evt.y
        x = evt.x_root - cx
        y = evt.y_root - cy
        print 'geometry: %(w)dx%(h)d\nplacement: %(x)dx%(y)d\ncursor: %(cx)dx%(cy)d\n' % locals()
        self.bcm.MoveWindow(x, y)

    def MainLoop(self):
        self.root.mainloop()

if __name__ == '__main__':
    import time
    t = Top()
    t.MainLoop()
