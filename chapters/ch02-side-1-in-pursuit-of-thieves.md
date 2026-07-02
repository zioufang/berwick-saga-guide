# Map 2-1 — In Pursuit of Thieves

[← Home](../index.md)

## Map

![Map 2-1 — In Pursuit of Thieves](images/ch02-side-1-in-pursuit-of-thieves.png)

## Objective Checklist

- Defeat Gariad and seize the throne.
- Gariad is a bounty target — killing fulfills the bounty, capturing yields double rewards.
- Open the locked doors, cells, and chests with Czene (8 EXP per lock).
- Bottom treasure vault: left chest holds a Carwenhau (multi-hit dagger), right chest holds a Heal orb.
- Rescue the two horses locked in the pens (any unit can pick up a horse).

## Notes on the Map

This map probably takes the cake for being the easiest map in *Berwick Saga*. What you see is what you get. The enemies in this cave are loosely scattered throughout, and there are notably zero enemy reinforcements. The power level and general threat of this level is so low that it almost feels unfinished, in a way. This is a prime moment to train up some of our characters and improve their weapon ranks.

Before Turn 24 of any map, a unit simply needs to attempt to attack with their weapons to gain weapon EXP - a crucial stat that's needed to promote almost everyone in your cast. With the enemy pressure so low, it's worth considering intentionally taking along very shoddy weapons that have extremely poor hit rates and intentionally hitting enemies with the hopes of missing hits to rack up more weapon ranks. Whether or not you want to commit to grinds like this is up to you, but for units with very annoying promotion requirements (Adel / Leon / Elbert / Christine / Ruby, etc.), it might be worth doing until you get bored of it, at least.

This map features some locked doors, cells, and chests. Czene, being our playable thief and someone who's force deployed on this map, can open these for free, gaining 8 EXP for each lock she breaks open. The bottom treasure vault contains two treasures - the left chest holds a Carwenhau, a decently powerful multi-hit dagger that's a welcome addition to Czene's arsenal, and the right chest holds a Heal orb. At this point in the game, your Izerna is likely running on fumes with her starting Heal, so getting a second one here is very welcomed.

The two horses locked in the pens need to be rescued. Any unit - even units that normally cannot ride horses - are able to walk up to a horse and take it into their inventory. Note that horses cannot be put into bags (obviously...  right?), and one unit can only hold one horse in their inventory. While carrying the horse, the unit will suffer penalties to their Speed and Avoid stats. At the end of every map, Tianna will scan the inventories of all playable units and remove any horses in your inventories, adding them to the town stable, where they can be assigned to a rider. Give the horses to units that won't see a lot of combat to prevent the speed drop from potentially negatively affecting you.

Finally, there's just the boss - Gariad. He is on the bounty list! Killing him will fulfill the bounty, but capturing him yields double rewards. With the nonexistent time pressure on this map, it is a good chance for you to practice capture strats. And because I don't have a lot of other things to talk about, let's spend some time going over cripple mechanics and how they work:

Whenever any unit takes a large amount of damage in one combat, they have a chance to be crippled. This calculation looks at 2 values: The HP of the target *before* and *after* the combat. It then calculates a value which is just the percentage of health damage the target took in this combat ((Starting HP - Ending HP) / Starting HP), and subtracts it by one of three values:

- If the target is healthy: -0.75
- If the target is a player unit, OR if the target was maimed (Sylvis' skill), OR if the target has the "Weakness"* passive skill: -0.50
- If the target is injured: -0.3

\* (As far as I know, all enemies that have "Weakness" don't actually have that skill listed in their skills list, but they are there nonetheless, just invisible)

The game then factors in some other factors: Like any sources that would increase your crippling odds, be it from the Kingfisher Pavilion's food, your weapon, or anything else. As an example, if your target had 10 HP, and you dealt 9 damage to them in one combat, leaving them at 1 HP. Your target has therefore lost 90% of their HP, meaning the base cripple value is 0.9. Then, **assuming you have no other sources of crippling bonuses**:

- If the target is healthy: (0.9 - 0.75) = 0.15 --> 15% chance to cripple
- If the target is a player unit, OR if the target was maimed, OR if the target has the "Weakness" passive skill: (0.9 - 0.5) = 0.4 --> 40% chance to cripple
- If the target is injured: (0.9 - 0.3) = 0.6 --> 60% chance to cripple

There are two takeaways here:

1. Diabolically, player units are always a lot more likely to be crippled from taking a heavy hit than enemies.
2. If you want to cripple someone, **injuring them first** makes the cripple a lot more consistent to land.

I have previously mentioned that, not factoring in any additional bonuses from weapons or food, all non-dagger weaponry have a 3% chance of injuring an enemy when dealing damage, and daggers have a base injury rate of 9%. This is admittedly pretty rare with no other modifiers, but with combat happening so often, you would have likely stumbled upon it sooner rather than later. **You can also tell if the hit was an injury hit if the damage number appears in green instead of blue. Likewise - enemies that have injured you will show the damage number in yellow instead of red**.

Arthur's Flourish skill is a fantastic setup tool, not only does it halve his attack to not overly damage the target, but it also adds a 33% chance to injury, making his swords a 36% injury rate by default. There are also other very powerful injury tools you can get later - things like the Bolt Knife or the Blizzard Orb. You will also get more and more units with the Mercy skill to intentionally leave units at 1 HP. Capturing enemies get much easier and readily possible as you play more of the game!

For now, for just Gariad, have Arthur poke him with Flourish until you see the green number, or stab him with your Harpoon a few times as a backup. Czene can also noodle him for just shy of a 1-in-10 chance to land the injury. Note that Injury statuses **do** wear off after a few turns, but Cripples can never be naturally cured by either the players or the enemies. There are Cripple-curing light orbs and potions, but at this stage in the game, we don't really have those in good supply.

Once you have killed or captured Gariad, and have taken the horses, seize the throne to end this map.
