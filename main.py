#Code Creator Tharyuu-desu

print("\033[0;37;118m-----------------------------------------------------------------------------------------")
print("Welcome to ARK ASSISTANT! For All your Statsy needs!")
print("Let Us Begin!!")
print("Please Provide the Creature details!")
print("\033[0;37;118m-----------------------------------------------------------------------------------------")

creature1 = input("\033[1;37;118mGive Creature:")
level1 = int(input("Give Wild Level:"))
gender1 = input("Give Gender (Female/Male):")
healt1 = float(input("Give Healt:"))
stamina1 = float(input("Give Stamina:"))
weight1 = float(input("Give Weight:"))
melee1 = float(input("Give Melee:"))
print(" ")
creature2 = input("Give Creature:")
level2 = int(input("Give Wild Level:"))
gender2 = input("Give Gender (Female/Male):")
healt2 = float(input("Give Healt:"))
stamina2 = float(input("Give Stamina:"))
weight2 = float(input("Give Weight:"))
melee2 = float(input("Give Melee:"))

print("\033[0;37;118m-----------------------------------------------------------------------------------------")

while healt1!=healt2 or stamina1!=stamina2 or weight1!=weight2 or melee1!=melee2:
    if gender1 == ("Female") and gender2 == ("Male"):
        print(f"\033[1;31;118mCreature:{creature1}")
        print(f"\033[1;31;118mLevel:{level1}")
        print(f"\033[1;31;118mGender:{gender1}")
        print(f"\033[1;31;118mHealt:{healt1}")
        print(f"\033[1;31;118mStamina:{stamina1}")
        print(f"\033[1;31;118mWeight:{weight1}")
        print(f"\033[1;31;118mMelee:{melee1}\n\n")
        print(f"\033[1;34;118mCreature:{creature2}")
        print(f"\033[1;34;118mLevel:{level2}")
        print(f"\033[1;34;118mGender:{gender2}")
        print(f"\033[1;34;118mHealt:{healt2}")
        print(f"\033[1;34;118mStamina:{stamina2}")
        print(f"\033[1;34;118mWeight:{weight2}")
        print(f"\033[1;34;118mMelee:{melee1}")

        print("\033[0;37;118m-----------------------------------------------------------------------------------------")

    if gender1 == ("Male") and gender2 == ("Female"):
        print(f"\033[1;34;118mCreature:{creature1}")
        print(f"\033[1;34;118mLevel:{level1}")
        print(f"\033[1;34;118mGender:{gender1}")
        print(f"\033[1;34;118mHealt:{healt1}")
        print(f"\033[1;34;118mStamina:{stamina1}")
        print(f"\033[1;34;118mWeight:{weight1}")
        print(f"\033[1;34;118mMelee:{melee1}\n\n")
        print(f"\033[1;31;118mCreature:{creature2}")
        print(f"\033[1;31;118mLevel:{level2}")
        print(f"\033[1;31;118mGender:{gender2}")
        print(f"\033[1;31;118mHealt:{healt2}")
        print(f"\033[1;31;118mStamina:{stamina2}")
        print(f"\033[1;31;118mWeight:{weight2}")
        print(f"\033[1;31;118mMelee:{weight2}")

        print("\033[0;37;118m-----------------------------------------------------------------------------------------")

    elif gender1 == ("Female") and gender2 == ("Female"):
        print(f"\033[1;31;118mCreature:{creature1}")
        print(f"\033[1;31;118mLevel:{level1}")
        print(f"\033[1;31;118mGender:{gender1}")
        print(f"\033[1;31;118mHealt:{healt1}")
        print(f"\033[1;31;118mStamina:{stamina1}")
        print(f"\033[1;31;118mWeight:{weight1}")
        print(f"\033[1;31;118mMelee:{melee1}\n\n")
        print(f"\033[1;33;118mCreature:{creature2}")
        print(f"\033[1;33;118mLevel:{level2}")
        print(f"\033[1;33;118mGender:{gender2}")
        print(f"\033[1;33;118mHealt:{healt2}")
        print(f"\033[1;33;118mStamina:{stamina2}")
        print(f"\033[1;33;118mWeight:{weight2}")
        print(f"\033[1;33;118mMelee:{melee2}")

        print("\033[0;37;118m-----------------------------------------------------------------------------------------")

    elif gender1 == ("Male") and gender2 == ("Male"):
        print(f"\033[1;34;118mCreature:{creature1}")
        print(f"\033[1;34;118mLevel:{level1}")
        print(f"\033[1;34;118mGender:{gender1}")
        print(f"\033[1;34;118mHealt:{healt1}")
        print(f"\033[1;34;118mStamina:{stamina1}")
        print(f"\033[1;34;118mWeight:{weight1}")
        print(f"\033[1;34;118mMelee:{melee1}\n\n")
        print(f"\033[1;32;118mCreature:{creature2}")
        print(f"\033[1;32;118mLevel:{level2}")
        print(f"\033[1;32;118mGender:{gender2}")
        print(f"\033[1;32;118mHealt:{healt2}")
        print(f"\033[1;32;118mStamina:{stamina2}")
        print(f"\033[1;32;118mWeight:{weight2}")
        print(f"\033[1;32;118mMelee:{weight2}")

        print("\033[0;37;118m-----------------------------------------------------------------------------------------")

    print("\033[1;37;118m0/0 BASE STATS")
    print(f"\033[1;37;118mCreature:{creature1}")
    if gender1==("Female") and gender2==("Male"):
        if healt1==healt2:
            print(f"\033[1;35;118mHealt:{healt1} DONE")
        elif healt1>healt2:
            print(f"\033[1;31;118mHealt:{healt1}")
        elif healt2 > healt1:
            print(f"\033[1;34;118mHealt:{healt2}")
        if stamina1==stamina2:
            print(f"\033[1;35;118mStamina:{stamina1} DONE")
        elif stamina1>stamina2:
            print(f"\033[1;31;118mStamina:{stamina1}")
        elif stamina2>stamina1:
            print(f"\033[1;34;118mStamina:{stamina2}")
        if weight1==weight2:
            print(f"\033[1;35;118mWeight:{weight1} DONE")
        elif weight1>weight2:
            print(f"\033[1;31;118mWeight:{weight1}")
        elif stamina2>stamina1:
            print(f"\033[1;34;118mWeight:{weight2}")
        if melee1==melee2:
            print(f"\033[1;35;118mMelee:{melee1} DONE")
        elif melee1>melee2:
            print(f"\033[1;31;118mMelee:{melee1}")
        elif melee2>melee1:
            print(f"\033[1;34;118mMelee:{melee2}")

        print("\033[0;37;118m-----------------------------------------------------------------------------------------")

    if gender1==("Male") and gender2==("Female"):
        if healt1==healt2:
            print(f"\033[1;35;118mHealt:{healt1} DONE")
        elif healt1>healt2:
            print(f"\033[1;34;118mHealt:{healt1}")
        elif healt2 > healt1:
            print(f"\033[1;31;118mHealt:{healt2}")
        if stamina1==stamina2:
            print(f"\033[1;35;118mStamina:{stamina1} DONE")
        elif stamina1>stamina2:
            print(f"\033[1;34;118mStamina:{stamina1}")
        elif stamina2>stamina1:
            print(f"\033[1;31;118mStamina:{stamina2}")
        if weight1==weight2:
            print(f"\033[1;35;118mWeight:{weight1} DONE")
        elif weight1>weight2:
            print(f"\033[1;34;118mWeight:{weight1}")
        elif weight2>weight1:
            print(f"\033[1;31;118mWeight:{weight2}")
        if melee1 == melee2:
            print(f"\033[1;35;118mMelee:{melee1} DONE")
        elif melee1 > melee2:
            print(f"\033[1;34;118mMelee:{melee1}")
        elif melee2 > melee1:
            print(f"\033[1;31;118mMelee:{melee2}")

        print("\033[0;37;118m-----------------------------------------------------------------------------------------")

    if gender1==("Female") and gender2==("Female"):
        if healt1==healt2:
            print(f"\033[1;35;118mHealt:{healt1} SAME")
        if healt1>healt2:
            print(f"\033[1;31;118mHealt:{healt1}")
        elif healt2 > healt1:
            print(f"\033[1;31;118mHealt:{healt2}")
        if stamina1 == stamina2:
            print(f"\033[1;35;118mStamina:{stamina1} SAME")
        if stamina1>stamina2:
            print(f"\033[1;31;118mStamina:{stamina1}")
        elif stamina2>stamina1:
            print(f"\033[1;31;118mStamina:{stamina2}")
        if weight1 == weight2:
            print(f"\033[1;35;118mWeight:{weight1} SAME")
        if weight1>weight2:
            print(f"\033[1;31;118mWeight:{weight1}")
        elif weight2>weight1:
            print(f"\033[1;31;118mWeight:{weight2}")
        if melee1 == melee2:
            print(f"\033[1;35;118mMelee:{melee1} SAME")
        if melee1 > melee2:
            print(f"\033[1;31;118mMelee:{melee1}")
        elif weight2 > weight1:
            print(f"\033[1;31;118mMelee:{melee2}")

        print("\033[0;37;118m-----------------------------------------------------------------------------------------")

    if gender1==("Male") and gender2==("Male"):
        if healt1==healt2:
            print(f"\033[1;35;118mHealt:{healt1} SAME")
        if healt1>healt2:
            print(f"\033[1;34;118mHealt:{healt1}")
        elif healt2 > healt1:
            print(f"\033[1;32;118mHealt:{healt2}")
        if stamina1 == stamina2:
            print(f"\033[1;35;118mStamina:{stamina1} SAME")
        if stamina1>stamina2:
            print(f"\033[1;34;118mStamina:{stamina1}")
        elif stamina2>stamina1:
            print(f"\033[1;32;118mStamina:{stamina2}")
        if weight1 == weight2:
            print(f"\033[1;35;118mWeight:{weight1} SAME")
        if weight1>weight2:
            print(f"\033[1;34;118mWeight:{weight1}")
        elif weight2>weight1:
            print(f"\033[1;32;118mWeight:{weight2}")
        if melee1 == melee2:
            print(f"\033[1;35;118mMelee:{melee1} SAME")
        if weight1>weight2:
            print(f"\033[1;34;118mMelee:{melee1}")
        elif weight2>weight1:
            print(f"\033[1;32;118mMelee:{melee2}")

        print("\033[0;37;118m-----------------------------------------------------------------------------------------")

    creature1 = input("\033[1;37;118mGive Creature:")
    level1 = int(input("\033[1;37;118mGive Wild Level:"))
    gender1 = input("\033[1;37;118mGive Gender (Female/Male):")
    healt1 = float(input("Give Healt:"))
    stamina1 = float(input("Give Stamina:"))
    weight1 = float(input("Give Weight:"))
    melee1 = float(input("Give Melee:"))
    print("")
    creature2 = input("Give Creature:")
    level2 = int(input("Give Wild Level:"))
    gender2 = input("Give Gender (Female/Male):")
    healt2 = float(input("Give Healt:"))
    stamina2 = float(input("Give Stamina:"))
    weight2 = float(input("Give Weight:"))
    melee1 = float(input("Give Melee:"))
    print("\033[0;37;118m-----------------------------------------------------------------------------------------")

print("\033[1;36;118mAll Stats DONE!")