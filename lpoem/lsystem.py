from dataclasses import dataclass
from random import choices
from typing import Dict, List, Tuple
from collections import defaultdict

@dataclass
class Rule:
    replacement: Tuple[str]
    probability: float

class Ruleset:
    def __init__(self):
        self._options:List[Rule] = []

    def add_option(self, token, probability):
        self._options.append(Rule(token, probability))

    def rule(self):
        return choices(self._options, \
            [r.probability for r in self._options])[0].replacement


class Expander:
    def __init__(self):
        self._rules:Dict[str,Ruleset] = defaultdict(Ruleset)

    def add_rule(self, token, replacement, probability=1):
        self._rules[token].add_option(replacement, probability)

    def expand_token(self, token):
        if token in self._rules:
            return self._rules[token].rule()
        return (token,)

def generate(seed, ex:Expander, depth=5):
    generations = [[seed]]
    poem = seed.split(" ")
    for _ in range(depth):
        generation = []
        for token in poem:
            generation += list(ex.expand_token(token))
        generations.append(generation)
        poem = generation
    return generations
