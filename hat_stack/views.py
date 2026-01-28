from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import random


MOCK_USERS = [
    {"id": 1, "name": "Alice Wonderland", "role": "Full Stack Dev"},
    {"id": 2, "name": "Bob Builder", "role": "DevOps Engineer"},
]

def get_user_list_html(request):
    """Helper function to render the user list partial."""
    return render(request, "partials/_user_list.html", {"users": MOCK_USERS})

def dashboard(request):
    context = {"users": MOCK_USERS}
    
    if request.headers.get("HX-Request"):
        return render(request, "partials/_user_list.html", context)
        
    return render(request, "index.html", context)

@require_http_methods(["POST"])
def create_user(request):
    name = request.POST.get("name")
    role = request.POST.get("role")
    
    new_user = {
        "id": random.randint(1000, 9999),
        "name": name,
        "role": role
    }
    MOCK_USERS.append(new_user)
    
    return get_user_list_html(request)

@require_http_methods(["PATCH"])
def update_user_role(request, user_id):
    for user in MOCK_USERS:
        if user["id"] == user_id:
            user["role"] = "Senior Engineer" if user["role"] != "Senior Engineer" else "CTO"
            break
            
    return get_user_list_html(request)

@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    global MOCK_USERS
    MOCK_USERS = [u for u in MOCK_USERS if u["id"] != user_id]
    
    return get_user_list_html(request)
