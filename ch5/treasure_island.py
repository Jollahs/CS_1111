_scene_id = 0
move_limit = 4

# QUEST AND FAILURE DESCRIPTIONS
# Create a quest
quest_description = "Find the treasure. You have " + str(move_limit) + " days (moves)!"

# What happens if you run out of moves?
failure_description = "After " + str(move_limit) + " days, you die!"

# LISTS
# Create a list of scene descriptions
# This creates a list [None, None, None, None, None, None, None, None, None, None]
scene_descriptions_list = [None] * scene_count


# Create a list of the choices from each place
scene_choices_list = [None] * scene_count

# SCENES
# SCENE 0: the starting beach
scene_id = 0  # this variable helps to avoid magic numbers
scene_descriptions_list[scene_id] = "You are on the beach. You can:\n" \
                        "0. Explore the shipwreck.\n" \
                        "1. Go into the forest.\n" \
                        "2. Explore the rocks."


scene_choices_list[scene_id] = [4, 2, 3]
