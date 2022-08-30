from unittest.util import sorted_list_difference
import search_helper as sh
import common_words as cw

def search_function(results, sorted_search):

    results_weighted = []


    for result in results:
        result_words = sh.search_helper(result)

        flag = True
        score = 0

        for word in result_words:
            if word in sorted_search or word + "s" in sorted_search or word[0:len(word)-1] in sorted_search:
                if word not in cw.common_words:
                    score+=10

        if score == 0 or results_weighted == []:
            results_weighted.append([result, score])
        else:
            i = 0
            results_copy = results_weighted.copy()
            for result2 in results_copy:
                if flag == True:
                    if score >= result2[1]:
                        results_weighted.insert(i, [result, score])
                        flag = False
                    else:
                        i+=1
        
    return results_weighted






