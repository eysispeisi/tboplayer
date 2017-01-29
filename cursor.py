import Tkinter

import ctypes
from PIL import Image
from cStringIO import StringIO


class VC_RECT_T(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
        ('width', ctypes.c_int32),
        ('height', ctypes.c_int32),
        ]

class Cursor:
    lib_bcm = ctypes.CDLL('libbcm_host.so')
    cursor_raw = '''\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x1e\x00\x00\x00*\x08\x06\x00\x00\x01\xd3\xdc\xdb\x8f\x00\x00\x00\tpHYs\x00\x00\x0e\xc7\x00\x00\x0e\xc4\x01\x13\xbf|\xb5\x00\x00\x02\xf8IDATx\xda\xedX=l\x12a\x18~H\xa8\xc9\xe1`C\xc3\xd2k\xd4\x18X4\xad,\xbdKt\xe8-\x0e\xd5\xc5@\xe2\xd4A\x13p\xb0\x01q\xb0\x0c.\xb78\xc0\xd2\xa6$\x0eBb\x07\\4%:\x08C\x97\xebP\x13\xe8RAY \xb1\x9a\xe0\xd2\xe4\xacC\xb9\xc4\x0ex\xdf\xc7O\xcb\xff\xc7OK\xd4\xbe\xe4r\xb9{\xef\xbd\xe7\xfd\xfb\xde\xe7>\x8c%]pL\x8ch\x90\xf67\xe4g2\xe4\xe7\xf2\xb1\x1b\xfaE\xf5\t\xb1\xce\xa4\x01\xc5\xde\x15E\xa27\x94\r\x05\xd2-\xe9\xe8\x89\xea\x85.\xdf\x1bQ>7\xa24J3jK\xd0\xaah\xbf4p&\x0e\x18k\xe3&w\x81\x83\xfb\x81\x1b\xe1W\xe1\xf6\xd9:\xae$\x11ut\xb2\xa3\x83lJ\xff\x13?\x02\xcb\x81\xd6J\x93\xc5\x84\xe0J\x10K\xbe\xa5fe\xe9\xa0\x04\x8f\xcf\x03\xe7=\'\xd6\xdf\xac\xd7+\xd5\x03\x15\x91p\xa4\xa6\xa8S\xae\xae\xac\xd2s"\x9e\xc0\xfc\xed\xf9\xd6\xdeV\x15L\xa1\x88m\x95]j\x8cA\xea\x8f\xbe\xd3\xdfScU\x85T\xc2|\xde\x0c\x97\xdb\xd5;2\xe9N\xd7\xa2nx\x08x\x9fzk5`2.\xee\x17iE9\x83\xde\xc1\x0f\xdd\xc8d3\xf4\x05\xe1\x97\xe1\xee\xc6\xca\x96\x02\xe7\xae\x13\xb9l\x0e\xd2M\t\xb1\x0f\xb1&\xc3\xb6\xc6\xc9T\x92\x9e\x05\xbb@\xcf\x9eG\x9e\xa1g[\x19\xac\xce\x03t\x98ad\x1d\xf6\xcf\x18\'\xde\'`\xbbn\x83\xf5\xb2\xb5wc\xad\xa4A\xddS\x91\xd7\x7f\xdd^\xd0\xec\xb6\xbe\x92\x84Y\x01\xa9\x9d\x14\n?\n\xe0\'\xf9\x1e\x90\x0f\xb5\xf2\x0b\xae\t\xc8\xef\xe6\xa1\x15+\xe4\xc1\x8aL\x0c\x08\xd3\xf0<\x0f\xed\xb7n<V\xcf<\x1dc\xa6\x06(\x1b\x14\xbe\x15\x90\xfe\x99\x86$I\xec\xa5"\xcc\xed\xf5y\x91\xfb\x9a\x83\xe3\xae\x83\xbd\xcedj\x04\x82\x01\xc8\xb2\x0c\xd3\xb8\x89=a\xae\xfbGC\x8f\xb8J\xc8\xa5\xaf\x0e#\xc6\xadb\xfd\xdfW\x958\x8a\x01\xd8\xaf\xd8\xf5\xe3\x93\x11#\x923\xe0\xd3\x90+\xcc5&#\x9c\xccC\xfe\x12?\x0c\xe0\x8b\xcc\x11\x93O\x9b\xd8\xdb\x18\xddf\x90\x99\xc2BB\xc3I\xb5\xce\x003\xf6\x19:\x15S\xdb)\x84\xe2!8\xee8\x06\xca\x00\x130\xe1-J=\x87\xe5o2r\x90\xafA\xb2m!\x84`\x1e7\x9f\\s\x919C\x89\xb3"V\x9b\x95n*\x0b{\x05,,. \xfa:z2\xa9&\x11S\xce4T\x18z\xac\x9c\t\xde\xc2#\xba\x16\x85\xba\xaf\xc2\xbf\xe4\xa7\xcc\xc6\x92\x01\xb6TW\x88\x9a:\xa0\xff2\xb9\x0c\xac\xbc\x15f\x8b\x996\xdb\x94m\n\xdc9\x8e2\x7fd-R\xb7I\x1b|\x1d\xeb\xa0\xc9\xed$\x92[I\xba\xc1s?v\xd3\x08\x13\x1b\t\x88\xb3"\xd2_\xd2\xc3O\xb5(\x884\xd5\x13\x93\x13\xb5\xff\x06\xe2\xef\xe2t\xd7\x10z\x11\x82\xa2(\xb4\xeb\xd3;\xe9\xe1\x02O_\x9d\xa6G\xab\xf5\xbd\xf9q\x13jV\xed\tt(#s\xee\xc6\xdc_3\xab\x953Z<u`\xc3(\x80\xff\x00e\x8b1M\x13\x9f\xe8\x1e\x00\x00\x00\x00IEND\xaeB`\x82'''


    def __init__(self, x, y, width, height):
        ret = self.lib_bcm.bcm_host_init()
        assert( not ret )
        self.display = self.lib_bcm.vc_dispmanx_display_open(0)
        assert( self.display )
        self.win_x = x
        self.win_y = y
        self.win_width = width
        self.win_height = height
        self.layer = 10

        image_type = 18 # VC_IMAGE_RGBA16
        self.img_p, img_width, img_height = self._get_img()

        self.dst_rect = VC_RECT_T(x, y, img_width, img_height)
        self.src_rect = VC_RECT_T(x, y, width<<16, height<<16)

        self.resource = self.lib_bcm.vc_dispmanx_resource_create(image_type, img_width, img_height, self.img_p);
        assert(self.resource)
        assert(not self.lib_bcm.vc_dispmanx_resource_write_data(self.resource, image_type, 0, self.img_p, ctypes.byref(self.dst_rect)) )

        update_handle = self.lib_bcm.vc_dispmanx_update_start(0)
        assert( update_handle )
        self.element = self.lib_bcm.vc_dispmanx_element_add(update_handle, self.display, self.layer,
            ctypes.byref(self.dst_rect), self.resource, ctypes.byref(self.src_rect), ctypes.c_uint32(0), 0, 0, 0, 0)
        assert( self.element )
        assert( not self.lib_bcm.vc_dispmanx_update_submit_sync(update_handle) )

    def _get_img(self):
        img = Image.open(StringIO(self.cursor_raw))
        width, height = img.size
        img_bytes = img.tobytes()
        img_arr = (ctypes.c_int16*len(img_bytes))()
        img_p = ctypes.cast(img_arr, ctypes.POINTER(ctypes.c_int16))
        for i, v in enumerate(img_bytes):
            img_arr[i] = ord(v)
        return img_p, width, height

    def MoveWindow(self, x, y):
        self.dst_rect.x = x
        self.dst_rect.y = y
        self._update_element()

    def ResizeWindow(self, x, y, width, height):
        self.src_rect.x = x
        self.src_rect.y = y
        self.src_rect.width = width
        self.src_rect.height = height
        self._update_element()

    def _update_element(self):
        assert( self.element )
        dispman_update = self.lib_bcm.vc_dispmanx_update_start(0)
        assert( dispman_update )
        change_flag = 1<<2 | 1<<3
        assert( not self.lib_bcm.vc_dispmanx_element_change_attributes(dispman_update, self.display, change_flag, 0, 0,
                                                                 ctypes.byref(self.dst_rect), ctypes.byref(self.src_rect), 0, 0) )
        assert( not self.lib_bcm.vc_dispmanx_update_submit_sync(dispman_update) )


    def __del__(self):
        update_handle = self.lib_bcm.vc_dispmanx_update_start(0)
        assert( update_handle )
        assert( not self.lib_bcm.vc_dispmanx_element_remove(update_handle, self.element) )
        assert( not self.lib_bcm.vc_dispmanx_update_submit_sync(update_handle) )
        assert( not self.lib_bcm.vc_dispmanx_resource_delete(self.resource) )
        assert( not self.lib_bcm.vc_dispmanx_display_close(self.display) )

class Top:

    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.bind("<Motion>", self.onMotion)
        self.root.bind("<Configure>", self.onConfigure)
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

    def onConfigure(self, evt):
        if hasattr(self, 'bcm'):
            w = self.root.winfo_width()
            h = self.root.winfo_height()
            x = evt.x
            y = evt.y
            print 'geometry: %(w)dx%(h)d\nplacement: %(x)dx%(y)d\n' % locals()
            self.bcm.ResizeWindow(x, y, w, h)


    def MainLoop(self):
        self.root.mainloop()

if __name__ == '__main__':
    import time
    t = Top()
    t.MainLoop()
