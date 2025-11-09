import random

characters = ["a dragon", "a princess", "a robot", "an astronaut", "a wizard"]
places = ["in a castle", "on the moon", "under the sea", "in a forest", "at school"]
actions = ["found a secret door", "lost their shoes", "learned to dance", "built a time machine", "started singing loudly"]

character = random.choice(characters)
place = random.choice(places)
action = random.choice(actions)

story = f"One day, {character} {place} {action}."
print(story)

