class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            if len(word)==0:
                result+= '~/'
                continue
    
            for index, char in enumerate(word):
                if not char.isalpha():
                        result += char
                else: 
                    ref = ord('a') if char.islower() else ord('A')
                    result += chr((ord(char) - ref + 1) % 26 + ref)
                if index == len(word) -1:
                    result += '/'
            
        return (result)
        


    def decode(self, s: str) -> List[str]:
        
        arr = s.split('/')        
        arr.pop()
        print(arr)
        final = []
        result= ""
        for word in arr:   
            if (word=="~"):
                    final.append("")
                    continue
            result = ""
            for char in word:
                
    
                if(char.isalpha()):
                    ref = ord('a') if char.islower() else ord('A')
                    result += chr((ord(char) - ref - 1) % 26 + ref)        
                else:
                    result += char
            final.append(result)
        return final

