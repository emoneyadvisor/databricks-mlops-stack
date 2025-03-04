from {{cookiecutter.project_name_alphanumeric_underscore}}.training.steps.transform import transformer_fn


def test_tranform_fn_returns_object_with_correct_spec():
    transformer = transformer_fn()
    assert callable(getattr(transformer, "fit", None))
    assert callable(getattr(transformer, "transform", None))
