# Dexelect Help

## Overview
Dexelect generates a Pokémon party for your selected game that respects the game's natural progression — every party member is obtainable at the point in the game you've reached.

## Modes

### Progression
Generates a party whose members are distributed across the game's progression spheres according to your config settings. Balance stats (Lean, Spread, Pattern) are shown after generating.

### Random
Generates a completely random party drawn from the full Pokédex for the selected game. Config balance settings are ignored in this mode.

## Stats

### Sphere
A broad chunk of game progression (e.g. Sphere 1 for Kanto spans Pallet Town to Cerulean City).

### Lean
The general bias of the party toward early or late game (early_game_heavy / balanced / late_game_heavy).

### Spread
How tightly grouped the party's acquisition spheres are (clustered / mixed_spread / wide_spread).

### Pattern
The qualitative shape of the party across spheres (single_cluster / dual_cluster / early_late_split / middle_only).

### Distribution
A breakdown of how many party members appear in each sphere.

## Configuration
Config files are located in the config/ directory (e.g. config_gen2.yaml for Gen 2 games). Use the Config tab to view and edit settings for the currently selected game. Changes take effect after clicking Save Config.
