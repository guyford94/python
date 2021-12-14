TEMPLATE = "template.htm"
PLAYERS_FILE = "players.csv"


def insert_data(template, profile):
    """
    Replace every %%NAME%% with the matching value from the dictionary. Returns new string after replacments
    """

    new = template
    for key in profile:
        new = new.replace("%%" + key + "%%", profile[key])
    return new


def save_profile(data, name):
    """
    Saves HTML file with the data
    """
    newfile = open(name + ".html", "w", encoding='utf-8')
    newfile.write(data)
    newfile.close()


def build_profile_dict(lines, fields):
    """
    gets the config lines and returns a list of player dicts using firle names
    """
    all = []
    for line in lines[1:]:
        new_line = line.strip().split(",")
        new_line_dic = {}
        for i in range(0, len(fields)):
            new_line_dic[fields[i]] = new_line[i]
        all.append(new_line_dic)
    return all


def get_config_lines(filename):
    """
    Reads the given filename and returns list
    """
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines


def get_template_code(filename):
    """
    Reads the given filename and returns string
    """
    temp = open(filename, "r", encoding='utf-8')
    template = temp.read()
    temp.close()
    return template


### MAIN ####
def main():
    # read file as lines array
    lines = get_config_lines(PLAYERS_FILE)

    # for the fields names, get first line and split it
    fields = lines[0].strip().split(",")

    # from second line, check each line and build player profile dict
    all = build_profile_dict(lines[1:], fields)

    # Get template
    template = get_template_code(TEMPLATE)

    # for each player, replace fields, then save
    for profile in all:
        new_profile = insert_data(template, profile)
        save_profile(new_profile, profile["id"])


if __name__ == '__main__':
    main()
