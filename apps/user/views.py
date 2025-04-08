from django.shortcuts import render
from .models import Person
from django.views import View
from django.db.models import F, functions, CharField, Value, IntegerField
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.aggregates import ArrayAgg
import json

# Create your views here.


class PersonView(View):
    def name_shorter(self, name):
        if len(name) > 10:
            full_name = name.split(" ")
            if len(full_name) > 1:
                first_name = full_name[0]
                names = [f"{name[0].upper()}." for name in full_name[1:]]
                name = f"{first_name} {' '.join(names)}"
            else:
                name = full_name[0]
        return name

    def get(self, request):
        rendered_data = Person.objects.annotate(
            birthDate=functions.Cast(F("birth_date"),CharField()),
            deathDate=functions.Cast(F("death_date"),CharField())
        )
        if not rendered_data.exists():
            listed_data = [
                {
                    "id": 1,
                    "pids": [2, 3],
                    "gender": "male",
                    "name": "Mardi Suroyo",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                    "birthDate": "1867-09-16",
                },
                {
                    "id": 2,
                    "pids": [1],
                    "gender": "female",
                    "name": "Kartini",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 3,
                    "pids": [1],
                    "gender": "female",
                    "name": "Kasmi",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 4,
                    "pids": None,
                    "gender": "male",
                    "fid": 1,
                    "mid": 2,
                    "name": "Jarkasih S.",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 5,
                    "pids": None,
                    "gender": "male",
                    "fid": 1,
                    "mid": 2,
                    "name": "Slamet H.",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 6,
                    "pids": None,
                    "gender": "male",
                    "fid": 1,
                    "mid": 2,
                    "name": "Dasri",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 7,
                    "pids": None,
                    "gender": "male",
                    "fid": 1,
                    "mid": 3,
                    "name": "Sumadi",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 8,
                    "pids": [9],
                    "gender": "male",
                    "fid": None,
                    "mid": None,
                    "name": "Sutio A.R.",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 9,
                    "pids": [8],
                    "gender": "female",
                    "fid": 1,
                    "mid": 3,
                    "name": "Surtiyati",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 10,
                    "pids": None,
                    "gender": "male",
                    "fid": 1,
                    "mid": 3,
                    "name": "Supardi",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 11,
                    "pids": None,
                    "gender": "male",
                    "fid": 1,
                    "mid": 3,
                    "name": "Jayuli",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 12,
                    "pids": None,
                    "gender": "male",
                    "fid": 1,
                    "mid": 3,
                    "name": "Sukarman",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 13,
                    "pids": None,
                    "gender": "male",
                    "fid": 1,
                    "mid": 3,
                    "name": "M. Subiantoro",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 14,
                    "pids": None,
                    "gender": "male",
                    "fid": 1,
                    "mid": 3,
                    "name": "Ismail",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 15,
                    "pids": None,
                    "gender": "female",
                    "fid": 1,
                    "mid": 3,
                    "name": "Mintarni",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
                {
                    "id": 16,
                    "pids": None,
                    "gender": "female",
                    "fid": 1,
                    "mid": 3,
                    "name": "Arum Arianti",
                    "photo": "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg",
                },
            ]
            return render(request, 'family_tree.html', {'data': json.dumps(listed_data)})

        listed_data = []
        for data in rendered_data:
            obj = {}
            obj["pids"] = list(data.partners.values_list("id", flat=True)) if data.partners.exists() else None
            obj["fid"] = data.father.id if data.father else None
            obj["mid"] = data.mother.id if data.mother else None
            obj["id"] = data.id
            obj["gender"] = data.gender
            obj["name"] = self.name_shorter(data.name)
            obj["photo"] = data.photo.url if data.photo else "https://t3.ftcdn.net/jpg/03/46/83/96/240_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg"
            obj["birthDate"] = data.birthDate
            obj["deathDate"] = data.deathDate
            listed_data.append(obj)
        return render(request, 'family_tree.html', {'data': json.dumps(listed_data)})
