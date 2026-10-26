from collections import Counter
from earg.canary import generate_scenes, violates, build_scene, Scene, Obj
import random


def test_count_and_exact_oracle():
    scenes=generate_scenes(20261026)
    assert len(scenes)==500
    assert Counter(s.case_kind for s in scenes)=={'positive':200,'hard_negative':200,'ordinary_negative':100}
    assert all(violates(s)==(s.case_kind=='positive') for s in scenes)


def test_seeded_scene_determinism():
    assert generate_scenes(42)==generate_scenes(42)
    assert generate_scenes(42)!=generate_scenes(43)


def test_relation_boundary():
    s=Obj('square','red',250,160,50)
    for cy,should in [(210,True),(271,False),(160,False)]:
        sc=Scene('x','test',(s,Obj('circle','blue',250,cy,50)))
        assert violates(sc) is should
    assert not violates(Scene('y','test',(s,Obj('circle','blue',300,210,50))))


def test_wrong_color():
    scene=Scene('x','test',(Obj('square','green',200,100,50),Obj('circle','blue',200,160,50)))
    assert not violates(scene)
