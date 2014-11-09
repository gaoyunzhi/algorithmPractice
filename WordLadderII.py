class Solution:
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return a list of lists of string

	 # This should be a tree and
	def cacheWords(self, start, end, dictionary):
		dictionary.add(start)
		dictionary.add(end)
		cache = {}
		for word in dictionary:
			cache[word] = []
			for i in range(len(word)):
				part1 = word[: i]; part2 = word[i+1: ]
				for j in 'abcdefghijklmnopqrstuvwxyz':
					if word[i] != j:
						nextword = part1 + j + part2
						if nextword in dictionary:
							cache[word].append(nextword)
		return cache

	def findLadders(self, start, end, dictionary):
		cache = self.cacheWords(start, end, dictionary)
		past_level_set = []
		past_level_set.append([start])
		is_end = False
		result = []
		dis = {start: 0}
		result_len = 0;
		while result_len < len(dictionary) + 2:
			result_len += 1
			current_level_set = past_level_set
			past_level_set = []

			for path in current_level_set:
				last_word = path[-1]
				for next_word in cache[last_word]:
					if next_word == end:
						is_end = True
					new_path = path[:] + [next_word]
					if next_word in dis and dis[next_word] < result_len:
						continue
					else:
						dis[next_word] = result_len

					past_level_set.append(new_path)

			if is_end:
				break

		for path in past_level_set:
			if path[-1] == end:
				result.append(path)

		return result



		# cache = self.cacheWords(start, end, dictionary)
		# print cache
		# queue = []
		# queue.append((start, [start]))
		# result = []
		# flag = False
		# dis-{}
		# dis[start] = 0;
		# while queue:
		# 	currentState, currentPath = queue.pop(0)
		# 	print len(currentPath)
		# 	#print currentState, currentPath
		# 	if not flag:
		# 		if currentState == end: 
		# 			result.append(currentPath)
		# 			breakLevel = len(currentPath)
		# 			print currentPath
		# 			flag = True
		# 		else:
		# 			wordList = self.newWordList((currentState, currentPath), cache)
		# 			for _word in wordList:	
		# 				_path = currentPath[:]
		# 				_path.append(_word)
		# 				queue.append((_word, _path))

		# 	else:
		# 		if currentState == end and len(currentPath) == breakLevel:
		# 			result.append(currentPath)

		# 		elif len(currentPath) < breakLevel:
		# 			wordList = self.newWordList((currentState, currentPath), cache)
		# 			for _word in wordList:	
		# 				_path = currentPath[:]
		# 				_path.append(_word)
		# 				queue.append((_word, _path))
		# return result

sol = Solution()
# start = "cet"
# end  = "ism"
# dictionary = set(["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"])

# start = "hit"
# end = "cog"
# dictionary = set(["hot","dot","dog","lot","log"])

start = "hot"
end = "dog"
dictionary = set(["hot", "dog"])

print sol.findLadders(start, end, dictionary)