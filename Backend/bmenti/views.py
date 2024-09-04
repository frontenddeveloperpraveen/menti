from django_nextjs.render import render_nextjs_page
from django.contrib.auth import login,user_logged_in

# async def jobs(request):
#     # Your custom logic
#     return await render_nextjs_page(request)

async def signup(request,name=None):
    print("new Request on signup route")

    return await render_nextjs_page(request)

async def Home(request,name=None):
    print
    return await render_nextjs_page(request=request)


