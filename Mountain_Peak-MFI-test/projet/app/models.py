from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Mountain_Peak(models.Model):
    
    id = fields.IntField(pk=True)
    name_attribute = fields.CharField(max_length=250)
    lattitude = fields.FloatField(max=53)
    longitude = fields.FloatField(max=53)
    alltitude_in_meters = fields.IntField(max_length=10)

    class PydanticMeta:
        pass

Mountain_Peak_Pydantic = pydantic_model_creator(Mountain_Peak, name= "MountainPeak")
Mountain_PeakIn_Pydantic = pydantic_model_creator(Mountain_Peak, name= "MountainPeakIn", exclude_readonly=True)
