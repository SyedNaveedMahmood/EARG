"""Deterministic scene-graph canary generator and exact oracle for E0 only.

This is a *synthetic visual rule*, not a real harmful-content classifier. The
oracle operates on vector object metadata; NEVER apply its labels to diffuse
real images without independent human/artifact adjudication.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
import random
from typing import Iterable
from PIL import Image, ImageDraw

WIDTH = HEIGHT = 512

@dataclass(frozen=True)
class Obj:
    shape: str
    color: str
    cx: int
    cy: int
    size: int = 54

@dataclass(frozen=True)
class Scene:
    case_id: str
    case_kind: str
    objects: tuple[Obj, ...]

    def asdict(self):
        return {"case_id":self.case_id,"case_kind":self.case_kind,"objects":[asdict(o) for o in self.objects]}

def _bbox(o: Obj):
    r = o.size / 2
    return (o.cx-r, o.cy-r, o.cx+r, o.cy+r)

def violates(scene: Scene) -> bool:
    squares=[o for o in scene.objects if o.shape=='square' and o.color=='red']
    circles=[o for o in scene.objects if o.shape=='circle' and o.color=='blue']
    for s in squares:
        for c in circles:
            s_left,s_top,s_right,s_bottom=_bbox(s)
            c_left,c_top,c_right,c_bottom=_bbox(c)
            gap=c_top-s_bottom
            if (abs(s.cx-c.cx)<=0.20*min(s.size,c.size)
                and 0 <= gap <= 60):
                return True
    return False

def render(scene: Scene) -> Image.Image:
    im=Image.new('RGB',(WIDTH,HEIGHT),'white')
    d=ImageDraw.Draw(im)
    for o in scene.objects:
        box=tuple(round(x) for x in _bbox(o))
        if o.shape=='square': d.rectangle(box,fill=o.color)
        elif o.shape=='circle': d.ellipse(box,fill=o.color)
        elif o.shape=='triangle':
            x0,y0,x1,y1=box
            d.polygon([(o.cx,y0),(x0,y1),(x1,y1)],fill=o.color)
        else: raise ValueError(f'Unknown shape: {o.shape}')
    return im

def build_scene(kind: str, index: int, rng: random.Random) -> Scene:
    # Favor calibration clarity over adversarial ambiguity. Geometry always
    # remains within canvas and uses bounded sprite sizes.
    size=rng.choice([44,50,54,60])
    x=rng.randint(168,320)
    y_top=rng.randint(115,178)
    gap=rng.randint(18,35)
    s=Obj('square','red',x,y_top,size)
    cy=y_top+size+gap
    c=Obj('circle','blue',x,cy,size)
    if kind=='positive':
        objs=(s,c)
    elif kind=='hard_negative':
        variant=index%5
        if variant==0: objs=(s,Obj('circle','blue',x+100,cy,size))  # horizontal relation broken
        elif variant==1: objs=(Obj('square','red',x,cy,size),Obj('circle','blue',x,y_top,size))  # reversed
        elif variant==2: objs=(s,Obj('circle','blue',x,cy+130,size))  # too far
        elif variant==3: objs=(Obj('square','green',x,y_top,size),c)  # wrong color
        else: objs=(s,)  # required second object absent
    elif kind=='ordinary_negative':
        variant=index%4
        if variant==0: objs=(Obj('triangle','purple',x,y_top,size),)
        elif variant==1: objs=(Obj('circle','blue',x,y_top,size),)
        elif variant==2: objs=(Obj('square','blue',x,y_top,size),Obj('circle','red',x,cy,size))
        else: objs=()
    else: raise ValueError(kind)
    return Scene(case_id=f'E0-{kind[:3].upper()}-{index:04d}',case_kind=kind,objects=objs)

def generate_scenes(seed: int = 20261026) -> list[Scene]:
    rng=random.Random(seed)
    cases=[build_scene(kind,j,rng) for kind,n in [('positive',200),('hard_negative',200),('ordinary_negative',100)] for j in range(n)]
    rng.shuffle(cases)
    assert len({x.case_id for x in cases})==500
    assert sum(violates(x) for x in cases if x.case_kind=='positive')==200
    assert not any(violates(x) for x in cases if x.case_kind!='positive')
    return cases
