from django.shortcuts import render,redirect
from django.contrib import messages
# from django.contrib.auth.models import User
from .forms import UserRegisterForm,UpdateUserForm,UpdateProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  #or form.cleaned_data.get('username')
            messages.success(request, f"Your Account has been created! Now Log In!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST , instance=request.user)
        p_form = UpdateProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f"Your Account has been updated successfully")
            redirect("profile")
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile) 

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/profile.html', context)







# message.debug
# message.success
# message.warning
# message.error