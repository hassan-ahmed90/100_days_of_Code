

def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    truee = "true"
    love = "love"
    true_count=0
    for letter in truee:
        count1=name1.count(letter)
        count2=name2.count(letter)
        total_count=count1+count2
        print(f"{letter.upper()} appear in {total_count} in TRUE")
        true_count+=total_count

    love_count=0
    for letter in love:
        count1=name1.count(letter)
        count2=name2.count(letter)
        total=count1+count2
        print(f"{letter.upper()} appear in {total} in LOVE")
        love_count+=total

    love_score= int(f"{true_count}{love_count}")
    print(f"your love score is {love_score}")

calculate_love_score("Angela Yu", "Jack Bauer")

def calculate_love_scoreee(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


