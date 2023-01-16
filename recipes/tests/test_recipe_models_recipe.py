
from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):

    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

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
