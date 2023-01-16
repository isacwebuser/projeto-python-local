from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    def test_recipe_view_home_function_ok(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.my_home)

    def test_recipe_home_view_status_code_response_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_load_template_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_show_not_found_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Modules not found here!',
                      response.content.decode('utf-8'))

    def test_recipe_home_template_load_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('Recipe title', content)
        self.assertEqual(len(response.context['recipes']), 1)

    def test_recipe_view_category_function_ok(self):
        view = resolve(reverse('recipes:category',
                       kwargs={'category_id': 1, }))
        self.assertIs(view.func, views.category)

    def test_recipe_view_category_status_code_404(self):
        response = self.client.get(reverse('recipes:category',
                                           kwargs={'category_id': 10000, }))
        self.assertEqual(response.status_code, 404)

    def test_recipe_view_detail_function_ok(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1, }))
        self.assertIs(view.func, views.recipe)

    def test_recipe_view_detail_status_code_404(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 100000, }))
        self.assertEqual(response.status_code, 404)
