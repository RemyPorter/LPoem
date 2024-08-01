from typing import Callable


class Parser:
    def __init__(self, file, rule_callback: Callable):
        self._f = file
        self._rc = rule_callback

    def parse(self):
        for line in self._f.readlines():
            line = line.strip()
            if "#" in line:
                line, _comment = line.split("#")
            if len(line) == 0:
                continue
            try:
                if "//" in line:
                    rule, prob = line.split("//")
                else:
                    rule = line.strip()
                    prob = 1

                if "::" in rule:
                    tok, sep = rule.split("::")
                    sep = sep.strip()
                    tok = tok.strip()

                seps = tuple(sep.split(" "))
                self._rc(tok.strip(), seps, float(prob))
            except:
                pass
