#Input words; get funny story maybe.
print "Welcome to MadLibs lil homie"
name = raw_input("What is your name?")
adj1 = raw_input("Give an adjective:")
adj2 = raw_input("Give another adjective:")
adj3 = raw_input("Give one more adjective:")
ver1 = raw_input("Give a verb:")
ver2 = raw_input("Give another verb:")
ver3 = raw_input("Give one last verb:")
nou1 = raw_input("Give a noun:")
nou2 = raw_input("Give another noun:")
nou3 = raw_input("Give a third noun:")
nou4 = raw_input("Last noun I promise:")
animal = raw_input("Name an animal:")
food = raw_input("Name a food:")
fruit = raw_input("Name a fruit:")
number = raw_input("Give us a number:")
superh = raw_input("Name a hero:")
country = raw_input("What country are you from?:")
dessert = raw_input("Your favorite dessert:")
year = raw_input("What year is it?:")

#The template for the story that doesn't want to work
STORY = "This morning I woke up and felt '{}' because '{}' was going to finally '{}' over the big '{}' '{}'. On the other side of the '{}' were many '{}' protesting to keep '{}' in stores. The crowd began to '{}' to the rhythm of the '{}', which made all of the '{}' very '{}'. '{}' tried to '{}' into the sewers and found '{}' rats. Needing help, '{}' quickly called '{}'. '{}' appeared and saved '{}' by flying to '{}' and dropping '{}' into a puddle of '{}'. '{}' then fell asleep and woke up in the year '{}', in a world where '{}' ruled the world.".format('adj1', 'adj2')

print STORY
# TODO: find out why this shit doesn't work
