from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def project1(request):
    html_code='''
    <head>
</head>
<body>
<h1 style="text-align:center; color:blue;"> Madaminoff_00 </h1>

</body>
</html>
    '''
    return HttpResponse(html_code)

def project2(request):
    html_code='''
    <head>
</head>
<body>
<h2 style="text-align:center; color:blue;"> Django Framework </h2>

</body>
</html>
    '''
    return HttpResponse(html_code)



