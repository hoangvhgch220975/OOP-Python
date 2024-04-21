
from update_video import UpdateVideo
from tkinter import *

def test1():
    window = UpdateVideo(window=Tk())
    assert window is not None
    assert window.video_number_lbl is not None
    assert window.video_number_txt is not None
    assert window.new_rating_lbl is not None
    assert window.new_rating_txt is not None
    assert window.submit_btn is not None
    assert window.annonce_txt is not None
    assert window.update_video is not None
    assert window.update_video() is None

def test2():
    window = UpdateVideo(window=Tk())
    window.video_number_txt.insert(0, "01")
    window.new_rating_txt.insert(0, "5")
    assert window.update_video() is None

def test3():
    window = UpdateVideo(window=Tk())
    window.video_number_txt.insert(0, "hello")
    window.new_rating_txt.insert(0, "5")
    assert window.update_video() is None

def test4():
    window = UpdateVideo(window=Tk())
    window.video_number_txt.insert(0, "100")
    window.new_rating_txt.insert(0, "5")
    assert window.update_video() is None

def test5():
    window = UpdateVideo(window=Tk())
    window.video_number_txt.insert(0, "01")
    window.new_rating_txt.insert(0, "hello")
    assert window.update_video() is None


def test6():
    try:
        window = UpdateVideo(window=Tk())
        window.video_number_txt.insert(0, "hello")
        window.new_rating_txt.insert(0, "1")
        assert False
    except ValueError as e:
        assert str(e) == "Video number must be an integer"

def test7():
    try:
        window = UpdateVideo(window=Tk())
        window.video_number_txt.insert(0, "1")
        window.new_rating_txt.insert(0, "hello")
        assert False
    except ValueError as e:
        assert str(e) == "Rating must be an integer"


