from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from demo_form.form.forms import AuthorFormOne


def formView(request):
    # 过滤 POST 方法的请求
    if request.method == "POST":
        form = AuthorFormOne(request.POST)
        # 验证表单
        if form.is_valid():
            # 一般过滤数据
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            information = form.cleaned_data['information']
            # 处理业务, 如查询数据库信息
            return HttpResponseRedirect('/')
    else:
        # 不是 GET 请求则显示表单
        form = AuthorFormOne()

    templateView = 'author.html'
    return render(request, templateView, {'form':form})