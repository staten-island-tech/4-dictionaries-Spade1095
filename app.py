students = [
{
    "name": "henry",
    "school": "Tech",
    "birthday": "07/15/11",
},
{
    "name": "ayaan",
    "school": "Tech",
    "birthday":"06/27/11"
}
]

for index, i in enumerate(students):
    print(index, ":", i["name"],i["school"],i["birthday"])