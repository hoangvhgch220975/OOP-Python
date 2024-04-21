
from create_video_list import CreateVideoList
from tkinter import *

def test1():
    window = CreateVideoList(window=Tk())
    assert window is not None
    assert window.list_videos_btn is not None
    assert window.enter_lbl is not None
    assert window.input_number is not None
    assert window.listvideo is not None
    assert window.playlist is not None
    assert window.detail_btn is not None
    assert window.detail_txt is not None
    assert window.add_video_btn is not None
    assert window.play_btn is not None
    assert window.reset_btn is not None
    assert window.status_lbl is not None
    assert window.list_videos_clicked() is None
    assert window.detail_clicked() is None
    assert window.add_video_clicked() is None
    assert window.play_playlist() is None
    assert window.reset_list_clicked() is None

def test2():
    window = CreateVideoList(window=Tk())
    window.input_number.insert(0, "01")
    assert window.detail_clicked() is None
    assert window.add_video_clicked() is None
    assert window.play_playlist() is None
    assert window.reset_list_clicked() is None

def test3():
    window = CreateVideoList(window=Tk())
    window.input_number.insert(0, "hello")
    assert window.detail_clicked() is None
    assert window.add_video_clicked() is None
    assert window.play_playlist() is None
    assert window.reset_list_clicked() is None

def test4():
    window = CreateVideoList(window=Tk())
    window.input_number.insert(0, "100")
    assert window.detail_clicked() is None
    assert window.add_video_clicked() is None
    assert window.play_playlist() is None
    assert window.reset_list_clicked() is None

def test5():
    try: 
        window = CreateVideoList(window=Tk())
        window.input_number.insert(0, "hello")
        assert False
    except ValueError as e:
        assert str(e) == "Video number must be an integer"