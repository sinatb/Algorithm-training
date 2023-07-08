class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        k = 0
        visited = [id]
        queue = [(id,k)]
        watched_dict = {}
        while queue:
            s = queue.pop(0) 
            if (s[1] > k):
                k += 1
            if (s[1] == level):
                for c in watchedVideos[s[0]]:
                    if watched_dict.has_key(c):
                        watched_dict[c] += 1
                    else:
                        watched_dict[c] = 1
            elif (s[1] > level):
                break
            print (s) 
            for neighbour in friends[s[0]]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append((neighbour,k+1))
        
        sorted_watched_dict = sorted(watched_dict.items(), key=lambda x:(x[1],x[0]))

        print(sorted_watched_dict)
        return map(lambda x:x[0],sorted_watched_dict)
            