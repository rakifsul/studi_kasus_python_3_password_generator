import random

# class untuk meng-generate password.
class PWDGen:
    def __init__(self):
        # daftar karakter valid.
        self.lower_case_chars = "qwertyuiopasdfghjklzxcvbnm"
        self.upper_case_chars = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.numbers_chars = "1234567890"
        self.symbols_chars = "`~!@#$%^&*()-_=+[{]}|;:'\",<.>?"

        # status jenis karakter di awal program dijalankan.
        self.is_lower_case = False
        self.is_upper_case = False
        self.is_numbers = False
        self.is_symbols = False

        self.unique_chars = False
        self.length = 5
        pass

    def __del__(self):
        pass

    def generate_password(self):
        result = ""
        processed = ""
        possible_length = 0

        if self.is_upper_case == True:
            # Jika pilihan uppercase dicentang.
            processed += self.upper_case_chars
            possible_length += len(self.upper_case_chars)
        if self.is_lower_case == True:
            # Jika pilihan lowercase dicentang.
            processed += self.lower_case_chars
            possible_length += len(self.lower_case_chars)
        if self.is_numbers == True:
            # Jika pilihan numbers dicentang.
            processed += self.numbers_chars
            possible_length += len(self.numbers_chars)
        if self.is_symbols == True:
            # Jika pilihan symbols dicentang.
            processed += self.symbols_chars
            possible_length += len(self.symbols_chars)

        if processed == "":
            result = "nothing"
            return result

        if self.unique_chars == True:
            # Jika pilihan karakter unik dicentang.
            if self.length > possible_length:
                result = "not possible"
                return result

            arr_list = []

            for _ in range(self.length):
                elm = random.choice(processed)
                while elm in arr_list:
                    elm = random.choice(processed)
                arr_list.append(elm)

            result = ''.join(arr_list)
        else:
            # Jika pilihan karakter unik tidak dicentang.
            arr_list = []

            for _ in range(self.length):
                elm = random.choice(processed)
                arr_list.append(elm)

            result = ''.join(arr_list)

        return result
