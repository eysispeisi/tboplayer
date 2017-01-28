#include <assert.h>

#include "bcm_host.h"

#define DISPMANX_ELEMENT_CHANGE_FLAG_DEST_RECT 1<<2
#define DISPMANX_ELEMENT_CHANGE_FLAG_SRC_RECT 1<<3

class Cursor {
public:
    Cursor(uint32_t win_x, uint32_t win_y, uint32_t win_width, uint32_t win_height);
    void DrawCursor(uint32_t x, uint32_t y);
    void MoveWindow(uint32_t win_x, uint32_t win_y, uint32_t win_width, uint32_t win_height);
private:
    void init_display();
    void update_win_pos();
    void update_cursor();
    DISPMANX_ELEMENT_HANDLE_T dispman_element_;
    DISPMANX_DISPLAY_HANDLE_T dispman_display_;
    uint32_t win_x_;
    uint32_t win_y_;
    uint32_t win_width_;
    uint32_t win_height_;
    uint32_t cursor_x_;
    uint32_t cursor_y_;
    uint32_t box_size_ = 10;
    int32_t layer_ = 10;    
};

Cursor::Cursor(uint32_t win_x, uint32_t win_y, uint32_t win_width, uint32_t win_height) :
win_x_(win_x),
win_y_(win_y),
win_width_(win_width),
win_height_(win_height)
{
    init_display();
};

void Cursor::MoveWindow(uint32_t win_x, uint32_t win_y, uint32_t win_width, uint32_t win_height) {
    win_x_ = win_x;
    win_y_ = win_y;
    win_width_ = win_width;
    win_height_ = win_height;
    update_win_pos();
};

void Cursor::DrawCursor(uint32_t x, uint32_t y) {
    cursor_x_ = x;
    cursor_y_ = y;
    update_cursor();
};

void Cursor::update_cursor() {
    assert(dispman_element_);
    VC_RECT_T src_rect;
    vc_dispmanx_rect_set(&src_rect, cursor_x_, cursor_y_, (cursor_x_+box_size_)<<16, (cursor_y_+box_size_)<<16);
    DISPMANX_UPDATE_HANDLE_T dispman_update;
    dispman_update = vc_dispmanx_update_start(0);
    assert(dispman_update);
    uint32_t change_flag = DISPMANX_ELEMENT_CHANGE_FLAG_DEST_RECT;
    vc_dispmanx_element_change_attributes(dispman_update, dispman_element_, change_flag, 0, 0,
                                                   0, &src_rect, 0, (DISPMANX_TRANSFORM_T) 0);
    assert(!vc_dispmanx_update_submit_sync(dispman_update));
};

void Cursor::update_win_pos() {
    // resize dispmanx element
    assert(dispman_element_);
    VC_RECT_T src_rect;
    vc_dispmanx_rect_set(&src_rect, win_x_, win_y_, win_width_<<16, win_height_<<16);
    DISPMANX_UPDATE_HANDLE_T dispman_update;
    dispman_update = vc_dispmanx_update_start(0);
    assert(dispman_update);
    uint32_t change_flag = DISPMANX_ELEMENT_CHANGE_FLAG_SRC_RECT;
    vc_dispmanx_element_change_attributes(dispman_update, dispman_element_, change_flag, 0, 0,
                                                   0, &src_rect, 0, (DISPMANX_TRANSFORM_T) 0);
    assert(!vc_dispmanx_update_submit_sync(dispman_update));
};

void Cursor::init_display() {
    VC_RECT_T dst_rect;
    dst_rect.x = win_x_;
    dst_rect.y = win_y_;
    dst_rect.width = win_x_+box_size_;
    dst_rect.height = win_y_+box_size_;

    VC_RECT_T src_rect;
    src_rect.x = win_x_;
    src_rect.y = win_y_;
    src_rect.width = win_width_ << 16;
    src_rect.height = win_height_ << 16;        

    dispman_display_ = vc_dispmanx_display_open(0);
    assert(dispman_display_);

    auto dispman_update = vc_dispmanx_update_start(0);
    assert(dispman_update);
    assert(!vc_dispmanx_update_submit_sync(dispman_update));

    dispman_element_ =
            vc_dispmanx_element_add(dispman_update,
                                dispman_display_,
                                layer_,
                                &dst_rect,
                                0 /*src*/,
                                &src_rect,
                                DISPMANX_PROTECTION_NONE,
                                0 /*alpha*/,
                                0 /*clamp*/,
                                DISPMANX_STEREOSCOPIC_MONO);
    assert(dispman_element_);
};
