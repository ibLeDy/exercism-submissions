def find_anagrams(word, candidates):
    result = []
    
    for cand in candidates:
        if word.lower() == cand.lower():
            result.append(cand)

    if len(result) > 0:
        return []
    else:
        word_count = []
        
        for i in range(len(word.split())):
            word_count.append([str(j) for j in word.lower()])
        for j in range(0, len(word_count)):
            word_count[j].sort()

        letters = []
        for candidate in candidates:
            letters_temp = []
            
            for letter in candidate.lower():
                letters_temp.append(letter)
            letters.append((candidate, letters_temp))
            
            for i in range(len(letters)):
                letters[i][1].sort()

        for i in range(len(letters)):
            temp = []
            key = letters[i][0]

            for j in letters[i][1]:
                temp.append(j)

            if len(word_count) > 1:
                for w in range(0, len(word_count)):
                    if temp == word_count[w]:
                        result.append(key)
            else:
                if temp == word_count[0]:
                    result.append(key)

        return result