def solution(word):
    words = []
    alp = "AEIOU"
    def dfs(cnt, w):
        if cnt == 5:
            return

        for i in range(len(alp)):
            words.append(w + alp[i])
            dfs(cnt + 1, w + alp[i])
    
    dfs(0,"")
    return words.index(word) + 1