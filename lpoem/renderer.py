from typing import List, Callable
from dataclasses import dataclass

@dataclass
class RenderState:
    indent_level:int = 0
    def indent_up(self):
        self.indent_level+=1

    def indent_down(self):
        self.indent_level-=1
        if self.indent_level < 0:
            self.indent_level = 0

    def clear_indent(self):
        self.indent_level = 0


# type RenderRule = Callable[[RenderState, str], str]

def line_break(r:RenderState, token:str) -> str:
    return "\n"

def stanza_break(r:RenderState, token:str) -> str:
    r.clear_indent()
    return "\n\n"

def indent_up(r:RenderState, token:str) -> str:
    r.indent_up()
    return "\n"

def indent_down(r:RenderState, token:str) -> str:
    r.indent_down()
    return "\n"

class Renderer:
    def __init__(self):
        self._state = RenderState()
        self._rules = {
            "*": line_break,
            "&": stanza_break,
            "[": indent_up,
            "]": indent_down
        }

    def render_generational_poem(self, poem:List[str]):
        return " ".join([self.render_poem(" ".join(p)) for p in poem])

    def render_poem(self, poem:List[str]):
        res = [""]
        for c in poem:
            if c in self._rules:
                replaced = self._rules[c](self._state, c)
                if replaced:
                    res.append(replaced)
                    if res[-1] == "\n":
                        res += "\t" * self._state.indent_level
                continue
            res.append(c)
        return " ".join(res)
            

    