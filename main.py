"""This is an implementation of two easy ciphers"""
from string import ascii_lowercase, digits, punctuation

REFERENCE = ascii_lowercase + digits + punctuation


class Vigenere:
    def __init__(self, message: str, key: str) -> None:
        self.message = message.lower()
        self.key = key.lower()

    def encrypt(self):
        # first modify the key such that it has the same length
        # as the message.(if the key is shorter)
        lenDiff = len(self.message) - len(self.key)
        modifiedKey = self.key[:]
        if lenDiff > 0:
            count = 0
            for i in range(lenDiff):
                try:
                    modifiedKey += self.key[count]
                except IndexError:
                    modifiedKey += self.key[0]
                    count = 1
        messagePosition = self.getOrdinaryPosition(self.message)
        keywordPosition = self.getOrdinaryPosition(self.key)
        res = ""
        for ithletter in range(len(self.message)):
            if self.message[ithletter] == " ":
                res += " "
                continue
            Sum = (
                messagePosition[self.message[ithletter]]
                + keywordPosition[modifiedKey[ithletter]]
            )
            while Sum > 68:
                Sum -= 68
            res += REFERENCE[Sum]
        self.message = res
        return res

    def decrypt(self):
        # first modify the key such that it has the same length
        # as the message.(if the key is indeed shorter)
        lenDiff = len(self.message) - len(self.key)
        modifiedKey = self.key[:]
        if lenDiff > 0:
            count = 0
            for i in range(lenDiff):
                try:
                    modifiedKey += self.key[count]
                except IndexError:
                    modifiedKey += self.key[0]
                    count = 1
        messagePosition = self.getOrdinaryPosition(self.message)
        keywordPosition = self.getOrdinaryPosition(self.key)
        res = ""
        for ithletter in range(len(self.message)):
            if self.message[ithletter] == " ":
                res += " "
                continue
            encryptedLetterPosition = messagePosition[self.message[ithletter]]
            decryptedInd = (
                encryptedLetterPosition - keywordPosition[modifiedKey[ithletter]]
            )
            if decryptedInd < 0:
                decryptedInd += 68
            res += REFERENCE[decryptedInd]
        self.message = res

    def getOrdinaryPosition(self, word):
        res = dict()
        for letter in word:
            try:
                res[letter] = REFERENCE.index(letter)
            except ValueError:
                continue
        return res

    def __str__(self):
        return f"Message: {self.message} | Key: {self.key}"


class Caesar:
    def __init__(self, message: str, shift: int) -> None:
        self.message = message.lower()
        while shift > 67:
            shift -= 67
        self.shift = shift
        self.reference = dict()

    def encrypt(self):
        self.buildReference(False)
        res = ""
        for letter in self.message:
            if letter == " ":
                res += " "
                continue
            res += REFERENCE[self.reference[letter]]
        self.message = res
        return res

    def decrypt(self):
        self.buildReference(True)
        res = ""
        for letter in self.message:
            if letter == " ":
                res += " "
                continue
            refInd = self.reference[letter]
            res += REFERENCE[refInd]
        self.message = res
        return res

    def buildReference(self, backwards: bool):
        res = dict()
        count = 0
        if backwards:
            for letter in REFERENCE:
                newInd = count - self.shift
                while newInd < 0:
                    newInd += 67
                res[letter] = newInd
                count += 1
            self.reference = res
        else:
            for letter in REFERENCE:
                newInd = count + self.shift
                while newInd > 67:
                    newInd -= 67
                res[letter] = newInd
                count += 1
            self.reference = res

    def __str__(self):
        return f"Message: {self.message} | Shift: {self.shift}"


if __name__ == "__main__":
    cipher = Vigenere("decrypt me lol", "mosquito")
    cipher.encrypt()
    print(f"Encrypted text: {cipher}")
    cipher.decrypt()
    print(f"Encrypted text: {cipher}")
