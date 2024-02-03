import random

SYMBOLS = ".,!?"

class chatbot:
    def __init__(self):
        self.LM = [{():{"":0}}]
    
    def add_LM(self, LM):
        self.LM.update([{tuple([w.strip(SYMBOLS).lower() for w in s.split(" ")]):[{w.replace("{name}", self.name):p} for w, p in a.items()]}
               for s, a in LM.items()])
        """for s, a in LM.items():
            c = {}
            b = tuple([w.strip(".,!?").lower() for w in s.split(" ")])
            for w in s.split(" "):
                b.append(w.strip(".,!?").lower())
            b = tuple(b)
            e = [{w.replace("{name}", self.name):p} for w, p in a.items()]
            for w, p in a.items():
                e.append({w.replace("{name}", self.name):p})
            c.update({b:e})
            self.LM.append({tuple([w.strip(".,!?").lower() for w in s.split(" ")]):[{w.replace("{name}", self.name):p} for w, p in a.items()]})"""
    
    def talk(self, inp):
        inp_words = [w.strip(SYMBOLS).lower() for w in inp.split(" ")]
        ans_candidates = self.candidate(inp_words=inp_words)
        return random.choices(tuple(ans_candidates.keys()), weights=tuple(ans_candidates.values()))[0]
    
    def candidate(self, inp_words):
        ans = []
        for q in self.LM:
            c = 0
            for word in inp_words:
            	if word in q:
                    c += 1
            ans.append((q, c))
        ans_candidate = {}
        for q, c in ans:
            if q in ans_candidate.keys():
                ans_candidate.update({q:ans_candidate[q] + c})
            else:
                ans_candidate.update({q:c})
        return self.LM[random.choices(tuple(ans_candidate.keys()), weights=tuple(ans_candidate.values()))[0]]