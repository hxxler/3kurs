import random as rd

class ElipticCurves:
    
    def __init__(self):
        self.p = 751
        self.a = -1
        self.b = 1
        self.G = (0, 1)
        
        self.Gq23 = (-1, 1)
        
        self.G5 = (416, 55)
        self.n = 13
        
        self.G6 = (562, 89)
        
        self.G_test = (384, 475)
        
        self.alphabet = {
        ' ' : (33, 355), '!' : (33, 396), '"' : (34, 74), '#' : (34, 677), '$' : (36, 87), '%' : (36, 664), '&' : (39, 171), '\'' : (39, 171), '(' : (43, 224), ')' : (43, 527),
        '*' : (44, 366), '+' : (44, 385), ',' : (45, 31), '-' : (45, 720), '.' : (47, 349), '/' : (47, 402), '0' : (48, 49), '1' : (48, 702), '2' : (49, 183), '3' : (49, 568), 
        '4' : (53,227), '5' : (53, 474), '6' : (56, 332), '7' : (56, 419), '8' : (58, 139), '9' : (58, 612), ':' : (59, 365), ';' : (59, 386), '<' : (61, 129), '=' : (61, 622), 
        '>' : (62, 372), '?' : (62, 379), '@' : (66, 199), 'A' : (66, 552), 'B' : (67, 84), 'C' : (67, 667), 'D' : (69, 241), 'E' : (69, 510), 'F' : (70, 195), 'G' : (70, 556),
        'H' : (72, 254), 'I' : (72, 497), 'J' : (73, 72), 'K' : (73, 679), 'L' : (74, 170), 'M' : (74, 581), 'N' : (75, 318), 'O' : (75, 433), 'P' : (78, 271), 'Q' : (78, 480),
        'R' : (79, 111), 'S' : (79, 640), 'T' : (80, 318), 'U' : (80, 433), 'V' : (82, 270), 'W' : (82, 481), 'X' : (83, 373), 'Y' : (83, 378), 'Z' : (85, 35), '[' : (85, 716),
        '\\' : (86, 25), ']' : (86, 726), '^' : (90, 21), '_' : (90, 730), '`' : (93, 267), 'a' : (93, 484), 'b' : (98, 338), 'c' : (98, 413), 'd' : (99, 295), 'e' : (99, 456),
        'f' : (100, 364), 'g' : (100, 387), 'h' : (102, 267), 'i' : (102, 484), 'j' : (105, 369), 'k' : (105, 382), 'l' : (106, 24), 'm' : (106, 727), 'n' : (108, 247),
        'o' : (108, 504), 'p' : (109, 200), 'q' : (109, 551), 'r' : (110, 129), 's' : (110, 622), 't' : (114, 144), 'u' : (114, 607), 'v' : (115, 242), 'w' : (115, 509),
        'x' : (116, 92), 'y' : (116, 659), 'z' : (120, 147), '{' : (120, 604), '|' : (125, 292), '}' : (125, 459), '~' : (126, 33), 'А' : (189, 297), 'Б' : (189, 458),
        'В' : (192, 32), 'Г' : (192, 719), 'Д' : (194, 205), 'Е' : (194, 546), 'Ж' : (197, 145), 'З' : (197, 606), 'И' : (198, 224), 'Й' : (198, 527), 'К' : (200, 30),
        'Л' : (200, 721), 'М' : (203, 324), 'Н' : (203, 427), 'О' : (205, 372), 'П' : (205, 379), 'Р' : (206, 106), 'С' : (206, 645), 'Т' : (209, 82), 'У' : (209, 669),
        'Ф' : (210, 31), 'Х' : (210, 720), 'Ц' : (215, 247), 'Ч' : (215, 504), 'Ш' : (218, 150), 'Щ' : (218, 601), 'Ъ' : (221, 138), 'Ы' : (221, 613), 'Ь' : (226, 9),
        'Э' : (226, 742), 'Ю' : (227, 299), 'Я' : (227, 452), 'а' : (228, 271), 'б' : (228, 480), 'в' : (229, 151), 'г' : (229, 600), 'д' : (234, 164), 'е' : (234, 587),
        'ж' : (235, 19), 'з' : (235, 732), 'и' : (236, 39), 'й' : (236, 712), 'к' : (237, 297), 'л' : (237, 454), 'м' : (238, 175), 'н' : (238, 576), 'о' : (240, 309), 
        'п' : (240, 442), 'р' : (243, 87), 'с' : (243, 664), 'т' : (247, 266), 'у' : (247, 485), 'ф' : (249, 183), 'х' : (249, 568), 'ц' : (250, 14), 'ч' : (250, 737),
        'ш' : (251, 245), 'щ' : (251, 506), 'ъ' : (253, 211), 'ы' : (253, 540), 'ь' : (256, 121), 'э' : (256, 630), 'ю' : (257, 293), 'я' : (257, 458)
        }
    
    def extend_eucled(self, a, b):
        if a == 0:
            return (b, 0, 1)
        gcd, x1, y1 = self.extend_eucled(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)
    
    def gcd(self, a, m):
        if a == 0:
            return 0
        gcd, x, y = self.extend_eucled(a, m)
        if gcd != 1:
            print("error gcd")
            return
        return x % m
    
    def doubling_additing(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        
        x1, y1 = P
        x2, y2 = Q
        
        if P != Q:
            denom1 = (y2 - y1) % self.p
            denom2 = (x2 - x1) % self.p
            denom2_ = self.gcd(denom2, self.p) 
            lm = (denom1 * denom2_) % self.p
        elif P == Q:
            denom1 = (3 * x1 ** 2 + self.a) % self.p
            denom2 = (2 * y1) % self.p
            denom2_ = self.gcd(denom2, self.p)            
            lm = (denom1 * denom2_) % self.p

        x3 = (lm ** 2 - x1 - x2) % self.p
        y3 = (lm * (x1 - x3) - y1) % self.p
        
        return (x3, y3)
    
    def multiply_point(self, k, P):
        Q = None
        for i in range(k.bit_length()):
            if (k >> i) & 1:
                Q = self.doubling_additing(P, Q)
            P = self.doubling_additing(P, P)
        return Q
    
    def encrypt_char(self, k, Pb, char):
        C1 = self.multiply_point(k, self.G)
        C2 = self.multiply_point(k, Pb)
        C2_ = self.doubling_additing(C2, self.alphabet[char])
        C = (C1, C2_)
        return C
    
    def encrypt_text(self, k, Pb, plaintext):
        answer = []
        i = 0
        for i, char in enumerate(plaintext):
            answer.append(self.encrypt_char(k[i], Pb, char))
            print(f"x: {answer[i][0]} k * G, y: {answer[i][1]} Pm + k * Pb")
        print("\n")
    
    def reverse_sign(self, C):
        x, y = C
        C_ = (x, -y)
        return C_
    
    def find_key_by_value(self, value):
        for key, val in self.alphabet.items():
            if val == value:
                return key
        return None

    def decrypt_char(self, C, nb):        
        C_ = self.multiply_point(nb, C[0])
        C_m = self.reverse_sign(C_)
        C_a = self.doubling_additing(C[1], C_m)
        char = self.find_key_by_value(C_a)
        if char is None:
            print("err char ind")
            return
        return char

    def decrypt_text(self, nb, ciphertext):
        decrypted_text = ""
        for C in ciphertext:
            char = self.decrypt_char(C, nb)
            if char == None:
                print("error find char")
                return None
            decrypted_text += char

        print(decrypted_text)
        return decrypted_text
    
    def signature_generate(self, k, e, d):
        kG = self.multiply_point(k, self.G5)
        r = kG[0] % self.n
        z = self.gcd(k, self.n)
        s = z * (e + d * r) % self.n
        print(f"r: {r}, s: {s}")
        return (r, s)
    
    def signature_verification(self, e, rs, Q):
        if (rs[0] >= 1 and rs[0] <= self.n - 1) and (rs[1] >= 1 and rs[1] <= self.n - 1):
            v = self.gcd(rs[1], self.n)
            u1 = e * v % self.n
            u2 = rs[0] * 3 % self.n
            u1G = self.multiply_point(u1, self.G6)
            # u1G = self.multiply_point(u1, self.G_test)
            u2Q = self.multiply_point(u2, Q)
            X = self.doubling_additing(u1G, u2Q)
            X_ = X[0] % self.n
            if rs[0] == X_:
                print(f"r: {rs[0]}, x: {X_}")
                return True
            else:
                print(f"r: {rs[0]}, x: {X_}")
                return False
        else:
            print("error segn ver")
            return 
    
    
obj = ElipticCurves()

def designed(func):
    def wrapper():
        print("\n", func.__name__)
        func()
    return wrapper

@designed 
def task1():
    plaintext = "симметрия" 
    Pb = (489, 468)
    k = (3, 16, 17, 5, 16, 18, 3, 7, 15)


    print(obj.encrypt_text(k, Pb, plaintext))

@designed
def task2():
    nb = 48
    cipher = [
        ((179, 275), (712, 186)),
        ((725, 195), (395, 414)),
        ((72, 254), (434, 136)),
        ((425, 663), (251, 506)),
        ((16, 416), (383, 340)),
        ((745, 210), (102, 484)),
        ((346, 242), (78, 271)),
        ((179, 275), (712, 186)),
        ((725, 195), (739, 574)),
        ((346, 242), (78, 271)),
    ]
    obj.decrypt_text(nb, cipher)

@designed
def task3():
    P = (61, 129)
    Q = (69, 510)
    R = (72, 497)
    kP = 2
    kQ = 3

    p2 = obj.multiply_point(kP, P)
    q3 = obj.multiply_point(kQ, Q)
    r_ = obj.reverse_sign(R)
    p2q3 = obj.doubling_additing(p2, q3)
    C = obj.doubling_additing(p2q3, r_)
    print(f"x: {C[0]}, y: {C[1]}")

@designed
def task4():
    P = (49, 568)
    k = 124

    C = obj.multiply_point(k, P)
    print(f"x: {C[0]}, y: {C[1]}")

@designed
def task5():
    k = 3
    e = 8
    d = 6  

    obj.signature_generate(k, e, d)

@designed
def task6():
    e = 8
    rs = (3, 1)
    Q = (384, 276)

    obj.signature_verification(e, rs, Q)

task1()
task2()
task3()
task4()
task5()
task6()