from django.shortcuts import render
from .models import UserMessage


def getform(request):
    # all_message = UserMessage.objects.all()
    #
    # for message in all_message:
    #     print(message.name)

    # 处理post请求
    if request.method == 'POST':
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')

        # 实例化一个模型对象
        user_message = UserMessage()
        # 为对象添加属性
        # user_message.name = 'salmond2'
        # user_message.message = '你也帅'
        # user_message.address = '上海'
        # user_message.email = 'salmondma@163.com'
        # user_message.object_id = 'efgh'
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = 'ijkl'
        # 调用save方法进行保存
        user_message.save()

    # 删除数据
    all_message = UserMessage.objects.filter(name='salmond',address='上海')
    # all_message.delete()
    for message in all_message:
        message.delete()

    return render(request, 'message_form.html')
