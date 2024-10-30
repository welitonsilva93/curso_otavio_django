from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

class RecipeViewsTest(TestCase):

   def test_recipe_home_view_fuction_is_correct(self):
      view = resolve(reverse('recipes:home'))
      self.assertIs(view.func, views.home)

   def test_recipe_category_view_fuction_is_correct(self):
      view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
      self.assertIs(view.func, views.category)

   def test_recipe_detail_view_fuction_is_correct(self):
      view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
      self.assertIs(view.func, views.recipe)

   def test_recipe_home_view_returns_status_code_200_ok(self):
      reponse = self.client.get(reverse('recipes:home'))
      self.assertEqual(reponse.status_code, 200)

   def test_recipe_home_view_loads_correct_loads_templates(self):
      response = self.client.get(reverse('recipes:home'))
      self.assertTemplateUsed(response, 'recipes/pages/home.html')