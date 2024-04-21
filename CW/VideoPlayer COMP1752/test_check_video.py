from check_videos import CheckVideos
from tkinter import *


def test_1():
    window = CheckVideos(window=Tk())
    assert window is not None
    assert window.list_txt is not None
    assert window.video_txt is not None
    assert window.status_lbl is not None
    assert window.input_txt is not None
    assert window.list_videos_clicked is not None
    assert window.check_video_clicked is not None
    assert window.list_videos_clicked() is None
    assert window.check_video_clicked() is None


def test_2():
    window = CheckVideos(window=Tk())
    window.input_txt.insert(0, "01")
    assert window.check_video_clicked() is None
    assert window.list_videos_clicked() is None
    
def test_3():
    window = CheckVideos(window=Tk())
    window.input_txt.insert(0, "hello")
    assert window.check_video_clicked() is None
    assert window.list_videos_clicked() is None

def test_4():
    windơw = CheckVideos(window=Tk())
    windơw.input_txt.insert(0, "100")
    assert windơw.check_video_clicked() is None
    assert windơw.list_videos_clicked() is None


def test_5():
    try:
        window = CheckVideos(window=Tk())
        window.input_txt.insert(0, "hello")
        assert False
    except ValueError as e:
        assert str(e) == "Video number must be an integer"