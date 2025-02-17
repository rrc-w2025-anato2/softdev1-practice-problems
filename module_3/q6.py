"""Calculate batter's hitting percentage."""

num_of_hits = int(input("Enter the batter's hits: "))
num_of_athits = int(input("Enter the number of at-hits: "))

batters_hit_percentage = num_of_hits / num_of_athits

win_msg = "Player is eligible for a for the All Stars Game"
lose_msg = "Player is not eligible for the All Stars Game"

print(win_msg if batters_hit_percentage > 0.3 else lose_msg)