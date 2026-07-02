# Calculations

[← Home](index.md)

## Mercenary Happiness

Happiness is a hidden statistic that is never displayed or mentioned in-game. It is only important for permanently recruiting mercenary units. All units begin with 0 Happiness.

| Event | Happiness Bonus |
| ----- | --------------- |
| Being Hired ¹ | +0.5 |
| Deploying on a Mission ² | +1.0 (main mission), +0.5 (sidequest) |
| Leveling Up via Capture ² | +0.1 |
| Reese's Promotion ³ | +0.2 |
| Eating Food (base) | +0.5 (Rank A), +0.4 (Rank B), +0.3 (Rank C), +0.2 (Rank D), +0.1 (Rank E) |
| Eating Food (modifier) | +0.2 (liked), -0.2 (disliked) |
| Bartered via Prisoner Exchange | +1.0 |
| Being Crippled via Combat ⁴ | +1.0 |

¹ Units are hired for half-price after the main mission for the chapter. Units are also hired for half-price for main missions upon being hired for the previous chapter without ever being deployed, UNLESS the Mercenary Warning was set to ON, and the unit was not hired during the hire screen upon progressing to the following chapter.

² Happiness gain via deployment and level up via capture only apply when the unit in question is hired. The corresponding gains do not occur for force-deployed mercenary units that are not hired.

³ Only applies to units whose Happiness is above 0 at that point.

⁴ The Happiness gain via being inflicted the Cripple status via combat occurs at the moment of being inflicted the Cripple status, and therefore may occur multiple times during a map if one has the means to cure the Cripple status. Faye and Saphira do not gain Happiness from being "crippled" post-mission due to reaching 0 HP and proceeding to be rescued by Faramir and Paramythis, respectively.

## Injury and Crippling

Units with the skill **Robust** or **Robust II** are immune to being injured and crippled.

| Property | Calculation |
| -------- | ----------- |
| Injury Rate (knives) | 9 + Weapon bonus + Skill bonus + Food bonus + enemy Food penalty |
| Injury Rate (non-knives) | 3 + Weapon bonus + Skill bonus + Food bonus + enemy Food penalty |
| Reference Value | (enemy HP at beginning of combat − enemy HP at end of combat) / (enemy HP at beginning of combat) |
| Cripple Rate (against unafflicted enemy units) | (Reference Value − 0.75) × Food bonus × Weapon bonus1 × 50% + Weapon bonus2 − enemy Food bonus |
| Cripple Rate (against unafflicted player units) | (Reference Value − 0.50) × Food bonus × Weapon bonus1 × 50% + Weapon bonus2 − enemy Food bonus |
| Cripple Rate (against injured units) | (Reference Value − 0.30) × Food bonus × Weapon bonus1 × 100% + Weapon bonus2 − enemy Food bonus |
| Cripple Rate (against units with Vulnerable, or when Maim is activated) | (Reference Value − 0.50) × Food bonus × Weapon bonus1 × 100% + Weapon bonus2 − enemy Food bonus |

## Accuracy

| Property | Calculation |
| -------- | ----------- |
| Accuracy | (weapon Precision × 10) + weapon Skill + Skill bonus + Support bonus + Food bonus |
| Shield Rate | (shield Precision × 10) + shield Skill + Skill bonus |
| Attack Speed | Speed − (weapon Weight + shield Weight − Strength/2, 0 if negative) |
| Avoid (physical, range 0~1) | (Attack Speed × 2) + Terrain bonus + Food bonus, 0 if negative |
| Avoid (magic, range 0~1) | (Attack Speed × 2) + Food bonus, 0 if negative |
| Avoid (range 2+) | (Attack Speed × 2) + (Terrain bonus × 2) + Food bonus, 0 if negative |
| Hit Rate | Accuracy − enemy Avoid |

### Skills Affecting Accuracy Non-Linearly

The "-Bane" skills (Swordbane, Spearbane, Axebane, Arrowbane, Magicbane) and Miracle affect hit rate by forcing re-evaluations of hit chances.

| Property | Calculation |
| -------- | ----------- |
| Effective Hit Rate (against "-Bane" skills) | 100 − [(100 − original Hit) + (original Hit/100) × maximum(67, 100 − original Hit)] |
| Effective Hit Rate (against Miracle skill) | 100 − [(100 − original Hit) + (original Hit/100) × (110 − original Hit)], 0 if negative |

## Critical Hits

| Property | Calculation |
| -------- | ----------- |
| Critical Damage | normal Damage + random(10~20) *(added damage pierces defenses)* |
| Critical Rate | weapon Critical + (weapon Skill − 50, 0 if negative) + Skill bonus + Support bonus + Food bonus |
| Critical Dodge | 0 + Food bonus |
| Battle Critical Rate | Critical Rate − enemy Critical Dodge |

## Equipment Durability

Applies only to weapons and shields with a durability class (a letter A–F or S), which break based on probability, rather than equipment with an exact number of uses.

All brand-new weapons start with 101 durability points, but some units begin with already-used equipment. If an item's durability counter ever falls below 1 without breaking, it is set to 1. If it would ever go above 101, it is set to 101.

### Durability Depletion

Each time a weapon hits an enemy or a shield blocks an attack, its durability points decrease by a fixed amount. (Missing with a weapon does not decrease durability.) The amount lost depends on the item's durability class.

The skill **Armsthrift** has a 20% chance to prevent weapon durability points from being depleted. Its activation is never announced to the player.

| Durability Class | Depletion per use (weapon) | Depletion per use (shield) |
| :--------------: | :------------------------: | :------------------------: |
| S | 1 | 4  |
| A | 2 | 8  |
| B | 3 | 12 |
| C | 4 | 16 |
| D | 5 | 20 |
| E | 6 | 24 |
| F | 7 | 28 |

### Durability Points and Break Chance

Each time an item's durability points decrease, it has a chance to break. The chance depends on the item's remaining durability points *before* the decrease. The colored indicator next to the weapon's icon on the status screen approximates remaining points, which also affect sell value (as a percentage of buy value when new).

| Durability Points | Display Color | Break Chance | Sell Value |
| :---------------: | :-----------: | :----------: | :--------: |
| 101    | Blue   | 0%   | 50% |
| 62-100 | Blue   | 0%   | 40% |
| 42-61  | Green  | 1%   | 30% |
| 22-41  | Yellow | 2%   | 20% |
| 2-21   | Orange | 4%   | 10% |
| ≤1     | Red    | 100% | 10% |

### Repairstones

Using a Repairstone on an item consumes as many uses as it takes to return the item to 101 durability points, or until the Repairstone runs out of uses.

| Property | Calculation |
| -------- | ----------- |
| Points restored *(per Repairstone use)* | 100 / (Item Cost When New / 1000, rounded up), rounded down |

| Full Cost | Points Repaired per Use |
| :-------: | :---------------------: |
| 1~1000     | 100 |
| 1001~2000  | 50  |
| 2001~3000  | 33  |
| 3001~4000  | 25  |
| 4001~5000  | 20  |
| 5001~6000  | 16  |
| 6001~7000  | 14  |
| 7001~8000  | 12  |
| 8001~9000  | 11  |
| 9001~10000 | 10  |
