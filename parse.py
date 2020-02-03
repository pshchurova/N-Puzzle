import sys

comment_charac = '#'

def check_validity(tab, dim):
    '''Function that goes through the parsed result and throws an error if it is of invalid dimension, contains any duplicate or any character out of valid range'''
    vert_dim = len(tab)
    hash_tab = {}
    if vert_dim < 2:
        raise Exception("Your tile should be at least 2x2")
    if vert_dim != dim:
        raise Exception("Invalid file, tile should be a square")
    for i in range(dim):
        for j in range(dim):
            if tab[i][j] >= dim * dim or tab[i][j] < 0:
                raise Exception("Character " + str(tab[i][j])+ " is out of range should be between 0 and " + str(dim * dim - 1) + ", position : (" + str(i + 1) + "," + str(j + 1) + ")")
            if tab[i][j] not in hash_tab:
                hash_tab[tab[i][j]] = 1
            else:
                raise Exception("Duplicate Character " + str(tab[i][j]) + " at position : (" + str(i + 1) + "," + str(j + 1) + ")")
    return tab

def parse_line(line):
    '''Function that transforms a lign into an array containing numbers, throws an arry if it encounters anything else than letters and whitespaces'''
    convert = []
    for each in line.split():
        try:
            splitted = each.split('#')
            if each[0] == comment_charac:
                break
            converted = int(splitted[0])
            convert.append(converted)
            if len(splitted) > 1:
                break
        except Exception as e:
            raise Exception(each + ' is not a valid number')
    if len(convert) == 0:
        return False
    return convert

def is_comment(line):
    '''Function that states if a given line is a commnent'''
    if (not line or not isinstance(line, str)):
        return False
    for each in line:
        if each in ' \t':
            pass
        elif each == comment_charac:
            return True
        else:
            return False
    return False
    
def checkEndFile(content, i):
    for line in content[i:]:
        if (is_comment(line)):
            continue
        else:
            try: 
                if (not parse_line(line)):
                    continue
            except:
                return False
        return False
    return True

def parse_file(file):
    '''Function that parses the file to check it and return a new tile instance based on its content'''
    try:
        fd = open(file)
        content = fd.read().split('\n')
        dim = None
    except Exception:
        raise Exception("File doesn't exist or isn't valid format")
    result = []
    for i, line in enumerate(content):
        if (is_comment(line)):
            pass
        else:
            convert = parse_line(line)
            if not convert:
                if (checkEndFile(content, i)):
                    break
                else:
                    raise Exception('Invalid puzzle format')
            elif dim is None:
                try: 
                    if len(convert) != 1:
                        raise(e)
                    dim = convert[0]
                    initDim = dim
                except Exception:
                    raise Exception('Dimension declaration isn\'t valid')
            elif dim != len(convert):
                raise Exception("Invalid file, wrong puzzle dimension")
            else:
                result.append(convert)
                dim = len(convert)
    result = check_validity(result, dim)
    return result