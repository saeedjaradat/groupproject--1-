from django.db import models
import  re
import bcrypt

class Usermanager(models.Manager):
    def member_validator(self, postData ):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        password_regex =re.compile(r'^[a-zA-Z0-9.+_-]')
        special_symbols = ['$','@','#','%','^','&']

        if len(postData['first_name']) < 3 :
            errors['first_name'] = "first name should be at least 3 characters"
        if len(postData['last_name']) < 3 :
            errors['last_name'] = "last name should be at least 3 characters"
        # if len(postData['user_level']) < 2:
        #     errors["user_level"] = "user_level should be at least 2characters"
        if len(postData['experience']) < 1:
            errors["experience"] = "experience should be at least 2characters"
        if len(postData['mobile_num']) < 9:
            errors["mobile_num"] = "number should be at least 9characters"
        if len(postData['address']) < 2:
            errors["Address"] = "Address should be at least 2characters"
        if len(postData['skill']) < 2:
            errors["skill"] = "skill should be at least 2characters"
        if len(postData['password']) < 8:
            errors["password"] = "user password should be at least 8characters"
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if not any(characters.isupper() for characters in postData['password']):
            errors['password_notInclude_upper'] = "Password must have at least one uppercase character"
        if not any(characters.islower() for characters in postData['password']):
            errors['password_notInclude_lower'] = "Password must have at least one lowercase character"
        if not any(characters.isdigit() for characters in postData['password']):
            errors['password_notInclude_number'] = "Password must have at least one numeric character."
        if not any(characters in special_symbols for characters in postData['password']):
            errors['password_symbol'] = "Password should have at least one of the symbols $@#%^&"
        if postData['password'] != postData['confirm_password']:
            errors['not_the_same'] = "please insert password similer as above"
        return errors

    def customer_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        password_regex =re.compile(r'^[a-zA-Z0-9.+_-]')
        special_symbols = ['$','@','#','%','^','&']

        if len(postData['full_name']) < 2:
            errors["full_name"] = "name should be at least 2characters"
        if len(postData['Address']) < 2:
            errors["Address"] = "Address should be at least 2characters"
        if len(postData['mobile_num']) < 9:
            errors["mobile_num"] = "number should be at least 9characters"
        if len(postData['identity_num']) < 10:
            errors["identity_num"] = "scope of work should be at least 10characters"
        if len(postData['password']) < 8:
            errors["password"] = "user password should be at least 8characters"
        if len(postData['cpassword']) <8:
            errors["cpassword"] = "user cpassword should be at least 8characters"
        return errors 

class userLevel(models.Model):
    name = models.CharField(max_length=255)
    # members = list of members
    created_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 

class members(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    skill=models.CharField(max_length=255)
    experience=models.IntegerField()
    address=models.CharField(max_length=255)
    mobile_num=models.IntegerField()
    password=models.CharField(max_length=255)
    user_level=models.ManyToManyField(userLevel , related_name="members" ,default='employee')
    identity_image = models.FileField(upload_to="identity_images/", max_length=250,null=True,blank=True,default='')
    created_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = Usermanager()

# register new member
def Register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    skill = request.POST['skill']
    experience = request.POST['experience']
    address = request.POST['address']
    mobile_num = request.POST['mobile_num']
    password = request.POST['password']
    identity_image = request.FILE['identity_image']
    user_level = request.POST['user_level']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    if (request.POST['confirm_password'] == password):
        member =  members.objects.create(first_name = first_name , last_name = last_name, email = email , skill=skill , experience=experience , address=address ,mobile_num=mobile_num , identity_image = identity_image , password = pw_hash, user_level=user_level)
