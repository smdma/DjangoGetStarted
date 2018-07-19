from django.shortcuts import render
from .models import UserMessage


def getform(request):
    message = None
    # filter获取的是一个queryset查询集，可以用索引。get则不行
    all_message = UserMessage.objects.filter(
        name='salmond', address='上海')
    print("all_message",all_message)

    # if 判断是否存在数据
    if all_message:
        # all_message是一个list，可以使用切片。
        message = all_message[0]

    return render(request, 'message_form.html', {
        'my_message': message
    })
