import search_helper as sh
import common_words as cw

def search_function(results, sorted_search):

    scores = []
    results_weighted = {}

    for result in results:
        result_words = sh.search_helper(result)

        score = 0

        for word in result_words:
            if word in sorted_search or word + "s" in sorted_search or word[0:len(word)-1] in sorted_search:
                if word not in cw.common_words:
                    score+=10
                
        scores.append(score)
            
    i = 0
    for score in scores:
        results_weighted[results[i]] = score
        i+=1
    
    return results_weighted