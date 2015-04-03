scripts:

- `names.py`: generates a list of 20 random magic item names, using the files `patterns.txt`, `concrete_noun.txt`, `title.txt`, `adjective.txt` and `abstract_noun.txt`.
- `flavor.py`: generates a single block of flavor for a magic item. Includes Creator/Intended User, Historic Details, Minor Properties and Quirks. Allows for rerolling. Relies on `creators.txt`, `historicdetails.txt`, `minorproperties.txt` and `quirks.txt`
- `main.py`: essentially a combination of names and flavors. Rolls one item at a time, allows rerolling of names and flavors.

todo:

- rewrite command structure. Instead of using numbered commands, try words (for instance "reroll name", "write-in history", "pick quirk", "remove properties")
- some mention of power of the magic item
- write-in the item's features. Do this in a quiz style, where the program asks "What does this item look like?", "After spending a short rest identifying this item, what does a character learn?", "After spending a short rest attuning to this item, how does the character's interaction with it change?"
- refactor to use an object class instead of a dictionary

discussion:

what's the purpose of this program? What are its use cases

- Mid-session: To quickly come up with a believable, random magic item on the fly
- Mid-session: To answer unexpected questions the player has about their new item
- Pre-session: To fine-tune a magic item for a specific character
- Post-session: To store items in a list, so that the DM can return to them later
- Post-session: To export the list of magic items in CSV format (in case DM wants to store his list elsewhere)