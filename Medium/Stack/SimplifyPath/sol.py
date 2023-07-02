def simplify(path):
    cleanedPath = path.split('/')
    canonicalPath = []

    for directory in cleanedPath:
        print(len(canonicalPath))
        if len(directory)==0:
            continue #in case we had a double slash
        elif directory == '.':
            continue
        elif directory == ".." and len(canonicalPath)!=0:
            canonicalPath.pop()
        else:
            canonicalPath.append(directory)

    canonicalString="/"+('/'.join(canonicalPath))

    return canonicalString


simplify("/../")