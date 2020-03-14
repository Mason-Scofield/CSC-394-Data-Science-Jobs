import json

def countPay(data):
    res = {"<50,000": 0, "50,000-75,000": 0, "75,001-100,000": 0, ">100,000": 0}

    for d in data:
        num = float(d['Pay'])
        if num <= 50000:
            res["<50,000"] += 1
        elif 50000 < num <= 75000:
            res["50,000-75,000"] += 1
        elif 75001 <= num <= 100000:
             res["75,001-100,000"] += 1
        else:
             res[">100,000"] += 1
    return res


def countSkills(data):
    res = ""
    keywords = {'linux': 0, 'mac': 0, 'windows': 0,
                'machine learning': 0, 'artificial intelligence': 0, 'algorithms': 0,
                'analysis': 0, 'statistic': 0, 'computer science': 0, 'math': 0, 'deep learning': 0,
                'software development': 0, 'software engineering': 0, 'data engineering': 0,
                'neural networks': 0, 'communications': 0, 'creativity': 0, 'resilience': 0, '': 0}
    for d in data:
        for word in d['Skills']:
            keywords[word] += 1
    for key, value in sorted(keywords.items(), key=lambda item: item[1], reverse=True):
        if key != '':
            res += ("%s: %s" % (key, value) + "\n")
    return res


def countTechs(data):
    res = ""
    keywords = {'python': 0, 'sql': 0, 'spark': 0,
                'hadoop': 0, 'aws': 0, 'tensorflow': 0,
                'scala': 0, 'c++': 0, 'css': 0,
                'excel': 0, 'azure': 0, 'java': 0,
                'pytorch': 0, 'git': 0, 'c#': 0,
                'docker': 0, 'nosql': 0, 'javascript': 0,
                'html': 0, 'keras': 0, 'mongodb': 0, '': 0}
    for d in data:
        for word in d['Technology']:
            keywords[word] += 1
    for key, value in sorted(keywords.items(), key=lambda item: item[1], reverse=True):
        if key != '':
            res += ("%s: %s" % (key, value) + "\n")
    return res


def main():
    github = open("github_data.json")
    usa = open("usajob_data.json")
    github_data = json.load(github)
    usa_data = json.load(usa)
    job_type = github_data[0]['JobType']
    github.close()
    usa.close()

    outfile = open(job_type + ".txt", "w")
    outfile.write("Technologies for: " + job_type + "\n")
    outfile.write("USAJOBS DATA:\n" + countTechs(usa_data[0]))
    outfile.write("\nGITHUB DATA:\n" + countTechs(github_data))

    outfile.write("\n------------------------------------\n")
    outfile.write("\nSkills for: " + job_type + "\n")
    outfile.write("USAJOBS DATA:\n" + countSkills(usa_data[0]))
    outfile.write("\nGITHUB DATA:\n" + countSkills(github_data))

    outfile.close()
    outfile = open("pays.txt", "w")
    outfile.write(str(countPay(usa_data[0])))
    outfile.close()

if __name__ == '__main__':
    main()
