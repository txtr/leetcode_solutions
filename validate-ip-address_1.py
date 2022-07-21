class Solution:
    def validIPv4(self, queryIP: str) -> bool:
        number = None
        number_colons = 0
        for x in range(len(queryIP)):
            if queryIP[x] == '.':
                number_colons = number_colons + 1
                if number_colons > 3:
                    print(254)
                    return False
                else:
                    if number is None or number > 255:
                        print(645)
                        return False
                    else:
                        number = None
            elif queryIP[x].isdigit():
                if number == 0:
                    print(867)
                    return False
                else:
                    if number == None:
                        number = 0
                    number = number * 10 + int(queryIP[x])
                    if number > 255:
                        print(726)
                        return False
            else:
                print(798, queryIP[x])
                return False
        if number_colons < 3 or number == None:
            print(835)
            return False
        return True
                
                
    
    def validIPv6(self, queryIP: str) -> bool:
        substring_len = None
        colon_count = 0
        for x in range(len(queryIP)):
            character = queryIP[x]
            if character == ':':
                colon_count = colon_count + 1
                if colon_count > 7:
                    return False
                elif substring_len == None:
                    return False
                else:
                    substring_len = None
            elif character in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'}:
                if substring_len is None:
                    substring_len = 0
                substring_len = substring_len + 1
                if substring_len > 4:
                    return False
            else:
                return False
        if substring_len is None:
            return False
        return True
                
            
    
    def validIPAddress(self, queryIP: str) -> str:
        if self.validIPv4(queryIP):
            return "IPv4"
        elif self.validIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"