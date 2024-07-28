from argparse import ArgumentParser
from pathlib import Path

from .lsystem import *
from .parser import *
from .renderer import Renderer

ap = ArgumentParser(prog="LSystem Poetry Generator", 
    description="Generate poetry based on lsystems.")
ap.add_argument("-r", "--rules", type=str, 
    help="The rule file to use for this poem")
ap.add_argument("-d", "--depth", type=int, 
    help="The recursive depth to evaluate to", default=5)
ap.add_argument("-l","--last", action="store_true", 
    help="Output only the last generation. Default is to output all generations")
ap.add_argument("-nb", "--no-banner", action="store_true", 
    help="Suppress the generation banner. Default is to put a banner before each generation")
ap.add_argument("seed", type=str, help="The first generation of the poem- your axiom or seed")

args = ap.parse_args()

ex = Expander()
rend = Renderer()

with open(Path(args.rules)) as f:
    p = Parser(f, ex.add_rule)
    p.parse()

gens =  generate(args.seed, ex, args.depth)

if args.last:
    print(rend.render_poem(" ".join(gens[-1])))
else:
    for i,gen in enumerate(gens):
        if (not args.no_banner):
            print(f"--------{i}-------")
        print(rend.render_poem(" ".join(gen)))