# LPoem - an LSystem Poetry Generator

This program generates poetry by recursively expanding rule files from an axiom (or seed). See [the wiki](https://en.wikipedia.org/w/index.php?title=L-system&useskin=vector) for an overview.

## Usage

This is a Python3 program with no external dependencies. Simply pull this repo, navigate to its root, and:

```
python3 -m lpoem --rules=examples/fish.txt --depth=5 --no-banner fish
```

Would output:

```
fish
algae
algae fish
algae fish algae
algae fish algae algae fish
algae fish algae algae fish algae fish algae
```

### Description
```
usage: LSystem Poetry Generator [-h] [-r RULES] [-d DEPTH] [-l] [-nb] seed

Generate poetry based on lsystems.

positional arguments:
  seed                  The first generation of the poem- your axiom or seed

options:
  -h, --help            show this help message and exit
  -r RULES, --rules RULES
                        The rule file to use for this poem
  -d DEPTH, --depth DEPTH
                        The recursive depth to evaluate to
  -l, --last            Output only the last generation. Default is to output all generations
  -nb, --no-banner      Suppress the generation banner. Default is to put a banner before each generation
```

## Rules
Rules must be stored in a rule file. These are the LSystem expansion rules, which support a simple replacement.

### Simple Rules
Simple rules are just a replacement rule, expressed like so:

```
token::replacement
```

When the input contains "token", the expander will replace it with "replacement". Replacements can be long strings, e.g.:

```
replacement::this has been replaced
```

So, for example, the algae poem, inspired by the first LSystem ever defined, has these rules:

```
algae::algae fish
fish::algae
```

When we encounter "algae", we expand to "algae fish. When we encounter "fish" we expand to "algae".

### Comments
A "#" comments out everything until the end of the line, e.g.,

```
rule::replacement # a comment on this line
```

### Special Glyphs
There are special glyphs you can include in your rules. These glyphs control how the poem gets *rendered*, and allow you to take some typographic control of the poem.

    * `*`: ends a line
    * `&`: ends a stanza
    * `[`: increases the indent
    * `]`: decreases the indent

### Probabilistic Rules
You may add rules which expand only with a certain probability. A probabilistic rule reads:

```
token::replacement//0.25
token::token token//0.25
token::most of the time we do this//0.5
```

When `token` is encountered, the appropriate rule will be chosen at random, weighted by the probabilities after the `//`.

## Writing Poetry
To write a poem, I recommend starting with your seed or axiom. Then expand each word in that using an LSystem rule, then expand each of those words. Effective LPoems need self-similarity, so you want rules that generate token sequences that create "loops" in your rule. The algae example above is a good example: the two rules create a repeating pattern.

You must also make a choice: does your LPoem expand with each generation, or do you only want the *last* generation. The way you write the poem is likely going to be different. I think the algae poem is *fun* in that it leverages the natural behavior of LSystems to structure the poem. But many more natural sounding poems are most interesting when we only output the last generation.

# Examples
See [poems](./poems/)

# danger
The LPoem "danger", by Remy Porter

```
 where moment of danger

 as a part of your time of growing
 along your time within your death

 as a part of flowing
 along where time as fertile soil

 as a part of dying
 moment of danger
 as changing

 growing a part changing the flooded banks changing the sun

 along dying
 lives
 dying
 a moment of danger

 as a part of your time of growing

 becoming a tributary unto changing dying
 the flooded banks along the sun
 along the lives along the my rising along the banks
 flowing a stream
```

Axiom: "danger down the line"
Rules:
```
danger::fertile soil//0.5
danger::your death//0.5
fertile::where you grow in
soil::heart of the sun *
grow::wither//0.5
grow::wander//0.5
death::time of growing
line::wake of the river
down::along
river::my life passing &
life::rising along the banks *
wither::lives
wander::death *
in::within the
within::* as a part of
part::tributary//0.5
part::portion//0.5
portion::part
tributary::you
you::death
growing::changing
time::moment of danger *
moment::time
wake::funeral
funeral::grow//0.5
funeral::wither//0.5
heart::flooded banks
passing::as a current
current::stream
changing::growing//0.333
changing::flowing//0.333
changing::dying *//0.333
of::as//0.333
of::unto//0.333
of::within//0.333
unto::down
as::becoming//0.15
as::changing//0.85
becoming::becoming part of
```

Command: `python3 -m lpoem -r poems/danger.txt -d 11 -l "danger down the line"`
