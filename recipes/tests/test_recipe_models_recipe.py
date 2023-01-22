
from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeModelTest(RecipeTestBase):

    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_default_field(self):
        recipe = Recipe(
            category=self.make_category(name='default_category'),
            author=self.make_author(username='default_user'),
            title='Recipe title',
            description='Description ',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutes',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe preparation steps',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def test_recipe_field_title_raises_error_if_string_more_then_65(self):
        self.recipe.title = 'A' * 66

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    @parameterized.expand([
        ('title', 65),
        ('description', 200),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_len_error_if_string_more_then_raises(self,
                                                                    field,
                                                                    max_len):

        setattr(self.recipe, field, 'A' * (max_len + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparations_steps_is_html_false_by_default(self):
        recipe = self.make_recipe_no_default_field()
        self.assertFalse(recipe.preparation_steps_is_html)

    def test_recipe_preparations_steps_is_publish_false_by_default(self):
        recipe = self.make_recipe_no_default_field()
        self.assertFalse(recipe.is_published)

    def test_recipe_representation_string(self):
        title = 'Teste Representation'
        self.recipe.title = title
        self.recipe.full_clean()
        self.assertEqual(str(self.recipe), title)
