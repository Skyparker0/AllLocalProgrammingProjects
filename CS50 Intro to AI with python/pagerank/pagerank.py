import os
import random
import re
import sys
import numpy as np

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probDict = {}
    
    if len(corpus[page]) == 0:
        for p in corpus.keys():
            probDict[p] = 1/len(corpus.keys())
    else:
        for p in corpus.keys():
            probDict[p] = (1-damping_factor)/len(corpus.keys())
        for clickedPage in corpus[page]:
            probDict[clickedPage] += damping_factor / len(corpus[page])
            
    return probDict
        


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pageVisits = {page:0 for page in corpus.keys()}
    
    currentPage = random.choice(list(corpus.keys()))
    
    for i in range(n):
        tModel = transition_model(corpus, currentPage, damping_factor)
        
        currentPage = random.choices(list(tModel.keys()), list(tModel.values()))[0]
        
        pageVisits[currentPage] += 1
        
    for page in pageVisits.keys():
        pageVisits[page] /= n
        
    return pageVisits


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    def pagerank(corpus, damping_factor, page, pageranks):
        total = 0
        total += (1-damping_factor)/len(pageranks)
        linksToPage = [p for p in corpus.keys() if page in corpus[p]]
        
        sumOfLinkTos = 0
        for linkTo in linksToPage:

            sumOfLinkTos += (pageranks[linkTo])/len(corpus[linkTo])
            
        total += sumOfLinkTos * damping_factor
        return total
        
    newpageranks = {page:1/len(corpus.keys()) for page in corpus.keys()}
    oldPageRanks = {page:100 for page in corpus.keys()}
    
    # for i in range(1):
    #     print(newpageranks, oldPageRanks)
        
    #     oldPageRanks = newpageranks.copy()
        
    #     for page in newpageranks:
    #         newpageranks[page] = pagerank(corpus,damping_factor, page, oldPageRanks)
            
    #     print(newpageranks, oldPageRanks)
    
    while sum((np.array(list(newpageranks.values())) - np.array(list(oldPageRanks.values())))**2) > 0.00001:
        oldPageRanks = newpageranks.copy()
        
        for page in newpageranks:
            newpageranks[page] = pagerank(corpus,damping_factor, page, oldPageRanks)
            
    return newpageranks


if __name__ == "__main__":
    main()
