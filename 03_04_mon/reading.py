with open('recipe.txt', 'r') as fin:
    recipe = fin.readlines()

print(recipe)
# clean_recipe = []
# for line in recipe:
#     line = line.rstrip()
#     clean_recipe.append(line)
#
# print(clean_recipe)


# buff up the recipe for family time!
# don't worry about this part yet!
family_recipe = ["10" + line[1:] for line in recipe]
print(family_recipe)

with open('family_recipe.txt', 'w') as fout:
    for line in family_recipe:
        fout.write(line)
