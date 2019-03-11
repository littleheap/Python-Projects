# 检查特殊值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
    # Marie, you can post a response if you wish.
