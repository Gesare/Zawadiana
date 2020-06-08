from django.test import TestCase
from .models import Profile,Projects
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Gesare')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='image.jpg', bio='We are testing the profile ', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

class ProjectsTestCase(TestCase):
    def setUp(self, project_name='GitSearch', project_photo='lol.jpg', description='some description', github_repo='git repo', url='lol.com', owner='Mercurial'):
        return Projects.objects.create(project_name=project_name, project_photo=project_photo, description=description, github_repo=github_repo, url=url, owner=owner)

    def projectSave(self):
        initialization = self.setUp()
        self.assertTrue(save > 0)
