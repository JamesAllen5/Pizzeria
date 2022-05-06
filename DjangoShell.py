import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from MainApp.models import Pizza

pizzas = Pizza.objects.all() #same as select * From Topic

for t in pizzas: #print topics
    print(t.id, '   ',t.text)

t = Pizza.objects.get(id=1) #only print topics that id=1

print(t.text)
print(t.date_added)

#print entries
topping = t.topping_set.all()

for e in topping:
    print(e.text)

