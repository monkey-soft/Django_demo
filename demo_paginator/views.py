from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def paginator_view(request):
    book_list = []
    '''
    这里的数据应该从 models 中获取，但我为了方便。直接使用生成器来获取数据。
    '''
    for x in range(1, 26):  # 一共 25 本书
        book_list.append('Book ' + str(x))

    # 将数据按照规定每次数量, 进行分割
    paginator = Paginator(book_list, 10)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)

    template_view = 'page.html'
    return render(request, template_view, {'books': books})
