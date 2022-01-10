from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='Kimutai')
        self.user.save()
        self.profile = Profile( profile_picture='black and orange',bio='programmer',contact="0743880558",user=self.user)
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)


        #project test class

class CommmentTestClass(TestCase):
    def setUp(self):
        self.project = Profile(title = 'baboon', image='baboon.jpg', description="baboon",link="https://en.wikipedia.org/wiki/Tiger")

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
         self.assertTrue(isinstance(self.project, Project))
    def test_save_method(self):
        self.project.save_project()
        projects = Profile.objects.all()
        self.assertTrue(len(projects)>0)
    def test_delete_method(self):
        self.project.save_project()
        projects = Profile.objects.all()
        self.project.delete_project()
        projects = Profile.objects.all()
        self.assertTrue(len(projects)==0)


class PostTestclass(TestCase):
    def setUp(self):
        self.user = User(username='amos')
        self.user.save()
        self.project = Profile(title='baboon', image='boboon.jpg', description="baboon", link="https://en.wikipedia.org/wiki/Tiger")
        self.project.save_project()

        self.new_review=Post(design="9",usability="9",conent="10",user=self.user,project=self.project)
        self.new_review.save_review()
    def tearDown(self):
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))

    def test_save_comment(self):
        reviews = Post.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_delete_comment(self):
        self.new_review.save_review()
        self.new_review.delete_review()
        reviews = Post.objects.all()
        self.assertTrue(len(reviews)==0)


