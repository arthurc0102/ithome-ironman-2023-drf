from django.db import models


class CreatedAtField(models.DateTimeField):
    def __init__(self, *args, **kwargs) -> None:
        kwargs["auto_now_add"] = True
        super().__init__(*args, **kwargs)


class UpdatedAtField(models.DateTimeField):
    def __init__(self, *args, **kwargs) -> None:
        kwargs["auto_now"] = True
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if add:
            for field in model_instance._meta.get_fields():
                if not isinstance(field, CreatedAtField):
                    continue

                value = getattr(model_instance, field.name)
                setattr(model_instance, self.attname, value)
                return value

        return super().pre_save(model_instance, add)
