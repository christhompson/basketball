import basketball

adventureSets = {"sci-fi": "sci-fi_filler.txt", "adventure": "adventure_filler.txt"}
colorSets = {"sci-fi": "green", "adventure": "cyan"}

def chooseAdventure(templateFile, adventureSet, colorSet):
	choice = ""
	while (not (choice in adventureSets)):
		print "Which adventure would you like? (pick one from below)"
		for key in iter(adventureSets):
			print key
		choice = raw_input(">").strip()
	basketball.main(colorSet[choice], False, adventureSet[choice], templateFile)

if __name__ == "__main__":
	chooseAdventure("script_template.txt", adventureSets, colorSets)
