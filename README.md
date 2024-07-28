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