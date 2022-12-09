class User:
    
    @staticmethod
    def is_vaild_name(name):
        try:
            return name.isalpha()
        except:
            return False

print(User.is_vaild_name(1234))
print(User.is_vaild_name('길동'))