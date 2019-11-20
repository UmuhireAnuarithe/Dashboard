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
    profiles = Profile.objects.filter(user = current_user.id).first()
    if request.method == 'POST':
        form = AnswerForm(request.POST,request.FILES)
        if form.is_valid():
            answers = form.save(commit=False)
            answers.user = profiles
            answers.question = question
            answers.save()
            return redirect('home')
    else:
        form = AnswerForm()
    title = "Question"
    return render(request, 'answer.html',{"form":form, "id":id} )




def new_profile(request):
  current_user = request.user
  new_profile = Profile.objects.filter(id=current_user.id)
  if request.method == 'POST':
      form = ProfileForm(request.POST, request.FILES)
      if form.is_valid():
          profile = form.save(commit=False)
          profile.username = current_user.profile
          profile.save()
      return redirect('profile')
  else:
      form = ProfileForm()
  return render(request, 'new-profile.html',{"form":form})



def profile(request):
 current_user = request.user
 myprofile = Profile.objects.filter(user = current_user).first()
 username = User.objects.filter(id = current_user.id).first()
 return render(request, 'profile.html', { "myprofile":myprofile})


