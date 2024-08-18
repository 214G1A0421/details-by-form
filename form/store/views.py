from django.shortcuts import render
from django.http import HttpResponse
def func1(request,pid):
    list=[{'id':1,'name':'Dharani','mobile':9836276323,'Details':'Ramapuram,owk,kurnool'},
    {'id':2,'name':'Sai Akhila','mobile':94894202358,'Details':'tirupathi'},
    {'id':3,'name':'Lavanya','mobile':9843962798,'Details':'Ganthimarri'},
    {'id':4,'name':'janu','mobile':8572836287,'Details':'tirupathi'},
    {'id':5,'name':'sruu','mobile':7834962334,'Details':'Aathmakuru'},
    {'id':6,'name':'Pallu','mobile':7342694872,'Details':'chinthalacheruvu'},
    {'id':7,'name':'pani','mobile':7231918822,'Details':'uravakonda'}
    ]
    result=None
    for item in list:
        if item.get('id')==pid:
            result=item
            break
    return HttpResponse(f"<p>user name:{result.get('name')}<br> mobile number:{result.get('mobile')} <br> user details:{result.get('Details')}</p>")
# Create your views here.
