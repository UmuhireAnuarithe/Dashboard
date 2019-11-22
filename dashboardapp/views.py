from django.shortcuts import render,redirect
# from .models import Post,Profiles,Answer,Category
from .models import Question,Profile,User,Answer
from .forms import PostForm ,ProfileForm ,AnswerForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    current_user = request.user
    posts=Question.objects.all()
    solutions = Answer.objects.filter(id = current_user.id).first()
    return render(request,'home.html',{'posts':posts,"solutions":solutions})

      
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('home')

    else:
        form = PostForm()
    return render(request, 'newpost.html', {"form": form})


@login_required(login_url='/accounts/login')
def post(request, id):
    current_user = request.user
    question = Question.objects.filter(id=id).first()
    profile = Profile.objects.filter(user = current_user.id).first()
    if request.method == 'POST':
        form = AnswerForm(request.POST,request.FILES)
        if form.is_valid():
            answers = form.save(commit=False)
            answers.user = current_user
            answers.question = question
            answers.save()
            return redirect('home')
    else:
        form = AnswerForm()
    title = "Question"
    return render(request, 'answer.html',{"form":form, "id":id} )


def new_profile(request):_
    current_user = request.user
    if request.method == 'POST':
        if Profile.objects.filter(user_id=current_user).exists():
            form = ProfileForm(request.POST, request.FILES,instance=Profile.objects.get(user_id=current_user))
        else:
            form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')
    else:
        if Profile.objects.filter(user_id=current_user).exists():
            form = ProfileForm(instance = Profile.objects.get(user_id=current_user))
        else:
            form = ProfileForm()
    return render(request, 'new-profile.html', {"form": form})


def profile(request,profile_id):
    current_user = request.user
    user = User.objects.get(pk=profile_id)
    myprofile = Profile.objects.filter(user = profile_id)
   
    return render (request, 'profile.html', {'current_user': current_user,'myprofile':myprofile})

def likes(request,id):
   likes=0
   answer = Answer.objects.get(id=id)
   answer.likes = answer.likes+1
   answer.save()
   return redirect("/")



